from rest_framework import serializers
from pizza_lisa.models import MessagesModel


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessagesModel
        fields = ["message","user_page","author_message","new"]