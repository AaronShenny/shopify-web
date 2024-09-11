from django.shortcuts import render
from django.shortcuts import render,redirect
# from .. shop.models import Product
from .form import ProductForm
# Create your views here.
def CreateProduct(request):
    navbar = {'show_user_navbar': True}
    if request.POST:
        frm = ProductForm(request.POST,request.FILES)
        print(request.FILES) 
        if frm.is_valid():
            frm.save()
            return redirect('/')
    else:
        frm = ProductForm()
     # Add this line to check if products are being fetched
    return render(request, "create.html", {'navbar': navbar,'frm':frm})
