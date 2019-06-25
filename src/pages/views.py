

from django.http import HttpResponse
from  django.shortcuts import render

# Create your views here.

def home_view(request , *args,**kwargs):
  #    return HttpResponse("<h1>Hello World</h1>")   # String for HTML Code
       return render(request, "home.html", {})

def contact_view(request , *args,**kwargs):
  #    return HttpResponse("<h1>Contact page</h1>")   # String for HTML Code
    return render(request , "contact.html" , {})

def about_view(request , *args,**kwargs):
  #    return HttpResponse("<h1>Hello World</h1>")   # String for HTML Code

       my_context = {
           "title" : "Wedso Company",
           "my_text" : "This is about our company",
           "my_number" : 6137770001,
           "my_list" : {123,456,789,741,852,963,753,951,456,96356,"abc"}
       }
       return render(request ,"about.html", my_context)