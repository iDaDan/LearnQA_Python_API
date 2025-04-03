from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserDelete(BaseCase):
    def setup_method(self):
        self.user_id_after_auth = None
        self.email = None
        self.password = None
        self.auth_sid = None
        self.token = None
        self.user_id_from_auth_method = None

    def create_second_user(self):
        data_create = self.prepare_registration_data()
        response_create = MyRequests.post(
            "/user/",
            data_create
        )
        Assertions.assert_code_status(response_create, 200)
        Assertions.assert_json_has_key(response_create, "id")
        second_id = response_create.json()["id"]
        return second_id

    def test_try_delete_special_authorised_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        #Login
        response_login = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response_login, "auth_sid")
        self.token = self.get_header(response_login, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response_login, "user_id")
        self.user_id_after_auth = self.user_id_from_auth_method

        Assertions.assert_user_login_results(response_login)

        response_auth = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response_auth,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

        #Delete

        response_delete = MyRequests.delete("/user/2",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid})
        print(f"response_delete.status_code: {response_delete.status_code}, response_delete.content: {response_delete.content}")
        Assertions.assert_code_status(response_delete,400)
        assert response_delete.text == '{"error":"Please, do not delete test users with ID 1, 2, 3, 4 or 5."}'

        #GET ID AFTER DELETE
        resp_get_after_delete = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            resp_get_after_delete,
            "user_id",
            2,
            f"Special User 2 is deleted"
        )



    def test_delete_authorised_user(self):

        user_data=self.create_user_and_login()
        # LOGIN
        self.auth_and_check(
            user_data["user_id"],
            user_data["x-csrf-token"],
            user_data["auth_sid"])

        #GET STAT CODE
        response = MyRequests.get(f"/user/{user_data["user_id"]}")
        Assertions.assert_code_status(response, 200)
        #DELETE
        response_delete = MyRequests.delete(f"/user/{user_data["user_id"]}",
                                            headers={"x-csrf-token": user_data["x-csrf-token"]},
                                            cookies={"auth_sid": user_data["auth_sid"]})
        Assertions.assert_code_status(response_delete, 200)
        assert response_delete.text == '{"success":"!"}'

        response = MyRequests.get(f"/user/{user_data["user_id"]}")
        Assertions.assert_code_status(response,404)

    def test_try_delete_another_user(self):
        first_user_data = self.create_user_and_login()
        second_user_data = self.create_user_and_login()

        self.auth_and_check(
            first_user_data["user_id"],
            first_user_data["x-csrf-token"],
            first_user_data["auth_sid"])


        # GET STAT CODE
        response = MyRequests.get(f"/user/{second_user_data["user_id"]}")
        Assertions.assert_code_status(response, 200)

        # DELETE
        response_delete = MyRequests.delete(f"/user/{second_user_data["user_id"]}",
                                            headers={"x-csrf-token": first_user_data["x-csrf-token"]},
                                            cookies={"auth_sid": first_user_data["auth_sid"]})

        Assertions.assert_code_status(response_delete, 400)
        # тут похоже баг