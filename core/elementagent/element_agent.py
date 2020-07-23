from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as Conditions
from selenium.webdriver.support.ui import WebDriverWait

import core.preferences.corepreferences as selenapreferences

_selena_preferences = selenapreferences.fetch_core_preferences()
delay_default = None


class DOMElementAgent:
    def __init__(self):
        self.delay = 3
        self.explicit_delay = 10

    def element_xpath_agent(self, x_driver, locator, delay=delay_default):
        if delay is None:
            delay = self.delay
        sleep(delay)
        try:
            found_element = x_driver.find_element_by_xpath(locator)
        except NoSuchElementException:
            return None
        except TimeoutException:
            return False
        return found_element

    def element_id_agent(self, x_driver, element_id, delay=delay_default):
        if delay is None:
            delay = self.delay
        sleep(delay)
        try:
            found_element = x_driver.find_element_by_id(element_id)
        except NoSuchElementException:
            return None
        except TimeoutException:
            return False
        return found_element

    def element_linktext_agent(self, x_driver, link_text, delay=delay_default):
        if delay is None:
            delay = self.delay
        sleep(delay)
        try:
            found_element = x_driver.find_element_by_link_text(link_text)
        except NoSuchElementException:
            return None
        except TimeoutException:
            return False
        return found_element

    def element_partial_linktext_agent(self, x_driver, partial_link_text, delay=delay_default):
        if delay is None:
            delay = self.delay
        sleep(delay)
        try:
            found_element = x_driver.find_element_by_partial_link_text(partial_link_text)
        except NoSuchElementException:
            return None
        except TimeoutException:
            return False
        return found_element

    def element_name_agent(self, x_driver, element_name, delay=delay_default):
        if delay is None:
            delay = self.delay
        sleep(delay)
        try:
            found_element = x_driver.find_element_by_name(element_name)
        except NoSuchElementException:
            return None
        except TimeoutException:
            return False
        return found_element

    def elements_tag_agent(self, x_driver, elements_tag, delay=delay_default):
        if delay is None:
            delay = self.delay
        sleep(delay)
        try:
            found_elements = x_driver.find_elements_by_tag_name(elements_tag)
        except NoSuchElementException:
            return None
        except TimeoutException:
            return False
        return found_elements

    def elements_class_agent(self, x_driver, element_class_name, delay=delay_default):
        if delay is None:
            delay = self.delay
        sleep(delay)
        try:
            found_elements = x_driver.find_elements_by_class_name(element_class_name)
        except NoSuchElementException:
            return None
        except TimeoutException:
            return False
        return found_elements

    def elements_css_selector_agent(self, x_driver, css_selector, delay=delay_default):
        if delay is None:
            delay = self.delay
        sleep(delay)
        try:
            found_elements = x_driver.find_elements_by_css_selector(css_selector)
        except NoSuchElementException:
            return None
        except TimeoutException:
            return False
        return found_elements

    def explicit_element_agent(self, x_driver, locator_type, locator, delay=None):
        if delay is None:
            delay = self.explicit_delay
        try:
            discovered_element = WebDriverWait(x_driver, delay).until(
                Conditions.element_to_be_clickable((locator_type, locator)))
            return discovered_element
        except NoSuchElementException:
            return None
        except TimeoutException:
            return False

    def explicit_elements_agent(self, x_driver, locator_type, locator, delay=None):
        if delay is None:
            delay = self.explicit_delay
        try:
            discovered_elements = WebDriverWait(x_driver, delay).until(
                Conditions.presence_of_all_elements_located((locator_type, locator)))
            return discovered_elements
        except NoSuchElementException:
            return None
        except TimeoutException:
            return False
