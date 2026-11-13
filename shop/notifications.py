"""Уведомления менеджеру о новых заказах с сайта.

Главное правило: письмо должно уйти, даже если в данных заказа что-то не так. Каждое поле достаётся
с запасным значением, а если не собралось всё письмо целиком, уходит короткое текстовое письмо
с номером заказа и ссылкой на админку.
"""
import logging
import re
import smtplib
from decimal import Decimal, ROUND_HALF_UP

from django.conf import settings
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

logger = logging.getLogger(__name__)

SITE_NAME = 'cubekazan.ru'
MISSING = '—'


def format_rub(value):
    """15400 -> '15 400 ₽', 12.5 -> '12,50 ₽'. Пробелы неразрывные, чтобы сумма не переносилась."""
    try:
        value = Decimal(value).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    except Exception:
        return MISSING
    whole, _, frac = f'{value:,.2f}'.partition('.')
    text = whole.replace(',', ' ')
    if frac != '00':
        text += f',{frac}'
    return f'{text} ₽'


def _text(value, default=MISSING):
    """Строка для письма: None и пустые значения заменяются на прочерк."""
    if value is None:
        return default
    value = str(value).strip()
    return value or default


def _order_number(order):
    return _text(getattr(order, 'id', None), default='?')


def _created_at(order):
    try:
        return timezone.localtime(order.created_at).strftime('%d.%m.%Y %H:%M')
    except Exception:
        return timezone.localtime().strftime('%d.%m.%Y %H:%M')


def _admin_url(order):
    try:
        if settings.SITE_URL:
            return settings.SITE_URL + reverse('admin:shop_orders_change', args=[order.pk])
    except Exception:
        logger.exception('Заказ №%s: не удалось построить ссылку на админку', _order_number(order))
    return ''


def _item(info):
    """Одна позиция заказа. Битый товар не роняет письмо: показываем то, что удалось достать."""
    product = None
    try:
        product = info.product
    except Exception:
        pass

    name = _text(getattr(product, 'name', None), default='')
    if not name:
        product_id = getattr(info, 'product_id', None)
        name = f'Товар #{product_id} (без названия)' if product_id else 'Товар не найден'

    count = getattr(info, 'count', None)
    line = getattr(info, 'price', None)
    # ProductInfo.price — стоимость всей позиции (цена за штуку × количество), см. shop/pricing.line_total.
    try:
        unit = format_rub(Decimal(line) / count) if count else MISSING
    except Exception:
        unit = MISSING

    return {
        'name': name,
        'size': _text(getattr(product, 'size', None), default=''),
        'count': _text(count),
        'unit_price': unit,
        'line_total': format_rub(line) if line is not None else MISSING,
    }


def _items(order):
    items = []
    try:
        infos = list(order.productinfo_set.select_related('product').order_by('pk'))
    except Exception:
        logger.exception('Заказ №%s: не удалось загрузить состав заказа', _order_number(order))
        return items
    for info in infos:
        try:
            items.append(_item(info))
        except Exception:
            logger.exception('Заказ №%s: не удалось разобрать позицию', _order_number(order))
            items.append({'name': 'Позиция не разобрана, смотрите заказ в админке', 'size': '',
                          'count': MISSING, 'unit_price': MISSING, 'line_total': MISSING})
    return items


def order_email_context(order):
    phone = _text(getattr(order, 'phone_number', None))
    digits = re.sub(r'\D', '', phone)
    return {
        'order_number': _order_number(order),
        'site_name': SITE_NAME,
        'created_at': _created_at(order),
        'customer_name': _text(getattr(order, 'name', None)),
        'phone': phone,
        'phone_tel': f'+{digits}' if digits else '',
        'whatsapp_link': f'https://wa.me/{digits}' if digits else '',
        'items': _items(order),
        'total': format_rub(getattr(order, 'total', None)),
        'admin_url': _admin_url(order),
    }


def order_email_subject(order):
    return f'Новая заявка №{_order_number(order)} с сайта {SITE_NAME}'


def _from_email():
    return f'Сайт {SITE_NAME} <{settings.DEFAULT_FROM_EMAIL}>'


def build_order_email(order):
    context = order_email_context(order)
    message = EmailMultiAlternatives(
        subject=order_email_subject(order),
        body=render_to_string('shop/emails/new_order.txt', context),
        from_email=_from_email(),
        to=settings.ORDER_NOTIFY_EMAILS,
    )
    message.attach_alternative(render_to_string('shop/emails/new_order.html', context), 'text/html')
    return message


def build_fallback_email(order):
    """Запасное письмо без шаблонов и состава заказа — если полное собрать не удалось."""
    lines = [f'Новая заявка №{_order_number(order)} с сайта {SITE_NAME}', f'Дата: {_created_at(order)}', '']
    for label, field in (('Имя', 'name'), ('Телефон', 'phone_number')):
        try:
            lines.append(f'{label}: {_text(getattr(order, field, None))}')
        except Exception:
            pass
    lines += ['', 'Полное письмо собрать не удалось, состав заказа смотрите в админке.']
    admin_url = _admin_url(order)
    if admin_url:
        lines.append(admin_url)
    return EmailMessage(subject=order_email_subject(order), body='\n'.join(lines),
                        from_email=_from_email(), to=settings.ORDER_NOTIFY_EMAILS)


def send_order_email(order):
    """Письмо менеджеру. Заказ уже сохранён, поэтому сбой почты не должен превращаться в 500 для клиента."""
    number = _order_number(order)
    if not settings.ORDER_NOTIFY_EMAILS:
        logger.error('Письмо о заказе №%s не отправлено: не задан ORDER_NOTIFY_EMAILS', number)
        return
    try:
        try:
            message = build_order_email(order)
        except Exception:
            logger.exception('Письмо о заказе №%s: не собралось полное письмо, отправляю короткое', number)
            message = build_fallback_email(order)
        message.send()
    except (smtplib.SMTPException, OSError) as exc:
        # В лог только класс и текст ошибки SMTP: пароль в них не попадает.
        logger.error('Письмо о заказе №%s не отправлено: %s: %s', number, exc.__class__.__name__, exc)
        return
    except Exception:
        logger.exception('Письмо о заказе №%s не отправлено', number)
        return
    logger.info('Письмо о заказе №%s отправлено', number)
