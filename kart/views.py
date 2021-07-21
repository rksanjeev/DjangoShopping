from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from .kart import Kart
from store.models import Product

# Create your views here.

def cart_summary(request):
    cart = Kart(request=request)
    return render(request, 'cart/summary.html', {'cart': cart})

def cart_add_item(request):
    cart = Kart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
    basketqty = cart.size()
    baskettotal = cart.get_total_price()
    response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
    return response

def cart_remove_item(request):
    cart=Kart(request)
    if request.POST.get('action') == 'delete':
        product_id = int(request.POST.get('productid'))
        cart.remove(product=product_id)

        basketqty = cart.size()
        baskettotal = cart.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response

def cart_update_item(request):
    cart = Kart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart.update(product=product_id, quantity=product_qty)
    basketqty = cart.size()
    baskettotal = cart.get_total_price()
    response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
    return response