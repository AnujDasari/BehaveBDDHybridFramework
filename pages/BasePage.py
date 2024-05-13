from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def verify_page_title(self, expected_title):
        return self.driver.title.__eq__(expected_title)

    def get_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def get_elements(self, locator_type, locator_value):
        elements = None
        if locator_type.endswith("_id"):
            elements = self.driver.find_elements(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            elements = self.driver.find_elements(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            elements = self.driver.find_elements(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            elements = self.driver.find_elements(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_xpath"):
            elements = self.driver.find_elements(By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            elements = self.driver.find_elements(By.CSS_SELECTOR, locator_value)
        return elements

    @staticmethod
    def get_element_locator(locator_type, locator_value):
        locator = None
        if locator_type.endswith("_id"):
            locator = (By.ID, locator_value)
        elif locator_type.endswith("_name"):
            locator = (By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            locator = (By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_link_text"):
            locator = (By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_xpath"):
            locator = (By.XPATH, locator_value)
        elif locator_type.endswith("_css"):
            locator = (By.CSS_SELECTOR, locator_value)
        return locator

    def click_on_element(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        element.click()

    def type_into_element(self, locator_type, locator_value, text_to_type):
        element = self.get_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_type)

    def element_text_contains(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__contains__(expected_text)

    def element_text_equals(self, locator_type, locator_value, expected_text):
        element = self.get_element(locator_type, locator_value)
        return element.text.__eq__(expected_text)

    def is_element_displayed(self, locator_type, locator_value):
        element = self.get_element(locator_type, locator_value)
        return element.is_displayed()

    def wait_for_visibility_of_element(self, locator_type, locator_value):
        wait = WebDriverWait(self.driver, timeout=60)
        return wait.until(
            expected_conditions.visibility_of_element_located(
                self.get_element_locator(locator_type, locator_value)))

    def wait_for_invisibility_of_element(self, locator_type, locator_value):
        wait = WebDriverWait(self.driver, timeout=60)
        return wait.until(
            expected_conditions.invisibility_of_element_located(
                self.get_element_locator(locator_type, locator_value)))

    def select_option_from_dropdown_based_on_text(self, locator_type, locator_value, dropdown_option_text):
        self.wait_for_element_to_be_clickable(locator_type, locator_value, )
        element = self.get_element(locator_type, locator_value)
        select = Select(element)
        select.select_by_visible_text(dropdown_option_text)

    def wait_for_element_to_be_clickable(self, locator_type, locator_value):
        wait = WebDriverWait(self.driver, timeout=60)
        return wait.until(
            expected_conditions.element_to_be_clickable(self.get_element_locator(locator_type, locator_value)))

    def move_to_element(self, locator_type, locator_value):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_element(locator_type, locator_value)).perform()
