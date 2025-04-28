from tests.api.api_endpoints.login_user import LoginUser
from tests.api.api_endpoints.register_user import RegisterUser
from tests.api.payload.payload import valid_user_payload, valid_task_payload
import os
import pytest
import requests
import psycopg2

URL = "http://web:5000/api/" # для докера


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



