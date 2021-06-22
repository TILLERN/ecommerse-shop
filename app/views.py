from django.shortcuts import render,redirect,get_object_or_404
from store.utils import *
from .models import *
from store.models import *
# Create your views here.
def app_home(request):
    data = cartData(request)
    cart_items = data['cartItems']
    abouts=About.objects.all()
    context={
        'cart_items':cart_items,
        'abouts':abouts,
    }
    return render(request, 'app/home.html', context)

def contacts(request):
    data = cartData(request)
    cart_items = data['cartItems']
    socials = Social_media.objects.all()
    phone_numbers=Phone_number.objects.all()
    emails=Email.objects.all()
    physical_addresses=Physical_address.objects.all()
    context={
        'cart_items':cart_items,
        'socials':socials,
        'phone_numbers':phone_numbers,
        'emails':emails,
        'physical_addresses':physical_addresses,
    }
    return render(request, 'app/contacts.html', context)

def orders(request):
    orders = Order.objects.all().order_by('-is_new','-date_ordered')
    context={
        'orders':orders,
    }
    return render(request, 'app/orders.html', context)


def order_details(request,order_id):
    order=get_object_or_404(Order, pk=order_id)
    order.is_new=False
    order.save()
    items = order.orderitem_set.all()
    context={
        'order':order,
        'items':items,
    }
    return render(request, 'app/order.html', context)

def mark_as_complete(request,order_id):
    order=get_object_or_404(Order, pk=order_id)
    order.complete=True
    order.save()
    return redirect("orders")