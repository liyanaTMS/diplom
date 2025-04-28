from tests.api.api_endpoints.login_user import LoginUser
from tests.api.api_endpoints.register_user import RegisterUser
import requests
import pytest


# параметризация. проверка логина с валидными и невалидными кредами
@pytest.mark.parametrize(
    "register_data, login_data, exp_status, exp_msg",
    [
        ({"username": "anna85", "password": "test"}, {"username": "anna85", "password": "test"}, 200, 'Успешный вход в систему'), # валидный юзер
        ({"username": "anna86", "password": "test"}, {"username": "anna86", "password": "test1"}, 401, "Неверное имя пользователя или пароль. Пожалуйста, укажите правильный пароль"), # невалидный юзер
        ({"username": "anna87", "password": "test"}, {"username": "", "password": "test"}, 401, "Неверное имя пользователя или пароль. Пожалуйста, укажите имя пользователя"), # невалидный юзер. Баг в приложении. В сваггере код 401, а возвращает 200
        ({"username": "anna88", "password": "test"}, {"username": "anna64", "password": ""}, 401, "Неверное имя пользователя или пароль. Пожалуйста, укажите пароль"), # невалидный юзер Баг в приложении. В сваггере код 401, а возвращает 200
        ({"username": "anna89", "password": "test"}, {"username": "", "password": ""},  401, "Неверное имя пользователя или пароль. Пожалуйста, укажите имя пользователя и пароль") # невалидный юзер  В сваггере код 401,и возвращает 401
    ]

)
def test_login_user(register_data, login_data, exp_status, exp_msg):
    new_user = RegisterUser()
    new_user.new_user(register_data)

    session = requests.Session()
    log_user = LoginUser()

    log_user.login_user(login_data, session)
    log_user.check_response_is_(exp_status)


