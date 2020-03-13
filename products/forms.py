from django import forms

from products.models import Review, RestaurantReview

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']

    
class RestaurantReviewForm(forms.ModelForm):
    class Meta:
        model = RestaurantReview
        fields = ['comment']