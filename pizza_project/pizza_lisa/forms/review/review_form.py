from django.forms import ModelForm
from pizza_lisa.models import ReviewModel

class ReviewForm(ModelForm):
    class Meta:
        model = ReviewModel
        fields = ["review"]