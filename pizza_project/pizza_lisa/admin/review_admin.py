from django.contrib import admin
from pizza_lisa.models import ReviewModel

@admin.register(ReviewModel)
class ReviewAdmin (admin.ModelAdmin):
    list_display = ["user", "pizza","review","time"]