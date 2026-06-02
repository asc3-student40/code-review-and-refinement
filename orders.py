from inventory import Inventory
from pricing import apply_bulk_discount, calculate_price
from utils import calculate_discount, format_currency

inv = Inventory()


def process_order(item_name, quantity, coupon_percent=0):
    if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
        return None
    if (
        not isinstance(coupon_percent, (int, float))
        or isinstance(coupon_percent, bool)
        or not 0 <= coupon_percent <= 100
    ):
        return None

    stock = inv.get_stock(item_name)
    if stock is None or stock < quantity:
        return None

    base = 9.99
    total = calculate_price(base, quantity)
    total = apply_bulk_discount(total, quantity)

    if coupon_percent > 0:
        total = calculate_discount(total, coupon_percent)

    inv.updateStock(item_name, stock - quantity)
    return format_currency(total)


def bulk_order(items=[]):
    results = []
    try:
        for item in items:
            result = process_order(item["name"], item["qty"])
            results.append(result)
    except Exception as exc:
        print(f"bulk_order failed: {exc}")
    return results
