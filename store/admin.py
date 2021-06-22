from django.contrib import admin
from .models import  *
# Register your models here.
class Cartegory_admin(admin.ModelAdmin):
    list_display=['name']

admin.site.register(Cartegory,Cartegory_admin)

class Product_admin(admin.ModelAdmin):
    list_display=['name','cartegory','description','price']

admin.site.register(Product,Product_admin)

class Customer_admin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','phone_number']

admin.site.register(Customer,Customer_admin)

class Order_admin(admin.ModelAdmin):
    list_display=['id','date_ordered','complete']

admin.site.register(Order,Order_admin)

class OrderItem_admin(admin.ModelAdmin):
    list_display=['product','quantity','order']

admin.site.register(OrderItem,OrderItem_admin)

class Shipping_address_admin(admin.ModelAdmin):
    list_display=['city_or_town','estate','street','building','additional_information']

admin.site.register(Shipping_address,Shipping_address_admin)