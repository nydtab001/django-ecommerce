from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import generic

from products.forms import ProductUpdateForm
from products.models import Product, Category


class ProductList(generic.ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        # Get the category slug from the URL
        try:
            category_slug = self.kwargs['category_slug']
            # Filter the products based on the category slug
            queryset = super().get_queryset()
            queryset = queryset.filter(category__slug=category_slug)
            return queryset
        except KeyError:
            queryset = super().get_queryset()
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        try:
            category_query = Category.objects.get(name=self.kwargs['category_slug'])
            context['category_query'] = category_query
        except KeyError:
            pass
        return context


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'category']

    def form_valid(self, form):
        return super().form_valid(form)


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        p_form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if p_form.is_valid():
            if not p_form.cleaned_data.get('image'):
                # Use the default image value
                product.image = 'product_images/default.svg'
            product.save()
            return redirect('product-detail', pk=pk)
    else:
        p_form = ProductUpdateForm(instance=product)
    return render(request, 'products/product_update.html', {'p_form': p_form})


class ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        even_numbers = list(range(2, 11, 2))  # Generates a list of even numbers from 2 to 10
        context['stars'] = even_numbers
        return context


def product_search(request):
    query = request.GET.get('q')
    results = []
    categories = Category.objects.all()

    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'products/search_results.html', {'categories': categories, 'query': query, 'results': results})
