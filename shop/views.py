from django.shortcuts import render,redirect
from .models import Product,Customers
from .form import ProductForm,UsersLoginForm
from django.contrib import messages
# Create your views here.
def shop(request):
    products = Product.objects.all()  
    navbar = {'show_user_navbar': True}
    if request.POST:
        frm = ProductForm(request.POST,request.FILES)
        print(request.FILES) 
        if frm.is_valid():
            frm.save()
            return redirect('create')
    else:
        frm = ProductForm()
    print(products)  # Add this line to check if products are being fetched
    return render(request, "index.html", {'products': products, 'navbar': navbar})


def login(request):
    navbar = {'show_user_navbar': True}
    if request.method == 'POST':
        frm = UsersLoginForm(request.POST)
        print(request.POST)
        
        if frm.is_valid():
            try:
                # Corrected the get() method with keyword arguments
                user = Customers.objects.get(name=request.POST['name'])
                print(user)
                print('Login Successful')
                return redirect('/')  # You can also use reverse('home') if you have a URL name
            except Customers.DoesNotExist:
                messages.error(request, 'User does not exist.')
            except Customers.MultipleObjectsReturned:
                messages.error(request, 'Multiple users found with this name.')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        frm = UsersLoginForm()
    return render(request, "login-user.html", {'navbar': navbar,'frm':frm})

def addtocart(request):
    if request.method ==  'POST':
        print(request.POST)