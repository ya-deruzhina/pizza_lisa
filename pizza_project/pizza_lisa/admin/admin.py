# from django.contrib import admin
# from ..models import *

# # Register your models here.

# @admin.register(CatalogModel)
# class CatalogAdmin (admin.ModelAdmin):
#     list_display = ["name_pizza", "ingredients", "price","price_diskont"]

# class MessageInline(admin.TabularInline):
#     model = MessagesModel
#     list_display = ["author_message", "message"]
#     ordering = ["-date_create"]

# @admin.register(User)
# class UserAdmin (admin.ModelAdmin):
#     fields = ["username","phone_number","first_name","password"]
#     inlines = [MessageInline]

#     def new_message (self,obj:User):
#         message = MessagesModel.objects.filter(user_page_id=obj.id)
#         mes = message.filter(new=True)
#         return len(mes)

# @admin.register(OrderModel)
# class OrderAdmin (admin.ModelAdmin):
#     list_display = ["order_number", "order_time","status","status","name_pizza","count","user","name","phone","comment"]


# @admin.register(ReviewModel)
# class ReviewAdmin (admin.ModelAdmin):
#     list_display = ["user", "review",""]