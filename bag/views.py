from django.shortcuts import render


def view_bag(request):
    """ shopping bag template """
    return render(request, 'bag/bag.html')
