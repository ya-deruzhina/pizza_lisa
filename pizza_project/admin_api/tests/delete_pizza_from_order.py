from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User, PizzaInOrder
from admin_api.views import DeletePizzaFromOrderView
from rest_framework import status
from rest_framework.test import force_authenticate

# DeletePizzaFromOrderView
class DeletePizzaFromOrderViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_delete_pizza_from_order_get (self):
        user_admin = User.objects.get(username='admin')
        pizza = PizzaInOrder.objects.all()[0]     
        
        request = APIRequestFactory().get('/main/catalog/pizza/delete_from_order/')
        force_authenticate(request, user=user_admin)
        response = DeletePizzaFromOrderView.as_view()(request,pizza_id = pizza.id)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_delete_pizza_from_order_without_admin_get(self):
        user = User.objects.get(username='for_test')
        pizza = PizzaInOrder.objects.all()[0]
        
        request = APIRequestFactory().get('/main/catalog/pizza/delete_from_order/')
        force_authenticate(request, user=user)
        response = DeletePizzaFromOrderView.as_view()(request,pizza_id = pizza.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_pizza_from_order_without_pizza_id_get(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        pizza_id = 999999999999999999999999999999999999999999999 
        
        request = APIRequestFactory().get('/main/catalog/pizza/delete_from_order/')
        force_authenticate(request, user=user_admin)
        response = DeletePizzaFromOrderView.as_view()(request,pizza_id = pizza_id)
        
        assert response.status_code == 200