from django.urls import path
from . import views

app_name = 'kart'

urlpatterns = [
    path('summary/',views.cart_summary, name='summary'),
    path('add_item/', views.cart_add_item, name ='cart_add_item'),
    path('remove_item/', views.cart_remove_item, name ='basket_delete'),
    path('update_item/', views.cart_update_item, name ='basket_update'),
]