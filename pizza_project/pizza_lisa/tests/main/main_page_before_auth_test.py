from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.views import FirstPageView
from rest_framework import status

class MainPageBeforeAuthTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Тест на FirstPageView (get)
    def test_first_page_before_auth_get(self):
        request = APIRequestFactory().get('/pizza/')
        response = FirstPageView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)