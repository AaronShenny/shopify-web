from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
# from .. shop.models import Product
from .form import ProductForm,EditForm
from shop.models import Product
from django.contrib import messages
# Create your views here.

def index(request):
    products = Product.objects.all()  
    navbar = {'show_user_navbar': False}
    # if request.POST:
    #     frm = ProductForm(request.POST,request.FILES)
    #     print(request.FILES) 
    #     if frm.is_valid():
    #         frm.save()
    #         return redirect('create')
    # else:
    #     frm = ProductForm()
    print(products)  # Add this line to check if products are being fetched
    return render(request, "index-admin.html", {'products': products, 'navbar': navbar})

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

def EditProduct(request, id):
    navbar = {'show_user_navbar': True}
    # Use get_object_or_404 for better error handling
    product = get_object_or_404(Product, id=id)
    
    if request.method == 'POST':
        frm = EditForm(request.POST,request.FILES, instance=product)
        if frm.is_valid():
            frm.save()  # Save changes to the database
            messages.success(request, 'Product details updated successfully!')
            return redirect('/')  # Redirect to a list view or another page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        frm = EditForm(instance=product) 
    
    return render(request, "edit.html", {'navbar': navbar, 'frm': frm})

def delete_product(request, pk):
    """View to delete a product."""
    product = get_object_or_404(Product, pk=pk)

    # Ensure that deletion only happens on a POST request
    
    product.delete()
    return redirect('/')  # Redirect to the list view after deletion
    
    # If the request is GET, return a response or a confirmation message
    return HttpResponse("To delete the product, please confirm through a POST request.")  # Redirect to the list view or any other view after deletion