from django.urls import path, include
from pizza_lisa.views import *
from django.views.generic.base import RedirectView 

from dotenv import load_dotenv
import os
load_dotenv()

urlpatterns = [

    path("",FirstPageView.as_view(),name='pizza'),
    path("registrate/form/",UserRegistrationView.as_view()),
    path('sign_in/logout/',RedirectView.as_view(url=(f'http://{os.getenv("DATABASE_HOST")}:8000/pizza/'))),
    path("sign_in/",include('rest_framework.urls')),

    path("lisa/",FirstPageAfterAuthView.as_view(), name='lisa'),

    # Catalog
    path("lisa/catalog/",CatalogView.as_view()),
    path("lisa/catalog/discont/",CatalogDiscontView.as_view()),
    path("lisa/<int:pizza_id>/",PizzaView.as_view(), name = 'pizza-view'),

    # User
    path("lisa/about_user/",AboutUserView.as_view(),name='user-view'),
    # path("lisa/user_update/tranzit/",UserUpdateView.as_view(),name='user-update-tranzit'),
    path("lisa/user_update/",UserUpdateView.as_view(), name='user-update'),
    path("lisa/user_delete/",UserDeleteView.as_view(),name='user-delete'),

    # Messages
    path("lisa/message/",MessageView.as_view()),
    path("lisa/message/delete/<int:id>/",MessageDelete.as_view()),

    # Basket
    path("lisa/basket/", BasketView.as_view(), name = 'view-basket'),
    path("lisa/basket/<int:pizza_id>/", BasketView.as_view(), name = 'add-one-to-basket'),
    path("lisa/basket/delete/<int:basket_id>/",BasketDelete.as_view()),
    path("lisa/basket/add/<int:basket_id>/",BasketAdd.as_view()),

    # Order
    path("lisa/order/", OrderView.as_view()),
    path("lisa/user_orders/", OrdersUserView.as_view()),
    path("lisa/order/<int:order_id>/", OneOrdersUserView.as_view()),
    path("lisa/order/cancel/<int:order_id>/", CancelOrderView.as_view()),

]