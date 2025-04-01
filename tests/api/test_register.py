from tests.api.api_endpoints.register_user import RegisterUser
from tests.api.payload.payload import valid_user_payload, invalid_user_payload


def test_register_user():
    """Эта функция проверяет создание пользователя и возврат ошибок 201 и 400"""
    new_user = RegisterUser()
    new_user.new_user(valid_user_payload)
    new_user.check_response_is_(201)
    print("User creation (response 201): Пользователь успешно зарегистрирован")

    new_user.new_user(valid_user_payload)
    new_user.check_response_is_(400)
    print("User creation (response 400): Неверный запрос или пользователь уже существует")

    new_user.new_user(invalid_user_payload)




