from django.contrib import admin
from django.apps import AppConfig
from django.conf import settings
from aadil.models import Clothing
from decimal import Decimal


class CartConfig(AppConfig):
    name = 'cart'
 

class Cart(object):
    
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart 

    def add_product(self,product, quantity=1, override_quantity=False):
        product_id = str(product.id) 

        if product_id not in self.cart: 
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)} 

        if override_quantity: 
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        self.session.modified = True 

    def remove_product(self,product):
     
        product_id = str(product.id) 
        
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

  

    def __iter__(self):
    
        product_id = self.cart.keys() 

        products = Clothing.objects.filter(id__in = product_id) 

        cart =  self.cart.copy()

        for product in products:
            
            cart[str(product.id)]['product'] = product

        for item in cart.values(): 
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    def get_total_price(self):
        return sum(Decimal(item['price'])*item['quantity']for item in self.cart.values())

    def __len__(self):
           return sum(item['quantity']for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()            