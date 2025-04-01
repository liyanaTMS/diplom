from tests.ui.pages.login_page import LoginPage
from tests.ui.pages.register_page import RegisterPage
import allure
from allure_commons.types import AttachmentType
from tests.ui.pages.task_page import TaskPage


@allure.feature("Пользователь на странице задач")
@allure.story("Переход на страницу задач, проверка имени и логаут")
def test_user_on_tasks(driver, db_connection):
    # данный юзер будет регистрироваться в тесте
    name = "test0"
    password = "12121212"
    # Навигация на страницу регистрации и регистрация
    with allure.step("Навигация на страницу регистрации и регистрация"):
        register_page = RegisterPage(driver)
        register_page.get_register_page()
        register_page.valid_registration(name, password) # регистрируемся с юзером: {name = "test", password = "12121212"}
        allure.attach(driver.get_screenshot_as_png(), name="Успешная регистрация", attachment_type=AttachmentType.PNG)
    # Навигация на логин страницу и авторизация
    with allure.step("Навигация на логин страницу и авторизация"):
        on_task_page = LoginPage(driver)
        on_task_page.get_login_page()
        on_task_page.valid_login(name, password)
    # Проверка сообщения об успешной авторизации
    with allure.step("Проверка сообщения об успешной авторизации"):
        allure.attach(driver.get_screenshot_as_png(), name="Успешная авторизация", attachment_type=AttachmentType.PNG)
        task_page = TaskPage(driver)
        assert task_page.get_success_message() == "Вы успешно вошли в систему", "Ошибка в сообщении об успешном входе в систему"
    # Проверка имени юзера в системе
    with allure.step("Валидация имени юзера в системе"):
        assert "tasks" in driver.current_url, "Пользователь не перешел на страницу с задачами"
        assert  name in task_page.get_logout_menu(), "Имя пользователя не видно в системе"
    # Нажатие кнопки Выйти
    with allure.step("Выход из системы"):
        task_page.click_logout_menu()
        allure.attach(driver.get_screenshot_as_png(), name="Возврат на страницу логина", attachment_type=AttachmentType.PNG)
    # Проверка успешного выхода из системы, проверка сообщения
    with allure.step("Проверка успешного выхода из системы"):
        assert "login" in driver.current_url, "Пользователь не вернулся на старницу логина"
        on_task_page_again = LoginPage(driver)
        assert "Вы вышли из системы" in on_task_page_again.get_info_message(), "Ошибка в сообщении о выходе из системы"
