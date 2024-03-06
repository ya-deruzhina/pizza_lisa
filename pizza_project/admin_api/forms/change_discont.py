from django.forms import ModelForm
from pizza_lisa.models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["discont"]