from .kart import Kart

def cart(request):
    return {'cart' : Kart(request)}