from django.forms import ModelForm
from pizza_lisa.models import User
from django import forms

class UpdateUserForm (forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].required=False
        self.fields['phone_number'].required=False
        self.fields['password'].required=False
        self.fields['username'].required=False
    class Meta:
        model = User
        fields = ["username","password","first_name","phone_number"]