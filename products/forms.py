from django import forms
from products.models import Product


class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']


class ProductUpdateForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']
