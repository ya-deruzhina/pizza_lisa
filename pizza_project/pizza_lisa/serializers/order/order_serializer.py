from rest_framework import serializers
from pizza_lisa.models import OrderModel,PizzaInOrder

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['user','name','phone','comment','address']
        
        def create(self, validated_data):
            return OrderModel.objects.create(**validated_data)
        
class OrderPizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaInOrder
        fields = ['order','pizza','count','price_one']
        
        def create(self, validated_data):
            return PizzaInOrder.objects.create(**validated_data)