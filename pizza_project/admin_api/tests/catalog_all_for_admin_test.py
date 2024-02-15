from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import CatalogModel, User
from admin_api.views import CatalogAdminView
from rest_framework import status
from rest_framework.test import force_authenticate

# CatalogAdminView (get)
class AllCatalogViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_view_all_catalog_get (self):
        user = User.objects.get(username='admin')
        
        request = APIRequestFactory().get('/main/catalog/')
        force_authenticate(request, user=user)
        response = CatalogAdminView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_view_all_catalog_without_admin_get(self):
        user = User.objects.get(username='for_test')
        
        request = APIRequestFactory().get('/main/catalog/')
        force_authenticate(request, user=user)
        response = CatalogAdminView.as_view()(request)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

# CatalogAdminView (post)
class CreateCatalogViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_create_catalog_post(self):
        user = User.objects.get(username='admin')
        first_len = len(CatalogModel.objects.all())

        data = {"name_pizza":"NEW","ingredients":"NEW","price":10,"price_disсont":5}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = CatalogAdminView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        new_catalog = CatalogModel.objects.all().order_by('-id')
        assert first_len + 1 == len(new_catalog)
        new_pizza = new_catalog[0]
        assert new_pizza.name_pizza == "NEW"
        assert new_pizza.ingredients == "NEW"
        assert new_pizza.price == 10
        assert new_pizza.price_disсont == 5

    def test_create_catalog_without_price_discont_post(self):
        user = User.objects.get(username='admin')
        first_len = len(CatalogModel.objects.all())

        data = {"name_pizza":"NEW","ingredients":"NEW","price":10}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = CatalogAdminView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        new_catalog = CatalogModel.objects.all().order_by('-id')
        assert first_len + 1 == len(new_catalog)
        new_pizza = new_catalog[0]
        assert new_pizza.name_pizza == "NEW"
        assert new_pizza.ingredients == "NEW"
        assert new_pizza.price == 10
        assert new_pizza.price_disсont == 0

    def test_create_catalog_false_price_post(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='admin')

        data = {"name_pizza":"NEW","ingredients":"NEW","price":"test"}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = CatalogAdminView.as_view()(request)

        assert response.status_code == 200

    def test_create_catalog_false_price_discont_post(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='admin')

        data = {"name_pizza":"NEW","ingredients":"NEW","price":10,"price_disсont":"test"}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = CatalogAdminView.as_view()(request)

        assert response.status_code == 200

    def test_create_catalog_without_admin_post(self):
        user = User.objects.get(username='for_test')
        
        data = {"name_pizza":"NEW","ingredients":"NEW","price":10}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = CatalogAdminView.as_view()(request)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)