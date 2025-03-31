import os
import psycopg2
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
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
    sql_delete =  """DELETE FROM "user" WHERE username != 'test1'"""
    print(f"🔍 Удаление всех пользователей из БД... (кроме test1) ")
    cur.execute(sql_delete)
    print(f"🔍 Проверка УДАЛЕНИЯ пользователей из БД...")
    cur.execute('SELECT username, password FROM "user" WHERE username != %s', ('test1',))
    del_user = cur.fetchone()
    cur.close()
    assert del_user is None, f" ❌ Удаленные пользователи найдены в БД"
    print(f"✅ Удаленные пользователи не найдены в БД! ")
    # Фиксируем изменения
    conn.commit()

    # Узнаем, сколько строк было удалено
    rows_deleted = cur.rowcount
    print(f"Удалено строк: {rows_deleted}")

    conn.close()  # Закрываем соединение после теста
    print("🔌 Соединение с БД закрыто.")
