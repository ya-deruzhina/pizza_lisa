from rest_framework.test import APIRequestFactory, APITestCase
from pizza_lisa.models import User
from pizza_lisa.views import AboutUserView,UserUpdateView
from rest_framework import status
from rest_framework.test import force_authenticate

import json
        
# Тест на AboutUserView - get
class AboutUserViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_about_user_view_get(self):
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/lisa/about_user/')
        force_authenticate(request, user=user)
        response = AboutUserView.as_view()(request)
        
        response.status_code == 200
        assert user.username == 'for_test'

# Тест на UpdateUserView Transit - get
class UpdateUserTransitViewTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_transit_update_user_view_get(self):
        user = User.objects.get(username='for_test')
        request = APIRequestFactory().get('/lisa/user_update/')
        force_authenticate(request, user=user)
        response = UserUpdateView.as_view()(request)
        
        response.status_code == 200

# Тест на UpdateUserView - post
class UserUpdateTestCase(APITestCase):
    fixtures=['dump_data'] 

    def test_user_update_first_name_post (self):
        user = User.objects.get(username='for_test')
        user_id = user.id 

        data = {'first_name':'Updated'}
        request = APIRequestFactory().post('/lisa/user_update/',data)
        force_authenticate(request, user=user)
        response = UserUpdateView.as_view()(request)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        new_first_name = User.objects.get(id = user_id ).first_name        
        assert new_first_name == 'Updated'
    
    def test_user_update_username_post (self):
        user = User.objects.get(username='for_test')
        user_id = user.id 

        data = {'username':'updated'}
        request = APIRequestFactory().post('/lisa/user_update/',data)
        force_authenticate(request, user=user)
        response = UserUpdateView.as_view()(request)
        new_username = User.objects.get(id = user_id ).username

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)        
        assert new_username == 'updated'

    def test_user_update_password_post (self):
        user = User.objects.get(username='for_test')
        user_id = user.id
        user_password_1 = user.password 

        data = {'password':'updated'}
        request = APIRequestFactory().post('/lisa/user_update/',data)
        force_authenticate(request, user=user)
        response = UserUpdateView.as_view()(request)
        new_password = User.objects.get(id = user_id ).password

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert user_password_1 != new_password

    def test_user_without_data_post (self):
        user = User.objects.get(username='for_test')

        request = APIRequestFactory().post('/lisa/user_update/')
        force_authenticate(request, user=user)
        response = UserUpdateView.as_view()(request)
        
        response.status_code == 200


    def test_user_update_phone_correct_post (self):
        user = User.objects.get(username='for_test')
        user_id = user.id 

        data = {'phone_number':'375291472589'}
        request = APIRequestFactory().post('/lisa/user_update/',data)
        force_authenticate(request, user=user)
        response = UserUpdateView.as_view()(request)

        new_phone_number = User.objects.get(id = user_id ).phone_number

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        assert new_phone_number == int(data['phone_number'])


    def test_user_update_phone_false_len_more_12_post (self):
        user = User.objects.get(username='for_test')

        data = {'phone_number':'37521147258911111111111'}
        request = APIRequestFactory().post('/lisa/user_update/',data)
        force_authenticate(request, user=user)
        response = UserUpdateView.as_view()(request)

        assert response.status_code == 200
        assert json.dumps({'Warning':'Mistake: Not Correct Number. Please, Check'}).encode("utf-8") == response.content

    def test_user_update_phone_false_start_333_post (self):
        user = User.objects.get(username='for_test')

        data = {'phone_number':'333211472589'}
        request = APIRequestFactory().post('/lisa/user_update/',data)
        force_authenticate(request, user=user)
        response = UserUpdateView.as_view()(request)

        assert response.status_code == 200
        assert json.dumps({'Warning':'Mistake: Not Start 375'}).encode("utf-8") == response.content


    def test_user_update_phone_false_21_post (self):
        user = User.objects.get(username='for_test')

        data = {'phone_number':'375211472589'}
        request = APIRequestFactory().post('/lisa/user_update/',data)
        force_authenticate(request, user=user)
        response = UserUpdateView.as_view()(request)

        assert response.status_code == 200
        assert json.dumps({'Warning':'Mistake: Not Code 29,33,44,25'}).encode("utf-8") == response.content

    def test_user_update_phone_false_less_1000000_post (self):
        user = User.objects.get(username='for_test')

        data = {'phone_number':'375290999999'}
        request = APIRequestFactory().post('/lisa/user_update/',data)
        force_authenticate(request, user=user)
        response = UserUpdateView.as_view()(request)

        assert response.status_code == 200
        assert json.dumps({'Warning':'Mistake: Not Real Number'}).encode("utf-8") == response.content