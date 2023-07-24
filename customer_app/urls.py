from django.urls import path
from . import views

app_name='customer_app'

urlpatterns=[
    path('base/',views.base,name='base'),
]