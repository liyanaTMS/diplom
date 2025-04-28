import requests
from tests.api.api_endpoints.base_endpoint import EndpointApi

class ChangeTask(EndpointApi):
    schema = {
            "title": {"type": "string"},
            "description": {"type": "string"},
            "completed": {"type": "boolean"}
        }

    def change_task(self, change_id, payload, session):
        self.response = session.post(f"{self.url}/tasks/{change_id}/toggle", json=payload)
        self.response_json = self.response.json()
        print("Task after change task: ", self.response_json)

    def change_task_for404(self, change_id, payload, session):
        self.response = session.post(f"{self.url}/tasks/{change_id}/toggle", json=payload)
        if self.response.status_code == 200:
            data = self.response.json()
            print("Task after change task. Success response! Response data:", data)
        elif self.response.status_code == 404:
            # Обработка случая, когда ресурс не найден
            print("Not found response. Status code:", self.response.status_code)
            # Если сервер вернул HTML, response.json() упадёт, поэтому проверяем тип
            print("Response text:", self.response.text)

    def check_task_change(self):
        print("Changed task status (response 200): Статус задачи изменен")
        self.check_response_is_(200)