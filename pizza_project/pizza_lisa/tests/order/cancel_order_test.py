from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User, OrderModel
from pizza_lisa.views import CancelOrderView
from rest_framework import status
from rest_framework.test import force_authenticate

# Тест на Cancel Order (get)
class CancelOrderTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_cancel_order_get(self):
        user = User.objects.get(username='for_test')
        order_id = OrderModel.objects.filter(status = "NEW")[0].id
        
        request = APIRequestFactory().get('/lisa/order/cancel/')
        force_authenticate(request, user=user)
        response = CancelOrderView.as_view()(request,order_id = order_id)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        status_by_order = OrderModel.objects.get(id = order_id).status
        assert status_by_order == 'CANCELED'

    def test_cancel_order_false_id_get(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='for_test')
        order_id = 999999999999999999999
        
        request = APIRequestFactory().get('/lisa/order/cancel/')
        force_authenticate(request, user=user)
        response = CancelOrderView.as_view()(request,order_id = order_id)

        assert response.status_code == 200

    def test_cancel_order_false_status_get(self):
        user = User.objects.get(username='for_test')
        order_id = OrderModel.objects.exclude(status = "NEW")[0].id
        
        request = APIRequestFactory().get('/lisa/order/cancel/')
        force_authenticate(request, user=user)
        response = CancelOrderView.as_view()(request,order_id = order_id)

        assert response.status_code == 200