import random
import string
import allure

class Methods:

    @allure.title('Рандомная геренация строки')
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(length))
        return random_string

    @allure.title('Рандомная генерация пользовательских данныхтам')
    @staticmethod
    def generate_user_data():
        email = Methods.generate_random_string(6) + '@yandex.ru'
        password = Methods.generate_random_string(10)
        name = Methods.generate_random_string(10)
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        return payload

