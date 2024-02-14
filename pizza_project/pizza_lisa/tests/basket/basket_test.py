from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User, BasketModel
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
        user = User.objects.get(username='for_test')
        basket_first_count = len(BasketModel.objects.all())

        request = APIRequestFactory().post('/lisa/basket/')
        force_authenticate(request, user=user)
        response = BasketView.as_view()(request,pizza_id = 1)


        if response.status_code == 302:
            basket_second_count = len(BasketModel.objects.all())
            assert (basket_first_count + 1) == (basket_second_count)

        else:
            assert response.status_code == 200

class BasketDeleteTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_delete_view_basket_get(self):
        user = User.objects.get(username='for_test')
        basket = BasketModel.objects.all()
        basket_id = basket[0].id
        basket_count_first = basket[0].count

        request = APIRequestFactory().get('/lisa/basket/delete/')
        force_authenticate(request, user=user)
        response = BasketDelete.as_view()(request,basket_id = basket_id)

        if response.status_code == 302:
            basket_count_second = BasketModel.objects.get(id = basket_id).count
            assert (basket_count_first - 1) == (basket_count_second)

        else:
            assert response.status_code == 200


class BasketAddTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_delete_view_basket_get(self):
        user = User.objects.get(username='for_test')
        basket = BasketModel.objects.all()
        basket_id = basket[0].id
        basket_count_first = basket[0].count

        request = APIRequestFactory().get('/lisa/basket/add/')
        force_authenticate(request, user=user)
        response = BasketAdd.as_view()(request,basket_id = basket_id)

        if response.status_code == 302:
            basket_count_second = BasketModel.objects.get(id = basket_id).count
            assert (basket_count_first + 1) == (basket_count_second)

        else:
            assert response.status_code == 200