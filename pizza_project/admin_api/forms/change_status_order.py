from django.forms import ModelForm
from pizza_lisa.models import OrderModel, User

class ChangeStatusOrderForm(ModelForm):
    class Meta:
        model = OrderModel
        fields = ["status"]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["discont"]