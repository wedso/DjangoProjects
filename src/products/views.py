from django.shortcuts import render
from .models import Products
# Create your views here.

def product_detail_view(request):
    obj = Products.objects.get(id=2)


    # context = {
    #     'title' : obj.title,
    #     'description'  : obj.description,
    #     'price'    : obj.price,
    #     "Summary"    : obj.summary
    #
    # }

    context = {
        'object' : obj
    }

    return  render(request, "product/detail.html" , context)