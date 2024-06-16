from django.db import models
from customers.models import Customer
from products.models import Products

'''
    cart is only for a purticular user so, when we creating a cart model,
    it want a connection between user and product to the cart modal, A user can have multiple orders and multiple carts
    so it's connection want a many to many field relation
'''

class Order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE ,'Delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERD = 3
    ORDER_REJECTED = 4
    STATUS_CHOICES = (
        (ORDER_CONFIRMED,'ORDER_CONFIRMED'),
        (ORDER_PROCESSED,'ORDER_PROCESSED'),
        (ORDER_DELIVERD,'ORDER_DELIVERD'),
        (ORDER_REJECTED,'ORDER_REJECTED'),
        )
    order_status = models.IntegerField(choices=STATUS_CHOICES, default=CART_STAGE)
    owner = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL, related_name='orders') # In some conditions when we delete a customer we want to keep the cart data(on_delete=set_null)
    delete_status = models.IntegerField(choices = DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True) # auto matically add created date of a product when a product adding
    updated_at = models.DateTimeField(auto_now=True) # when a change came in this product modal, at that time will store this updated_at field

# a cart have multiple cart items
class OrderedItem(models.Model):
    product = models.ForeignKey(Products, related_name='added_cart', null=True, on_delete=models.SET_NULL) # for access product details
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='added_items') # One order have multiple items