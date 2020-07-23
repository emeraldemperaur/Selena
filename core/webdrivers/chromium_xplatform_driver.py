import os
import platform
import time

from selenium import webdriver

import core.preferences.log_manager as selena_logger
import core.preferences.x_driver_configs as driver_options

local_host = platform.system()
_selena_log_listener = selena_logger.selenaLogger()


class Chromium:
    def runChromium(self):
        if platform.architecture()[0] == "32bit":
            x_driver = x_platform_driver("x86")
            return x_driver

        elif platform.architecture()[0] == "64bit":
            x_driver = x_platform_driver("x64")
            return x_driver


def x_platform_driver(arch):
    options = driver_options.xDriverHeadlessConfig().fetch_xdriver_config()
    local_root = os.path.dirname(os.path.abspath(__file__))
    virgil_root = os.path.dirname(local_root)
    virgil = os.path.join(virgil_root, 'virgil')
    if local_host == "Windows":
        selena_os_output = f"-->> Localhost: Windows Operating System ({platform.architecture()[0]})"
        _selena_log_listener.info(selena_os_output)
        print(selena_os_output)
        executable_file_path = f"{virgil}\\{arch}\\windows\\chromedriver.exe"
        x_driver = webdriver.Chrome(executable_path=executable_file_path, chrome_options=options)
        version_sleuth(x_driver)
        selena_x_driver_output = f"\t ...Executing Chrome Driver\n"
        _selena_log_listener.info(selena_x_driver_output)
        print(selena_x_driver_output)
        # x_driver.get("http://www.empiaurhouse.com")
        return x_driver
    elif local_host == "Linux":
        selena_os_output = f"-->> Localhost: Linux Operating System ({platform.architecture()[0]})\n"
        _selena_log_listener.info(selena_os_output)
        print(selena_os_output)
        executable_file_path = f"{virgil}/{arch}/linux/chromedriver"
        x_driver = webdriver.Chrome(executable_path=executable_file_path, chrome_options=options)
        version_sleuth(x_driver)
        _selena_x_driver_output = f"\t...Executing Chrome Driver\n"
        _selena_log_listener.info(_selena_x_driver_output)
        print(_selena_x_driver_output)
        return x_driver
    elif local_host == "Darwin":
        selena_os_output = f"-->> Localhost: Apple Operating System ({platform.architecture()[0]})\n"
        print(selena_os_output)
        _selena_log_listener.info(selena_os_output)
        executable_file_path = f"{virgil}/{arch}/darwin/chromedriver"
        x_driver = webdriver.Chrome(executable_path=executable_file_path, chrome_options=options)
        version_sleuth(x_driver)
        selena_x_driver_output = f"\t...Executing Chrome Driver\n"
        _selena_log_listener.info(selena_x_driver_output)
        print(selena_x_driver_output)
        return x_driver
    else:
        anomaly_os_output_a = "\t-->| What is this?..."
        anomaly_os_output_b = "...What is this, please?"
        anomaly_os_output_c = "\t-->> Localhost: Unknown Operating System detected...Please update Selena Core"
        print(anomaly_os_output_a)
        _selena_log_listener.error(anomaly_os_output_a)
        time.sleep(3)
        print(anomaly_os_output_b)
        _selena_log_listener.error(anomaly_os_output_b)
        time.sleep(3)
        print(anomaly_os_output_c)
        _selena_log_listener.error(anomaly_os_output_c)
        exit(1)


def version_sleuth(found_driver):
    raw_browser_version = found_driver.capabilities['browserVersion']
    raw_driver_version = found_driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
    browser_version_str = raw_browser_version[0:2]
    driver_version_str = raw_driver_version[0:2]
    selena_web_version_output = f"\t Chrome Web Version # -->> {raw_browser_version}"
    selena_driver_version_output = f"\t Chrome Driver Version # -->> {raw_driver_version}"
    _selena_log_listener.info(selena_web_version_output)
    print(selena_web_version_output)
    _selena_log_listener.info(selena_driver_version_output)
    print(selena_driver_version_output)
    if int(browser_version_str) > int(driver_version_str):
        selena_response_a = f"\t Detected Chrome Browser {browser_version_str} is higher than the found Chrome Driver {driver_version_str}"
        selena_response_b = f"\t Please download an up-to-date Chrome Driver for {browser_version_str}"
        selena_response_c = "https://chromedriver.chromium.org/"
        _selena_log_listener.warn(selena_response_a)
        _selena_log_listener.warn(selena_response_b)
        _selena_log_listener.warn(selena_response_c)
        print(selena_response_a)
        print(selena_response_b)
        print(selena_response_c)
    elif int(browser_version_str) < int(driver_version_str):
        selena_response_a = f"\t Found Chrome Driver {driver_version_str} is higher than the detected Chrome Browser {browser_version_str}"
        selena_response_b = "\t That's sort of an anomaly...You'll need to update your Chrome browser to a newer version resolve"
        selena_response_c = "https://www.google.com/chrome/"
        _selena_log_listener.warn(selena_response_a)
        _selena_log_listener.warn(selena_response_b)
        _selena_log_listener.warn(selena_response_c)
        print(selena_response_a)
        print(selena_response_b)
        print(selena_response_c)
