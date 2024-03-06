from pizza_lisa.views.main.main_page_before_auth_api import FirstPageView
from pizza_lisa.views.user.registration_api import UserRegistrationView
from pizza_lisa.views.main.main_page_after_auth_api import FirstPageAfterAuthView
from pizza_lisa.views.catalog.catalog_api import CatalogView
from pizza_lisa.views.catalog.pizza_api import PizzaView
from pizza_lisa.views.catalog.catalog_discont_api import CatalogDiscontView
from pizza_lisa.views.user.about_user_api import AboutUserView,UserUpdateView
from pizza_lisa.views.user.delete_user_api import UserDeleteView
from pizza_lisa.views.messages.message_api import MessageDelete,MessageView
from pizza_lisa.views.basket.basket_api import BasketView,BasketDelete,BasketAdd
from pizza_lisa.views.order.order_api import OrderView
from pizza_lisa.views.order.history_of_orders_api import OrdersUserView
from pizza_lisa.views.order.one_order_api import OneOrdersUserView
from pizza_lisa.views.order.cancel_order_api import CancelOrderView


all = (
    "FirstPageView",
    "UserRegistrationView",
    "FirstPageAfterAuthView",
    "CatalogView",
    "PizzaView",
    "CatalogDiscontView",
    "AboutUserView",
    "UserUpdateView",
    "UserDeleteView",
    "MessageDelete",
    "MessageView",
    "BasketView",
    "BasketDelete",
    "OrderView",
    "OrdersUserView",
    "OneOrdersUserView",
    "BasketAdd",
    "CancelOrderView",
)