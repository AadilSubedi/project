
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from aadil.models import Clothing #
from .cart import Cart
from django.views.decorators.http import require_POST
from .forms import AddToBasket

@require_POST
def cart_add(request,product_id):
    
    cart = Cart(request)

    
    product = get_object_or_404(Clothing, id = product_id)

    
    form = AddToBasket(request.POST)

    if form.is_valid():
        data = form.cleaned_data 

        cart.add_product(product=product,quantity=data['quantity'],override_quantity=data['override'],body_size=data['size'])

    return redirect('cart:cart_detail') 

@require_POST
def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Clothing, id = product_id)
    cart.remove_product(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_form'] = AddToBasket(initial={
                                        'quantity':item['quantity'],
                                        'override': True,
                                        'size':item['size']

        })
    return render(request,'cart/Cart.html',{'cart':cart})