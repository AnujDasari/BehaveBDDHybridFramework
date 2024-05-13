from pages.BasePage import BasePage


class EmployeeListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    right_chevron_icon_xpath = "//i[contains(text(),'chevron_right')]"
    employee_name_search_field_id = "employee_name_quick_filter_employee_list_value"
    employee_name_search_field_search_icon_id = "quick_search_icon"
    employee_details_in_table_xpath = "//table[@id='employeeListTable']/tbody/tr"
    employee_id_in_employee_details_table_xpath = "//table[@id='employeeListTable']//td[2]/a"
    no_records_found_message_xpath = "//div[@class='toast-message']"

    def enter_employee_name(self, employee_name):
        self.type_into_element("employee_name_search_field_id", self.employee_name_search_field_id, employee_name)

    def click_on_employee_name_field_search_icon(self):
        self.click_on_element("employee_name_search_field_search_icon_id",
                              self.employee_name_search_field_search_icon_id)

    def is_employee_detail_displayed(self):
        return self.is_element_displayed("employee_details_in_table_xpath", self.employee_details_in_table_xpath)

    def wait_for_visibility_of_right_chevron_icon(self):
        self.wait_for_visibility_of_element("right_chevron_icon_xpath", self.right_chevron_icon_xpath)

    def wait_for_invisibility_of_right_chevron_icon(self):
        self.wait_for_invisibility_of_element("right_chevron_icon_xpath",
                                              self.right_chevron_icon_xpath)

    def check_employee_id_from_employee_details_table(self, employee_id):
        return self.element_text_equals("employee_id_in_employee_details_table_xpath",
                                        self.employee_id_in_employee_details_table_xpath, employee_id)

    def check_no_records_found_toast_message(self, toast_message):
        self.wait_for_visibility_of_element("no_records_found_message_xpath", self.no_records_found_message_xpath)
        return self.element_text_equals("no_records_found_message_xpath", self.no_records_found_message_xpath,
                                        toast_message)
