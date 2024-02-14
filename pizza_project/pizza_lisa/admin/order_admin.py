from django.contrib import admin
from pizza_lisa.models import OrderModel

@admin.register(OrderModel)
class OrderAdmin (admin.ModelAdmin):
    list_display = ["id", "status","user","name","phone","comment"]