import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

@allure.epic("user delete cases")
class TestUserDelete(BaseCase):

    @allure.description("this method unsuccessfully deleting user from special list")
    def test_try_delete_special_authorised_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        with allure.step(f"try to delet special user with data = {data}"):
            response_login = MyRequests.post("/user/login", data=data)

            auth_variables = self.get_from_response_header_cookie_json(
                response_login,
                "x-csrf-token",
                "auth_sid",
                "user_id"
            )

        Assertions.assert_user_login_results(response_login)

        self.auth_and_check(auth_variables)

        #Delete
        response_delete = MyRequests.delete("/user/2",
            headers={"x-csrf-token": auth_variables["x-csrf-token"]},
            cookies={"auth_sid": auth_variables["auth_sid"]})

        Assertions.assert_code_status(response_delete,400)
        assert response_delete.text == '{"error":"Please, do not delete test users with ID 1, 2, 3, 4 or 5."}'

        #GET ID AFTER DELETE
        resp_get_after_delete = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": auth_variables["x-csrf-token"]},
            cookies={"auth_sid": auth_variables["auth_sid"]}
        )

        Assertions.assert_json_value_by_name(
            resp_get_after_delete,
            "user_id",
            2,
            f"Special User 2 is deleted"
        )

    @allure.description("this method successfully deleting authorised user")
    def test_delete_authorised_user(self):

        user_data=self.create_user_and_login()
        # LOGIN
        self.auth_and_check(user_data)

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

    @allure.description("this method unsuccessfully try to delete another user")
    def test_try_delete_another_user(self):
        first_user_data = self.create_user_and_login()
        second_user_data = self.create_user_and_login()

        self.auth_and_check(first_user_data)

        # GET STAT CODE
        response = MyRequests.get(f"/user/{second_user_data["user_id"]}")
        Assertions.assert_code_status(response, 200)

        # DELETE
        response_delete = MyRequests.delete(f"/user/{second_user_data["user_id"]}",
                                            headers={"x-csrf-token": first_user_data["x-csrf-token"]},
                                            cookies={"auth_sid": first_user_data["auth_sid"]})

        Assertions.assert_code_status(response_delete, 400)
        # тут похоже баг