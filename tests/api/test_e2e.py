from tests.api.api_endpoints.register_user import RegisterUser
from tests.api.payload.payload import valid_user_payload, valid_task_payload, valid_update_task_payload, invalid_user_payload, invalid_task_payload
from tests.api.conftest import db_connection_for_user, db_connection_for_task, db_connection_for_deleted_task
from tests.api.api_endpoints.login_user import LoginUser
from tests.api.api_endpoints.create_task import CreateTask
from tests.api.api_endpoints.update_task import UpdateTask
from tests.api.api_endpoints.delete_task import DeleteTask
from tests.api.api_endpoints.get_task import GetTask
from tests.api.api_endpoints.change_task_status import ChangeTask
import requests
import allure


@allure.feature("EndToEnd Тест")
@allure.story("Сценарий1: Полный цикл задачи")
def test_e2e_scenario(db_connection):
    """Тест проверяет регистрацию пользователя, аутентификацию пользователя, создание новой задачи, получение задачи по ИД, проверка записи в БД, обновление задачи, изменение статуса, удаление задачи, проверка удаления задачи"""

    # создание usera
    with allure.step("Регистрация пользователя"):
        new_user = RegisterUser()
        a = new_user.new_user(valid_user_payload)
        print(f"*****************************следующий юзер был создан:", a )
        new_user.check_user_register()


    with allure.step("Проверка пользователя в БД"):
        db_connection_for_user(db_connection)


    # аутентификация  usera
    with allure.step("Аутентификация пользователя"):
        print("---------Аутентификация пользователя:")
        session = requests.Session()
        log_user = LoginUser()
        log_user.login_user(valid_user_payload, session)
        log_user.check_user_login()

    # создание новой задачи
    with allure.step("Создание новой задачи"):
        print("---------Создание новой задачи:")
        new_task = CreateTask()
        new_task.create_task(valid_task_payload, session)
        new_task.check_task_creation()
        created_task_id = new_task.get_id_()
        print(f'Task ID : {created_task_id}')

    # получение задачи по ИД
    with allure.step("Получение задачи по ID"):
        print("---------Получение задачи по ID:")
        got_task = GetTask()
        got_task.get_task(created_task_id, session)
        got_task.check_task_get()

    # проверка, что задача записана в БД
    with allure.step("Проверка, что задача записана в БД"):
        db_connection_for_task(db_connection, created_task_id)


    # обновление задачи
    with allure.step("Обновление задачи"):
        print("---------Обновление задачи по ID:")
        up_task = UpdateTask()
        up_task.update_task(created_task_id, valid_update_task_payload, session)
        up_task.check_task_update()

    # изменение статуса задачи
    with allure.step("Изменение статуса задачи"):
        print("---------Изменение статуса задачи:")
        ch_task = ChangeTask()
        ch_task.change_task(created_task_id, valid_task_payload, session)
        ch_task.check_task_change()


    # удаление задачи
    with allure.step("Удаление задачи"):
        print("---------Удаление задачи:")
        del_task = DeleteTask()
        del_task.delete_task(created_task_id, session)
        del_task.check_task_delete()

    # проверка, что задача удалена из БД
    with allure.step("Проверка, что задача удалена из БД"):
        db_connection_for_deleted_task(db_connection, created_task_id)









