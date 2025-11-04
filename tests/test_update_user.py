import allure
import requests
from conftest import *
import pytest

class TestUpdateUser:
    def setup_class(cls):
        cls.updated_user_data = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_username()
        }


    @allure.title('Проверка ответа на запрос изменения данных аутентифицированного пользователя')
    def test_update_user_authenticated_success(self, create_new_user_and_delete):
        access_token = create_new_user_and_delete[1]['accessToken']
        response = requests.patch(Urls.user_update, headers={'Authorization': access_token}, json=self.updated_user_data)
        deserialized_response = response.json()

        assert response.status_code == 200
        assert deserialized_response.get('success') is True
        assert deserialized_response['user']['email'] == self.updated_user_data['email']
        assert deserialized_response['user']['name'] == self.updated_user_data['name']

    @allure.title('Проверка ответа на запрос изменения данных неаутентифицированного пользователя')
    def test_update_user_unauthenticated_expected_error(self):
        response = requests.patch(Urls.user_update, headers=Urls.headers, json=self.updated_user_data)

        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': 'You should be authorised'}