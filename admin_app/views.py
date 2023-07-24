from django.shortcuts import render

# Create your views here.

def base(request):
   return render(request,'admin_app_templates/base.html')

def admin_dashboard(request):
   return render(request,'admin_app_templates/admin_dashboard.html')

def all_customers(request):
   return render(request,'admin_app_templates/all_customers.html')

def add_destination(request):
   return render(request,'admin_app_templates/add_destination.html')

def view_destination(request):
   return render(request,'admin_app_templates/view_destination.html')

def edit_destination(request):
   return render(request,'admin_app_templates/edit_destination.html')

def add_blog(request):
   return render(request,'admin_app_templates/add_blog.html')

def adminView_blog(request):
   return render(request,'admin_app_templates/adminView_blog.html')


def adminBlog_edit(request):
   return render(request,'admin_app_templates/adminBlog_edit.html')

def view_booking(request):
   return render(request,'admin_app_templates/view_booking.html')

def view_queries(request):
   return render(request,'admin_app_templates/view_queries.html')

def change_password(request):
   return render(request,'admin_app_templates/change_password.html')