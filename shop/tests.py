import smtplib
from decimal import Decimal
from unittest import mock

from django.core import mail
from django.test import TestCase, override_settings

from shop.models import Category, Orders, Product, ProductInfo
from shop.notifications import format_rub, send_order_email


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    DEFAULT_FROM_EMAIL='orders@example.com',
    ORDER_NOTIFY_EMAILS=['manager@example.com'],
    SITE_URL='https://cubekazan.ru',
)
class OrderEmailTests(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Коробки', slug='boxes', image_cat='shop/images_cat/x.jpg')
        product = Product.objects.create(category=category, name='Коробка 300×200×150', description='-',
                                         size='300×200×150', price_1=50)
        self.order = Orders.objects.create(name='Иван', phone_number='+7 (999) 123-45-67', pickup=False,
                                           address='Казань, ул. Баумана, 1', total=Decimal('4500'))
        ProductInfo.objects.create(order=self.order, product=product, count=100, price=Decimal('4500'))

    def test_email_contains_order(self):
        send_order_email(self.order)

        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertEqual(message.subject, f'Новая заявка №{self.order.id} с сайта cubekazan.ru')
        self.assertEqual(message.to, ['manager@example.com'])
        self.assertIn('<orders@example.com>', message.from_email)
        self.assertIn('Коробка 300×200×150', message.body)
        self.assertIn('100 шт × 45 ₽ = 4 500 ₽', message.body)
        self.assertIn('Казань, ул. Баумана, 1', message.body)
        html = message.alternatives[0][0]
        self.assertIn('tel:+79991234567', html)
        self.assertIn(f'https://cubekazan.ru/admin/shop/orders/{self.order.pk}/change/', html)

    def test_smtp_error_is_logged_not_raised(self):
        with mock.patch('django.core.mail.EmailMultiAlternatives.send',
                        side_effect=smtplib.SMTPAuthenticationError(535, b'auth failed')), \
                self.assertLogs('shop.notifications', 'ERROR'):
            send_order_email(self.order)

    @override_settings(ORDER_NOTIFY_EMAILS=[])
    def test_no_recipients_skips_sending(self):
        with self.assertLogs('shop.notifications', 'ERROR'):
            send_order_email(self.order)
        self.assertEqual(len(mail.outbox), 0)

    def test_format_rub(self):
        self.assertEqual(format_rub(15400), '15 400 ₽')
        self.assertEqual(format_rub(Decimal('12.5')), '12,50 ₽')
