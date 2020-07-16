from django.shortcuts import render
from .models import Product


def all_products(request):

    products = Product.objects.all()

    context = {
        'products': products,
    }
    """ call the folder from shop > templates > ... """
    return render(request, 'products/products.html', context)
