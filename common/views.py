from django.shortcuts import render

# Create your views here.

def base(request):
   
    return render(request,'common_templates/base.html')

def index(request):
   
    return render(request,'common_templates/index.html')

def view_destinations(request):
   
    return render(request,'common_templates/view_destinations.html')

def destination_booking(request):
   return render(request,'common_templates/destination_booking.html')

def blog(request):
   
    return render(request,'common_templates/blog.html')

def view_blog(request):
   
    return render(request,'common_templates/view_blog.html')

def aboutus(request):
   
    return render(request,'common_templates/aboutus.html')

def contactus(request):
   
    return render(request,'common_templates/contactus.html')


def customer_register(request):
   
    return render(request,'common_templates/customer_register.html')

def customer_login(request):
   
    return render(request,'common_templates/customer_login.html')


def my_booking(request):
   
    return render(request,'common_templates/my_booking.html')

def view_profile(request):
   
    return render(request,'common_templates/view_profile.html')

def edit_profile(request):
   
    return render(request,'common_templates/edit_profile.html')


def change_password(request):
   
    return render(request,'common_templates/change_password.html')

def customer_logout(request):
   
    return render(request,'common_templates/customer_logout.html')
# /////////////// ADMIN //////////////////////

def admin_register(request):
   
    return render(request,'common_templates/admin_register.html')


def admin_login(request):
   
    return render(request,'common_templates/admin_login.html')


