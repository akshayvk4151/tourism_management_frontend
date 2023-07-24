from django.urls import path
from . import views
app_name='admin_app'


urlpatterns=[
    path('base',views.base,name='base'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('all_customers/',views.all_customers,name='all_customers'),
    path('add_destination/',views.add_destination,name='add_destination'),
    path('view_destination/',views.view_destination,name='view_destination'),
    path('edit_destination/',views.edit_destination,name='edit_destination'),
    path('add_blog/',views.add_blog,name='add_blog'),
    path('adminView_blog/',views.adminView_blog,name='adminView_blog'),
    path('adminBlog_edit/',views.adminBlog_edit,name='adminBlog_edit'),
    path('view_booking/',views.view_booking,name='view_booking'),
    path('view_queries/',views.view_queries,name='view_queries'),
    path('change_password/',views.change_password,name='change_password'),
]