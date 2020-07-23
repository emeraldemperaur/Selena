import os
import platform
import time

from selenium import webdriver

import core.preferences.log_manager as selena_logger

local_host = platform.system()
_selena_log_listener = selena_logger.selenaLogger()


class Explorer:
    def run_Explorer(self):
        if platform.architecture()[0] == "32bit":
            x_driver = explorer_driver("x86")
            return x_driver

        elif platform.architecture()[0] == "64bit":
            x_driver = explorer_driver("x64")
            return x_driver


def explorer_driver(arch):
    local_root = os.path.dirname(os.path.abspath(__file__))
    virgil_root = os.path.dirname(local_root)
    virgil = os.path.join(virgil_root, 'virgil')
    if local_host == "Windows":
        selena_os_output = f"-->> Localhost: Windows Operating System ({platform.architecture()[0]})"
        _selena_log_listener.info(selena_os_output)
        print(selena_os_output)
        executable_file_path = f"{virgil}\\{arch}\\windows\\IEDriverServer.exe"
        x_driver = webdriver.Ie(executable_path=executable_file_path)
        selena_x_driver_output = "\t ...Executing Internet Explorer Driver\n"
        _selena_log_listener.info(selena_x_driver_output)
        print(selena_x_driver_output)
        selena_x_driver_output_b = "\t\tNOTE: Unless absolutely necessary for the task objective, I'd advise you to use a less archaic web client!\n"
        _selena_log_listener.info(selena_x_driver_output_b)
        print(selena_x_driver_output_b)
        return x_driver
    else:
        anomaly_os_output_a = "\t-->| Uh Oh..Looks like I've got good and bad news..."
        anomaly_os_output_b = "\t  ...Good news is your OS doesn't support Internet Explorer"
        anomaly_os_output_c = "\t  ...So yeah, I guess it's only just good news for now...Try using a less archaic browser"
        _selena_log_listener.info(anomaly_os_output_a)
        print(anomaly_os_output_a)
        time.sleep(3)
        _selena_log_listener.info(anomaly_os_output_b)
        print(anomaly_os_output_b)
        time.sleep(3)
        _selena_log_listener.info(anomaly_os_output_c)
        print(anomaly_os_output_c)
        exit(1)
