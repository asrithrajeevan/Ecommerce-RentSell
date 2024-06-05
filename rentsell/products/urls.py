from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.list_products, name='products'),
    path('product_details/', views.detail_product, name='product_details'),
]
