from allure_commons.types import AttachmentType
import pytest
from tests.ui.pages.login_page import LoginPage
import allure
from tests.ui.pages.task_page import TaskPage


@pytest.mark.parametrize(
    ("name", "password"), [
        ('test1', '12121212'), # созданный заранее юзер
        ('', 'password'),
        ('username', ''),
        ('', '')
    ]
)

@allure.feature("Логин пользователя")
@allure.story("Логин пользователя с различными кредами")
def test_user_login(driver, db_connection, name, password):
    # Настройка опций Chrome
    with allure.step("Навигация на логин страницу и авторизация"):
        login_page = LoginPage(driver)
        login_page.get_login_page()
        assert "login" in driver.current_url, "Пользователь не на логин старнице"

    # Заполнение полей
    with allure.step("Ввод пользователя и пароля"):
        login_page.enter_username(name)
        login_page.enter_password(password)
    # Нажатие кнопки Войти
    with allure.step("Нажать кнопку Войти"):
        login_page.click_login()
        allure.attach(driver.get_screenshot_as_png(), name="Успешная авторизация", attachment_type=AttachmentType.PNG)
    # Валидация логина
    with allure.step("Валидация логина"):
        # Если вводятся невалидные данные
        if name == '':
            assert login_page.get_error_message() == "Имя пользователя обязательно", "Авторизация без пользователя.Неправильное сообщение об ошибке"
        elif password == '':
            assert login_page.get_error_message() == "Пароль обязателен", "Авторизация без пароля. Неправильное сообщение об ошибке"
        elif password == '' and name == '':
            assert login_page.get_error_message() == "Пароль обязателен", "Авторизация без пароля. Неправильное сообщение об ошибке"
            assert login_page.get_error_message() == "Имя пользователя обязательно", "Авторизация без пользователя. Неправильное сообщение об ошибке"
        # Если ввели валидного созданного заранее юзера
        else:
            assert login_page.get_success_message(), "Пользователь не авторизовался"
            assert "tasks" in driver.current_url, "Пользователь не перешел на страницу с задачами"
            allure.attach(driver.get_screenshot_as_png(), name="Переход на страницу задач",
                          attachment_type=AttachmentType.PNG)
            on_task_page = TaskPage(driver)
            assert on_task_page.get_success_message(), "Пользователь не перешел на старницу задач"
            assert "Вы успешно вошли в систему" in on_task_page.get_success_message(), "Ошибка в сообщении об успешном входе в систему"


