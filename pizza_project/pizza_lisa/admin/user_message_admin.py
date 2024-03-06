from django.contrib import admin
from pizza_lisa.models import User, MessagesModel

class MessageInline(admin.TabularInline):
    model = MessagesModel
    list_display = ["author_message", "message"]
    ordering = ["-date_create"]

@admin.register(User)
class UserAdmin (admin.ModelAdmin):
    fields = ["username","phone_number","first_name","password"]
    inlines = [MessageInline]