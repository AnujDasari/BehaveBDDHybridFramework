from pages.BasePage import BasePage


class RetryLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    invalid_credentials_toast_message_xpath = "//div[@class='toast-message']"

    def wait_for_visibility_of_toast_message(self):
        self.wait_for_visibility_of_element("invalid_credentials_toast_message_xpath",
                                            self.invalid_credentials_toast_message_xpath)

    def check_invalid_credentials_toast_message(self, expected_warning_message):
        self.wait_for_visibility_of_toast_message()
        return self.element_text_equals("invalid_credentials_toast_message_xpath",
                                        self.invalid_credentials_toast_message_xpath, expected_warning_message)
