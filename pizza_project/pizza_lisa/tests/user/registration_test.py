from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User
from pizza_lisa.views import UserRegistrationView

import json

# Тест на Registration Transit UserRegistrationView - get
class CreateUserTransitViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_transit_update_user_view_get(self):
        request = APIRequestFactory().get('/registrate/form/')
        response = UserRegistrationView.as_view()(request)
        
        response.status_code == 200

# Тест на UserRegister (post)
class UserCreatePostViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_user_create_post(self):
        username = password = first_name = 'username'
        phone_number = 375291472589
        url = '/registrate/form/'
        user_first_count = len(User.objects.all())
        request = APIRequestFactory().post(url,{"username":username,"password":password,"first_name":first_name,"phone_number":phone_number})
        response = UserRegistrationView.as_view()(request)

        users = User.objects.all()        
        id_user = users.get(username=username).id

        assert response.status_code == 302
        assert len(users) == (user_first_count+1)           
        assert users.get(id=id_user).username == username
        assert users.get(id=id_user).first_name == first_name
        assert users.get(id=id_user).phone_number == phone_number
            
    def test_user_create_phone_false_len_more_12_post (self):
        username = password = first_name = 'username'
        phone_number = 37521147258911111111111
        url = '/registrate/form/'
        request = APIRequestFactory().post(url,{"username":username,"password":password,"first_name":first_name,"phone_number":phone_number})
        response = UserRegistrationView.as_view()(request)
        
        assert response.status_code == 200
        assert json.dumps({'Warning':'Mistake: Not Correct Number. Please, Check'}).encode("utf-8") == response.content

    def test_user_create_phone_false_start_333_post (self):
        username = password = first_name = 'username'
        phone_number = 333211472589
        url = '/registrate/form/'
        request = APIRequestFactory().post(url,{"username":username,"password":password,"first_name":first_name,"phone_number":phone_number})
        response = UserRegistrationView.as_view()(request)
        
        assert response.status_code == 200
        assert json.dumps({'Warning':'Mistake: Not Start 375'}).encode("utf-8") == response.content


    def test_user_create_phone_false_21_post (self):
        username = password = first_name = 'username'
        phone_number = 375211472589
        url = '/registrate/form/'
        request = APIRequestFactory().post(url,{"username":username,"password":password,"first_name":first_name,"phone_number":phone_number})
        response = UserRegistrationView.as_view()(request)

        assert response.status_code == 200
        assert json.dumps({'Warning':'Mistake: Not Code 29,33,44,25'}).encode("utf-8") == response.content

    def test_user_create_phone_false_less_1000000_post (self):
        username = password = first_name = 'username'
        phone_number = 375290999999
        url = '/registrate/form/'
        request = APIRequestFactory().post(url,{"username":username,"password":password,"first_name":first_name,"phone_number":phone_number})
        response = UserRegistrationView.as_view()(request)
        
        assert response.status_code == 200
        assert json.dumps({'Warning':'Mistake: Not Real Number'}).encode("utf-8") == response.content


