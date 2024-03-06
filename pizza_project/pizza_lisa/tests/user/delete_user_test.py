from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User
from pizza_lisa.views import UserDeleteView
from rest_framework.test import force_authenticate

# Тест на DeleteUserView - get
class UserDeleteTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_delete_user_get(self):
        user = User.objects.get(username='for_test')
        user_first = len(User.objects.all())

        request = APIRequestFactory().get('/lisa/user_delete/')
        force_authenticate(request, user=user)
        response = UserDeleteView.as_view()(request)

        if response.status_code == 302:
            user_second = len(User.objects.all())
            assert (user_first - 1) == user_second

        else:
            assert response.status_code == 200