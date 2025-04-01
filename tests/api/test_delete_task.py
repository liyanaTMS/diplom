from tests.api.api_endpoints.delete_task import DeleteTask
from tests.api.api_endpoints.create_task import CreateTask
from tests.api.payload.payload import valid_task_payload


def test_delete_task(register_and_login_user):
    new_task = CreateTask()
    new_task.create_task(valid_task_payload, register_and_login_user)
    created_task_id = new_task.get_id_()

    del_task = DeleteTask()
    # удаление задачи (response 204). успешно
    del_task.delete_task_for404(created_task_id, register_and_login_user)
    print("Deleted task (response 204): Задача удалена")
    del_task.check_response_is_(204)
    del_task.return_response()
    # проверка соответствия пришедшего респонса и отправленного респонса
    del_task.check_none_fields()

    # удаление задачи (response 404). НЕуспешно
    del_task.delete_task_for404(55555, register_and_login_user)
    print("Deleted task (response 404): Задача не найдена")
    del_task.check_response_is_(404)
    del_task.return_response()
