from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User, MessagesModel
from pizza_lisa.views import MessageDelete, MessageView
from rest_framework import status
from rest_framework.test import force_authenticate
        
class MessageViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Тест на "MessageView", (get)
    def test_message_view_get(self):
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/lisa/message/')
        force_authenticate(request, user=user)
        response = MessageView.as_view()(request)
        
        response.status_code == 200


class MessageCreateTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Тест на "MessageView", (post)
    def test_message_create_post (self):
        user = User.objects.get(username='for_test') 
        message_first_count = len(MessagesModel.objects.all())

        data = {'message':'new'}
        request = APIRequestFactory().post('/lisa/message/',data)
        force_authenticate(request, user=user)
        response = MessageView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        messages = MessagesModel.objects.all()        
        assert len(messages) == (message_first_count + 1)
        

        message_by_user = MessagesModel.objects.filter(user_page_id = user).order_by('date_create')[0].message
        assert message_by_user == data['message']


    def test_message_create_false_data_post (self):
        print("\nMistake is OK!")
        user = User.objects.get(username='for_test') 
        message_first_count = len(MessagesModel.objects.all())

        request = APIRequestFactory().post('/lisa/message/')
        force_authenticate(request, user=user)
        response = MessageView.as_view()(request)

        response.status_code == 200


class MessageDeleteTestCase(APITestCase):
    fixtures=['dump_data'] 

    # Тест на "MessageDelite", (get)
    def test_message_delete_get(self):
        user = User.objects.get(username='for_test')
        message = MessagesModel.objects.all()
        message_id = message[0].id        
        message_first_count = len(message)

        request = APIRequestFactory().get('/lisa/message/delete/')
        force_authenticate(request, user=user)
        response = MessageDelete.as_view()(request,id = message_id)
        

        if response.status_code == 302:
            self.assertEqual(response.status_code, status.HTTP_302_FOUND)
            messages = MessagesModel.objects.all()        
            assert len(messages) == (message_first_count-1)
        else:
            print("\nMistake is OK!")
            assert response.status_code == 200  

    def test_message_delete_false_get(self):
        print("\nMistake is OK!")
        user = User.objects.get(username='for_test')
        message_id = 9999999999999999999        

        request = APIRequestFactory().get('/lisa/message/delete/')
        force_authenticate(request, user=user)
        response = MessageDelete.as_view()(request,id = message_id)
        
        assert response.status_code == 200  
        
