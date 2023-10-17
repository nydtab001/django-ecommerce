from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
#from users.models import OrderHistory, Order, Profile
from users.forms import UserUpdateForm, UserRegisterForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'u_form': u_form})


'''class Orders(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = "users/order_list.html"
    context_object_name = "orders_list"
    ordering = ["-order_date"]

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user)'''
