from django.urls import path
from . import views

app_name = 'kart'

urlpatterns = [
    path('',views.cart_summary, name='summary'),
    path('add_item/', views.cart_add_item, name ='cart_add_item'),


]