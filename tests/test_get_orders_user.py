from conftest import *
import requests


class TestGetOrdersUser:

    @allure.title('Проверка успешного доступа к списку заказов для аутентифицированного пользователя')
    def test_authenticated_user_successfully_retrieves_orders(self, create_user_and_order_and_delete):
        token = create_user_and_order_and_delete[0]
        headers = {'Authorization': token}
        response = requests.get(Urls.get_user_orders, headers=headers)
        deserialized_response = response.json()

        assert response.status_code == 200
        assert deserialized_response.get('success') is True
        assert 'orders' in deserialized_response
        assert 'total' in deserialized_response



    @allure.title('Проверка ответа для неаутентифицированного пользователя при запросе списка заказов')
    def test_unauthenticated_user_fails_to_get_orders(self):
        response = requests.get(Urls.get_user_orders, headers=Urls.headers)

        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': 'You should be authorised'}