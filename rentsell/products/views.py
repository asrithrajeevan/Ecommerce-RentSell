from django.shortcuts import render
from django.core.paginator import Paginator # To display product like page ways 
from . models import Products
# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_products(request):
    page = 1 
    name = ''
    if request.GET:
        page = request.GET.get('page',1)
        name = request.GET.get('name')
        # print('name--->',request.GET)
    product_list = Products.objects.all()
    product_paginator = Paginator(product_list, 8)
    requested_page = product_paginator.get_page(page)
    context = {
        'products' : requested_page
    }

    return render(request, 'products.html', context)

def detail_product(request):
    return render(request, 'product_details.html')