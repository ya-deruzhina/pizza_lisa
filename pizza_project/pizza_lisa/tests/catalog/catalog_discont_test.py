from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User
from pizza_lisa.views import CatalogDiscontView
from rest_framework import status
from rest_framework.test import force_authenticate

# Тест на CatalogView (get)
class CatalogDiscontViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_catalog_discont_view_get(self):
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/lisa/catalog/discont/')
        force_authenticate(request, user=user)
        response = CatalogDiscontView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)