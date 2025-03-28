import requests
from tests.api.payload.payload import headers
from tests.api.api_endpoints.base_endpoint import EndpointApi


class UpdateTask(EndpointApi):
    schema = {
            "title": {"type": "string"},
            "description": {"type": "string"},
            "completed": {"type": "boolean"}
        }


    def update_task(self, up_id, payload, session):
        self.response = session.put(f"{self.url}/tasks/{up_id}", json=payload, headers=headers)
        self.response_json = self.response.json()
        print("Task after update:", self.response_json)

    def update_task_for404(self, up_id, payload, session):
        self.response = session.put(f"{self.url}/tasks/{up_id}", json=payload, headers=headers)
        if self.response.status_code == 200:
            data = self.response.json()
            print("Task after update task. Success response! Response data:", data)
        elif self.response.status_code == 404:
            # Обработка случая, когда ресурс не найден
            print("Not found response. Status code:", self.response.status_code)
            # Если сервер вернул HTML, response.json() упадёт, поэтому проверяем тип
            print("Response text:", self.response.text)


    def check_task_update(self):
        print("Update task (response 200): Задача обновлена")
        self.check_response_is_(200)
