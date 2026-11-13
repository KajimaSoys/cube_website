"""Расчёт цены по тарифной сетке «от N шт» — так же, как на фронте (Order.vue: currentPriceOne/calculatePrice)."""
from decimal import Decimal


def unit_price(tiers, count):
    """Цена за штуку для заданного количества.

    tiers — итерируемое из (порог, цена). Берётся цена самого большого порога, который не превышает count.
    Если count меньше всех порогов, берётся цена самого маленького порога (на фронте это порог «от 1 шт»).
    Возвращает None, если у товара нет цен.
    """
    tiers = sorted(tiers, key=lambda t: t[0])
    if not tiers:
        return None
    price = tiers[0][1]
    for threshold, tier_price in tiers:
        if count >= threshold:
            price = tier_price
    return Decimal(price)


def line_total(tiers, count):
    """Стоимость позиции заказа: цена за штуку × количество (как ProductInfo.price на фронте)."""
    price = unit_price(tiers, count)
    return None if price is None else (price * count).quantize(Decimal('0.01'))
