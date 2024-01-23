"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from cart.views import CartDetailView, add_to_cart, remove_from_cart, update_quantity
from orders.views import OrderListView, OrderDetailView
from payments.views import checkout, payment_completed, payment_failed
from products.views import ProductList, ProductCreateView, ProductDetailView, update_product, product_search
from reviews.views import add_review
from users import views as user_views

from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductList.as_view(), name='home'),
    path('profile/', views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('category/<slug:category_slug>/', ProductList.as_view(), name='category_detail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('product/update/<int:pk>', update_product, name='product-create'),
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update-quantity/<int:cart_item_id>/', update_quantity, name='update-quantity'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('orders/<uuid:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('checkout/', checkout, name='checkout'),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-completed/', payment_completed, name='success'),
    path('payment-failed/', payment_failed, name='fail'),
    path('write-review/<int:product_id>/', add_review, name='add_review'),
    path('search_results/', product_search, name='search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
