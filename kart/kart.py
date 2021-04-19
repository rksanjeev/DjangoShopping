import uuid

class Kart():

    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('session_data')
        if 'session_data' not in request.session:
            cart = self.session['session_data'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = product.id
        if str(product_id) not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'qty': quantity}
        self.session.modified = True
    
    def size(self):
        ''' Calculate total item quantity in a cart'''
        print([item for item in self.cart.values()])
        total_qty = sum(item['qty'] for item in self.cart.values())
        print(total_qty)
        return total_qty
        


