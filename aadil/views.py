
from django.shortcuts import render, get_object_or_404
from .models import Category, Clothing
from cart.forms import AddToBasket


def list_product(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Clothing.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'product/list_clothes.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Clothing,
                                id=id,
                                slug=slug,
                                available=True)
    
    cart_form=AddToBasket()
    return render(request,
                  'product/detail_product.html',
                  {'product': product,
                  'cart_form':cart_form,
                   })
                  

def Quiz(request):
    return render(request, 'product/Quiz.html') 

    
