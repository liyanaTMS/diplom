from allure_commons.types import AttachmentType
import pytest
import time
from tests.ui.pages.login_page import LoginPage
# from tests.ui.pages.register_page import RegisterPage
from tests.ui.pages.register_page import RegisterPage
import allure
import requests
from tests.api.api_endpoints.base_endpoint import EndpointApi


@pytest.mark.parametrize(
    ("p_name", "p_password"), [
        ('te', '12345'), # невалидный юзер, не должен зарегистрироваться
        ('tes', '12345'), # невалидный юзер, не должен зарегистрироваться
        ('', '123456'), # невалидный юзер, не должен зарегистрироваться
        ('test', ''), # невалидный юзер, не должен зарегистрироваться
        ('', ''), # невалидный юзер, не должен зарегистрироваться
        ('test12', '12121212'),# уже зарегистрированный юзер, не должен зарегистрироваться (сообщение: Пользователь с таким именем уже существует)
        ('user1', '1234567') # валидный юзер, должен зарегистрироваться

    ]
)
@allure.feature("Регистрация пользователя")
@allure.story("Регистрация пользователя с разными кредами")
def test_user_registration(driver, db_connection, p_name, p_password):
    name = "test12"
    password = "12121212"
    # Навигация на страницу регистрации и создание тестового юзера "test12"
    register_page = RegisterPage(driver)
    register_page.get_register_page()
    register_page.valid_registration(name, password)

    # Навигация на страницу регистрации
    with allure.step("Навигация на страницу регистрации"):
        time.sleep(0.5)
        register_page1 = RegisterPage(driver)
        register_page1.get_register_page()
        assert "register" in driver.current_url, "Пользователь не на старнице регистрации"
    # Заполнение полей
    with allure.step("Ввод пользователя и пароля"):
        register_page1.enter_username(p_name)
        register_page1.enter_password(p_password)
        allure.attach(driver.get_screenshot_as_png(), name="Страница регистрации", attachment_type=AttachmentType.PNG)
    # Нажатие кнопки Зарегистрироваться
    with allure.step("Нажать кнопку Зарегистрироваться"):
        register_page1.click_register_btn()
        time.sleep(0.5)
        allure.attach(driver.get_screenshot_as_png(), name="Успешная регистрация", attachment_type=AttachmentType.PNG)
    #  Валидация регистрации
    with allure.step("Валидация регистрации"):
    # Если вводятся невалидные данные
        if p_name == '':
            assert register_page.get_error_message() == "Имя пользователя обязательно", "Регистрация без пользователя.Неправильное сообщение об ошибке"
        elif p_password == '':
            assert register_page.get_error_message() == "Пароль обязателен", "Регистрация без пароля. Неправильное сообщение об ошибке"
        elif p_password == '' and name == '':
            assert register_page.get_error_message() == "Пароль обязателен", "Регистрация без пароля. Неправильное сообщение об ошибке"
            assert register_page.get_error_message() == "Имя пользователя обязательно", "Регистрация без пользователя. Неправильное сообщение об ошибке"
        elif len(p_name) < 3:
            assert register_page.get_error_message() == "Имя пользователя должно содержать не менее 3 символов", "Регистрация без пароля. Неправильное сообщение об ошибке"
        elif len(p_password) < 6:
            assert register_page.get_error_message() == "Пароль должен содержать не менее 6 символов", "Регистрация без пароля. Неправильное сообщение об ошибке"
        elif len(p_password) < 6 and len(name) < 3:
            assert register_page.get_error_message_password() == "Пароль должен содержать не менее 6 символов", "Регистрация без пароля. Неправильное сообщение об ошибке"
            assert register_page.get_error_message_name() == "Имя пользователя должно содержать не менее 3 символов", "Регистрация без пароля. Неправильное сообщение об ошибке"
        elif p_name == 'test12': # если ввели уже зарегистрированного юзера
            assert register_page.get_error_message() == "Пользователь с таким именем уже существует", "Регистрация под зарегистрированным пользователем. Неправильное сообщение об ошибке"
    # Если ввели валидного юзера
        else:
            with allure.step("Проверка успешной регистрации в системе"):
                assert "login" in driver.current_url, "Пользователь не перешел на страницу с логином"
                on_login_page = LoginPage(driver)
                assert on_login_page.get_success_message(), "Пользователь не зарегистрировался"
                assert "Регистрация успешна! Теперь вы можете войти" in on_login_page.get_success_message(), "Ошибка в сообщении об успешном входе в систему"

