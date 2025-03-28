from tests.api.api_endpoints.login_user import LoginUser
from tests.api.payload.payload import valid_user_payload
from tests.api.payload.payload import invalid_user_payload
from tests.api.api_endpoints.register_user import RegisterUser
import requests
import pytest
# ({"username": "anna64", "password": "test"}, 200, 'Успешный вход в систему'),
# ({"username": "anna64", "password": "test1"}, 401, "Неверное имя пользователя или пароль. Пожалуйста, укажите правильный пароль"),

# параметризация. проверка логина с валидными и невалидными кредами
@pytest.mark.parametrize(
    "login_data, exp_status, exp_msg",
    [
        ({"username": "anna68", "password": "test"}, 200, 'Успешный вход в систему'), # валидный юзер
        ({"username": "anna68", "password": "test1"}, 401, "Неверное имя пользователя или пароль. Пожалуйста, укажите правильный пароль"), # невалидный юзер
        ({"username": "", "password": "test"}, 401, "Неверное имя пользователя или пароль. Пожалуйста, укажите имя пользователя"), # невалидный юзер. Баг в сваггере. В сваггере д.б. код 400
        ({"username": "anna64", "password": ""}, 401, "Неверное имя пользователя или пароль. Пожалуйста, укажите пароль"), # невалидный юзер Баг в сваггере. В сваггере д.б. код 400
        ({"username": "", "password": ""},  401, "Неверное имя пользователя или пароль. Пожалуйста, укажите имя пользователя и пароль") # невалидный юзер  Баг в сваггере. В сваггере д.б. код 400
    ]

)
def test_login_user(login_data, exp_status, exp_msg):
    new_user = RegisterUser()
    new_user.new_user(valid_user_payload)

    session = requests.Session()
    log_user = LoginUser()

    log_user.login_user(login_data, session)
    log_user.check_response_is_(exp_status)


