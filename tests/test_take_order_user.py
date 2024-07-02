import allure
import requests

from data import Urls, TextAnswer, Ingredients


class TestTakeOrderUser:
    @allure.title("Получение заказа авторизованным пользователем")
    def test_take_order_auth_user(self, create_user):

        respons_created, data = create_user

        token = respons_created.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        ingredients = {"ingredients": [Ingredients.BUN, Ingredients.KOKLETA, Ingredients.SAUCE, Ingredients.BUN]}
        requests.post(Urls.CREATE_ORDER, data=ingredients, headers=headers)
        order = requests.get(Urls.GET_ORDER, headers=headers)

        assert order.status_code == 200
        assert respons_created.json()['success'] is True

    @allure.title("Получение заказа неавторизованным пользователем")
    def test_take_order_unauthorized_user(self):

        order = requests.get(Urls.GET_ORDER)

        assert order.status_code == 401
        assert order.json()['success'] is False
        assert order.json()['message'] == TextAnswer.ORDER_WITHOUT_AUTH