from django.contrib import admin
from pizza_lisa.models import CatalogModel

# Register your models here.

@admin.register(CatalogModel)
class CatalogAdmin (admin.ModelAdmin):
    list_display = ["name_pizza", "ingredients", "price","price_disсont"] 