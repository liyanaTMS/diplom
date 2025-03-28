from selenium.webdriver.common.by import By
from tests.ui.pages.base_page import BasePage

class RegisterPage(BasePage):
    FORM_NAME = (By.CSS_SELECTOR, '[class ="text-center"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '[data-testid="username-input"]')
    USERNAME_LABEL = (By.CSS_SELECTOR, '[data-testid="username-label"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="password-input"]')
    PASSWORD_LABEL = (By. CSS_SELECTOR, '[data-testid="password-label"]')
    LOGOUT_MENU = (By.CSS_SELECTOR, '[data-testid="nav-logout"]')
    LABEL_MENU = (By.CSS_SELECTOR, '[data-testid="navbar-brand"]')
    MY_TASKS_MENU = (By.CSS_SELECTOR, '[data-testid="nav-tasks"]')
    CREATE_TASK_MENU = (By.CSS_SELECTOR, '[data-testid="nav-create-task"]')
    API_DOCS_MENU = (By.CSS_SELECTOR, '[data-testid="nav-api-docs"]')
    REGISTER_BTN = (By.CSS_SELECTOR, '[data-testid="register-button"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-testid="flash-message-danger"]')
    ERROR_MESSAGE_NAME = (By.XPATH, '//div[starts-with(@class, "navbar")]/div[1]')
    ERROR_MESSAGE_PASSWORD = (By.XPATH, '//div[starts-with(@class, "navbar")]/div[2]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[data-testid="flash-message-success"]')

    def get_register_page(self):
        self.open_url(f'{self.url}/register')

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    # def clear_username(self, username):
    #     self.clear(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_register_btn(self):
        self.click_element(self.REGISTER_BTN)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text

    def get_error_message_name(self):
        return self.find_element(self.ERROR_MESSAGE_NAME).text

    def get_error_message_password(self):
        return self.find_element(self.ERROR_MESSAGE_PASSWORD).text

    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text

    def valid_registration(self, username, password):
       # self.get_register_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_register_btn()
        assert "login" in self.driver.current_url, "Пользователь не на логин старнице"

