from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User, OrderModel
from admin_api.views import OneOrderPageView
from rest_framework import status
from rest_framework.test import force_authenticate

# OneOrderPageView (get)
class OneOrderViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Тест на OneOrderPageView (get)
    def test_admin_one_order_view_get(self):
        user_admin = User.objects.get(username='admin')
        order = OrderModel.objects.all()[0]

        request = APIRequestFactory().get('/main/user/orders/')
        force_authenticate(request, user=user_admin)
        response = OneOrderPageView.as_view()(request,order_id = order.id)
        
        response.status_code == 200

    def test_admin_one_order_without_admin_view_get(self):
        user_admin = User.objects.get(username='for_test')
        order = OrderModel.objects.all()[0]

        request = APIRequestFactory().get('/main/user/orders/')
        force_authenticate(request, user=user_admin)
        response = OneOrderPageView.as_view()(request,order_id = order.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_one_order_without_order_view_get(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        order_id = 9999999999999999999999999999999999 

        request = APIRequestFactory().get('/main/user/orders/')
        force_authenticate(request, user=user_admin)
        response = OneOrderPageView.as_view()(request,order_id = order_id)
        
        assert response.status_code == 200

# OneOrderPageView (post)
class OneOrderPostTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Тест на OneOrderPageView (get)
    def test_admin_one_order_to_archive_post(self):
        user_admin = User.objects.get(username='admin')
        order = OrderModel.objects.exclude(status = "ARCHIVE")[0]
        order_id = order.id
        order_money = order.total_money
        user_id = order.user_id
        first_money = User.objects.get(id=user_id).total_shopping

        data = {"status":"ARCHIVE"}
        request = APIRequestFactory().post('/main/user/orders/', data)
        force_authenticate(request, user=user_admin)
        response = OneOrderPageView.as_view()(request,order_id = order_id)

        second_money = User.objects.get(id=user_id).total_shopping
        
        assert OrderModel.objects.get(id=order_id).status == "ARCHIVE"
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert first_money + order_money == second_money

    def test_admin_one_order_new_post(self):
        user_admin = User.objects.get(username='admin')
        order = OrderModel.objects.exclude(status = "ARCHIVE")[0]
        order_id = order.id
        order_money = order.total_money
        user_id = order.user_id
        first_money = User.objects.get(id=user_id).total_shopping

        data = {"status":"NEW"}
        request = APIRequestFactory().post('/main/user/orders/', data)
        force_authenticate(request, user=user_admin)
        response = OneOrderPageView.as_view()(request,order_id = order_id)

        second_money = User.objects.get(id=user_id).total_shopping
        
        assert OrderModel.objects.get(id=order_id).status == "NEW"
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert first_money - order_money == second_money

    def test_admin_one_order_with_unreal_status_post(self):
        print("\nMistake is OK!")

        user_admin = User.objects.get(username='admin')
        order = OrderModel.objects.exclude(status = "ARCHIVE")[0]
        order_id = order.id

        data = {"status":"UNREAL"}
        request = APIRequestFactory().post('/main/user/orders/', data)
        force_authenticate(request, user=user_admin)
        response = OneOrderPageView.as_view()(request,order_id = order_id)      

        assert response.status_code == 200

    def test_admin_one_order_with_unreal_order_post(self):
        print("\nMistake is OK!")

        user_admin = User.objects.get(username='admin')
        order_id = 9999999999999999999999999999999999999999999999999

        data = {"status":"NEW"}
        request = APIRequestFactory().post('/main/user/orders/', data)
        force_authenticate(request, user=user_admin)
        response = OneOrderPageView.as_view()(request,order_id = order_id)      

        assert response.status_code == 200


    def test_admin_one_order_not_admin_post(self):
        user_admin = User.objects.get(username='for_test')
        order = OrderModel.objects.exclude(status = "ARCHIVE")[0]
        order_id = order.id

        data = {"status":"ARCHIVE"}
        request = APIRequestFactory().post('/main/user/orders/', data)
        force_authenticate(request, user=user_admin)
        response = OneOrderPageView.as_view()(request,order_id = order_id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)