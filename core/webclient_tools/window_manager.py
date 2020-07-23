import platform

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver import ActionChains

import core.preferences.corepreferences as selenapreferences
import core.preferences.log_manager as selena_logger
from core.elementagent import element_agent


# _x_driver = webdriver.Chrome()


class windowManager:
    def __init__(self):
        self.__selena_preferences__ = selenapreferences.fetch_core_preferences()
        self.__scout__ = element_agent.DOMElementAgent()
        self.__local_host__ = platform.system()
        self._selena_log_listener = selena_logger.selenaLogger()

    def x_tab_opener(self):
        pass

    def x_window_opener(self):
        pass

    def drag_n_drop(self, _x_driver,  from_element, to_element):
        from_element_found = self.__scout__.element_xpath_agent(_x_driver, from_element, None)
        to_element_found = self.__scout__.element_xpath_agent(_x_driver, to_element, None)
        if from_element_found and to_element_found:
            try:
                selena_action = ActionChains(_x_driver)
                selena_action.drag_and_drop(from_element_found, to_element_found).perform()
                selena_output = f"-->| Performed drag and drop action on element(s) w/ XPATH: '{from_element}' to '{to_element}'"
                if self.__selena_preferences__['narrator'] == "enabled":
                    print(selena_output)
                self._selena_log_listener.info(selena_output)
                return True
            except ElementNotInteractableException:
                selena_bad_output = f"-->| Oh Crap!...Drag and Drop action on element w/ XPATH: {from_element} failed"
                if self.__selena_preferences__['narrator'] == "enabled":
                    print(selena_bad_output)
                self._selena_log_listener.error(selena_bad_output)
                return False
        elif from_element_found or to_element_found is False or None:
            selena_error_output = f"-->| Oh Crap!...Encountered an issue finding drag n drop elements with the XPATHs: '{from_element}' and '{to_element}'"
            self._selena_log_listener.warn(selena_error_output)
            print(selena_error_output)

