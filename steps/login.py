from behave import *

from pages.LoginPage import LoginPage
from pages.RetryLoginPage import RetryLoginPage
from utilities.LoggerUtility import LoggerUtility

logger = LoggerUtility.my_logger()


@given(u'User navigated to Login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    logger.info("User navigated to Login page")


@when(u'User enters valid username as "{username}" and password as "{password}" into the fields')
def step_impl(context, username, password):
    context.login_page.enter_username(username)
    context.login_page.enter_password(password)
    logger.info("User entered username and password")


@when(u'User clicks on Login button')
def step_impl(context):
    context.employee_management_page = context.login_page.click_on_login_button()
    logger.info("User clicked on Login button")


@then(u'User should get logged in')
def step_impl(context):
    assert context.employee_management_page.is_logout_link_displayed()
    logger.info("Asserting if login is successful")


@then(u'User should get a proper warning message as "{error_message}"')
def step_impl(context, error_message):
    context.retry_login_page = RetryLoginPage(context.driver)
    assert context.retry_login_page.check_invalid_credentials_toast_message(error_message)
    logger.info("Checking if toast message is displayed")


@when(u'User enters invalid username and invalid password into the fields')
def step_impl(context):
    for row in context.table:
        context.login_page.enter_username(row["username"])
        context.login_page.enter_password(row["password"])
    logger.info("User entered invalid username and password")


@when(u'User does not enter anything into username and password fields')
def step_impl(context):
    context.login_page.enter_username("")
    context.login_page.enter_password("")
    logger.info("User does not enter anything in username and password fields")


@then(u'User should see proper warning message under username and password fields')
def step_impl(context):
    for row in context.table:
        assert context.login_page.check_username_cannot_be_empty_message(row["username_error_message"])
        assert context.login_page.check_password_cannot_be_empty_message(row["password_error_message"])
    logger.info("Appropriate warning messages should be displayed under username and password fields")
