from tests.api.api_endpoints.update_task import UpdateTask
from tests.api.api_endpoints.create_task import CreateTask
from tests.api.payload.payload import valid_task_payload
from tests.api.payload.payload import invalid_task_payload
from tests.api.payload.payload import valid_update_task_payload


def test_update_task(register_and_login_user):
    new_task = CreateTask()
    new_task.create_task(valid_task_payload, register_and_login_user)
    created_task_id = new_task.get_id_()

    up_task = UpdateTask()
    up_task.update_task_for404(created_task_id, valid_update_task_payload, register_and_login_user)
    print("Update task (response 200): Задача обновлена")
    up_task.check_response_is_(200)

    up_task.update_task_for404(created_task_id, invalid_task_payload, register_and_login_user)
    print("Update task (response 400): Неверный запрос")
    up_task.check_response_is_(400)

    up_task.update_task_for404(55555, valid_task_payload, register_and_login_user)
    print("Update task (response 404): Задача не найдена")
    up_task.check_response_is_(404)



