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
        needed_headers = {'Date', 'Content-Type',
                          'Content-Length',
                          'Connection', 'Keep-Alive', 'Server',
                          'Set-Cookie',
                          'Cache-Control', 'Expires', 'Bulka', 'Palka'}
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        resp_headers = response.headers
        len_resp_headers=len(resp_headers)
        len=
        assert len(resp_headers) > len(needed_headers), "too much headers"
        for header in needed_headers:
            assert resp_headers.get(header), f"no {header} header"
            # if resp_headers.get(header):
            #     print(f'header {header} presented')
            # else:
            #     print(f"no {header} header")
        #print(f"headers = {resp_headers}")
        #assert needed_headers in resp_headers , "не валидные хедеры"