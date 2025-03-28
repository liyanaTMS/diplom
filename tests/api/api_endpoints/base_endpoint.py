import requests
import jsonschema
# default_session = requests.Session()

class EndpointApi:
    response = None
    response_json = None
    response_status = None
    #session = default_session
    schema = {}
    # url = "http://localhost:5000/api/" для  локльаного запуска
    url = "http://web:5000/api/" # для докера

    def check_response_is_(self, value):
        assert self.response.status_code == value, \
            f'{self.response.status_code}'
    def return_response(self):
        print("Response returns:", self.response_json)



    def check_response_is_200(self):
        assert self.response.status_code == 200, \
            f'{self.response.status_code}'

    def get_data(self):
        return self.response.json()

    def get_id_(self):
        return self.response_json.get('id')

    def get_title(self):
        return self.get_data()['title']

    def get_description(self):
        return self.get_data()['description']

    def get_completed(self):
        return self.get_data()['completed']


    def validate_response(self, data):
        jsonschema.validate(instance=data, schema=self.schema)

    def check_all_fields(self, expected_data):
        assert self.get_title() == expected_data['title'], 'wrong title was responsed'
        assert self.get_description() == expected_data['description'], 'wrong description was responsed'
        assert self.get_completed() == expected_data['completed'], 'wrong completed was responsed'

    def check_none_fields(self):
        if self.response_json == None:
            print("Задача была удалена")
        else:
            print("Response:", self.response_json)


    def check_response_is_201(self):
        assert self.response.status_code == 201, \
            f'Expected 201, got {self.response.status_code}'



    def check_response_is_204(self):
        assert self.response.status_code == 204, \
            f'Expected 204, got {self.response.status_code}'