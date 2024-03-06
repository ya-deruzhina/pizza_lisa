from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User
from admin_api.views import UserADMINDeleteView
from rest_framework import status
from rest_framework.test import force_authenticate


# Тест на "MessageAdminDelete", (get)
class UserAdminDeleteTestCase(APITestCase):
    fixtures=['dump_data'] 
    
    def test_user_delete_get(self):
        users = User.objects.all()
        user_admin = users.get(username='admin')
        user = users.get(username='for_test')
        first_len = len(users)
        
        request = APIRequestFactory().get('/main/user/delete/')
        force_authenticate(request, user=user_admin)
        response = UserADMINDeleteView.as_view()(request,user_id = user.id)

        second_len = len(User.objects.all())

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert first_len - 1 == second_len
        
    def test_user_delete_without_admin_get(self):
        users = User.objects.all()
        user_admin = user = users.get(username='for_test')
        
        request = APIRequestFactory().get('/main/user/delete/')
        force_authenticate(request, user=user_admin)
        response = UserADMINDeleteView.as_view()(request,user_id = user.id)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_delete_without_message_get(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        user_id = 99999999999999999        

        request = APIRequestFactory().get('/main/user/delete/')
        force_authenticate(request, user=user_admin)
        response = UserADMINDeleteView.as_view()(request,user_id = user_id)

        assert response.status_code == 200