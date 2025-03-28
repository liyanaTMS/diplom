from tests.api.api_endpoints.change_task_status import ChangeTask
from tests.api.api_endpoints.create_task import CreateTask
from tests.api.payload.payload import valid_task_payload
from tests.api.payload.payload import invalid_task_payload


def test_change_task(register_and_login_user):
    new_task = CreateTask()
    new_task.create_task(valid_task_payload, register_and_login_user)
    created_task_id = new_task.get_id_()

    ch_task = ChangeTask()
    ch_task.change_task(created_task_id, valid_task_payload, register_and_login_user)
    print("Changed task status (response 200): Статус задачи изменен")
    ch_task.check_response_is_(200)
    ch_task.return_response()
    # проверка соответсвия пришедшего респонса и отправленного респонса
    ch_task.check_all_fields(valid_task_payload)

    ch_task.change_task_for404(1888888, valid_task_payload, register_and_login_user)
    print("Changed task status (response 404): Задача не найдена")
    ch_task.check_response_is_(404)




