from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User, BasketModel, CatalogModel
from pizza_lisa.views import BasketView,BasketDelete, BasketAdd
from rest_framework import status
from rest_framework.test import force_authenticate

from django.urls import reverse

# Тест на BasketView (get)
class BasketViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_only_view_basket_get(self):
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/lisa/basket/')
        force_authenticate(request, user=user)
        response = BasketView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_view_basket_without_token_get(self):
        response = self.client.get(
            reverse('view-basket')
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_add_basket_post (self):
        user = User.objects.get(username='user')
        pizza = BasketModel.objects.all()[0]
        pizza_ = pizza.pizza
        pizza_id = pizza_.id
        first_amount = CatalogModel.objects.get(id=pizza_id).amount


        request = APIRequestFactory().post('/lisa/basket/')
        force_authenticate(request, user=user)
        response = BasketView.as_view()(request,pizza_id = pizza_id)

        if response.status_code == 302:
            basket_second_count = len(BasketModel.objects.all())
            assert (first_amount - 1) == CatalogModel.objects.get(id=pizza_id).amount

        else:
            assert response.status_code == 200

    

class BasketDeleteTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_delete_view_basket_get(self):
        user = User.objects.get(username='for_test')
        baskets = BasketModel.objects.all()
        basket_id = baskets[0].id
        basket_count_first = baskets[0].count
        amount = CatalogModel.objects.exclude(amount = 0)[0]
        amount_id = amount.id
        first_amount = CatalogModel.objects.get(id=amount_id).amount

        request = APIRequestFactory().get('/lisa/basket/delete/')
        force_authenticate(request, user=user)
        response = BasketDelete.as_view()(request,basket_id = basket_id)

        if response.status_code == 302:
            basket_count_second = BasketModel.objects.get(id = basket_id).count
            assert (basket_count_first - 1) == (basket_count_second)
            assert (first_amount + 1) == CatalogModel.objects.get(id=amount_id).amount

        else:
            assert response.status_code == 200


class BasketAddTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_add_view_basket_get(self):
        user = User.objects.get(username='for_test')
        basket = BasketModel.objects.all()
        basket_id = basket[0].id
        basket_count_first = basket[0].count
        amount = CatalogModel.objects.exclude(amount = 0)[0]
        amount_id = amount.id
        first_amount = CatalogModel.objects.get(id=amount_id).amount

        request = APIRequestFactory().get('/lisa/basket/add/')
        force_authenticate(request, user=user)
        response = BasketAdd.as_view()(request,basket_id = basket_id)

        if response.status_code == 302:
            basket_count_second = BasketModel.objects.get(id = basket_id).count
            assert (basket_count_first + 1) == (basket_count_second)
            assert (first_amount - 1) == CatalogModel.objects.get(id=amount_id).amount

        else:
            assert response.status_code == 200