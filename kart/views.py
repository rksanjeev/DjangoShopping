from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from .kart import Kart
from store.models import Product

# Create your views here.

def cart_summary(request):
    return render(request, 'cart/summary.html')

def cart_add_item(request):
    cart = Kart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
    response = JsonResponse({'a':'b'})
    return response
