from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from cart.models import Cart
from orders.models import Order, OrderItem


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class OrderDetailView(LoginRequiredMixin, generic.DetailView):
    model = Order

    def get_object(self, queryset=None):
        # Retrieve the cart object based on the logged-in user
        order = get_object_or_404(Order, id=self.kwargs['pk'], user=self.request.user)
        return order
