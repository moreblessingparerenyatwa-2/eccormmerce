from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Order, OrderItem
from .forms import CheckoutForm

def home(request):
    featured_products = Product.objects.all()[:6]
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())
    return render(request, 'store/home.html', {
        'featured_products': featured_products,
        'cart_count': cart_count
    })


def product_list(request):
    products = Product.objects.all()
    categories = Product.objects.values_list('category', flat=True).distinct()
    category_filter = request.GET.get('category', '')
    
    if category_filter:
        products = products.filter(category=category_filter)
    
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values())
    
    return render(request, 'store/products.html', {
        'products': products,
        'categories': categories,
        'selected_category': category_filter,
        'cart_count': cart_count
    })


def add_to_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1

    request.session['cart'] = cart
    request.session.modified = True
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'store/cart_response.html', {'success': True})
    return redirect('cart')


def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for id, quantity in cart.items():
        try:
            product = Product.objects.get(id=id)
            item_total = product.price * quantity
            total += item_total

            items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total
            })
        except Product.DoesNotExist:
            pass

    cart_count = sum(cart.values())
    
    return render(request, 'store/cart.html', {
        'items': items,
        'total': round(total, 2),
        'cart_count': cart_count
    })


def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    if str(id) in cart:
        del cart[str(id)]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')


def checkout(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for id, quantity in cart.items():
        try:
            product = Product.objects.get(id=id)
            item_total = product.price * quantity
            total += item_total
            items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total
            })
        except Product.DoesNotExist:
            pass

    if not items:
        messages.warning(request, 'Your cart is empty!')
        return redirect('cart')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save()
            
            for id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=id)
                    OrderItem.objects.create(
                        product=product,
                        order=order,
                        quantity=quantity
                    )
                except Product.DoesNotExist:
                    pass
            
            request.session['cart'] = {}
            request.session.modified = True
            request.session['order_id'] = order.id
            
            return redirect('order_confirmed')
    else:
        form = CheckoutForm()

    cart_count = sum(cart.values())
    
    return render(request, 'store/checkout.html', {
        'form': form,
        'items': items,
        'total': round(total, 2),
        'cart_count': cart_count
    })


def order_confirmed(request):
    order_id = request.session.get('order_id')
    
    if not order_id:
        return redirect('home')
    
    try:
        order = Order.objects.get(id=order_id)
        order_items = OrderItem.objects.filter(order=order)
    except Order.DoesNotExist:
        return redirect('home')

    cart_count = 0
    
    return render(request, 'store/confirmation.html', {
        'order': order,
        'order_items': order_items,
        'cart_count': cart_count
    })


def checkout(request):
    cart = request.session.get('cart', {})

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save()

            for id, quantity in cart.items():
                product = Product.objects.get(id=id)
                OrderItem.objects.create(
                    product=product,
                    order=order,
                    quantity=quantity
                )

            request.session['cart'] = {}
            return redirect('order_confirmed')
    else:
        form = CheckoutForm()

    return render(request, 'store/checkout.html', {'form': form})


def order_confirmed(request):
    return render(request, 'store/confirmed.html')
