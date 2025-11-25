import os
import sys

import allure
import pytest
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from data import *
from urls import *


@pytest.fixture
@allure.title('Фикстура создает пользователя с рандомными учётными данными и удаляет его из базы после теста')
def create_new_user_and_delete():
    # Генерируем случайные данные
    payload_cred = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_username()
    }

    @allure.step('Регистрируем пользователя')
    def register_user(payload):
        response = requests.post(Urls.user_register, data=payload)
        return response.json()

    @allure.step('Удаляем пользователя')
    def delete_user(access_token):
        response = requests.delete(Urls.user_delete, headers={'Authorization': access_token})
        return response

    # Регистрируем пользователя
    response_body = register_user(payload_cred)

    yield payload_cred, response_body

    # Удаляем пользователя по окончании теста
    access_token = response_body.get('accessToken')
    if access_token:  # Проверяем, что токен существует
        delete_user(access_token)


@pytest.fixture
@allure.title('Фикстура создает пользователя и заказ для его аккаунта')
def create_user_and_order_and_delete(create_new_user_and_delete):
    access_token = create_new_user_and_delete[1]['accessToken']
    headers = {'Authorization': access_token}

    @allure.step('Создаем заказ для пользователя')
    def create_order(payload):
        response = requests.post(Urls.order_create, data=payload, headers=headers)
        return response

    # Формируем данные для заказа
    payload = {'ingredients': [IngredientData.burger_2]}

    # Создаем заказ
    response_body = create_order(payload)

    yield access_token, response_body

    @allure.step('Удаляем пользователя')
    def delete_user(token):
        response = requests.delete(Urls.user_delete, headers={'Authorization': token})
        return response

    # Удаляем пользователя по окончании теста
    delete_user(access_token)