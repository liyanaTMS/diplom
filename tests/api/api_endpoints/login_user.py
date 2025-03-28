import requests
from tests.api.api_endpoints.base_endpoint import EndpointApi


class LoginUser(EndpointApi):
    schema = {
            "username": {"string"},
            "password": {"string"}
        }
    def login_user(self, payload, session):
        # session = requests.Session()
        self.response = session.post(f"{self.url}/login", json=payload)
        self.response_json = self.response.json()
        print(f"User {payload} was logged in the system : ", self.response_json)
        return session
    

    def check_user_login(self):
        self.check_response_is_(200)
        print("User login (response 200): Успешный вход в систему")