import core.preferences.corepreferences as selenapreferences
import core.preferences.log_manager as selena_logger
import core.preferences.x_dir_configs as selena_directory
import core.webdrivers.chromium_xplatform_driver as chromium_driver
import core.webdrivers.edge_xplatform_driver as ms_edge_driver
import core.webdrivers.firefox_xplatform_driver as phoenix_driver
import core.webdrivers.ie_windows_driver as ie_driver
import core.webdrivers.opera_xplatform_driver as opera_driver

# _selena_log_listener = selena_logger.selenaLogger()
selena_root = selena_directory.SelenaDir().init_root_dir()
assets_dir = selena_directory.SelenaDir().init_assets()
reports_dir = selena_directory.SelenaDir().init_reports()
diary_log = selena_directory.SelenaDir().init_log_diary()
file_repo = selena_directory.SelenaDir().init_file_repo()
snapshot = selena_directory.SelenaDir().init_snapshot_dir()
# selena_preferences = selenapreferences.fetch_core_preferences()


class initXDriver:
    def __init__(self):
        self._selena_log_listener = selena_logger.selenaLogger()
        self.selena_root = selena_directory.SelenaDir().init_root_dir()
        self.assets_dir = selena_directory.SelenaDir().init_assets()
        self.reports_dir = selena_directory.SelenaDir().init_reports()
        self.diary_log = selena_directory.SelenaDir().init_log_diary()
        self.file_repo = selena_directory.SelenaDir().init_file_repo()
        self.snapshot = selena_directory.SelenaDir().init_snapshot_dir()
        self.selena_preferences = selenapreferences.fetch_core_preferences()

    def init_driver(self):
        if self.selena_preferences['x_driver'] == "chrome":
            x_driver = chromium_driver.Chromium().runChromium()
            return x_driver
        elif self.selena_preferences['x_driver'] == "gecko":
            x_driver = phoenix_driver.PheonixFox().runPheonixFox()
            return x_driver
        elif self.selena_preferences['x_driver'] == "opera":
            x_driver = opera_driver.Opera().runOpera()
            return x_driver
        elif self.selena_preferences['x_driver'] == "msedge":
            x_driver = ms_edge_driver.Edge().run_Edge()
            return x_driver
        elif self.selena_preferences['x_driver'] == "ie":
            x_driver = ie_driver.Explorer().run_Explorer()
            return x_driver
        else:
            invalid_config_response = "\n==================================================\n" \
                                      "  Uh Oh...Invalid Selena x_driver Configuration!\n" \
                                      "==================================================\n" \
                                      f"'{self.selena_preferences['x_driver']}' in CorePreferences isn't a invalid option\n" \
                                      f"\t Please apply a valid x_driver option:\n" \
                                      f"\t\t->| chrome, gecko, opera, msedge, ie |<-\n"
            self._selena_log_listener.error(invalid_config_response)
            print(invalid_config_response)
            exit(1)

    def legion_mode(self):
        if self.selena_preferences['legion_mode'] == "enabled":
            selena_driver = chromium_driver.Chromium().runChromium()
            selena_duo_driver = phoenix_driver.PheonixFox().runPheonixFox()
            selena_trio_driver = opera_driver.Opera().runOpera()
            selena_quad_driver = ms_edge_driver.Edge().run_Edge()
            selena_quint_driver = ie_driver.Explorer().run_Explorer()
            driver_carousel = [selena_driver, selena_duo_driver, selena_trio_driver, selena_quad_driver,
                               selena_quint_driver]
            selena_response = "-->> Legion Mode: Enabled"
            self._selena_log_listener.info(selena_response)
            print(selena_response)
            return driver_carousel
        elif self.selena_preferences['legion_mode'] != "enabled":
            invalid_preference_response = "============================\n" \
                                          "\tINVALID CORE PREFERENCE\n" \
                                          "============================\n" \
                                          "\n\t-->>| To use Selena Legion Mode you'll need to set 'legion_mode':{selena_preferences['legion_mode']}" \
                                          " to 'enabled' in Core Preferences |<<--\n"
            self._selena_log_listener.warn(invalid_preference_response)
            print(invalid_preference_response)
            exit(1)
