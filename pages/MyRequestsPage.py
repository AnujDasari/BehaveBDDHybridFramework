from pages.BasePage import BasePage


class MyRequestsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_my_requests_page_title(self, expected_title):
        return self.verify_page_title(expected_title)
