from rest_framework import serializers
from pizza_lisa.models import ReviewModel

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ["user","pizza","review"]