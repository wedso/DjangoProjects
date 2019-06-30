from django.shortcuts import render
from .models import Products
from .Forms import ProductForm


# Create your views here.

# def Prodect_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "product/product_create.html", context)

def Prodect_create_view(request):
    context = {}
    return render(request, "product/product_create.html", context)



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
        'object': obj
    }
    return  render(request,"product/detail.html", context)
