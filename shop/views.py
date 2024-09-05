from django.shortcuts import render

# Create your views here.
def shop(request):
    navbar = {'show_user_navbar': True}  
    return render(request, "index.html",navbar)