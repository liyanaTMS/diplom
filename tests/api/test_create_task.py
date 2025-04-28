from tests.api.api_endpoints.create_task import CreateTask
import pytest


# параметризация. проверка создания задачи с валидным и невалидным payload
@pytest.mark.parametrize(
    "task_data, exp_status, exp_msg",
    [
        ({"title": "task3", "description": "test task", "completed": True}, 201, 'Задача создана'), # валидная таска
        ({"title": "","description": "test task", "completed": False}, 400, "Неверный запрос"), # невалидная таска Баг в сваггере. В сваггере код 400, а приложение возвращает 201.
        ({"title": "task4", "description": "", "completed": False}, 400, "Неверный запрос"), # невалидная таска Баг в сваггере. В сваггере код 400, а приложение возвращает 201.
        ({"title": "task6", "description": "test task"}, 400, "Неверный запрос") # невалидная таска Баг в сваггере. В сваггере код 400, а приложение возвращает 201.
    ]
)

def test_create_task(register_and_login_user, task_data, exp_status, exp_msg):
    new_task = CreateTask()
    new_task.create_task(task_data, register_and_login_user)
    new_task.check_response_is_(exp_status)

    # проверка соответствия пришедшего респонса и отправленного респонса
    new_task.check_all_fields(task_data)

    # валидация схемы
    new_task.validate_response(new_task.get_data())
