from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User
from admin_api.views import AdminAboutUserView
from rest_framework import status
from rest_framework.test import force_authenticate

# AdminAboutUserView (get)
class AdminAboutUserViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_admin_about_user_get (self):
        user_admin = User.objects.get(username='admin')
        user = User.objects.all()[0]
        
        request = APIRequestFactory().get('/main/user/')
        force_authenticate(request, user=user_admin)
        response = AdminAboutUserView.as_view()(request, user_id = user.id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_about_user_without_admin_get(self):
        user = User.objects.get(username='for_test')
        
        request = APIRequestFactory().get('/main/user/')
        force_authenticate(request, user=user)
        response = AdminAboutUserView.as_view()(request,user_id = user.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_about_user_with_unreal_id_get(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        user_id = 999999999999999999999999999999999999999999999 
        
        request = APIRequestFactory().get('/main/user/')
        force_authenticate(request, user=user_admin)
        response = AdminAboutUserView.as_view()(request,user_id = user_id)
        
        assert response.status_code == 200

# AdminAboutUserView (post)
class ChangeDiscontTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_chenge_discont_post(self):
        user_admin = User.objects.get(username='admin')
        user = User.objects.all()[0]
        
        data = {"discont":5}
        request = APIRequestFactory().post('/main/user/',data)
        force_authenticate(request, user=user_admin)
        response = AdminAboutUserView.as_view()(request, user_id = user.id)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert User.objects.get(id=user.id).discont == 5

    def test_change_discont_false_post(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        user = User.objects.all()[0]

        data = {"discont":"test"}
        request = APIRequestFactory().post('/main/user/',data)
        force_authenticate(request, user=user_admin)
        response = AdminAboutUserView.as_view()(request, user_id = user.id)

        assert response.status_code == 200

    def test_change_discont_without_admin_post(self):
        user = User.objects.get(username='for_test')
        
        data = {"discont":5}
        request = APIRequestFactory().post('/main/user/',data)
        force_authenticate(request, user=user)
        response = AdminAboutUserView.as_view()(request, user_id = user.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_change_discont_with_unreal_id_post(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        user_id = 999999999999999999999999999999999999999999999 
        
        data = {"discont":5}
        request = APIRequestFactory().post('/main/user/',data)
        force_authenticate(request, user=user_admin)
        response = AdminAboutUserView.as_view()(request, user_id = user_id)
        
        assert response.status_code == 200