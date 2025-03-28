from tests.api.api_endpoints.create_task import CreateTask
from tests.api.payload.payload import valid_task_payload
from tests.api.payload.payload import invalid_task_payload
import requests
import pytest



# параметризация. проверка логина с валидными и невалидными кредами
@pytest.mark.parametrize(
    "task_data, exp_status, exp_msg",
    [
        ({"title": "task3", "description": "test task", "completed": True}, 201, 'Задача создана'), # валидная таска
        ({"title": "","description": "test task", "completed": False}, 400, "Невернй запрос"), # невалидная таска Баг в сваггере. В сваггере код 400, а приложение возвращает 201.
        ({"title": "task4", "description": "", "completed": False}, 400, "Невернй запрос"), # невалидная таска Баг в сваггере. В сваггере код 400, а приложение возвращает 201.
        ({"title": "task5", "description": "test task"}, 400, "Невернй запрос") # невалидная таска Баг в сваггере. В сваггере код 400, а приложение возвращает 201.

        # ({"username": "", "password": "test"}, 401, "Не авторизован") # невалидная таска.

    ]

)
def test_create_task(register_and_login_user, task_data, exp_status, exp_msg):
    new_task = CreateTask()
    new_task.create_task(task_data, register_and_login_user)
    new_task.check_response_is_(exp_status)
    # print("Task creation (response 201): Задача создана.")
    # new_task.return_response()
    # проверка соответсвия пришедшего респонса и отправленного респонса
    new_task.check_all_fields(task_data)



    # валидация схемы
    new_task.validate_response(new_task.get_data())
    #
    # new_task.create_task(invalid_task_payload, register_and_login_user)
    # new_task.check_response_is_(401)
    # print("Task creation (response 401): Не авторизован")
    #
    # new_task.create_task(invalid_task_payload, register_and_login_user)
    # new_task.check_response_is_(400)
    # print("Task creation (response 400): Неверный запрос")