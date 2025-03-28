from tests.api.api_endpoints.register_user import RegisterUser
from tests.api.payload.payload import valid_user_payload
from tests.api.payload.payload import invalid_user_payload



def test_create_user():
    new_user = RegisterUser()
    new_user.new_user(valid_user_payload)
    print("User creation (response 201): Пользователь успешно зарегистрирован")
    new_user.check_response_is_(201)

    new_user.new_user(valid_user_payload)
    print("User creation (response 400): Неверный запрос или пользователь уже существует")
    new_user.check_response_is_(400)


    new_user.new_user(invalid_user_payload)




