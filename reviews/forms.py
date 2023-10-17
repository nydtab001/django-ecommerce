from django import forms
from reviews.models import ProductReview


class CreateReviewForm(forms.ModelForm):
    rating = forms.IntegerField(
        label='',
        widget=forms.RadioSelect()
    )

    class Meta:
        model = ProductReview
        fields = ['rating', 'title', 'comment']
