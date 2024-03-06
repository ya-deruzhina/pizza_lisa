from django.forms import ModelForm
from pizza_lisa.models import User 
from django import forms

class RegisterForm (ModelForm):
    class Meta:
        model = User
        fields = ["username","password","first_name","phone_number"]