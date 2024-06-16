from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.add_to_cart, name='cart'),
]
