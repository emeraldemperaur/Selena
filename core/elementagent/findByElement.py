import core.preferences.corepreferences as selenapreferences
import core.preferences.log_manager as selena_logger
from core.elementagent import element_agent


# x_driver = xDriver.initXDriver().init_driver()


class findByElement:
    def __init__(self):
        self.scout = element_agent.DOMElementAgent()
        self._selena_preferences = selenapreferences.fetch_core_preferences()
        self.selena_log_listener = selena_logger.selenaLogger()

    def x_path(self, x_driver, x_path, delay=None):
        discovered_element = self.scout.element_xpath_agent(x_driver, x_path, delay)
        selena_output = f"-->| An Element with XPATH: '{x_path}' was found"
        if discovered_element and self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
            self.selena_log_listener.info(selena_output)
            return discovered_element
        if discovered_element and self._selena_preferences['narrator'] != "enabled":
            self.selena_log_listener.info(selena_output)
            return discovered_element
        elif discovered_element is None:
            # implement lost element recovery system here
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find that element you're looking for with the XPATH: '{x_path}'"
            self.selena_log_listener.warn(selena_bad_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_bad_output)
            return None

    def dom_id(self, x_driver, element_id, delay=None):
        discovered_element = self.scout.element_id_agent(x_driver, element_id, delay)
        selena_output = f"-->| An element with HTML DOM ID: '{element_id}' was found"
        if discovered_element and self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
            self.selena_log_listener.info(selena_output)
            return discovered_element
        elif discovered_element and self._selena_preferences['narrator'] != "enabled":
            discovered_element.click()
            self.selena_log_listener.info(selena_output)
            return discovered_element
        elif discovered_element is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find that element you're looking for with HTML DOM ID: '{element_id}'"
            self.selena_log_listener.warn(selena_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_bad_output)
            return None

    def dom_name(self, x_driver, element_name, delay=None):
        discovered_element = self.scout.element_id_agent(x_driver, element_name, delay)
        selena_output = f"-->| An element with HTML DOM Name: '{element_name}' was found"
        if discovered_element and self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
            self.selena_log_listener.info(selena_output)
            return discovered_element
        elif discovered_element and self._selena_preferences['narrator'] != "enabled":
            self.selena_log_listener.info(selena_output)
            return discovered_element
        elif discovered_element is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find that element you're looking for with HTML DOM Name: '{element_name}'"
            self.selena_log_listener.warn(selena_bad_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_bad_output)
            return None

    def link_text(self, x_driver, element_link_text, delay=None):
        discovered_element = self.scout.element_linktext_agent(x_driver, element_link_text, delay)
        selena_output = f"-->| An element with Hyperlink text: '{element_link_text}' was found"
        if discovered_element and self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
            self.selena_log_listener.info(selena_output)
            return discovered_element
        elif discovered_element and self._selena_preferences['narrator'] != "enabled":
            self.selena_log_listener.info(selena_output)
            return discovered_element
        elif discovered_element is None:
            selena_alt_output = f"-->| An element with partial Hyperlink text: '{element_link_text}' was found"
            discovered_element = self.scout.element_partial_linktext_agent(x_driver, element_link_text, delay)
            if discovered_element and self._selena_preferences['narrator'] == "enabled":
                print(selena_alt_output)
                self.selena_log_listener.info(selena_alt_output)
                return discovered_element
            elif discovered_element and self._selena_preferences['narrator'] != "enabled":
                self.selena_log_listener.info(selena_alt_output)
                return discovered_element
            elif discovered_element is None:
                selena_alt_bad_output = f"-->| Oh Crap!...I wasn't able to find that element you're looking for with Hyperlink text: '{element_link_text}'"
                self.selena_log_listener.warn(selena_alt_bad_output)
                if self._selena_preferences['narrator'] == "enabled":
                    print(selena_alt_bad_output)
                return None

    def explicit_locator(self, x_driver, by_locator_type, locator, delay=None):
        discovered_element = self.scout.explicit_element_agent(x_driver, by_locator_type, locator, delay)
        selena_output = f"-->| An element was found '{by_locator_type}' using the locator value: '{locator}'"
        if discovered_element and self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
            self.selena_log_listener.info(selena_output)
            return discovered_element
        elif discovered_element and self._selena_preferences['narrator'] != "enabled":
            self.selena_log_listener.info(selena_output)
            return discovered_element
        elif discovered_element is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find that element you're looking for by '{by_locator_type}': '{locator}'"
            self.selena_log_listener.warn(selena_bad_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_bad_output)
            return None


# x_driver.get("http://www.cnn.com")
# xpath = "//*[@id='header-nav-container']/div/div[1]/div/div[2]/nav/ul/li[3]/a"
# elections_2020 = "//*[@id='header-nav-container']/div/div[1]/div/div[2]/nav/ul/li[5]/a"
# test = findByElement()
# found_element = test.x_path(xpath, 3)
# time.sleep(5)
# found_element_two = test.x_path(elections_2020, 3)
# x_driver.quit()
