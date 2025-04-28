import requests
from tests.api.api_endpoints.base_endpoint import EndpointApi

class DeleteTask(EndpointApi):
    schema = {
            "title": {"type": "string"},
            "description": {"type": "string"},
            "completed": {"type": "boolean"}
        }

    def delete_task(self, del_id, session):
        self.response = session.delete(f"{self.url}/tasks/{del_id}")
        # self.response_json = self.response.json() тут нам не нужно так как апи не возвращает никчего кроме кода
        print("Task after delete task:", self.response_json)

    def delete_task1(self, del_id):
        self.response = requests.delete(f"{self.url}/tasks/{del_id}")
        # self.response_json = self.response.json() тут нам не нужно так как апи не возвращает никчего крое кода
        print(self.response_json)

    def delete_task_for404(self, del_id, session):
        self.response = session.delete(f"{self.url}/tasks/{del_id}")
        if self.response.status_code == 204:
            #
            #
            # data = self.response.json() тут нам не нужно так как апи не возвращает никчего кроме кода
            print("Task after delete task. Success response!")
        elif self.response.status_code == 404:
            # Обработка случая, когда ресурс не найден
            print("Not found response. Status code:", self.response.status_code)
            # Если сервер вернул HTML, response.json() упадёт, поэтому проверяем тип
            print("Response text:", self.response.text)




    def check_task_delete(self):
        print("Deleted task  (response 204): Задача удалена")
        self.check_response_is_(204)
