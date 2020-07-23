import os
import platform
from datetime import datetime
from time import sleep

from selenium.common.exceptions import JavascriptException

import core.preferences.corepreferences as selenapreferences
import core.preferences.log_manager as selena_logger
import core.preferences.x_dir_configs as _selena_directory
from core.elementagent import element_agent


class browserAgent:
    def __init__(self):
        self._scout = element_agent.DOMElementAgent()
        self._local_host = platform.system()
        self._selena_preferences = selenapreferences.fetch_core_preferences()
        self._current_time = datetime.now()
        self.time_stamp = self._current_time.strftime("%I_%M_%p")
        self._selena_log_listener = selena_logger.selenaLogger()

    def get_page_title(self, x_driver):
        current_page_name = x_driver.title
        current_page_url = x_driver.current_url
        page_title = f"{current_page_name} - {current_page_url}"
        selena_output = f"-->| Current HTML Page Title: {page_title}"
        if self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
            # returns list object that contains the DOM title[0] and Url[1]
        self._selena_log_listener.info(selena_output)
        return [current_page_name, current_page_url]

    def get_page_source(self, x_driver, objective_caption_text):
        # init File Repo dir and get path to File Repo dir
        _selena_directory.SelenaDir().init_file_repo()
        # init File Repository Ops Objective directory for file storage and return path object
        ops_objective_dir = _selena_directory.SelenaDir().fetch_ops_objective_dir("File Repository", self._selena_preferences['ops_objective'])
        raw_html_name = dir_filename_validator(objective_caption_text)
        htm_file_name = raw_html_name[0:22]
        source_html_file_name = f"{htm_file_name.rstrip()} - {self.time_stamp}"
        source_html_code = x_driver.page_source
        htm_file = f"{source_html_file_name}.html"
        htm_file_path = os.path.join(ops_objective_dir, htm_file)
        # creates html page source file to be saved in File Repository/Ops_Objective_Directory
        htm_file = open(htm_file_path, "w+", encoding="utf-8")
        htm_file.write(source_html_code)
        htm_file.close()
        selena_output = f"-->| {htm_file_name} HTML source code captured, output file location: {htm_file_path}"
        if self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
        self._selena_log_listener.info(selena_output)
        return f"{source_html_file_name}.html"

    def get_page_selfie(self, x_driver, objective_caption_text):
        # init Snapshot
        _selena_directory.SelenaDir().init_snapshot_dir()
        # init Snapshot Ops Objective directory for file storage and return path object
        ops_objective_dir = _selena_directory.SelenaDir().fetch_ops_objective_dir("Snapshot", self._selena_preferences['ops_objective'])
        raw_caption = dir_filename_validator(objective_caption_text)
        selfie_caption = raw_caption[0:22]
        snapshot_file_name = f"{selfie_caption.rstrip()} - {self.time_stamp}.png"
        snapshot_path = os.path.join(ops_objective_dir, snapshot_file_name)
        sleep(2)
        x_driver.save_screenshot(snapshot_path)
        selena_output = f"-->| '{snapshot_file_name}' HTML page render snapshot was taken, output file location: {snapshot_path}"
        if self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
        self._selena_log_listener.info(selena_output)
        return snapshot_path

    def get_element_selfie(self, x_driver, by_locator, locator, objective_caption_text):
        discovered_element = self._scout.explicit_element_agent(x_driver, by_locator, locator, None)
        # init Snapshot
        _selena_directory.SelenaDir().init_snapshot_dir()
        # init Snapshot Ops Objective directory for file storage and return path object
        ops_objective_dir = _selena_directory.SelenaDir().fetch_ops_objective_dir("Snapshot", self._selena_preferences['ops_objective'])
        raw_caption = dir_filename_validator(objective_caption_text)
        selfie_caption = raw_caption[0:22]
        element_snapshot_file_name = f"{selfie_caption.rstrip()} - {self.time_stamp}.png"
        element_snapshot_path = os.path.join(ops_objective_dir, element_snapshot_file_name)
        discovered_element.screenshot(element_snapshot_path)
        selena_output = f"-->| '{element_snapshot_file_name}' HTML DOM element snapshot was taken, output file location: {element_snapshot_path}"
        if self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
        self._selena_log_listener.info(selena_output)
        return element_snapshot_path

    def maximize_viewport(self, x_driver):
        old_window_size = x_driver.get_window_size()
        stale_height = old_window_size['height']
        stale_width = old_window_size['width']
        stale_size = f"{stale_width}px x {stale_height}px"
        x_driver.maximize_window()
        new_window_size = x_driver.get_window_size()
        height = new_window_size['height']
        width = new_window_size['width']
        new_size = f"{width}px x {height}px"
        selena_output = f"-->| Maximized viewport from '{stale_size}' to '{new_size}'" \
                        f" for Ops Objective: {self._selena_preferences['ops_objective']}"
        if self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
            # returns 'new_window_size' dictionary object with width, height, hCode and class key-values
        self._selena_log_listener.info(selena_output)
        return new_window_size

    def minimize_viewport(self, x_driver):
        old_window_size = x_driver.get_window_size()
        stale_height = old_window_size['height']
        stale_width = old_window_size['width']
        _stale_size = f"{stale_width}px x {stale_height}px"
        x_driver.minimize_window()
        _new_window_size = x_driver.get_window_size()
        height = _new_window_size['height']
        width = _new_window_size['width']
        _new_size = f"{width}px x {height}px"
        selena_output = f"-->| Minimized viewPort from '{_stale_size}' to '{_new_size}" \
                        f" for Ops Objective: {self._selena_preferences['ops_objective']}"
        if self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
            # returns '_new_window_size' dictionary object with width, height, hCode and class key-values
        self._selena_log_listener.info(selena_output)
        return _new_window_size
    
    def get_viewport_size(self, x_driver):
        viewport_size_dict = x_driver.get_window_size()
        viewport_width = viewport_size_dict['width']
        viewport_height = viewport_size_dict['height']
        viewport_size_char = f"{viewport_width}px x {viewport_height}px"
        selena_output = f"-->| Current viewport size is '{viewport_size_char}' "
        if self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
            # returns a viewport size list object that contains the detected width [0] and height[1]
        self._selena_log_listener.info(selena_output)
        return [int(viewport_width), int(viewport_height)]

    def do_viewport_scroll(self, x_driver, scroll_direction):
        x_driver.implicitly_wait(3)
        try:
            if scroll_direction == "Up":
                x_driver.execute_script("window.scrollBy(0, -1000);")
                selena_output = f"-->| Performed an {scroll_direction}ward viewport scroll action..."
                if self._selena_preferences['narrator'] == "enabled" and scroll_direction == "Up":
                    print(selena_output)
                self._selena_log_listener.info(selena_output)
                return True
            elif scroll_direction == "Down":
                x_driver.execute_script("window.scrollBy(0, 1000);")
                selena_output = f"-->| Performed a {scroll_direction}ward viewport scroll action..."
                if self._selena_preferences['narrator'] == "enabled" and scroll_direction == "Down":
                    print(selena_output)
                self._selena_log_listener.info(selena_output)
                return True
            elif scroll_direction != "Up" or "Down":
                selena_bad_output = f"-->| Invalid scroll direction request >> '{scroll_direction}'...Please scroll 'Up' or 'Down' only"
                self._selena_log_listener.warn(selena_bad_output)
                print(selena_bad_output)
                return False
        except JavascriptException:
            _selena_bad_output = f"-->| Oh Crap!...I wasn't able to apply scroll to web client viewport"
            if self._selena_preferences['narrator'] == "enabled":
                print(_selena_bad_output)
            self._selena_log_listener.warn(_selena_bad_output)
            return False

    def scroll_to_element(self, x_driver, by_locator, element_locator):
        discovered_element = self._scout.explicit_element_agent(x_driver, by_locator, element_locator, None)
        try:
            x_driver.execute_script("arguments[0].scrollIntoView(true);", discovered_element)
            selena_output = f"-->| Scrolled web client viewport to element with '{by_locator}': '{element_locator}' "
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_output)
            self._selena_log_listener.info(selena_output)
            return True
        except JavascriptException:
            selena_bad_output = f"-->| Oh Crap!...I wasn't able to scroll web client viewport to element with '{by_locator}': '{element_locator}' "
            if self._selena_preferences['narrator'] == "enabled":
                print(selena_bad_output)
            self._selena_log_listener.warn(selena_bad_output)
            return False

    def report_html_sourcecode(self, x_driver):
        # init File Repo dir and get path to File Repo dir
        _selena_directory.SelenaDir().init_file_repo()
        # init File Repository Ops Objective directory for file storage and return path object
        ops_objective_dir = _selena_directory.SelenaDir().fetch_ops_objective_dir("Reports", self._selena_preferences['ops_objective'])
        report_source_code = x_driver.page_source
        html_file_name = "selenaReport.html"
        html_file_path = os.path.join(ops_objective_dir, html_file_name)
        # creates html page source file to be saved in File Repository/Ops_Objective_Directory
        html_file = open(html_file_path, "w+", encoding="utf-8")
        html_file.write(report_source_code)
        html_file.close()
        selena_output = f"-->| '{html_file_name}' HTML source code captured, output file location: {html_file_path}"
        if self._selena_preferences['narrator'] == "enabled":
            print(selena_output)
        self._selena_log_listener.info(selena_output)
        return f"{html_file_path}"


def dir_filename_validator(invalid_file_dir_name):
    invalid_chars = ['*', '/', ':', '?', '"', "<", ">", "|"]
    valid_name = ''.join(a for a in invalid_file_dir_name if a not in invalid_chars)
    return valid_name
