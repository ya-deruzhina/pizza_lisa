from admin_api.tests.about_all_users_test import AboutAllUersPageViewViewTestCase
from admin_api.tests.admin_about_user_test import AdminAboutUserViewTestCase,ChangeDiscontTestCase
from admin_api.tests.all_orders_by_user_test import OrderByUserViewTestCase,OrderByUserViewArchiveTestCase
from admin_api.tests.catalog_all_for_admin_test import AllCatalogViewTestCase,CreateCatalogViewTestCase
from admin_api.tests.catalog_one_for_admin_test import PizzaDeleteTestCase,OnePizzaCatalogViewTestCase,ChangePizzaTestCase
from admin_api.tests.delete_user_test import UserAdminDeleteTestCase
from admin_api.tests.first_admin_page_test import MainPageAdminAfterAuthTestCase
from admin_api.tests.message_admin_test import MessageAdminViewTestCase,MessageAdminCreateTestCase,MessageAdminDeleteTestCase,MessageAdminReadTestCase
from admin_api.tests.one_page_of_order_test import OneOrderViewTestCase,OneOrderPostTestCase



print ('63 tests - OK')

all =(
    "MainPageAdminAfterAuthTestCase",
    "MessageAdminView",
    "MessageAdminCreateTestCase",
    "MessageAdminDeleteTestCase",
    "MessageAdminReadTestCase",
    "OneOrderViewTestCase",
    "OneOrderPostTestCase",
    "UserAdminDeleteTestCase",
    "PizzaDeleteTestCase",
    "OnePizzaCatalogViewTestCase",
    "ChangePizzaTestCase",
    "AllCatalogViewTestCase",
    "CreateCatalogViewTestCase",
    "OrderByUserViewTestCase",
    "OrderByUserViewArchiveTestCase",
    "AdminAboutUserViewTestCase",
    "ChangeDiscontTestCase",
    "AboutAllUersPageViewViewTestCase",
)

