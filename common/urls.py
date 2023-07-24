from django.urls import path
from . import views
app_name='common'


urlpatterns=[
  
    path('',views.index,name='home'),
    path('view_destinations/', views.view_destinations, name='destinations'),
    path('destination_booking/', views.destination_booking, name='destination_booking'),
    path('blog/',views.blog,name='blog'),
    path('view_blog/',views.view_blog,name='view_blog'),
    path('aboutus',views.aboutus,name='about'),
    path('contactus',views.contactus,name='contact'),
    path('customer_register/',views.customer_register,name='customer_register'),
    path('customer_login/',views.customer_login,name='customer_login'),
    path('my_booking/',views.my_booking,name='my_booking'),
    path('view_profile/',views.view_profile,name='view_profile'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('customer_logout/',views.customer_logout,name='customer_logout'),
   

    path('admin_register/',views.admin_register,name='admin_register'),
    path('admin_login/',views.admin_login,name='admin_login'),
]