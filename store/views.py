from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .utils import *
from .forms import *

# Create your views here.
def store_home(request):
    data = cartData(request)
    cart_items = data['cartItems']
    products = Product.objects.all().order_by("-date_added")
    context={
        'products':products,
        'cart_items':cart_items,
    }
    return render(request, 'store/home.html', context)


def product_details(request,product_id):
    data = cartData(request)
    cart_items = data['cartItems']
    product=get_object_or_404(Product, pk=product_id)
    context={
        'product':product,
        'cart_items':cart_items,
    }
    return render(request, 'store/product_details.html', context)


def cart(request):
    data = cartData(request)
    order = data['order']
    items = data['items']
    cart_items = data['cartItems']
    context={
        'cart_items':cart_items,
        'order':order,
        'items':items,
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)
    order = data['order']
    cart_items = data['cartItems']
    grand_total=order['get_cart_total']
    delivery_fee=250
    grand_total+=delivery_fee

    if request.method=="POST":
        filled_form=checkout_form(request.POST)
        if filled_form.is_valid():
            first_name=filled_form.cleaned_data['first_name']
            last_name=filled_form.cleaned_data['last_name']
            phone_number=filled_form.cleaned_data['phone_number']
            email=filled_form.cleaned_data['email']
            customer, created = Customer.objects.get_or_create(email=email)
            customer.first_name=first_name
            customer.last_name=last_name
            customer.phone_number=phone_number
            customer.save()

            delivery_address=filled_form.cleaned_data['delivery_address']
            if delivery_address =='custom_address':
                city_or_town=filled_form.cleaned_data['city_or_town']
                estate=filled_form.cleaned_data['estate'] 
                street=filled_form.cleaned_data['street']
                building=filled_form.cleaned_data['building']
                additional_information=filled_form.cleaned_data['additional_information']
                
            elif  delivery_address =='CBD_pickup':
                city_or_town='Nairobi'
                estate='',
                street='Tom Mboya Street'
                building='Dominion House'
                additional_information='Shop B1.Right at the main entrance'

            shipping_address = Shipping_address.objects.create(
                city_or_town=city_or_town,
                estate=estate,
                street=street,
                building=building,
                additional_information=additional_information
            )
            shipping_address.save()

            cookieData = cookieCart(request)
            items = cookieData['items']
            order = Order.objects.create(
                customer=customer,
                shipping_address=shipping_address,
                complete=False,
                )
            for item in items:
                product = Product.objects.get(id=item['id'])
                orderItem = OrderItem.objects.create(
                    product=product,
                    order=order,
                    quantity=item['quantity'],
                )

            context={
            }
            return render(request, 'store/order_confirmation.html', context)
        else:
            form=filled_form
            context={
                'form':form,
            }
            return render(request,'store/checkout.html',context)
    else:
        form=checkout_form()
        context={
            'cart_items':cart_items,
            'order':order,
            'grand_total':grand_total,
            'delivery_fee':delivery_fee,
            'form':form
        }
    return render(request, 'store/checkout.html', context)