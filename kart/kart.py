import uuid

class Kart():

    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = product.id
        if str(product_id) not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'qty': quantity}
        self.session.modified = True
    
    def size(self):
        ''' Calculate total item quantity in a cart'''
        return sum(item['qty'] for item in self.cart.values())
        


