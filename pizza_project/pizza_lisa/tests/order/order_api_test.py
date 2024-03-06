from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User, OrderModel
from pizza_lisa.views import OrderView
from rest_framework import status
from rest_framework.test import force_authenticate
        
class OrderViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Тест на OrderView (get)
    def test_order_view_true_get(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/lisa/order/')
        force_authenticate(request, user=user)
        response = OrderView.as_view()(request)
        
        response.status_code == 200


class OrderCreateTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Тест на OrderView (post)
    def test_order_create_true_post (self):
        user = User.objects.get(username='for_test') 
        order_first_count = len(OrderModel.objects.all())

        request = APIRequestFactory().post('/lisa/order/')
        force_authenticate(request, user=user)
        response = OrderView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        order_second_count = len(OrderModel.objects.all())        
        assert (order_first_count +1 ) == (order_second_count)

        