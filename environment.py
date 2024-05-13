import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import ConfigReaderUtility


def before_scenario(context, driver):
    context.web = ConfigReaderUtility.read_configuration("basic info", "web")
    if context.web.__eq__("True"):
        browser_name = ConfigReaderUtility.read_configuration("basic info", "browser")
        if browser_name.__eq__("chrome"):
            context.driver = webdriver.Chrome()
        elif browser_name.__eq__("firefox"):
            context.driver = webdriver.Firefox()
        elif browser_name.__eq__("edge"):
            context.driver = webdriver.Edge()

        context.driver.maximize_window()
        context.driver.get(ConfigReaderUtility.read_configuration("basic info", "url"))


def after_scenario(context, driver):
    if context.web.__eq__("True"):
        context.driver.quit()


def before_step(context, step):
    context.step = step


def after_step(context, step):
    if context.web.__eq__("True"):
        if step.status == 'failed':
            allure.attach(context.driver.get_screenshot_as_png(),
                          name=context.step.name + "_failed",
                          attachment_type=AttachmentType.PNG)

        else:
            allure.attach(context.driver.get_screenshot_as_png(),
                          name=context.step.name,
                          attachment_type=AttachmentType.PNG)
