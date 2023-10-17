from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from orders.models import Order, OrderItem
from products.models import Product
from reviews.forms import CreateReviewForm


# Create your views here.
from reviews.models import ProductReview


@login_required
def add_review(request, product_id):
    if not OrderItem.objects.filter(order__user=request.user, product_id=product_id).exists():
        product = get_object_or_404(Product, pk=product_id)
        return HttpResponse(f"purchase {product} from this store before leaving a review")
    try:
        u_review = ProductReview.objects.filter(user=request.user, product__id=product_id).first()
        if request.method == 'POST':
            review = CreateReviewForm(request.POST, instance=u_review)
            if review.is_valid():
                review.save()
                messages.success(request, "Thank you your review has been updated!")
                return redirect("product-detail", pk=product_id)
            else:
                messages.error(request, "There was an issue with your review.")
        else:
            review = CreateReviewForm(instance=u_review)
            return render(request, 'reviews/review_form.html', {'r_form': review})
    except ProductReview.DoesNotExist:
        if request.method == 'POST':
            r_form = CreateReviewForm(request.POST)
            print(r_form)
            if r_form.is_valid():
                review = r_form.save(commit=False)
                review.user = request.user
                review.rating = request.POST.get('rating')
                product = get_object_or_404(Product, pk=product_id)
                review.product = product
                review.save()
                print("saved")
                return redirect('product-detail', pk=product_id)
        else:
            r_form = CreateReviewForm()
        return render(request, 'reviews/review_form.html', {'r_form': r_form})
