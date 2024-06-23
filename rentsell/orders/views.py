from django.shortcuts import render, redirect
from .models import Order, OrderedItem

# Create your views here.
def cart_view(request):
    user = request.user
    customer = user.customer
    cart_obj, create = Order.objects.get_or_create(
        order_status = Order.CART_STAGE,
        owner = customer
    )
    return render(request, 'cart.html', {'cart' : cart_obj})

def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer
        quantity = int(request.POST.get('quantity'))
        product_id = request.POST.get('product_id')
        cart_obj, create = Order.objects.get_or_create(
            order_status = Order.CART_STAGE,
            owner = customer,
        )
        ordered_item = OrderedItem.objects.create(
            product = product_id,
            owner = cart_obj,
            quantity = quantity
        )
    return redirect("cart")
