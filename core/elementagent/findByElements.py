import time

import core.preferences.corepreferences as selenapreferences
import core.preferences.init_x_driver as xDriver
import core.preferences.log_manager as selena_logger
from core.elementagent import element_agent
from core.webclient_tools import browser_agent

x_driver = xDriver.initXDriver().init_driver()

browser_tools = browser_agent.browserAgent()


class findByElements:
    def __init__(self):
        self._selena_preferences = selenapreferences.fetch_core_preferences()
        self.scout = element_agent.DOMElementAgent()
        self._selena_log_listener = selena_logger.selenaLogger()

    def dom_tag(self, dom_tag, delay):
        discovered_elements = self.scout.elements_tag_agent(x_driver, dom_tag, delay)
        selena_output = f"-->| {len(discovered_elements)} Element(s) with HTML TAG: '{dom_tag}' were found in DOM - [{x_driver.current_url}]"
        if discovered_elements and self._selena_preferences['narrator'] == "enabled":
            self._selena_log_listener.info(selena_output)
            print(selena_output)
            return discovered_elements
        if discovered_elements and self._selena_preferences['narrator'] != "enabled":
            self._selena_log_listener.info(selena_output)
            return discovered_elements
        elif discovered_elements is None:
            # implement lost element recovery system here
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find the element(s) you're looking for with the HTML TAG: {dom_tag}"
            self._selena_log_listener.warn(selena_bad_output)
            print(selena_bad_output)
            return None

    def class_name(self, dom_class_name, delay):
        discovered_elements = self.scout.elements_class_agent(x_driver, dom_class_name, delay)
        selena_output = f"-->| {len(discovered_elements)} Element(s) with HTML Class attribute: '{dom_class_name}' were found in DOM - [{x_driver.current_url}]"
        if discovered_elements and self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
            self._selena_log_listener.info(selena_output)
            return discovered_elements
        if discovered_elements and self._selena_preferences['narrator'] != "enabled":
            self._selena_log_listener.info(selena_output)
            return discovered_elements
        elif discovered_elements is None:
            selena_bad_output = "-->| Oh Crap!...I wasn't able to find the element(s) you're looking for with the HTML Class: {dom_class_name}"
            # implement lost element recovery system here
            self._selena_log_listener.warn(selena_bad_output)
            print(selena_bad_output)

    def css_selector(self, x_driver, css_selector, delay):
        discovered_elements = self.scout.elements_css_selector_agent(x_driver, css_selector, delay)
        selena_output = "-->| {len(discovered_elements)} Element(s) with CSS Selector: '{css_selector}' were found in DOM - [{x_driver.current_url}]"
        if discovered_elements and self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
            self._selena_log_listener.info(selena_output)
            return discovered_elements
        if discovered_elements and self._selena_preferences['narrator'] != "enabled":
            self._selena_log_listener.info(selena_output)
            return discovered_elements
        elif discovered_elements is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find the element(s) you're looking for with the CSS Selector: {css_selector}"
            # implement lost element recovery system here
            self._selena_log_listener.warn(selena_bad_output)
            print(selena_bad_output)

    def explicit_locator(self, x_driver, locator_type, locator, delay):
        discovered_elements = self.scout.explicit_elements_agent(x_driver, locator_type, locator, delay)
        selena_output = f"-->| {len(discovered_elements)} Element(s) were found by {locator_type}: '{locator}' in DOM - [{x_driver.current_url}]"
        if discovered_elements and self._selena_preferences['narrator'] == "enabled":
            self._selena_log_listener.info(selena_output)
            print(selena_output)
        if discovered_elements and self._selena_preferences['narrator'] != "enabled":
            self._selena_log_listener.info(selena_output)
            return discovered_elements
        elif discovered_elements is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find the element(s) you're looking for by {locator_type}: {locator}"
            # implement lost element recovery system here
            self._selena_log_listener.warn(selena_bad_output)
            print(selena_bad_output)


x_driver.get("http://www.cnn.com")
class_name = "cd__headline-text"
html_tag = "section"
class_name_two = "cd__content"
html_tag_two = "iframe"
class_name_three = "cd__wrapper"
html_tag_three = "article"
class_name_four = "pg__background__image_wrapper"
html_tag_four = "div"


test = findByElements()
# found_elements = test.class_name(class_name, 3)
found_tag = test.dom_tag(html_tag, 3)
time.sleep(5)
# found_elements_two = test.class_name(class_name_two, 3)
found_tag_two = test.dom_tag(html_tag_two, 3)
time.sleep(5)
# found_elements_three = test.class_name(class_name_three, 3)
found_tag_three = test.dom_tag(html_tag_three, 3)
time.sleep(5)
# found_elements_four = test.class_name(class_name_four, 3)
found_tag_four = test.dom_tag(html_tag_four, 3)
page_title = browser_tools.get_page_title(x_driver)
window_size = browser_tools.maximize_viewport(x_driver)
time.sleep(2)
_new_window_size = browser_tools.minimize_viewport(x_driver)
page_source = browser_tools.get_page_source(x_driver, "CNN Home")
selfie = browser_tools.get_page_selfie(x_driver, "Login Page")
print(page_source)
print(selfie)
x_driver.quit()
