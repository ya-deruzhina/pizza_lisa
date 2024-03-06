from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User
from pizza_lisa.views import CatalogView
from rest_framework import status
from rest_framework.test import force_authenticate

# Тест на CatalogView (get)
class CatalogViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_catalog_view_get(self):
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/lisa/catalog/')
        force_authenticate(request, user=user)
        response = CatalogView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)