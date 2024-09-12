from django.forms import ModelForm
from . models import Product,Customers
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model= Product
        fields= '__all__'

class UsersLoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta: 
        model= Customers
        fields= '__all__'