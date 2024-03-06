from rest_framework import serializers
from pizza_lisa.models import BasketModel

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketModel
        fields = ['user','pizza','count']
        
        def create(self, validated_data):
            return BasketModel.objects.create(**validated_data)
        