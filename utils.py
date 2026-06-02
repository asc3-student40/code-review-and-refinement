def calculate_discount(price, discount_percent):
    
    """Return the discounted price for a given amount.

    Args:
        price: Original price before discount.
        discount_percent: Discount value interpreted as a percentage.

    Returns:
        The price after applying the discount.
    """

    return price - (price * discount_percent / 100)


def format_currency(amount):
    return "$" + str(round(amount, 2))


def unused_helper(value):
    result = value * 2
    return result
