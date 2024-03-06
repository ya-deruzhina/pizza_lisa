from django.contrib import admin
from pizza_lisa.models import CatalogModel, ReviewModel

# Register your models here.

class ReviewInline(admin.TabularInline):
    model = ReviewModel
    list_display = ["user", "pizza","review","time"]
    ordering = ["-time"]

@admin.register(CatalogModel)
class CatalogAdmin (admin.ModelAdmin):
    list_display = ["name_pizza", "ingredients", "price","price_disсont"] 
    fields = ["name_pizza", "ingredients", "price","price_disсont"] 
    inlines = [ReviewInline]