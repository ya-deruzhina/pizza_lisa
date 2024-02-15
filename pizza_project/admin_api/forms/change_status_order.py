from django.forms import ModelForm
from pizza_lisa.models import OrderModel

class ChangeStatusOrderForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = ["status"]
