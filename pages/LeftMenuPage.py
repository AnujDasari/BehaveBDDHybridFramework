from pages.BasePage import BasePage
from pages.RequestTypePage import RequestTypePage


class LeftMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    hr_administration_option_xpath = "(//span[contains(text(),'HR Administration')])[1]"
    request_desk_option_xpath = "(//span[contains(text(),'Request Desk')])[1]"

    def click_on_request_desk_option(self):
        self.wait_for_element_to_be_clickable("hr_administration_option_xpath", self.hr_administration_option_xpath)
        self.move_to_element("hr_administration_option_xpath", self.hr_administration_option_xpath)
        self.move_to_element("request_desk_option_xpath", self.request_desk_option_xpath)
        self.click_on_element("request_desk_option_xpath", self.request_desk_option_xpath)
        return RequestTypePage(self.driver)
