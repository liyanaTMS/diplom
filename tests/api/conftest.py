import pytest
from tests.api.api_endpoints.login_user import LoginUser
from tests.api.api_endpoints.register_user import RegisterUser
from tests.api.payload.payload import valid_user_payload, valid_task_payload

import os
import pytest
import allure
import requests
import psycopg2


URL = "http://web:5000/api/" # для докера


# Параметры подключения к БД (из переменных окружения или дефолтные значения)
DB_PARAMS = {
    'dbname': os.environ.get('POSTGRES_DB', 'taskmanager'),
    'user': os.environ.get('POSTGRES_USER', 'postgres'),
    'password': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
    'host': os.environ.get('POSTGRES_HOST', 'db'),
    'port': os.environ.get('POSTGRES_PORT', '5432')
}

# URL API-сервера
#BASE_URL = "http://web:5000/api"

# Данные тестового пользователя
TEST_USER = {"username": "testuser1", "password": "testpass"}

@pytest.fixture(scope="function")
def db_connection():
    """Фикстура для подключения к БД"""
    print("🔌 Подключение к БД...")
    conn = psycopg2.connect(**DB_PARAMS)  # Устанавливаем соединение с БД
    yield conn  # Передаем соединение в тест
    #cursor = conn.cursor()
    cur = conn.cursor()
    sql_delete = 'DELETE FROM task'
    cur.execute(sql_delete)
    sql_delete = 'DELETE FROM "user"'
    cur.execute(sql_delete)
    # Фиксируем изменения
    conn.commit()

    # Узнаем, сколько строк было удалено
    rows_deleted = cur.rowcount
    print(f"Удалено строк: {rows_deleted}")
    # print(f"🔍 Удаление пользователя {valid_user_payload['username']} из БД...")
    # cursor.execute('DELETE FROM "user" WHERE username = %s', (valid_user_payload["username"],))
    # conn.commit()
    # print(f"🔍 Проверка УДАЛЕНИЯ пользователя из БД...")
    # cursor.execute('SELECT username, password FROM "user" WHERE username = %s', (valid_user_payload["username"],))
    # del_user = cursor.fetchone()
    # cursor.close()
    # assert del_user is None, f" ❌ Удаленный пользователь найден в БД: ID {valid_user_payload['username']}"
    # print(f"✅ Удаленный пользователь {valid_user_payload['username']} не найден в БД! ")

    conn.close()  # Закрываем соединение после теста
    print("🔌 Соединение с БД закрыто.")


@pytest.fixture(scope="function")
def register_and_login_user():
    """Фикстура для регистрации и авторизации пользователя"""
    test_user_data = {
        "username": "L",
        "password": "123456"
    }
    # 1 регистрация пользователя
    new_user = RegisterUser()
    new_user.new_user(test_user_data)
    print("New user was created via fixture")

    # 2 авторизация пользователя
    session = requests.Session()
    log_user = LoginUser()
    log_user.login_user(test_user_data, session)
    print("New user was logged in via fixture ")
    return session

def db_connection_for_user(db_conn):
    """Функция для проверки пользователя в БД"""
  # Создаём курсор для выполнения SQL-запросов
    print(f"🔍 Проверка пользователя в БД...")
    cursor = db_conn.cursor()
    cursor.execute('SELECT id, username, password FROM "user" WHERE username = %s', (valid_user_payload['username'],))
    user = cursor.fetchone()
    cursor.close()
    print(f"---------Пользователь {user}")
  # проверка соответствия данных API данным в БД
    assert valid_user_payload["username"] == user[1], f'Expected {valid_user_payload["username"]}, got {user[1]}'
    user_id = user[0]
    assert user is not None, f"❌ Пользователь с ID {user_id} не найден в БД!"
    print(f"✅ Пользователь найден в БД: ID {user_id}")


def db_connection_for_task(db_conn, task_id):
    """Функция для проверки задачи в БД"""
  # Создаём курсор для выполнения SQL-запросов
    print(f"🔍 Проверка задачи с ID {task_id} в БД...")
    cursor = db_conn.cursor()
    cursor.execute('SELECT id, title, description, completed FROM "task" WHERE id = %s', (task_id,))
    task = cursor.fetchone()
    cursor.close()
    print(f"---------Задача {task}")
    # проверка соответствия данных API данным в БД
    assert valid_task_payload["title"] == task[1], f'Expected {valid_task_payload["title"]}, got {task[1]}'
    assert valid_task_payload["description"] == task[2], f'Expected {valid_task_payload["description"]}, got {task[2]}'
    assert valid_task_payload["completed"] == task[3], f'Expected {valid_task_payload["completed"]}, got {task[3]}'

    assert task is not None, f"❌ Задача {task_id} не найдена в БД!"
    print(f"✅ Задача найдена в БД: ID {task_id}")


def db_connection_for_deleted_task(db_conn, del_task_id):
    """Функция для проверки удаления задачи из БД"""
    print(f"🔍 Проверка УДАЛЕНИЯ задачи {del_task_id} из БД...")
    cursor = db_conn.cursor()
    cursor.execute('SELECT id, title, description, completed FROM "task" WHERE id = %s', (del_task_id,))
    task = cursor.fetchone()
    cursor.close()
    assert task is None, f" ❌ Удаленная задача найдена в БД: ID {del_task_id}"
    print(f"✅ Удаленная задача {del_task_id} не найдена в БД! ")




# @pytest.fixture
# def authenticated_user():
#     auth = AuthenticateUser()
#     auth.login_user(valid_user)
#     auth.check_response_is_200()
#     return auth

@pytest.fixture(params=[
    (valid_user_payload, True)
])
def test_data(request):
    return request.param