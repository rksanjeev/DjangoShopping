from django.shortcuts import get_object_or_404, render
from .models import Product, Category
# Create your views here.

def list_products(request):
    products = {'products': Product.objects.all()}
    return render(request, 'store/home.html', products)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/details.html', {'product':product})
    
def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(Category=category)
    return render(request, 'store/products/category.html', {'category':category,'products':products})