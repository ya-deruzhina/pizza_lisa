from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User,CatalogModel, BasketModel
from admin_api.views import PizzaInOrderAndBasketView,DeletePizzaFromBasketView
from rest_framework import status
from rest_framework.test import force_authenticate

# PizzaInOrderAndBasketView (get)
class PizzaInOrderAndBasketViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_pizza_in_basket_and_orders_get (self):
        user_admin = User.objects.get(username='admin')
        pizza = CatalogModel.objects.all()[0]
        
        request = APIRequestFactory().get('/main/catalog/pizza/')
        force_authenticate(request, user=user_admin)
        response = PizzaInOrderAndBasketView.as_view()(request,_id = pizza.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pizza_in_basket_and_orders_without_admin_get(self):
        user = User.objects.get(username='for_test')
        pizza = CatalogModel.objects.all()[0]
        
        request = APIRequestFactory().get('/main/catalog/pizza/')
        force_authenticate(request, user=user)
        response = PizzaInOrderAndBasketView.as_view()(request,_id=pizza.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_pizza_in_basket_and_orders_without_pizza_id_get(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        pizza_id = 999999999999999999999999999999999999999999999 
        
        request = APIRequestFactory().get('/main/catalog/pizza/')
        force_authenticate(request, user=user_admin)
        response = PizzaInOrderAndBasketView.as_view()(request,_id=pizza_id)
        
        assert response.status_code == 200



# DeletePizzaFromBasketView
class DeletePizzaFromBasketViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_delete_pizza_from_basket_get (self):
        user_admin = User.objects.get(username='admin')
        basket= BasketModel.objects.all()
        first_len = len(basket)
        basket= basket[0]
        
        
        request = APIRequestFactory().get('/main/catalog/pizza/delete_from_basket/')
        force_authenticate(request, user=user_admin)
        response = DeletePizzaFromBasketView.as_view()(request,basket_id = basket.id)

        second_len = len(BasketModel.objects.all())

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert (first_len - 1 )== second_len

    def test_delete_pizza_from_basket_without_admin_get(self):
        user = User.objects.get(username='for_test')
        basket= BasketModel.objects.all()[0]
        
        request = APIRequestFactory().get('/main/catalog/pizza/delete_from_basket/')
        force_authenticate(request, user=user)
        response = DeletePizzaFromBasketView.as_view()(request,basket_id=basket.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_pizza_from_basket_without_pizza_id_get(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        basket_id = 999999999999999999999999999999999999999999999 
        
        request = APIRequestFactory().get('/main/catalog/pizza/delete_from_basket/')
        force_authenticate(request, user=user_admin)
        response = DeletePizzaFromBasketView.as_view()(request,basket_id=basket_id)
        
        assert response.status_code == 200