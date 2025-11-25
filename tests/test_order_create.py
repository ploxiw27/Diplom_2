from conftest import *
from data import IngredientData


class TestOrderCreate:

    @allure.title('Проверка успешного создания заказа аутентифицированным пользователем с указанными ингредиентами')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_successful_order_creation_authenticated_user(self, create_new_user_and_delete, burger_ingredients):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': burger_ingredients}  # Изменено на список ингредиентов
        response = requests.post(Urls.order_create, json=payload, headers=headers)  # Используем json вместо data
        deserialized_response = response.json()

        assert response.status_code == 200
        assert deserialized_response.get('success') is True
        assert 'name' in deserialized_response
        assert 'number' in deserialized_response['order']

    @allure.title('Проверка создания заказа неаутентифицированным пользователем с указанными ингредиентами')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_order_creation_unauthenticated_user(self, burger_ingredients):
        payload = {'ingredients': burger_ingredients}
        response = requests.post(Urls.order_create, data=payload, headers=Urls.headers)

        assert response.status_code == 400


    @allure.title('Проверка ответа при создании заказа с пустыми ингредиентами аутентифицированным пользователем')
    def test_order_creation_empty_ingredients_authenticated_user(self, create_new_user_and_delete):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': []}
        response = requests.post(Urls.order_create, data=payload, headers=headers)

        assert response.status_code == 400


    @allure.title('Проверка ответа при создании заказа с пустыми ингредиентами неаутентифицированным пользователем')
    def test_order_creation_empty_ingredients_unauthenticated_user(self):
        payload = {'ingredients': []}
        response = requests.post(Urls.order_create, data=payload, headers=Urls.headers)

        assert response.status_code == 400


    @allure.title('Проверка ответа при создании заказа с неверным хэшем ингредиентов аутентифицированным пользователем')
    def test_order_creation_with_invalid_ingredients_authenticated_user(self, create_new_user_and_delete):
        headers = {'Authorization': create_new_user_and_delete[1]['accessToken']}
        payload = {'ingredients': [IngredientData.invalid_hash_ingredient]}
        response = requests.post(Urls.order_create, data=payload, headers=headers)

        assert response.status_code == 500
