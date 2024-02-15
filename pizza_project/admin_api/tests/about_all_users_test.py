from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User
from admin_api.views import AboutAllUersPageView
from rest_framework import status
from rest_framework.test import force_authenticate

# AboutAllUersPageView (get)
class AboutAllUersPageViewViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_admin_about_all_user_get (self):
        user_admin = User.objects.get(username='admin')
        user = User.objects.all()[0]
        
        request = APIRequestFactory().get('/main/user/all/')
        force_authenticate(request, user=user_admin)
        response = AboutAllUersPageView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_about_all_user_without_admin_get(self):
        user = User.objects.get(username='for_test')
        
        request = APIRequestFactory().get('/main/user/all/')
        force_authenticate(request, user=user)
        response = AboutAllUersPageView.as_view()(request)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
