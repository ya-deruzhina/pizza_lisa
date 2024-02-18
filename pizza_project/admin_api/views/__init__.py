from admin_api.views.first_admin_page import FirstAdminPageView
from admin_api.views.about_user.admin_about_user import AdminAboutUserView
from admin_api.views.about_order.one_page_of_order import OneOrderPageView
from admin_api.views.about_user.delete_user import UserADMINDeleteView
from admin_api.views.about_order.all_orders_by_user import OrdersByUserView,OrdersByUserArchiveView
from admin_api.views.about_user.message_api import MessageAdminView, MessageAdminDelete,MessageAdminRead
from admin_api.views.about_user.about_all_users import AboutAllUersPageView
from admin_api.views.about_catalog.catalog_all_for_admin import CatalogAdminView
from admin_api.views.about_catalog.catalog_one_for_admin import PizzaOneView,PizzaAdminDelete
from admin_api.views.about_catalog.pizza_in_order_and_basket import PizzaInOrderAndBasketView,DeletePizzaFromBasketView
from admin_api.views.about_order.all_orders import AllOrdersView
from admin_api.views.about_order.all_orders_in_work import AllOrdersInWorkView
from admin_api.views.about_order.delete_pizza_from_order import DeletePizzaFromOrderView

all = (
    "FirstAdminPageView",
    "AdminAboutUserView",
    "OneOrderPageView",
    "UserADMINDeleteView",
    "OrdersByUserView",
    "MessageAdminView",
    "MessageAdminDelete",
    "MessageAdminRead",
    "OrdersByUserArchiveView",
    "AboutAllUersPageView",
    "CatalogAdminView",
    "PizzaAdminDelete",
    "PizzaOneView",
    "PizzaInOrderAndBasketView",
    "DeletePizzaFromBasketView",
    "AllOrdersView",
    "AllOrdersInWorkView",
    "DeletePizzaFromOrderView",
    )
