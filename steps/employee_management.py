from behave import *

from pages.LeftMenuPage import LeftMenuPage
from utilities.LoggerUtility import LoggerUtility

logger = LoggerUtility.my_logger()


@when(u'User clicks on Employee List link')
def step_imp(context):
    context.employee_list_page = context.employee_management_page.click_on_employee_list_link()
    logger.info("User clicked on Employee List link")


@when(u'User enters valid employee name as "{existing_employee_name}" in the Employee Name search field')
def step_impl(context, existing_employee_name):
    context.employee_list_page.wait_for_visibility_of_right_chevron_icon()
    context.employee_list_page.enter_employee_name(existing_employee_name)
    logger.info("User entered valid employee name: ", existing_employee_name + " in Employee name search field")


@when(u'User clicks on Search icon')
def step_impl(context):
    context.employee_list_page.click_on_employee_name_field_search_icon()
    logger.info("User clicked on Search icon in Employee name field")


@then(u'Employee details with employee id "{employee_id}" should be displayed')
def step_impl(context, employee_id):
    context.employee_list_page.wait_for_invisibility_of_right_chevron_icon()
    assert context.employee_list_page.check_employee_id_from_employee_details_table(employee_id)
    logger.info("Employee details with the employee id: ", employee_id + " is displayed")


@when(u'User enters non existing employee name as "{non_existing_employee_name}" in the Employee Name search field')
def step_impl(context, non_existing_employee_name):
    context.employee_list_page.wait_for_visibility_of_right_chevron_icon()
    context.employee_list_page.enter_employee_name(non_existing_employee_name)
    logger.info("User entered invalid employee name: ", non_existing_employee_name + " in Employee name search field")


@then(u'Toast message "{no_records_found_message}" should be displayed')
def step_impl(context, no_records_found_message):
    assert context.employee_list_page.check_no_records_found_toast_message(no_records_found_message)
    logger.info("Toast with message: ", no_records_found_message + " is displayed")


@when(u'User clicks on Request Desk option from the left menu')
def step_impl(context):
    context.left_menu_page = LeftMenuPage(context.driver)
    context.request_type_page = context.left_menu_page.click_on_request_desk_option()
    logger.info("User clicked on 'Request Desk' option from the left menu")


@when(u'User selects Resignation Request from the Request type dropdown')
def step_impl(context):
    context.request_type_page.select_resignation_request_from_request_type_dropdown()
    logger.info("User selected 'Resignation Request' from the Request type dropdown")


@when(u'User clicks on Next button')
def step_impl(context):
    context.submit_request = context.request_type_page.click_on_next_button()
    logger.info("User clicked on Next button")


@when(u'User enters resignation reason as "{resignation_reason}"')
def step_impl(context, resignation_reason):
    context.submit_request.enter_request_description(resignation_reason)
    logger.info("User enters resignation reason: ", resignation_reason)


@when(u'User enters resolution date as "{resolution_date}"')
def step_impl(context, resolution_date):
    context.submit_request.enter_resolution_date(resolution_date)
    logger.info("User enters resolution date: ", resolution_date)


@when(u'User enters resignation date as "{resignation_date}"')
def step_impl(context, resignation_date):
    context.submit_request.enter_resignation_date(resignation_date)
    logger.info("User enters resignation date: ", resignation_date)


@when(u'User clicks on Cancel button')
def step_impl(context):
    context.my_requests_page = context.submit_request.click_on_cancel_button()
    logger.info("User clicks on Cancel button")


@then(u'Requests page should be displayed with title as "{my_requests_page_title}"')
def step_impl(context, my_requests_page_title):
    assert context.my_requests_page.check_my_requests_page_title(my_requests_page_title)
    logger.info("Requests page is displayed with page title as: ", my_requests_page_title)
