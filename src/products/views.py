from django.http import Http404
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Products
from .Forms import ProductForm , RawProductForm
from django.db.models import Q



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




#In order to simplify how forms work in purely HTML format see below


# def Prodect_create_view(request):
#
#     if request.method == "POST":     #this is only to treat POST request for security reasons
#         my_new_title = request.POST.get('title')      #this is to capture the title value from the form
#         print(my_new_title)
#
#     context = {}
#     return render(request, "product/product_create.html", context)


#This is the official way to create forms in Django

def product_create_view(request):
     my_form = RawProductForm()
     if request.method == "POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            #now my data is good
            print(my_form.cleaned_data)
            Products.objects.create(**my_form.cleaned_data)   #here we will pass the data in the form the the Model (hence Databse)
        else:
            print(my_form.errors)
     context = {
         "form": my_form
     }
     return render(request, "product/product_create.html", context)

def product_detail_view(request):
    obj = Products.objects.get(id=1)
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


# def dynamic_lookup_view(request,id):
#     obj = Products.objects.get(id=id)
#     context = {
#         "object": obj
#     }
#     return render(request, "product/detail.html", context)

def dynamic_lookup_view(request,my_id):

    try:
        obj = Products.objects.get(id=my_id)
    except Products.DoesNotExist:
        raise Http404
    context = {
        "object": obj
    }
    return render(request, "product/detail.html", context)

def product_delete_view(request,my_id):
    obj = get_object_or_404(Products, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object" : obj
    }
    return render(request, "product/product_delete.html", context)

def product_list_view(request):
    queryset = Products.objects.all()   # give list of objects
    context = {
        "object_list" : queryset
    }
    return render(request, "product/product_list.html", context)