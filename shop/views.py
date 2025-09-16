from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.select_related("category").all()
    return render(request, "shop/product_list.html", {"products": products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "shop/product_detail.html", {"product": product})

def about(request):
    return render(request, "shop/about.html")

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    qty = int(request.POST.get('quantity', 1))
    cart[str(product_id)] = cart.get(str(product_id), 0) + qty
    request.session['cart'] = cart
    return redirect('cart')

def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    total = 0
    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({'product': product, 'quantity': quantity, 'subtotal': subtotal})
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart')
