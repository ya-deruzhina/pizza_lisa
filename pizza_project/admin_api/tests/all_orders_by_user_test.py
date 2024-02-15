from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User
from admin_api.views import OrdersByUserView,OrdersByUserArchiveView
from rest_framework import status
from rest_framework.test import force_authenticate

# OrdersByUserView (get)
class OrderByUserViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_view_all_orders_get (self):
        user_admin = User.objects.get(username='admin')
        user = User.objects.all()[0]
        
        request = APIRequestFactory().get('/main/user/all_orders/')
        force_authenticate(request, user=user_admin)
        response = OrdersByUserView.as_view()(request, user_id = user.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_all_orders_without_admin_get(self):
        user = User.objects.get(username='for_test')
        
        request = APIRequestFactory().get('/main/user/all_orders/')
        force_authenticate(request, user=user)
        response = OrdersByUserView.as_view()(request,user_id = user.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_all_orders_with_unreal_id_get(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        user_id = 999999999999999999999999999999999999999999999 
        
        request = APIRequestFactory().get('/main/user/all_orders/')
        force_authenticate(request, user=user_admin)
        response = OrdersByUserView.as_view()(request,user_id = user_id)
        
        assert response.status_code == 200

# OrdersByUserArchiveView (get)
class OrderByUserViewArchiveTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_view_all_orders_get (self):
        user_admin = User.objects.get(username='admin')
        user = User.objects.all()[0]
        
        request = APIRequestFactory().get('/main/user/all_orders_archive/')
        force_authenticate(request, user=user_admin)
        response = OrdersByUserArchiveView.as_view()(request, user_id = user.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_all_orders_without_admin_get(self):
        user = User.objects.get(username='for_test')
        
        request = APIRequestFactory().get('/main/user/all_orders_archive/')
        force_authenticate(request, user=user)
        response = OrdersByUserArchiveView.as_view()(request,user_id = user.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_view_all_orders_with_unreal_id_get(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        user_id = 999999999999999999999999999999999999999999999 
        
        request = APIRequestFactory().get('/main/user/all_orders_archive/')
        force_authenticate(request, user=user_admin)
        response = OrdersByUserArchiveView.as_view()(request,user_id = user_id)
        
        assert response.status_code == 200