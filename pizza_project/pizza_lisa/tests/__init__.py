from pizza_lisa.tests.basket.basket_test import BasketViewTestCase,BasketDeleteTestCase, BasketAddTestCase
from pizza_lisa.tests.catalog.catalog_discont_test import CatalogDiscontViewTestCase
from pizza_lisa.tests.catalog.catalog_test import CatalogViewTestCase
from pizza_lisa.tests.catalog.pizza_test import PizzaViewTestCase,PizzaPostViewTestCase
from pizza_lisa.tests.main.main_page_before_auth_test import MainPageBeforeAuthTestCase
from pizza_lisa.tests.main.main_page_after_auth_test import MainPageAfterAuthTestCase
from pizza_lisa.tests.messages.message_test import MessageDeleteTestCase, MessageViewTestCase,MessageCreateTestCase
from pizza_lisa.tests.order.cancel_order_test import CancelOrderTestCase
from pizza_lisa.tests.order.history_of_orders_test import OrdersViewTestCase
from pizza_lisa.tests.order.one_order_test import OneOrderTestCase
from pizza_lisa.tests.order.order_api_test import OrderViewTestCase,OrderCreateTestCase
from pizza_lisa.tests.user.about_user_test import AboutUserViewTestCase,UpdateUserTransitViewTestCase,UserUpdateTestCase
from pizza_lisa.tests.user.delete_user_test import UserDeleteTestCase
from pizza_lisa.tests.user.registration_test import UserCreatePostViewTestCase,CreateUserTransitViewTestCase


print ('47 tests - OK')

all =(
    "MainPageBeforeAuthTestCase",
    "MainPageAfterAuthTestCase",
    "BasketViewTestCase",
    "BasketDeleteTestCase",
    "BasketAddTestCase",
    "CatalogViewTestCase",
    "CatalogDiscontViewTestCase",
    "PizzaViewTestCase",
    "PizzaPostViewTestCase",
    "MessageDeleteTestCase",
    "MessageViewTestCase",
    "MessageCreateTestCase",
    "CancelOrderTestCase",
    "OrderViewTestCase",
    "OneOrdersTestCase",
    "OrderViewTestCase",
    "OrderCreateTestCase",
    "AboutUserViewTestCase",
    "UpdateUserTransitViewTestCase",
    "UserUpdateTestCase",
    "UserDeleteTestCase",
    "UserCreatePostViewTestCase",
    "CreateUserTransitViewTestCase",
)