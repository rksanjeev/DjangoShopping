from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.list_products, name = 'all_products'),
    path('item/<slug:slug>/', views.product_detail, name= 'product_detail'),
    path('search/<slug:slug>/', views.category_list, name= 'category_list'),


]
