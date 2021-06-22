from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_home, name='app_home'),
    path('contacts/', views.contacts, name='contacts'),
    path('orders/', views.orders, name='orders'),
    path('order/<int:order_id>/', views.order_details, name='order_details'),
    path('mark_as_complete/<int:order_id>/', views.mark_as_complete, name='mark_as_complete'),
]