import time

from selenium.webdriver.common.by import By

import core.preferences.corepreferences as selenapreferences
import core.preferences.init_x_driver as xDriver
import core.preferences.log_manager as selena_logger
from core.elementagent import element_agent
from core.elementagent.clickByElement import clickByElement
from core.webclient_tools import browser_agent
from core.webclient_tools import window_manager

x_driver = xDriver.initXDriver().init_driver()
_browser_tools = browser_agent.browserAgent()
_window_manager = window_manager.windowManager()


class fillByElement:
    def __init__(self):
        self.scout = element_agent.DOMElementAgent()
        self._selena_preferences = selenapreferences.fetch_core_preferences()
        self._selena_log_listener = selena_logger.selenaLogger()

    def x_path(self, x_path, fill_keys, delay=None):
        if delay is None:
            delay = 10
        discovered_element = self.scout.explicit_element_agent(x_driver, By.XPATH, x_path, delay)
        if discovered_element:
            discovered_element.send_keys(fill_keys)
            selena_output = f"-->| Inputted keys '{fill_keys}' into Element with XPATH:'{x_path}'"
            self._selena_log_listener.info(selena_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_output)
            return discovered_element
        if discovered_element is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find the element you're looking for with XPATH: '{x_path}'"
            self._selena_log_listener.warn(selena_bad_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_bad_output)
                return None

    def dom_id(self, dom_id, fill_keys, delay=None):
        if delay is None:
            delay = 10
        discovered_element = self.scout.explicit_element_agent(x_driver, By.ID, dom_id, delay)
        if discovered_element:
            discovered_element.send_keys(fill_keys)
            selena_output = f"-->| Inputted keys '{fill_keys}' into Element with HTML DOM ID:'{dom_id}'"
            self._selena_log_listener.info(selena_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_output)
            return discovered_element
        if discovered_element is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find the element you're looking for with HTML DOM ID: '{dom_id}'"
            self._selena_log_listener.warn(selena_bad_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_bad_output)
                return None

    def dom_name(self, dom_name, fill_keys, delay=None):
        if delay is None:
            delay = 10
        discovered_element = self.scout.explicit_element_agent(x_driver, By.NAME, dom_name, delay)
        if discovered_element:
            discovered_element.send_keys(fill_keys)
            selena_output = f"-->| Inputted keys '{fill_keys}' into Element with HTML DOM NAME: '{dom_name}'"
            self._selena_log_listener.info(selena_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_output)
            return discovered_element
        if discovered_element is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find the element you're looking for with HTML DOM NAME: '{dom_name}'"
            self._selena_log_listener.warn(selena_bad_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_bad_output)
                return None

    def dom_class(self, dom_class, fill_keys, delay=None):
        if delay is None:
            delay = 10
        discovered_element = self.scout.explicit_element_agent(x_driver, By.CLASS_NAME, dom_class, delay)
        if discovered_element:
            selena_output = f"-->| Inputted keys '{fill_keys}' into Element with HTML DOM CLASS NAME: '{dom_class}'"
            discovered_element.send_keys(fill_keys)
            self._selena_log_listener.info(selena_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_output)
            return discovered_element
        if discovered_element is None:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to find the element you're looking for with HTML DOM CLASS: '{dom_class}'"
            self._selena_log_listener.warn(selena_bad_output)
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_bad_output)
                return None


x_driver.get("https://www.netflix.com/ca/")
time.sleep(3)
clicker = clickByElement()
filler = fillByElement()
notification_path = "//*[@id='cookie-disclosure']/div/button"
by_locator_type = By.XPATH
notice_btn = clicker.explicit_locator(x_driver, by_locator_type, notification_path, 3)
sign_in_link_text = "Sign In"
time.sleep(5)
sign_in = clicker.link_text(x_driver, sign_in_link_text, 3)
email_input = "//*[@id='id_userLoginId']"
password_input = "//*[@id='id_password']"
email_address = "egwim.emeka@gmail.com"
password = "30@Enterprise"
sign_in_btn_path = "//*[@id='appMountPoint']/div/div[3]/div/div/div[1]/form/button"
email_add = filler.x_path(email_input, email_address)
time.sleep(3)
pass_code = filler.x_path(password_input, password)
sign_in_btn = clicker.x_path(x_driver, sign_in_btn_path, 3)
page_source = _browser_tools.get_page_source(x_driver, "Netflix | Home")
sign_in_test = clicker.link_text(x_driver, sign_in_link_text, 3)
if sign_in_test is None:
    print("-->| Selenium Exception Override Successful")
time.sleep(6)
netflix_home_selfie = _browser_tools.get_page_selfie(x_driver, "Netflix Account")
avatar_xpath = "//*[@id='appMountPoint']/div/div/div[1]/div[1]/div[2]/div/div"
my_account_avatar = _browser_tools.get_element_selfie(x_driver, by_locator_type, avatar_xpath, "User Profiles")
emeka_user_path = "//*[@id='appMountPoint']/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a/div/div"
emeka_user_btn = clicker.x_path(x_driver, emeka_user_path, 4)
time.sleep(6)
scroll_down = _browser_tools.do_viewport_scroll(x_driver, "Down")
if not scroll_down:
    print("-->| Scroll Down Action Failed")
time.sleep(6)
scroll_up = _browser_tools.do_viewport_scroll(x_driver, "Up")
if not scroll_up:
    print("-->| Scroll Up Action Failed")
time.sleep(6)
continue_watching_title = "//*[text() = 'Continue Watching for Emeka']"
popular_on_netflix_title = "//*[text() = 'Popular in Netflix']"
continue_watching = _browser_tools.scroll_to_element(x_driver, By.XPATH, continue_watching_title)
if not continue_watching:
    print("-->| Scroll to Element Action Failed")
continue_watching_selfie = _browser_tools.get_page_selfie(x_driver, "Continue Watching")
time.sleep(9)
drag_drop_test = _window_manager.drag_n_drop(x_driver, continue_watching_title, popular_on_netflix_title)
if drag_drop_test is False:
    print("Drag and Drop Test Fail Successful")
time.sleep(6)
x_driver.quit()

