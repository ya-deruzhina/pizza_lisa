from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User
from pizza_lisa.views import PizzaView
from rest_framework import status
from rest_framework.test import force_authenticate
from pizza_lisa.models import CatalogModel, ReviewModel

from django.urls import reverse

# Тест на PizzaViewView (get)
class PizzaViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_pizza_view_get(self):
        user = User.objects.get(username='for_test')
        catalog = CatalogModel.objects.all()
        pizza_id = catalog[0].id

        request = APIRequestFactory().get('/lisa/')
        force_authenticate(request, user=user)
        response = PizzaView.as_view()(request,pizza_id = pizza_id)
        assert response.status_code == 200

    def test_pizza_false_view_get(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='for_test')
        pizza_id = 999999999999999999999

        request = APIRequestFactory().get('/lisa/')
        force_authenticate(request, user=user)
        response = PizzaView.as_view()(request,pizza_id = pizza_id)
        assert response.status_code == 200

# Тест на Review by user+pizza (post)
class PizzaPostViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_pizza_view_post(self):
        user = User.objects.get(username='for_test')
        catalog = CatalogModel.objects.all()
        pizza_id = catalog[0].id
        data = {"review":"review"}
        request = APIRequestFactory().post('/lisa/basket/',data)
        force_authenticate(request, user=user)
        response = PizzaView.as_view()(request,pizza_id = pizza_id)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

        review_by_pizza = ReviewModel.objects.filter(pizza_id = pizza_id)
        review_by_user = review_by_pizza.get(user_id = user).review
        assert review_by_user == data['review']

    def test_pizza_false_review_view_post(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='for_test')
        catalog = CatalogModel.objects.all()
        pizza_id = catalog[0].id
        request = APIRequestFactory().post('/lisa/basket/')
        force_authenticate(request, user=user)
        response = PizzaView.as_view()(request,pizza_id = pizza_id)

        assert response.status_code == 200
        

    def test_pizza_false_pizza_id_view_post(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='for_test')
        pizza_id = 999999999999999999999
        request = APIRequestFactory().post('/lisa/basket/')
        force_authenticate(request, user=user)
        response = PizzaView.as_view()(request,pizza_id = pizza_id)

        assert response.status_code == 200