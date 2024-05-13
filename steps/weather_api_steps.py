from behave import *

from utilities.ApiUtility import APIUtility
from utilities.LoggerUtility import LoggerUtility

api_util = APIUtility()
logger = LoggerUtility.my_logger()


@when('User sends "{method}" call to endpoint "{endpoint}" with city as "{city}"')
def step_impl(context, method, endpoint, city):
    context.response = api_util.method_call(method, endpoint, city)
    logger.info("User sends: ", method + " call to endpoint: ", endpoint + " with city as: ", city)


@then('User verifies the status code is "{status_code}"')
def step_impl(context, status_code):
    actual_status_code = context.response.status_code
    assert actual_status_code == int(status_code)
    logger.info("The status code returned is: ", status_code)


@step("User verifies GET response contains following information")
def step_impl(context):
    response_body = context.response.json()
    assert response_body['location']['name'] == context.table[0][0]
    assert response_body['location']['region'] == context.table[0][1]
    assert response_body['location']['country'] == context.table[0][2]
    logger.info("The GET response body contains the required details")
