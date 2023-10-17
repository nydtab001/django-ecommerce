from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from django.views import generic

from cart.models import Cart, CartItem
from orders.models import Order, OrderItem
from products.models import Product


class CartDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cart

    def get_object(self, queryset=None):
        # Retrieve the cart object based on the logged-in user
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)  # Assuming authenticated user
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
    cart_item.update_price()
    cart_item.update_subtotal()
    cart_item.save()
    cart.update_totals()
    cart.save()
    return redirect(reverse('cart-detail'))  # Redirect to the cart detail view


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart = Cart.objects.get(user=request.user)
    cart_item.delete()
    cart.update_totals()
    cart.save()
    return redirect(reverse('cart-detail'))


@login_required
def checkouta(request):
    cart = get_object_or_404(Cart, user=request.user)
    order = Order.objects.create(user=request.user, total_quantity=cart.total_quantity, total_price=cart.total_price)
    order.save()
    for item in cart.cartitem_set.all():
        orderitem = OrderItem.objects.create(order=order, product=item.product,
                                             quantity=item.quantity, price=item.price, subtotal=item.subtotal)
        orderitem.save()
    # Clear the cart items
    '''cart.cartitem_set.all().delete()
    cart.update_totals()
    cart.save()
    return redirect(reverse('orders'))'''
