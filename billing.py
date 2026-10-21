GST_RATE = 0.05
DISCOUNT_RATE = 0.10
DISCOUNT_THRESHOLD = 300


def calculate_total(items):
    
    subtotal = 0
    for price, quantity in items:
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative")
        subtotal += price * quantity

    discount = subtotal * DISCOUNT_RATE if subtotal > DISCOUNT_THRESHOLD else 0
    taxable = subtotal - discount
    gst = taxable * GST_RATE
    return round(taxable + gst, 2)