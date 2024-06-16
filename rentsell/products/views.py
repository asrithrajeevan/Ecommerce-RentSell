from django.shortcuts import render
from django.core.paginator import Paginator # To display product like page ways 
from . models import Products
# Create your views here.
def index(request):
    featured_product = Products.objects.order_by('priority')[:4]
    latest_product = Products.objects.order_by('-id')[:8]
    context = {
        'featured_product' : featured_product,
        'latest_product' : latest_product
    }
    return render(request, 'index.html', context)

def list_products(request):
    page = 1 
    name = ''
    if request.GET:
        page = request.GET.get('page',1) # 1 is default value
        name = request.GET.get('name')
        # print('name--->',request.GET)
    product_list = Products.objects.order_by('priority') # render the product basis of the priority
    product_paginator = Paginator(product_list, 8) # Paginator devide the entire product to 8 each pages
    # print('product_paginator--->',product_paginator)
    requested_page = product_paginator.get_page(page) # get_page will render the appropriate page
    # print('requested_page--->',requested_page)

    context = {
        'products' : requested_page
    }

    return render(request, 'products.html', context)

def detail_product(request,pk):
    product = Products.objects.get(pk=pk)
    # for single_product in product:
    # print('product-->',product.price)
    context = {
        'product' : product
    }
    return render(request, 'product_details.html', context)