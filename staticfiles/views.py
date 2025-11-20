import uuid

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm

from cart.models import Cart
from orders.models import Order, OrderItem


@login_required
def checkout(request):
    # Assuming you have retrieved cart items from the user's cart
    host = request.get_host()
    unique_id = uuid.uuid4().hex[:8]

    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cartitem_set.all()
    total_price = cart.total_price * 100  # Convert to cents

    line_items = []

    for cart_item in cart_items:
        line_item = {
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(cart_item.price * 100),  # Convert to cents
                'product_data': {
                    'name': cart_item.product.name,
                },
            },
            'quantity': cart_item.quantity,
        }
        line_items.append(line_item)

    paypal_dict = {
        'business': settings.PAYPAL_RECIEVER_EMAIL,
        'amount': cart.total_price,
        'item_name': str(unique_id),
        'invoice': 'INVOICE_NO-3',
        'currency_code': 'USD',
        'notify_url': request.build_absolute_uri(reverse("paypal-ipn")),
        'return': request.build_absolute_uri(reverse("success")),
        'cancel_return': request.build_absolute_uri(reverse("fail"))
    }

    pp_button = PayPalPaymentsForm(initial=paypal_dict)

    context = {'line_items': line_items,
               'total_price': total_price,
               'pp_button': pp_button
               }
    return render(request, 'payments/payment.html', context)


def payment_completed(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.cartitem_set.all()
    order = Order.objects.create(user=request.user, total_quantity=cart.total_quantity, total_price=cart.total_price)
    order.save()
    for item in cart_items():
        orderitem = OrderItem.objects.create(order=order, product=item.product,
                                             quantity=item.quantity, price=item.price, subtotal=item.subtotal)
        orderitem.save()

    cart.cartitem_set.all().delete()
    cart.update_totals()
    cart.save()
    return render(request, 'payments/payment_completed.html')


def payment_failed(request):
    return render(request, 'payments/payment_failed.html')
