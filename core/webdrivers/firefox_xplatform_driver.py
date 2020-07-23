import os
import platform
import time

from selenium import webdriver

import core.preferences.log_manager as selena_logger
import core.preferences.x_driver_configs as driver_options

local_host = platform.system()
_selena_log_listener = selena_logger.selenaLogger()


class PheonixFox:
    def runPheonixFox(self):
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
        executable_file_path = f"{virgil}\\{arch}\\windows\\geckodriver.exe"
        x_driver = webdriver.Firefox(executable_path=executable_file_path, options=options, service_log_path=os.devnull)
        version_sleuth(x_driver)
        selena_x_driver_output = "\t ...Executing Gecko Driver\n"
        _selena_log_listener.info(selena_x_driver_output)
        print(selena_x_driver_output)
        return x_driver
    elif local_host == "Linux":
        selena_os_output = f"-->> Localhost: Linux Operating System ({platform.architecture()[0]})\n"
        print(selena_os_output)
        executable_file_path = f"{virgil}/{arch}/linux/geckodriver"
        x_driver = webdriver.Firefox(executable_path=executable_file_path, options=options, service_log_path=os.devnull)
        version_sleuth(x_driver)
        selena_x_driver_output = "\t...Executing Gecko Driver\n"
        _selena_log_listener.info(selena_x_driver_output)
        print(selena_x_driver_output)
        return x_driver
    elif local_host == "Darwin":
        selena_os_output = f"-->> Localhost: Apple Operating System ({platform.architecture()[0]})\n"
        _selena_log_listener.info(selena_os_output)
        print(selena_os_output)
        executable_file_path = f"{virgil}/{arch}/darwin/geckodriver"
        x_driver = webdriver.Firefox(executable_path=executable_file_path, options=options, service_log_path=os.devnull)
        version_sleuth(x_driver)
        selena_x_driver_output = "\t...Executing Gecko Driver\n"
        _selena_log_listener.info(selena_x_driver_output)
        print(selena_x_driver_output)
        return x_driver
    else:
        anomaly_os_output_a = "\t-->| What is this?..."
        anomaly_os_output_b = "...What is this, please?"
        anomaly_os_output_c = "\t-->> Localhost: Unknown Operating System detected...Please update Selena Core"
        _selena_log_listener.error(anomaly_os_output_a)
        print(anomaly_os_output_a)
        time.sleep(3)
        _selena_log_listener.error(anomaly_os_output_b)
        print(anomaly_os_output_b)
        time.sleep(3)
        _selena_log_listener.error(anomaly_os_output_c)
        print(anomaly_os_output_c)
        exit(1)


def version_sleuth(found_driver):
    raw_browser_version = found_driver.capabilities['browserVersion']
    raw_driver_version = found_driver.capabilities['moz:geckodriverVersion'].split(' ')[0]
    selena_web_version_output = f"\t Firefox Web Version # -->> {raw_browser_version}"
    selena_driver_version_output = f"\t Gecko Driver Version # -->> {raw_driver_version}"
    _selena_log_listener.info(selena_web_version_output)
    print(selena_web_version_output)
    _selena_log_listener.info(selena_driver_version_output)
    print(selena_driver_version_output)
