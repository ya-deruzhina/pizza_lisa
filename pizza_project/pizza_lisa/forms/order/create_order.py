from django.forms import ModelForm
from pizza_lisa.models import OrderModel

class CreateOrderForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = ["comment","address"]