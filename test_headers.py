import pytest
import requests

from main import amount


class TestHeaders:
    def setup(self):
        needed_headers = {'Date', 'Content-Type',
                          'Content-Length',
                          'Connection', 'Keep-Alive', 'Server',
                          'Set-Cookie',
                          'Cache-Control', 'Expires'}

    def test_headers(self):
        expected_headers = {'Date': 'Tue, 21 Jan 2025 13:26:23 GMT', 'Content-Type': 'text/html; charset=utf-8',
                            'Content-Length': '0', 'Connection': 'keep-alive', 'Keep-Alive': 'timeout=10',
                            'Server': 'Apache',
                            'Set-Cookie': 'HomeWork=hw_value; expires=Fri, 21-Feb-2025 13:26:23 GMT; Max-Age=2678400; path=/; domain=playground.learnqa.ru; HttpOnly',
                            'Cache-Control': 'max-age=0', 'Expires': 'Tue, 21 Jan 2025 13:26:23 GMT'}
        # Для тестирования теста:
        #
        # resp_headers_more_example = {'Date': '',
        #                              'Cache-Control': '', 'Expires': '', 'Bulka': '', 'Palka': ''}
        # resp_headers_less_example = {'Date': '', 'Cache-Control': ''}
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        response_headers = response.headers
        new_headers = []
        lost_headers = []

        for header in expected_headers:
            if header not in response_headers:
                lost_headers.append(header)
        for header in response_headers:
            if header not in expected_headers:
                new_headers.append(header)
        sum_len = len(new_headers) + len(lost_headers)
        assert sum_len == 0, f"new headers: {new_headers}, lost headers {lost_headers}"
