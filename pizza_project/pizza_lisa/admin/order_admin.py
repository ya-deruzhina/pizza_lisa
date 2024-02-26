from django.contrib import admin
from pizza_lisa.models import OrderModel, PizzaInOrder

class PizzaInOrderInline(admin.TabularInline):
    model = PizzaInOrder
    list_display = ["order", "pizza","count","price_one"]

@admin.register(OrderModel)
class OrderAdmin (admin.ModelAdmin):
    list_display = ["id", "status","user","address","comment","order_time","total_money"]
    inlines = [PizzaInOrderInline]
