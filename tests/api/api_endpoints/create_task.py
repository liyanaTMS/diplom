import requests
from tests.api.api_endpoints.base_endpoint import EndpointApi
from tests.api.payload.payload import headers

class CreateTask(EndpointApi):
    schema = {
    "title": "string",
    "description": "string",
    "completed": True
}


    def create_task(self, payload, session):
        self.response = session.post(f"{self.url}/tasks", json=payload, headers=headers)
        self.response_json = self.response.json()
        print("Task after create:", self.response_json)

    def create_task1(self, payload):
        self.response = requests.post(f"{self.url}/tasks", json=payload, headers=headers)
        self.response_json = self.response.json()
        print("Task after create:", self.response_json)

    def check_task_creation(self):
        print("Task creation (response 201): Задача создана")
        self.check_response_is_(201)



    # def get_task_id(self):
    #     task_id = self.response_json.get("id")
    #     return task_id
