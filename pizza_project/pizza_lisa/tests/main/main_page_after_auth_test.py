from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from rest_framework.test import force_authenticate
from pizza_lisa.models import User
from pizza_lisa.views import FirstPageAfterAuthView

class MainPageAfterAuthTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Тест на FirstPageAfterAuthView (get)
    def test_first_page_after_auth_get(self):
        user = User.objects.get(username='for_test')
        
        request = APIRequestFactory().get('/lisa/')
        force_authenticate(request, user=user)
        response = FirstPageAfterAuthView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_first_page_after_auth_without_token_get(self):
        request = APIRequestFactory().get('/lisa/')
        response = FirstPageAfterAuthView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)