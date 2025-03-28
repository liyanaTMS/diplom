from selenium.webdriver.common.by import By
from tests.ui.pages.base_page import BasePage


class TaskPage(BasePage):
    FORM_NAME = (By.CSS_SELECTOR, '[data-testid ="tasks-title"]')
    CREATE_FIRST_TASK_LINK = (By.CSS_SELECTOR, '[data-testid="create-first-task-link"]')
    LOGOUT_MENU = (By.CSS_SELECTOR, '[data-testid="nav-logout"]')
    LABEL_MENU = (By.CSS_SELECTOR, '[data-testid="navbar-brand"]')
    MY_TASKS_MENU = (By.CSS_SELECTOR, '[data-testid="nav-tasks"]')
    CREATE_TASK_MENU = (By.CSS_SELECTOR, '[data-testid="nav-create-task"]')
    API_DOCS_MENU = (By.CSS_SELECTOR, '[data-testid="nav-api-docs"]')
    CREATE_TASK_BTN = (By.CSS_SELECTOR, '[data-testid="create-task-button"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '[data-testid="flash-message-success"]')

    def click_create_task_btn(self):
        self.click_element(self.CREATE_TASK_BTN)

    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text

    def get_logout_menu(self):
        return self.find_element(self.LOGOUT_MENU).text

    def click_logout_menu(self):
        return self.click_element(self.LOGOUT_MENU)