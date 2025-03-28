from selenium.webdriver.common.by import By
from tests.ui.pages.base_page import BasePage


class LoginPage(BasePage):
    FORM_NAME = (By.CSS_SELECTOR, '[class ="tasks-title"]')
    USERNAME_INPUT = (By.CSS_SELECTOR, '[data-testid="username-input"]')
    #USERNAME_INPUT1 = (By.ID, "username")
    USERNAME_LABEL = (By.CSS_SELECTOR, '[data-testid="username-label"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="password-input"]')
    #PASSWORD_INPUT1 = (By.ID, "password")
    PASSWORD_LABEL = (By. CSS_SELECTOR, '[data-testid="password-label"]')
    LOGOUT_MENU = (By.CSS_SELECTOR, '[data-testid="nav - logout"]')
    LABEL_MENU = (By.CSS_SELECTOR, '[data-testid="navbar-brand"]')
    MY_TASKS_MENU = (By.CSS_SELECTOR, '[data-testid="nav-tasks"]')
    CREATE_TASK_MENU = (By.CSS_SELECTOR, '[data-testid="nav-create-task"]')
    API_DOCS_MENU = (By.CSS_SELECTOR, '[data-testid="nav-api-docs"]')
    LOGIN_BTN = (By.CSS_SELECTOR, '[data-testid="login-button"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-testid="flash-message-danger"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[data-testid="flash-message-success"]')
    INFO_MESSAGE = (By.CSS_SELECTOR, '[data-testid="flash-message-info"]')
    REGISTR_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[data-testid="flash-message-success"]')

    def get_login_page(self):
        self.open_url(f'{self.url}/login')

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(self.LOGIN_BTN)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text

    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text

    def get_info_message(self):
        return self.find_element(self.INFO_MESSAGE).text

    def get_registr_success_message(self):
        return self.find_element(self.REGISTR_SUCCESS_MESSAGE).text

    def valid_login(self, username, password):
        self.get_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
