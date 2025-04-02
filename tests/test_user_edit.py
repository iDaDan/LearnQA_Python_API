import json
import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

@allure.epic("user edit cases")
class TestUserEdit(BaseCase):

    def setup_method(self):
        with allure.step("set expected_fields"):
            self.expected_fields = ["username", "email", "firstName", "lastName"]

    def get_id_second_user(self):
        data_create = self.prepare_registration_data()
        response_create = MyRequests.post(
            "/user/",
            data_create
        )
        Assertions.assert_code_status(response_create, 200)
        Assertions.assert_json_has_key(response_create, "id")
        second_id = response_create.json()["id"]
        return second_id


    def response_edit(self, user_credentials, operational_data):
        response_edit = MyRequests.put(
            f"/user/{user_credentials["user_id_after_check"]}",
            headers={"x-csrf-token": user_credentials["token"]},
            cookies={"auth_sid": user_credentials["auth_sid"]},
            data=operational_data
        )
        Assertions.assert_code_status(response_edit, 200)

    def response_edit_4000(self, user_credentials, operational_data):
        response_edit = MyRequests.put(
            f"/user/{user_credentials["user_id_after_check"]}",
            headers={"x-csrf-token": user_credentials["token"]},
            cookies={"auth_sid": user_credentials["auth_sid"]},
            data=operational_data
        )
        Assertions.assert_code_status(response_edit, 400)


    def test_edit_just_created_user(self):
        user_credentials= self.create_user_and_auth()
        # EDIT
        new_data = self.prepare_registration_data()
        self.response_edit(user_credentials,new_data)

        #GET INFO AFTER EDIT
        response_after_edit = MyRequests.get(f"/user/{user_credentials["user_id_after_check"]}",
                                   headers={"x-csrf-token": user_credentials["token"]},
                                   cookies={"auth_sid": user_credentials["auth_sid"]})

        Assertions.assert_json_has_keys(response_after_edit, self.expected_fields)
        email_after_edit = json.loads(response_after_edit.content)["email"]
        print(f"user_credentials: {user_credentials}")
        assert email_after_edit != user_credentials["email"], \
            f"email {user_credentials["email"]} is not edited"

    def test_try_edit_another_user(self):
        first_user_data = self.create_user_and_login()
        second_user_data= self.create_user_and_login()
        firstname_for_editing = {"firstName": "EditedFirsName"}

        #авторизация первым пользователем
        self.auth_and_check(
            first_user_data["user_id"],
            first_user_data["x-csrf-token"],
            first_user_data["auth_sid"])

        # TRY EDIT BEFORE SECOND USER AUTH
        print(f"data_for_editing {second_user_data["user_id"]}")
        response_edit1 = MyRequests.put(
            f"/user/{second_user_data["user_id"]}",
            headers={"x-csrf-token": first_user_data["x-csrf-token"]},
            cookies={"auth_sid": first_user_data["auth_sid"]},
            data=firstname_for_editing
        )
        Assertions.assert_code_status(response_edit1, 200)
        print(
            f"__response_edit.content__:{response_edit1.content} \n __response_edit.status_code__:{response_edit1.status_code}")

        # SECOND USER AUTH
        self.auth_and_check(
            second_user_data["user_id"],
            second_user_data["x-csrf-token"],
            second_user_data["auth_sid"])

        # EDIT
        print(f"data_for_editing {second_user_data["user_id"]}")
        response_edit = MyRequests.put(
            f"/user/{second_user_data["user_id"]}",
            headers={"x-csrf-token": first_user_data["x-csrf-token"]},
            cookies={"auth_sid": first_user_data["auth_sid"]},
            data=firstname_for_editing
        )

        Assertions.assert_code_status(response_edit, 200)
        print(f"__response_edit.content__:{response_edit.content} \n __response_edit.status_code__:{response_edit.status_code}")

        # GET INFO SECOND USER AFTER EDIT
        response_after_edit = MyRequests.get(
            f"/user/{second_user_data["user_id"]}",
            headers={"x-csrf-token": second_user_data["x-csrf-token"]},
            cookies={"auth_sid": second_user_data["auth_sid"]})
        Assertions.assert_json_has_keys(response_after_edit, self.expected_fields)

        firstname_after_edit = json.loads(response_after_edit.content)["firstName"]
        assert firstname_after_edit == second_user_data['firstName'], \
            (f"firstName {second_user_data['firstName']} "
             f"edited to invalid firstName:{firstname_after_edit}")

    def test_edit_just_created_user_invalid_email(self):
        user_credentials= self.create_user_and_auth()
        # EDIT
        default_mail=user_credentials["email"]
        print(f"default_mail={default_mail}")
        invalid_mail = "vjjjyashmelexmple.ru"
        user_credentials["email"] = invalid_mail

        self.response_edit()

        response_edit = MyRequests.put(
            f"/user/{user_credentials["user_id_after_check"]}",
            headers={"x-csrf-token": user_credentials["token"]},
            cookies={"auth_sid": user_credentials["auth_sid"]},
            data=user_credentials
        )
        Assertions.assert_code_status(response_edit, 400)

        # GET INFO AFTER EDIT
        response_after_edit = MyRequests.get(f"/user/{user_credentials["user_id_after_check"]}",
                                             headers={"x-csrf-token": user_credentials["token"]},
                                             cookies={"auth_sid": user_credentials["auth_sid"]})

        Assertions.assert_json_has_keys(response_after_edit, self.expected_fields)
        email_after_edit = json.loads(response_after_edit.content)["email"]
        assert email_after_edit == default_mail, f"email {default_mail} edited to invalid mail:{email_after_edit}"

    def test_edit_just_created_user_short_firstname(self):
        user_credentials = self.create_user_and_auth()
        default_firstname = user_credentials["firstName"]
        user_credentials["firstName"] = 'a'
        # EDIT

        response_edit = MyRequests.put(
            f"/user/{user_credentials["user_id_after_check"]}",
            headers={"x-csrf-token": user_credentials["token"]},
            cookies={"auth_sid": user_credentials["auth_sid"]},
            data=user_credentials
        )

        Assertions.assert_code_status(response_edit, 400)

        # GET INFO AFTER EDIT
        response_after_edit = MyRequests.get(f"/user/{user_credentials["user_id_after_check"]}",
                                             headers={"x-csrf-token": user_credentials["token"]},
                                             cookies={"auth_sid": user_credentials["auth_sid"]})

        Assertions.assert_json_has_keys(response_after_edit, self.expected_fields)
        firstname_after_edit = json.loads(response_after_edit.content)["firstName"]
        assert firstname_after_edit == default_firstname, f"firstname {default_firstname} edited to invalid(short) firstname:{firstname_after_edit}"

    def test_not_authorised_edit_user(self):
        user_credentials=self.create_user_and_auth()
        new_data = self.prepare_registration_data()

        response_edit = MyRequests.put(
            f"/user/{user_credentials["user_id_after_check"]}",
            data=new_data
        )
        print(f"response_edit.status_code: {response_edit.status_code}, response_edit.content: {response_edit.content}")
        Assertions.assert_code_status(response_edit, 400)

        #LOGIN
        data = {
            'email': user_credentials["email"],
            'password': user_credentials["password"]
        }

        response_login = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response_login, "auth_sid")
        self.token = self.get_header(response_login, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response_login, "user_id")
        self.user_id_after_auth = self.user_id_from_auth_method

        Assertions.assert_user_login_results(response_login)

        self.auth_and_check(self.user_id_after_auth, self.token, self.auth_sid)

        # GET INFO AFTER EDIT
        response_after_edit = MyRequests.get(f"/user/{self.user_id_after_auth}",
                                             headers={"x-csrf-token": self.token},
                                             cookies={"auth_sid": self.auth_sid})

        print(f"response_after_edit: {response_after_edit.content}")
        email_after_edit = json.loads(response_after_edit.content)["email"]
        Assertions.assert_json_has_keys(response_after_edit, self.expected_fields)
        assert email_after_edit == user_credentials["email"], f"email {email_after_edit} is edited without auth"