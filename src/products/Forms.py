from django import forms

from .models import Products

#This is a regular form without
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
           'title',
           'description',
           'price'
        ]


#this is  a Django Form
class RawProductForm(forms.Form):
    title       =   forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder":"Enter Product name"}) )
    description =   forms.CharField(
        required=False ,
        widget=forms.Textarea(
            attrs={
                "placeholder" : "Enter Product Description",
                "class" : "new-class-name two",
                "id"    : "my-id-for-textarea",
                "row"   : 20,
                'cols'  : 120
             }
        )
    )
    price       =   forms.DecimalField(initial=999.99)


