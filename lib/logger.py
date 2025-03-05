import datetime
import os


class Logger:
    file_name = f"logs/log" + str(datetime.datetime.now()) + ".log"

    @classmethod
    def _write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding="utf=8") as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url:str, data:dict, headers: dict, cookies:dict, method: str):
        testname = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {testname}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}"
        data_to_add += f"Request method: {method}"
        data_to_add += f"URL: {url}"
        data_to_add += f"Request data: {data}"
        data_to_add += f"Request headers: {headers}"
        data_to_add += f"Request cookies: {cookies}"
        data_to_add += f"\n"