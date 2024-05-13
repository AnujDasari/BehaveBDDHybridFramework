from pages.BasePage import BasePage
from pages.SubmitRequestPage import SubmitRequestPage


class RequestTypePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    request_type_header_xpath = "//h4[normalize-space()='Request Type']"
    request_type_dropdown_xpath = "//input[@class='select-dropdown']"
    resignation_request_option_xpath = "//span[text()='Resignation Request']"
    cancel_button_xpath = "//a[@class='modal-action modal-close waves-effect waves-green btn']"
    next_button_xpath = "//a[text()='Next']"

    def select_resignation_request_from_request_type_dropdown(self):
        self.wait_for_visibility_of_element("request_type_dropdown_xpath",
                                            self.request_type_dropdown_xpath)
        self.click_on_element("request_type_dropdown_xpath", self.request_type_dropdown_xpath)
        self.wait_for_element_to_be_clickable("resignation_request_option_xpath",
                                              self.resignation_request_option_xpath)
        self.click_on_element("resignation_request_option_xpath", self.resignation_request_option_xpath)

    def click_on_next_button(self):
        self.click_on_element("next_button_xpath", self.next_button_xpath)
        return SubmitRequestPage(self.driver)
