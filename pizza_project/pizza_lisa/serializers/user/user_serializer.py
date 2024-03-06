from rest_framework import serializers
from pizza_lisa.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password","first_name","phone_number"]
        
    def create(self, validated_data):
        return User.objects.create(**validated_data)
       
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    

class UserUpdateSerializer(serializers.Serializer): 
    id = serializers.IntegerField (read_only = True, required=False )
    username = serializers.CharField(max_length=50,required=False)
    password = serializers.CharField(required=False)
    first_name = serializers.CharField(max_length=20,required=False)
    phone_number = serializers.IntegerField(required=False)
   
    def update(self,instance,validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
    

