from django.forms import ModelForm
from pizza_lisa.models import CatalogModel

class CreateCatalogForm(ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['price_disсont'].required=False
        self.fields['amount'].required=False
    
    class Meta:
        model = CatalogModel
        fields = ["name_pizza","ingredients","price","price_disсont","amount"]


from django.forms import ModelForm
from pizza_lisa.models import User
from django import forms

class UpdateCatalogForm (forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['name_pizza'].required=False
        self.fields['ingredients'].required=False
        self.fields['price'].required=False
        self.fields['price_disсont'].required=False
        self.fields['amount'].required=False
    class Meta:
        model = CatalogModel
        fields = ["name_pizza","ingredients","price","price_disсont","amount"]   