from pages.BasePage import BasePage
from pages.EmployeeListPage import EmployeeListPage


class EmployeeManagementPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    employee_list_link_xpath = "//a[text()='Employee List ']"
    logout_link_xpath = "//span[text()='Log Out']"

    def is_logout_link_displayed(self):
        return self.is_element_displayed("logout_link_xpath", self.logout_link_xpath)

    def click_on_employee_list_link(self):
        self.click_on_element("employee_list_link_xpath", self.employee_list_link_xpath)
        return EmployeeListPage(self.driver)
