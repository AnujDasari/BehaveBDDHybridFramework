from pages.BasePage import BasePage
from pages.EmploymentManagementPage import EmployeeManagementPage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_text_field_id = "txtUsername"
    password_text_field_id = "txtPassword"
    login_button_xpath = "//button[@type='submit']"
    username_cannot_be_empty_message_id = "txtUsername-error"
    password_cannot_be_empty_message_id = "txtPassword-error"

    def check_login_page_title(self, expected_title):
        return self.verify_page_title(expected_title)

    def enter_username(self, username):
        self.type_into_element("username_text_field_id", self.username_text_field_id, username)

    def enter_password(self, password):
        self.type_into_element("password_text_field_id", self.password_text_field_id, password)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        return EmployeeManagementPage(self.driver)

    def check_username_cannot_be_empty_message(self, username_error_message):
        return self.element_text_equals("username_cannot_be_empty_message_id",
                                        self.username_cannot_be_empty_message_id, username_error_message)

    def check_password_cannot_be_empty_message(self, password_error_message):
        return self.element_text_equals("password_cannot_be_empty_message_id", self.password_cannot_be_empty_message_id,
                                        password_error_message)
