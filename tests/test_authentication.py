from conftest import *


class TestAuthentic:
    @allure.title('Проверка успешной аутентификации пользователя с валидными учетными данными существующего аккаунта')
    def test_authentication_of_existing_account_success(self, create_new_user_and_delete):
        payload = create_new_user_and_delete[0]
        response = requests.post(Urls.user_auth, data=payload)
        deserials = response.json()

        assert response.status_code == 200
        assert deserials['success'] is True
        assert 'accessToken' in deserials.keys()
        assert 'refreshToken' in deserials.keys()
        assert deserials['user']['email'] == create_new_user_and_delete[0]['email']
        assert deserials['user']['name'] == create_new_user_and_delete[0]['name']





    @allure.title('Проверка аутентификации с незарегистрированным email')
    def test_auth_with_unregistered_email(self):
        payload = {
            'email': create_random_email(),
            'password': UsersData.password,
        }
        response = requests.post(Urls.user_auth, data=payload)
        assert response.status_code == 401
        assert response.json() == {"success": False, "message": "email or password are incorrect"}

    @allure.title('Проверка аутентификации с неверным паролем')
    def test_auth_with_incorrect_password(self):
        payload = {
            'email': UsersData.email,
            'password': create_random_password(),
        }
        response = requests.post(Urls.user_auth, data=payload)
        assert response.status_code == 401
        assert response.json() == {"success": False, "message": "email or password are incorrect"}