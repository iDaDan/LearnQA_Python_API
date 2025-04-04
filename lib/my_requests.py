import requests
from lib.logger import Logger
import allure
from environment import ENV_OBJECT


class MyRequests():

    @staticmethod
    def post(url:str, data:dict = None, headers:dict = None, cookies: dict = None):
        with allure.step(f"POST request URL '{url}"):
            return MyRequests._send(url, data, headers, cookies, 'POST')

    @staticmethod
    def get(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"GET request URL '{url}"):
            return MyRequests._send(url, data, headers, cookies, 'GET')

    @staticmethod
    def put(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"PUT request URL '{url}"):
            return MyRequests._send(url, data, headers, cookies, 'PUT')

    @staticmethod
    def delete(url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        with allure.step(f"DELETE request URL '{url}"):
            return MyRequests._send(url, data, headers, cookies, 'DELETE')


    @staticmethod
    def _send(url:str, data:dict, headers: dict, cookies: dict, method: str):

        url = f"{ENV_OBJECT.get_base_url()}{url}" #а чем не подходит обычная переменная?

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        Logger.add_request(url,data,headers,cookies,method)

        if method == "GET":
            response = requests.get(url, params=data, headers=headers, cookies = cookies)
        elif method == "POST":
            response = requests.post(url, data=data, headers=headers, cookies = cookies)
        elif method == "PUT":
            response = requests.put(url, data=data, headers=headers, cookies=cookies)
        elif method == "DELETE":
            response = requests.delete(url, data=data, headers=headers, cookies = cookies)
        else:
            raise Exception(f"Bad HTTP method type '{method}' Was received")

        Logger.add_response(response)

        return response

    @staticmethod
    def user_auth_get(email, password):
        data = {
            'email': email,
            'password': password
        }

        response1 = MyRequests.post("/user/login", data=data)
        return response1
