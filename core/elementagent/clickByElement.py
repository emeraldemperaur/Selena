import core.preferences.corepreferences as selenapreferences
import core.preferences.log_manager as selena_logger
from core.elementagent import element_agent


# x_driver = xDriver.initXDriver().init_driver()


class clickByElement:
    def __init__(self):
        self.scout = element_agent.DOMElementAgent()
        self._selena_preferences = selenapreferences.fetch_core_preferences()
        self._selena_log_listener = selena_logger.selenaLogger()

    def x_path(self, x_driver, x_path, delay):
        discovered_element = self.scout.element_xpath_agent(x_driver, x_path, delay)
        selena_output = f"-->| An element with XPATH: '{x_path}' was clicked"
        if discovered_element and self._selena_preferences['narrator'] == "enabled":
            discovered_element.click()
            self._selena_log_listener.info(selena_output)
            print(selena_output)
            return discovered_element
        elif discovered_element and self._selena_preferences['narrator'] != "enabled":
            self._selena_log_listener.info(selena_output)
            discovered_element.click()
            return discovered_element
        elif discovered_element is not None:
            self._selena_log_listener.info(selena_output)
            discovered_element.click()
            return discovered_element
        elif discovered_element is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find the element you're looking for with the XPATH: '{x_path}'"
            self._selena_log_listener.warn(selena_bad_output)
            print(selena_bad_output)
            return None
    
    def dom_id(self, x_driver, element_id, delay):
        discovered_element = self.scout.element_id_agent(x_driver, element_id, delay)
        selena_output = f"-->| An element with HTML DOM ID: '{element_id}' was clicked"
        if discovered_element and self._selena_preferences['narrator'] == "enabled":
            discovered_element.click()
            self._selena_log_listener.info(selena_output)
            print(selena_output)
            return discovered_element
        elif discovered_element and self._selena_preferences['narrator'] != "enabled":
            self._selena_log_listener.info(selena_output)
            discovered_element.click()
            return discovered_element
        elif discovered_element is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find the element you're looking for with HTML DOM ID: '{element_id}'"
            self._selena_log_listener.warn(selena_bad_output)
            print(selena_bad_output)
            return None

    def dom_name(self, x_driver, element_name, delay):
        discovered_element = self.scout.element_id_agent(x_driver, element_name, delay)
        selena_output = f"-->| An element with HTML DOM Name: '{element_name}' was clicked"
        if discovered_element and self._selena_preferences['narrator'] == "enabled":
            discovered_element.click()
            self._selena_log_listener.info(selena_output)
            print(selena_output)
            return discovered_element
        elif discovered_element and self._selena_preferences['narrator'] != "enabled":
            discovered_element.click()
            self._selena_log_listener.info(selena_output)
            return discovered_element
        elif discovered_element is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find the element you're looking for with HTML DOM Name: '{element_name}'"
            self._selena_log_listener.warn(selena_bad_output)
            print(selena_bad_output)
            return None

    def link_text(self, x_driver, element_link_text, delay):
        discovered_element = self.scout.element_linktext_agent(x_driver, element_link_text, delay)
        selena_output = f"-->| An element with Hyperlink text: '{element_link_text}' was clicked"
        if discovered_element and self._selena_preferences['narrator'] == "enabled":
            self._selena_log_listener.info(selena_output)
            print(selena_output)
            discovered_element.click()
            return discovered_element
        elif discovered_element and self._selena_preferences['narrator'] != "enabled":
            self._selena_log_listener.info(selena_output)
            discovered_element.click()
            return discovered_element
        elif discovered_element is None:
            # implement (if element is none or) selenium exception override to try partial link text before exiting
            discovered_element = self.scout.element_partial_linktext_agent(x_driver, element_link_text, delay)
            selena_alt_output = f"-->| An element with partial Hyperlink text: '{element_link_text}' was clicked"
            if discovered_element and self._selena_preferences['narrator'] == "enabled":
                discovered_element.click()
                self._selena_log_listener.info(selena_alt_output)
                print(selena_alt_output)
                return discovered_element
            elif discovered_element and self._selena_preferences['narrator'] != "enabled":
                self._selena_log_listener.info(selena_alt_output)
                discovered_element.click()
                return discovered_element
            elif discovered_element is None:
                selena_alt_bad_output = f"-->| Oh Crap!...I wasn't able to find the element you're looking for with full or partial Hyperlink text: '{element_link_text}'"
                self._selena_log_listener.warn(selena_alt_bad_output)
                print(selena_alt_bad_output)
                return None

    def explicit_locator(self, x_driver, by_locator_type, locator, delay=None):
        discovered_element = self.scout.explicit_element_agent(x_driver, by_locator_type, locator, delay)
        selena_output = f"-->| An element was found by '{by_locator_type}' using the locator value: '{locator}' and clicked"
        if discovered_element and self._selena_preferences['narrator'] == "enabled":
            discovered_element.click()
            self._selena_log_listener.info(selena_output)
            print(selena_output)
            return discovered_element
        elif discovered_element and self._selena_preferences['narrator'] != "enabled":
            self._selena_log_listener.info(selena_output)
            return discovered_element
        elif discovered_element is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find that element you're looking for by '{by_locator_type}': '{locator}'"
            self._selena_log_listener.warn(selena_bad_output)
            print(selena_bad_output)
            return None


# x_driver.get("http://www.cnn.com")
# xpath = "//*[@id='header-nav-container']/div/div[1]/div/div[2]/nav/ul/li[3]/a"
# element_Id_one = "account-icon-button"
# link_one = "Business"
# elections_2020 = "//*[@id='header-nav-container']/div/div[1]/div/div[2]/nav/ul/li[5]/a"
# element_Id_two = "login-registration-link"
# link_two = "Tech"
# republican = "//*[@id='__next']/div[6]/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div/button[2]"
# link_three = "Media"
# element_Id_three = "edition-picker-toggle-desktop"
# key_info = "//*[@id='__next']/div[6]/div/div[1]/div/div[2]/div[1]/div/div[3]/button"
# element_Id_four = "edition-picker-toggle-desktop"
# link_four = "Videos"
# test = clickByElement()
# # found_element = test.x_path(xpath, 3)
# time.sleep(5)
# # found_elem = test.dom_id(element_Id_one, 3)
# found_link = test.link_text(link_one, 3)
# time.sleep(5)
# # found_element_two = test.x_path(elections_2020, 3)
# # found_elem_two = test.dom_id(element_Id_two, 3)
# found_link_two = test.link_text(link_two, 3)
# time.sleep(5)
# # found_element_three = test.x_path(republican, 3)
# # found_elem_three = test.dom_id(element_Id_three, 3)
# found_link_three = test.link_text(link_three, 3)
# # found_element_four = test.x_path(key_info, 3)
# # found_elem_four = test.dom_id(element_Id_four, 3)
# time.sleep(9)
# found_link_four = test.link_text(link_four, 3)
# time.sleep(5)
# x_driver.quit()
