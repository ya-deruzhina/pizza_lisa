from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from rest_framework.test import force_authenticate
from pizza_lisa.models import User
from admin_api.views import FirstAdminPageView

# Тест на FirstPageAfterAuthView (get)
class MainPageAdminAfterAuthTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_first_admin_page_after_auth_get(self):
        user = User.objects.get(username='admin')
        
        request = APIRequestFactory().get('/main/')
        force_authenticate(request, user=user)
        response = FirstAdminPageView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_first_admin_page_after_auth_without_token_get(self):
        request = APIRequestFactory().get('/main/')
        response = FirstAdminPageView.as_view()(request)
        
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_first_admin_page_after_auth_with_user_token_get(self):
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/main/')
        force_authenticate(request, user=user)
        response = FirstAdminPageView.as_view()(request)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)