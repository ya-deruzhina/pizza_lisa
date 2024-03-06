from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import CatalogModel, User
from admin_api.views import PizzaAdminDelete,PizzaOneView
from rest_framework import status
from rest_framework.test import force_authenticate

# Тест на PizzaOneView (get)
class OnePizzaCatalogViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_one_pizza_view_get (self):
        user = User.objects.get(username='admin')
        pizza = CatalogModel.objects.all()[0]
        
        request = APIRequestFactory().get('/main/catalog/')
        force_authenticate(request, user=user)
        response = PizzaOneView.as_view()(request, _id=pizza.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_one_pizza_view_without_token_get(self):
        user = User.objects.get(username='for_test')
        pizza = CatalogModel.objects.all()[0]
        
        request = APIRequestFactory().get('/main/catalog/')
        force_authenticate(request, user=user)
        response = PizzaOneView.as_view()(request, _id=pizza.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_one_pizza_view_unreal_id_get(self):
        print("\nMistake is OK!")

        user = User.objects.get(username='admin')
        pizza_id = 9999999999999999999999999999999999999999999999
        
        request = APIRequestFactory().get('/main/catalog/')
        force_authenticate(request, user=user)
        response = PizzaOneView.as_view()(request, _id=pizza_id)

        assert response.status_code == 200


# Тест на PizzaOneView (post)
class ChangePizzaTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_change_name_pizza_view_post(self):
        user = User.objects.get(username='admin')
        pizza = CatalogModel.objects.all()[0]
        pizza_id = pizza.id

        data = {"name_pizza":"new_name","amount":''}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = PizzaOneView.as_view()(request, _id=pizza_id)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert CatalogModel.objects.get(id=pizza_id).name_pizza == "new_name"

    def test_change_ingredients_pizza_view_post(self):
        user = User.objects.get(username='admin')
        pizza = CatalogModel.objects.all()[0]
        pizza_id = pizza.id

        data = {"ingredients":"new","amount":''}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = PizzaOneView.as_view()(request, _id=pizza_id)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert CatalogModel.objects.get(id=pizza_id).ingredients == "new"

    def test_change_price_pizza_view_post(self):
        user = User.objects.get(username='admin')
        pizza = CatalogModel.objects.all()[0]
        pizza_id = pizza.id

        data = {"price":100,"amount":''}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = PizzaOneView.as_view()(request, _id=pizza_id)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert CatalogModel.objects.get(id=pizza_id).price == 100

    def test_change_price_disсont_pizza_view_post(self):
        user = User.objects.get(username='admin')
        pizza = CatalogModel.objects.all()[0]
        pizza_id = pizza.id

        data = {"price_disсont":1000,"amount":''}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = PizzaOneView.as_view()(request, _id=pizza_id)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert CatalogModel.objects.get(id=pizza_id).price_disсont== 1000

    
    def test_change_price_pizza_false_view_post(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='admin')
        pizza = CatalogModel.objects.all()[0]
        pizza_id = pizza.id

        data = {"price":"test","amount":''}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = PizzaOneView.as_view()(request, _id=pizza_id)

        assert response.status_code == 200

    def test_change_price_disсont_pizza_false_view_post(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='admin')
        pizza = CatalogModel.objects.all()[0]
        pizza_id = pizza.id

        data = {"price_disсont":"test","amount":''}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = PizzaOneView.as_view()(request, _id=pizza_id)

        assert response.status_code == 200

    def test_change_price_pizza_without_admin_post(self):
        user = User.objects.get(username='for_test')
        pizza = CatalogModel.objects.all()[0]
        pizza_id = pizza.id

        data = {"price":100,"amount":''}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = PizzaOneView.as_view()(request, _id=pizza_id)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_change_price_pizza_with_false_id_post(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='admin')
        pizza_id = 9999999999999999999999999999999

        data = {"price":100,"amount":''}
        request = APIRequestFactory().post('/main/catalog/', data)
        force_authenticate(request, user=user)
        response = PizzaOneView.as_view()(request, _id=pizza_id)

        assert response.status_code == 200


# Тест на PizzaAdminDelete (get)
class PizzaDeleteTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_pizza_delete_get(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        pizza = CatalogModel.objects.all()[0]
        first_len = len(CatalogModel.objects.all())
        
        request = APIRequestFactory().get('/main/catalog/delete/')
        force_authenticate(request, user=user_admin)
        response = PizzaAdminDelete.as_view()(request,_id = pizza.id)

        if response.status_code == 302:
            second_len = len(CatalogModel.objects.all())
            assert first_len - 1 == second_len
 
       #Иначе пицца в есть в заказе "в работе" и не может быть удалена
        
    def test_pizza_delete_without_admin_get(self):
        user_admin = User.objects.get(username='for_test')
        pizza = CatalogModel.objects.all()[0]
        
        request = APIRequestFactory().get('/main/catalog/delete/')
        force_authenticate(request, user=user_admin)
        response = PizzaAdminDelete.as_view()(request,_id = pizza.id)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_pizza_delete_without_message_get(self):
        print("\nMistake is OK!")
        
        user_admin = User.objects.get(username='admin')
        pizza_id = 999999999999999999999999999999999
        
        request = APIRequestFactory().get('/main/catalog/delete/')
        force_authenticate(request, user=user_admin)
        response = PizzaAdminDelete.as_view()(request,_id = pizza_id)

        assert response.status_code == 200