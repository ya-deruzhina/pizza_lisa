from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User, MessagesModel
from admin_api.views import MessageAdminDelete, MessageAdminRead, MessageAdminView
from rest_framework import status
from rest_framework.test import force_authenticate
        
# Тест на "MessageAdminView", (get)
class MessageAdminViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_admin_message_view_get(self):
        user_admin = User.objects.get(username='admin')
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/main/user/message/')
        force_authenticate(request, user=user_admin)
        response = MessageAdminView.as_view()(request,user_id = user.id)
        
        assert response.status_code == 200

    def test_admin_message_view_without_token_get(self):
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/main/user/message/')
        response = MessageAdminView.as_view()(request,user_id = user.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_message_view_with_user_token_get(self):
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/main/user/message/')
        force_authenticate(request, user=user)
        response = MessageAdminView.as_view()(request,user_id = user.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# Тест на "MessageAdminView", (post)
class MessageAdminCreateTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_admin_message_create_post(self):
        user_admin = User.objects.get(username='admin')
        user = User.objects.get(username='for_test') 
        message_first_count = len(MessagesModel.objects.all())

        data = {'message':'new'}
        request = APIRequestFactory().post('/main/user/message/',data)
        force_authenticate(request, user=user_admin)
        response = MessageAdminView.as_view()(request,user_id = user.id)
        
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        messages = MessagesModel.objects.all()        
        
        message_by_user = MessagesModel.objects.filter(user_page_id = user).order_by('date_create')[0].message

        assert len(messages) == (message_first_count + 1)
        assert message_by_user == data['message']

    def test_admin_message_not_admin_user_create_post(self):
        user_admin = user = User.objects.get(username='for_test') 

        data = {'message':'new'}
        request = APIRequestFactory().post('/main/user/message/',data)
        force_authenticate(request, user=user_admin)
        response = MessageAdminView.as_view()(request,user_id = user.id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_message_not_message_user_create_post(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        user = User.objects.get(username='for_test') 

        request = APIRequestFactory().post('/main/user/message/')
        force_authenticate(request, user=user_admin)
        response = MessageAdminView.as_view()(request,user_id = user.id)
        
        assert response.status_code == 200

    def test_admin_message_not_real_user_create_post(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        user_id = 99999999999999999999999999999999 
        
        data = {'message':'new'}
        request = APIRequestFactory().post('/main/user/message/',data)
        force_authenticate(request, user=user_admin)
        response = MessageAdminView.as_view()(request,user_id = user_id)
        
        assert response.status_code == 200

# Тест на "MessageAdminDelete", (get)
class MessageAdminDeleteTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_message_delete_get(self):
        user_admin = User.objects.get(username='admin')
        user = User.objects.get(username='for_test')
        message = MessagesModel.objects.all()
        message_id = message[0].id        
        message_first_count = len(message)

        request = APIRequestFactory().get('/main/user/message/delete/')
        force_authenticate(request, user=user_admin)
        response = MessageAdminDelete.as_view()(request,user_id = user.id, _id = message_id)
        
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        messages = MessagesModel.objects.all()        
        
        assert len(messages) == (message_first_count-1)
        
    def test_message_delete_without_admin_get(self):
        user_admin = user = User.objects.get(username='for_test')
        message = MessagesModel.objects.all()
        message_id = message[0].id        

        request = APIRequestFactory().get('/main/user/message/delete/')
        force_authenticate(request, user=user_admin)
        response = MessageAdminDelete.as_view()(request,user_id = user.id, _id = message_id)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_message_delete_without_message_get(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        user = User.objects.get(username='for_test')
        message_id = 99999999999999999        

        request = APIRequestFactory().get('/main/user/message/delete/')
        force_authenticate(request, user=user_admin)
        response = MessageAdminDelete.as_view()(request,user_id = user.id, _id = message_id)

        assert response.status_code == 200

# Тест на "MessageAdminRead", (get)
class MessageAdminReadTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_message_read_get(self):
        user_admin = User.objects.get(username='admin')
        user = User.objects.get(username='for_test')
        message = MessagesModel.objects.filter(new=True)
        message_id = message[0].id        

        request = APIRequestFactory().get('/main/user/message/read/')
        force_authenticate(request, user=user_admin)
        response = MessageAdminRead.as_view()(request,user_id = user.id, _id = message_id)
        
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)   
        assert MessagesModel.objects.get(id=message_id).new == False

    def test_message_read_not_admin_get(self):
        user_admin = user = User.objects.get(username='for_test')
        message = MessagesModel.objects.filter(new=True)
        message_id = message[0].id        

        request = APIRequestFactory().get('/main/user/message/read/')
        force_authenticate(request, user=user_admin)
        response = MessageAdminRead.as_view()(request,user_id = user.id, _id = message_id)
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_message_read_not_message_get(self):
        print("\nMistake is OK!")
        user_admin = User.objects.get(username='admin')
        user = User.objects.get(username='for_test')
        message_id = 9999999999999999999999999999999999        

        request = APIRequestFactory().get('/main/user/message/read/')
        force_authenticate(request, user=user_admin)
        response = MessageAdminRead.as_view()(request,user_id = user.id, _id = message_id)
        
        assert response.status_code == 200
        
