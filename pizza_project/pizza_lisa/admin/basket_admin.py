from django.contrib import admin
from pizza_lisa.models import BasketModel

# Register your models here.

@admin.register(BasketModel)
class BasketAdmin (admin.ModelAdmin):
    list_display = ["user", "pizza", "count"]