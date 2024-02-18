from django.urls import path, include
from admin_api.views import *
from django.views.generic.base import RedirectView 

from dotenv import load_dotenv
import os
load_dotenv()

urlpatterns = [

    path("",FirstAdminPageView.as_view()),

    # Orders
    path("user/orders/<int:order_id>/",OneOrderPageView.as_view()),
    path("user/all_orders/<int:user_id>/",OrdersByUserView.as_view()),
    path("user/all_orders_archive/<int:user_id>/",OrdersByUserArchiveView.as_view()),
    path("all_orders_in_work/",AllOrdersInWorkView.as_view()),
    path("all_orders/",AllOrdersView.as_view()),

    # About User
    path("user/<int:user_id>/",AdminAboutUserView.as_view()),
    path("user/delete/<int:user_id>/",UserADMINDeleteView.as_view()),
    path("user/all/",AboutAllUersPageView.as_view()),
    
    # Message
    path("user/message/<int:user_id>/",MessageAdminView.as_view()),
    path("user/message/delete/<int:user_id>/<int:_id>/",MessageAdminDelete.as_view()),
    path("user/message/read/<int:user_id>/<int:_id>/",MessageAdminRead.as_view()),

    # Catalog
    path("catalog/", CatalogAdminView.as_view()),
    path("catalog/<int:_id>/", PizzaOneView.as_view()),
    path("catalog/delete/<int:_id>/", PizzaAdminDelete.as_view()),
    path("catalog/pizza/<int:_id>/", PizzaInOrderAndBasketView.as_view()),
    path("catalog/pizza/delete_from_basket/<int:basket_id>/",DeletePizzaFromBasketView.as_view()),
    path("catalog/pizza/delete_from_order/<int:pizza_id>/",DeletePizzaFromOrderView.as_view()),

    

]