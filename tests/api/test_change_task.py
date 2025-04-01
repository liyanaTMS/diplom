from tests.api.api_endpoints.change_task_status import ChangeTask
from tests.api.api_endpoints.create_task import CreateTask
from tests.api.payload.payload import valid_task_payload, changed_status_valid_task_payload


def test_change_task(register_and_login_user):
    new_task = CreateTask()
    new_task.create_task(valid_task_payload, register_and_login_user)
    created_task_id = new_task.get_id_()

    # изменения статуса задачи (completed: True --> False)
    ch_task = ChangeTask()
    ch_task.change_task(created_task_id, valid_task_payload, register_and_login_user)

    # проверка изменения статуса задачи (response 200). успешно
    ch_task.check_response_is_(200)
    print("Changed task status (response 200): Статус задачи изменен")
    ch_task.return_response()
    # проверка соответствия пришедшего респонса и отправленного респонса
    ch_task.check_all_fields(changed_status_valid_task_payload)

    # проверка изменения статуса задачи (response 404). НЕуспешно
    ch_task.change_task_for404(1888888, valid_task_payload, register_and_login_user)
    ch_task.check_response_is_(404)
    print("Changed task status (response 404): Задача не найдена")




