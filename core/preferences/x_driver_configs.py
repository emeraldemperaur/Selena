from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.opera.options import Options as OperaOptions

import core.preferences.corepreferences as selenapreferences
import core.preferences.log_manager as selena_logger

# _selena_log_listener = selena_logger.selenaLogger()
selena_preferences = selenapreferences.fetch_core_preferences()


class xDriverHeadlessConfig:
    def __init__(self):
        self._selena_log_listener = selena_logger.selenaLogger()

    def fetch_xdriver_config(self):
        if selena_preferences['headless'] == "enabled":
            options = x_driver_options_config()
            selena_headless_output = "==============================\n" \
                                     "# Selena Headless -->> ENABLED\n" \
                                     "==============================\n" \
                                     "-->| NOTE: Selena Headless is only supported for Chrome and Firefox\n"
            self._selena_log_listener.error(selena_headless_output)
            print(selena_headless_output)
            return options


def x_driver_options_config():
    # determine driver preference in Core Preferences and set headless option accordingly, then return option object
    # here then fetch returned option object in the class function 'fetch_headless_config' that returns options for
    # use in x_driver init_x_driver
    if selena_preferences['x_driver'] == "chrome":
        options = ChromeOptions()
        options.add_argument('--headless')
        options.headless = True
        options.add_argument("window-size=1200x600")
        options.add_argument('--disable-gpu')
        return options
    elif selena_preferences['x_driver'] == "gecko":
        options = FirefoxOptions()
        options.headless = True
        return options
    elif selena_preferences['x_driver'] == "opera":
        options = OperaOptions()
        options.headless = True
        options.add_argument("window-size=1200x600")
        options.add_argument('--disable-gpu')
        return options
    elif selena_preferences['x_driver'] == "msedge":
        options = EdgeOptions()
        options.headless = True
        options.use_chromium = True
        return options
    elif selena_preferences['x_driver'] == "ie":
        options = IEOptions()
        return options


class SecondConfigClass:
    def new_func(self):
        pass
