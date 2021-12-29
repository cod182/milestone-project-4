
from decimal import Decimal

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    delivery = Decimal(5.00)

    grand_total = total + delivery
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total
    }

    return context
