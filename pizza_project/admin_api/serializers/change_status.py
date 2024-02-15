from rest_framework import serializers
from pizza_lisa.models import OrderModel 


class ChangeStatusSerializer(serializers.Serializer):
    status = serializers.ChoiceField (choices= OrderModel.STATUS_ORDER)

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
