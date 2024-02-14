from rest_framework import serializers
from pizza_lisa.models import CatalogModel


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogModel
        fields = ["name_pizza","ingredients","price","price_disсont"]
        
    def create(self, validated_data):
        return CatalogModel.objects.create(**validated_data)
    

class UpdateCatalogSerializer(serializers.Serializer):
    name_pizza = serializers.CharField(required=False)
    ingredients = serializers.CharField(required=False)
    price = serializers.FloatField(required=False)
    price_disсont = serializers.FloatField(required=False)

    def update(self,instance,validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance