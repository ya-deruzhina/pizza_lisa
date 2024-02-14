from admin_api.views.first_admin_page import FirstAdminPageView
from admin_api.views.admin_about_user import AdminAboutUserView
from admin_api.views.one_page_of_order import OneOrderPageView
from admin_api.views.delete_user import UserADMINDeleteView
from admin_api.views.all_orders_by_user import OrdersByUserView,OrdersByUserArchiveView
from admin_api.views.message_api import MessageAdminView, MessageAdminDelete,MessageAdminRead
from admin_api.views.about_all_users import AboutAllUersPageView
from admin_api.views.catalog_all_for_admin import CatalogAdminView
from admin_api.views.catalog_one_for_admin import PizzaOneView,PizzaAdminDelete

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
    )
