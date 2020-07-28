from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product


def bag_contents(request):

    bag_items = []
    # Assign all local values to 0
    subtotal = 0
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal = quantity * product.price
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'subtotal': subtotal,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_TRIM_TRESHOLD:
        free_trim_delta = settings.FREE_TRIM_TRESHOLD - total
    else:
        delivery = 0
        free_trim_delta = 0

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'subtotal': subtotal,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_trim_delta': free_trim_delta,
        'free_trim_treshold': settings.FREE_TRIM_TRESHOLD,
        'grand_total': grand_total,
    }

    return context
