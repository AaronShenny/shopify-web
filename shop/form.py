from django.forms import ModelForm
from . models import Product,Customers
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model= Product
        fields= '__all__'

class UsersLoginForm(ModelForm):
    password = forms.CharField(
        label='Password',  # Custom label
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'id': 'exampleFormControlTextarea1', 
            'placeholder': 'Enter your password', 
            'required': True
        })
    )
    emailid = forms.EmailField(
        label='Email ID',  # Custom label
        max_length=200, 
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'id': 'exampleFormControlTextarea1', 
            'placeholder': 'Enter your email', 
            'required': True
        })
    )

    class Meta: 
        model = Customers
        fields = ['emailid', 'password'] 