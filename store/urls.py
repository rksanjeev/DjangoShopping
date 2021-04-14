from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.list_products, name = 'listproducts'),
    path('item/<slug:slug>/', views.product_detail, name= 'product_detail')


]