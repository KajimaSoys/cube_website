"""Уведомления менеджеру о новых заказах с сайта."""
import logging
import re
import smtplib
from decimal import Decimal, ROUND_HALF_UP

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone

logger = logging.getLogger(__name__)

SITE_NAME = 'cubekazan.ru'


def format_rub(value):
    """15400 -> '15 400 ₽', 12.5 -> '12,50 ₽'. Пробелы неразрывные, чтобы сумма не переносилась."""
    value = Decimal(value).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    whole, _, frac = f'{value:,.2f}'.partition('.')
    text = whole.replace(',', ' ')
    if frac != '00':
        text += f',{frac}'
    return f'{text} ₽'


def order_email_context(order):
    items = []
    # ProductInfo.price — стоимость всей позиции (цена за штуку × количество), см. shop/pricing.line_total.
    for info in order.productinfo_set.select_related('product').order_by('pk'):
        unit = info.price / info.count if info.count else info.price
        items.append({
            'name': info.product.name,
            'size': info.product.size or '',
            'count': info.count,
            'unit_price': format_rub(unit),
            'line_total': format_rub(info.price),
        })

    admin_url = ''
    if settings.SITE_URL:
        admin_url = settings.SITE_URL + reverse('admin:shop_orders_change', args=[order.pk])

    return {
        'order': order,
        'phone_tel': '+' + re.sub(r'\D', '', order.phone_number),
        'site_name': SITE_NAME,
        'created_at': timezone.localtime(order.created_at).strftime('%d.%m.%Y %H:%M'),
        'items': items,
        'total': format_rub(order.total),
        'admin_url': admin_url,
    }


def order_email_subject(order):
    return f'Новая заявка №{order.id} с сайта {SITE_NAME}'


def build_order_email(order):
    context = order_email_context(order)
    message = EmailMultiAlternatives(
        subject=order_email_subject(order),
        body=render_to_string('shop/emails/new_order.txt', context),
        from_email=f'Сайт {SITE_NAME} <{settings.DEFAULT_FROM_EMAIL}>',
        to=settings.ORDER_NOTIFY_EMAILS,
    )
    message.attach_alternative(render_to_string('shop/emails/new_order.html', context), 'text/html')
    return message


def send_order_email(order):
    """Письмо менеджеру. Заказ уже сохранён, поэтому сбой почты не должен превращаться в 500 для клиента."""
    if not settings.ORDER_NOTIFY_EMAILS:
        logger.error('Письмо о заказе №%s не отправлено: не задан ORDER_NOTIFY_EMAILS', order.id)
        return
    try:
        build_order_email(order).send()
    except (smtplib.SMTPException, OSError) as exc:
        # В лог только класс и текст ошибки SMTP: пароль в них не попадает.
        logger.error('Письмо о заказе №%s не отправлено: %s: %s', order.id, exc.__class__.__name__, exc)
        return
    logger.info('Письмо о заказе №%s отправлено', order.id)
