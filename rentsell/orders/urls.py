from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/', views.cart_view, name='add_to_cart'),
]
