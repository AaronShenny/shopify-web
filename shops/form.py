from django.forms import ModelForm
from shop.models import Product
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model= Product
        fields= '__all__'
    

class EditForm(ModelForm):
    pname = forms.CharField(
        label='Name',
        max_length=100,  # Specify max_length if required
        required=True,   # Set to True if the field is mandatory
    )
    pdesc = forms.CharField(
        label='Description',
        widget=forms.Textarea,  # Use Textarea widget for multiline input
        required=True,
    )
    pprice = forms.DecimalField(
        label='Price',
        max_digits=10,  # Adjust according to your model's price field configuration
        decimal_places=2,
        required=True,
    )

    class Meta:
        model = Product
        fields = ['pname','pdesc','pprice','images','show'] # Use this to include all fields from the model
