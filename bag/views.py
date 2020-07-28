from django.shortcuts import render, redirect
from django.contrib import messages


def view_bag(request):
    # shopping bag template
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    # adding items to shopping bag

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, 'Product added to The Paw Shop!')

    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
