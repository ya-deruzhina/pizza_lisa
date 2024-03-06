from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User
from admin_api.views import AllOrdersInWorkView,AllOrdersView
from rest_framework import status
from rest_framework.test import force_authenticate

# AllOrdersInWorkView (get)
class AllOrdersInWorkTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_all_orders_in_work_get (self):
        user_admin = User.objects.get(username='admin')
        
        request = APIRequestFactory().get('/main/all_orders_in_work/')
        force_authenticate(request, user=user_admin)
        response = AllOrdersInWorkView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_all_orders_in_work_without_admin_get(self):
        user = User.objects.get(username='for_test')
        
        request = APIRequestFactory().get('/main/all_orders_in_work/')
        force_authenticate(request, user=user)
        response = AllOrdersInWorkView.as_view()(request)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

# AllOrdersView (get)
class AllOrdersViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_view_all_orders_get (self):
        user_admin = User.objects.get(username='admin')
        
        request = APIRequestFactory().get('/main/all_orders/')
        force_authenticate(request, user=user_admin)
        response = AllOrdersView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_all_orders_without_admin_get(self):
        user = User.objects.get(username='for_test')
        
        request = APIRequestFactory().get('/main/all_orders/')
        force_authenticate(request, user=user)
        response = AllOrdersView.as_view()(request)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)