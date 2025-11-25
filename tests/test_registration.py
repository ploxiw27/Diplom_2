import requests
import pytest
import allure
from urls import *
from data import *


class TestRegistr:

    @allure.title('Проверка корректности регистрации аккаунта при введении валидных данных')
    def test_successful_registration_of_new_account(self):
        payload = {
            'email': create_random_email(),
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.post(Urls.user_register, data=payload)
        deserialized_response = response.json()

        assert response.status_code == 200
        assert deserialized_response.get('success') is True
        assert 'accessToken' in deserialized_response
        assert 'refreshToken' in deserialized_response
        assert deserialized_response['user']['email'] == payload['email']
        assert deserialized_response['user']['name'] == payload['name']

        # Удаление использованных тестовых данных из базы после теста
        access_token = deserialized_response['accessToken']
        requests.delete(Urls.user_delete, headers={'Authorization': access_token})


    @allure.title('Проверка ответа при регистрации с пустым обязательным полем')
    @pytest.mark.parametrize('credentials', UsersData.credentials_with_empty_field)
    def test_registration_missing_required_field(self, credentials):
        response = requests.post(Urls.user_register, json=credentials)
        assert response.status_code == 403
        assert response.json() == {
            'success': False,
            'message': 'Email, password and name are required fields'
        }


    @allure.title('Проверка ответа на регистрацию с уже зарегистрированным email')
    def test_registration_with_duplicate_email(self):
        payload = {
            'email': UsersData.email,
            'password': create_random_password(),
            'name': create_random_username()
        }
        response = requests.post(Urls.user_register, json=payload)  # Используем json
        assert response.status_code == 403
        assert response.json() == {
            'success': False,
            'message': 'User already exists'
        }