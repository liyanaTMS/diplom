import requests

from tests.api.api_endpoints.base_endpoint import EndpointApi


class GetTask(EndpointApi):

    def get_task(self, get_id, session):
        self.response = session.get(f"{self.url}/tasks/{get_id}")
        self.response_json = self.response.json()
        print("Task after getID task:", self.response_json)

    def get_task_for404(self, g_id, session):
        self.response = session.get(f"{self.url}/tasks/{g_id}")
        if self.response.status_code == 200:
            data = self.response.json()
            print("Task after getID task. Success response! Response data:", data)
        elif self.response.status_code == 404:
            # Обработка случая, когда ресурс не найден
            print("Not found response. Status code:", self.response.status_code)
            # Если сервер вернул HTML, response.json() упадёт, поэтому проверяем тип
            print("Response text:", self.response.text)



    def check_task_get(self):
        print("Get task (response 200): Успешный ответ")
        self.check_response_is_(200)