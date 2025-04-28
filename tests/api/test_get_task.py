from tests.api.api_endpoints.get_task import GetTask
from tests.api.api_endpoints.create_task import CreateTask
from tests.api.payload.payload import valid_task_payload


def test_get_task(register_and_login_user):
    new_task = CreateTask()
    new_task.create_task(valid_task_payload, register_and_login_user)
    created_task_id = new_task.get_id_()

    got_task = GetTask()
    # получение задачи (response 200). успешно
    got_task.get_task_for404(created_task_id, register_and_login_user)
    print("Get task (response 200): Успешный ответ")
    got_task.check_response_is_(200)
    got_task.return_response()
    # проверка соответствия пришедшего респонса и отправленного респонса
    got_task.check_all_fields(valid_task_payload)
    # валидация схемы
    got_task.validate_response(new_task.get_data())

    # получение задачи (response 404). НЕуспешно
    got_task.get_task_for404(55555, register_and_login_user)
    print("Get task (response 404): Задача не найдена")
    got_task.check_response_is_(404)
