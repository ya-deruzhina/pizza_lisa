from rest_framework import serializers
from pizza_lisa.models import OrderModel


class ChangeStatusSerializer(serializers.Serializer):
    KIND_CHOICES = ["NEW","COOKING","TASTING","PACKING","IN_DELIVERY","ARCHIVE","CANCELED"]
    status = serializers.ChoiceField (choices= KIND_CHOICES)

    def update(self,instance,validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    


class ChangeDiscontSerializer(serializers.Serializer):
    discont = serializers.IntegerField ()

    def update(self,instance,validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
