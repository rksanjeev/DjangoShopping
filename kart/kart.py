import uuid

class Kart():

    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('session_data', None)
        if 'session_key' not in request.session:
            cart = self.session['session_data'] = {'id' : str(uuid.uuid4())}
        self.cart = cart

    def add(self, product):
        product_id = product.id
        if str(product_id) not in self.cart:
            self.cart[str(product_id)] = {'price':product.price}
        self.session.modified = True

        


