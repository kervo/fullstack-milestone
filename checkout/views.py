from django.shortcuts import render, reverse, redirect
from django.contrib import messages


from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You haven't bought anything yet!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HAtxPGa7MB2SmjZOqR1e3XZOIwEcXH4jbqgPyv8stQxu4AOWDFZTEH4DTs5CtOjGQEcLw169mcyCu1eFhZqxeTE00hToKOE9q',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
