from django.forms import ModelForm
from pizza_lisa.models import MessagesModel

class CreateMessageForm(ModelForm):
    class Meta:
        model = MessagesModel
        fields = ["message"]
        
