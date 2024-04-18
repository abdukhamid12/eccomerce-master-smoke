from django.db.models import Sum
from django.shortcuts import render, get_object_or_404

from store.models import *


# Create your views here.
def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)


def detail(request, pk):
    products = get_object_or_404(Product, pk=pk)
    context = {
        "product": products
    }
    return render(request, 'store/detail.html', context)


def cart(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(complete=False)
        items = order.orderitem_set.all()
    else:
        # Create empty cart for now for non-logged in user
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'store/checkout.html', context)

