from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_home, name='store_home'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]