from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User, OrderModel
from pizza_lisa.views import OneOrdersUserView
from rest_framework.test import force_authenticate

# Тест на One Order (get)
class OneOrderTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_one_order_get(self):
        user = User.objects.get(username='for_test')
        order_id = OrderModel.objects.all()[0].id
        
        request = APIRequestFactory().get('/lisa/order/')
        force_authenticate(request, user=user)
        response = OneOrdersUserView.as_view()(request,order_id = order_id)

        assert response.status_code == 200


    def test_one_order_get(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='for_test')
        order_id = 999999999999999999999999
        
        request = APIRequestFactory().get('/lisa/order/')
        force_authenticate(request, user=user)
        response = OneOrdersUserView.as_view()(request,order_id = order_id)

        assert response.status_code == 200