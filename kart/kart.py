from store.models import Product
import uuid
from decimal import Decimal

class Kart():

    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if str(product_id) not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'qty': quantity}
        else:
            self.cart[product_id]['qty'] += quantity
        self.save()
    
    def remove(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def update(self, product, quantity):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = quantity
        self.save()
 
    def save(self):
        self.session.modified = True

    def size(self):
        ''' Calculate total item quantity in a cart''' 
        return sum(item['qty'] for item in self.cart.values()) or 0
        
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids, is_active=True, in_stock=True)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * int(item['qty'])
            yield item
            
    def get_total_price(self):
        return sum(Decimal(float(item['price'])*int(item['qty'])) for item in self.cart.values()) or 0


