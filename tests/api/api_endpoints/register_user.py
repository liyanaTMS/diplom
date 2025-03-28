import requests
from tests.api.api_endpoints.base_endpoint import EndpointApi

class RegisterUser(EndpointApi):
    schema = {
            "username": {"string"},
            "password": {"string"}
        }
    def new_user(self, payload):
        self.response = requests.post(f"{self.url}/register", json=payload)
        self.response_json = self.response.json()
        if self.response.status_code == 400:
            print(self.response_json)
        else:
            print("New user was created: ", self.response_json)

    def check_user_register(self):
        print("User creation (response 201): Пользователь успешно зарегистрирован")
        self.check_response_is_(201)
