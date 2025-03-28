import os

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.register_page import RegisterPage
import allure


@pytest.mark.parametrize(
    ("name", "password"), [
        ('te', '12345'),
        ('tes', '12345'),
        ('', '123456'),
        ('test', ''),
        ('', ''),
        ('test1', '12121212'),# уже зарегистрированный юзер, не должен зарегистрироваться (сообщение: Пользователь с таким именем уже существует)
        ('user1', '1234567') # валидный юзер, должен зарегистрироваться

    ]
)

@allure.feature("Регистрация пользователя")
@allure.story("Регистрация пользователя с разными кредами")
def test_user_registration(driver, db_connection, name, password):
    # Настройка опций Chrome
    with allure.step("Навигация на логин страницу"):
        register_page = RegisterPage(driver)
        register_page.get_register_page()
        assert "register" in driver.current_url, "Пользователь не на старнице регистрации"
    # Заполнение полей
    with allure.step("Ввод пользователя и пароля"):
        register_page.enter_username(name)
        register_page.enter_password(password)
        allure.attach(driver.get_screenshot_as_png(), name="Страница регистрации", attachment_type=AttachmentType.PNG)
    # Нажатие кнопки Зарегистрироваться
    with allure.step("Нажать кнопку Зарегистрироваться"):
        register_page.click_register_btn()
        allure.attach(driver.get_screenshot_as_png(), name="Успешная регистрация", attachment_type=AttachmentType.PNG)
    #  Валидация регистрации
    with allure.step("Валидация регистрации"):
    # Если вводятся невалидные данные
        if name == '':
            assert register_page.get_error_message() == "Имя пользователя обязательно", "Регистрация без пользователя.Неправильное сообщение об ошибке"
        elif password == '':
            assert register_page.get_error_message() == "Пароль обязателен", "Регистрация без пароля. Неправильное сообщение об ошибке"
        elif password == '' and name == '':
            assert register_page.get_error_message() == "Пароль обязателен", "Регистрация без пароля. Неправильное сообщение об ошибке"
            assert register_page.get_error_message() == "Имя пользователя обязательно", "Регистрация без пользователя. Неправильное сообщение об ошибке"
        elif len(name) < 3:
            assert register_page.get_error_message() == "Имя пользователя должно содержать не менее 3 символов", "Регистрация без пароля. Неправильное сообщение об ошибке"
        elif len(password) < 6:
            assert register_page.get_error_message() == "Пароль должен содержать не менее 6 символов", "Регистрация без пароля. Неправильное сообщение об ошибке"
        elif len(password) < 6 and len(name) < 3:
            assert register_page.get_error_message_password() == "Пароль должен содержать не менее 6 символов", "Регистрация без пароля. Неправильное сообщение об ошибке"
            assert register_page.get_error_message_name() == "Имя пользователя должно содержать не менее 3 символов", "Регистрация без пароля. Неправильное сообщение об ошибке"
        elif name == 'test1':
            assert register_page.get_error_message() == "Пользователь с таким именем уже существует", "Регистрация под испорченным пользователем. Неправильное сообщение об ошибке"
    # Если ввели валидного юзера
        else:
            with allure.step("Проверка успешной регистрации в системе"):
                assert "login" in driver.current_url, "Пользователь не перешел на страницу с логином"
                on_login_page = LoginPage(driver)
                assert on_login_page.get_success_message(), "Пользователь не зарегистрировался"
                assert "Регистрация успешна! Теперь вы можете войти" in on_login_page.get_success_message(), "Ошибка в сообщении об успешном входе в систему"
