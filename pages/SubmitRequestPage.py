from pages.BasePage import BasePage
from pages.MyRequestsPage import MyRequestsPage


class SubmitRequestPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    submit_request_header_xpath = "//h4[text()='Submit Request']"
    description_input_field_id = "description"
    resolution_date_field_id = "resolutionDate"
    resignation_date_field_xpath = "//input[@id='1']"
    cancel_button_xpath = "//a[@class='modal-action modal-close waves-effect waves-green btn']"

    def enter_request_description(self, request_description):
        self.wait_for_visibility_of_element("description_input_field_id", self.description_input_field_id)
        self.type_into_element("description_input_field_id", self.description_input_field_id, request_description)

    def enter_resolution_date(self, resolution_date):
        self.type_into_element("resolution_date_field_id", self.resolution_date_field_id, resolution_date)

    def enter_resignation_date(self, resignation_date):
        self.type_into_element("resignation_date_field_xpath", self.resignation_date_field_xpath, resignation_date)

    def click_on_cancel_button(self):
        self.click_on_element("cancel_button_xpath", self.cancel_button_xpath)
        return MyRequestsPage(self.driver)
