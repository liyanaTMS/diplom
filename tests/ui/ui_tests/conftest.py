import os
import psycopg2
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from tests.api.api_endpoints.register_user import RegisterUser
# from tests.api.api_endpoints.base_endpoint import url
import requests
import time
from tests.api.api_endpoints.base_endpoint import EndpointApi
# from webdriver_manager.chrome import ChromeDriverManager # Comment for docker

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager(driver_version="134.0.6998.89").install())
    config_driver = webdriver.Chrome(service=service, options=options)
    yield config_driver
    config_driver.quit()

DB_PARAMS = {
    'dbname': os.environ.get('POSTGRES_DB', 'taskmanager'),
    'user': os.environ.get('POSTGRES_USER', 'postgres'),
    'password': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
    'host': os.environ.get('POSTGRES_HOST', 'localhost'),
    'port': os.environ.get('POSTGRES_PORT', '5432')
}

@pytest.fixture(scope="function")
def db_connection():
    """Фикстура для подключения к БД"""
    print("🔌 Подключение к БД...")
    conn = psycopg2.connect(**DB_PARAMS)  # Устанавливаем соединение с БД
    yield conn  # Передаем соединение в тест
    #cursor = conn.cursor()
    cur = conn.cursor()
    sql_delete = 'DELETE FROM "task"'
    print(f"🔍 Удаление всех задач из БД... ")
    cur.execute(sql_delete)
    # sql_delete =  """DELETE FROM "user" WHERE username != 'test1'"""
    sql_delete = 'DELETE FROM "user"'
    print(f"🔍 Удаление всех пользователей из БД... (кроме test1) ")
    cur.execute(sql_delete)
    # Узнаем, сколько строк было удалено
    rows_deleted = cur.rowcount
    print(f"Удалено строк: {rows_deleted}")


    print(f"🔍 Проверка УДАЛЕНИЯ пользователей из БД...")
    #cur.execute('SELECT username, password FROM "user" WHERE username != %s', ('test1',))
    cur.execute('SELECT username, password FROM "user"')
    del_user = cur.fetchone()
    cur.close()
    assert del_user is None, f" ❌ Удаленные пользователи найдены в БД"
    print(f"✅ Удаленные пользователи не найдены в БД! ")
    # Фиксируем изменения
    conn.commit()


    conn.close()  # Закрываем соединение после теста
    print("🔌 Соединение с БД закрыто.")



@pytest.fixture(scope="function")
def register_user():
    """Фикстура для регистрации тестового пользователя"""
    test_user_data = {
        "username": "test1",
        "password": "12121212"
    }
    # регистрация пользователя
    new_user = RegisterUser()
    response = requests.post(f"http://web:5000/api/register", json=test_user_data)
    response_json = response.json()
    if response.status_code == 400:
        print(response_json)
    else:
        print("New test user was created: ", response_json)
        new_user.new_user(test_user_data)
        print("Test user {test1, 12121212} was created via fixture")
