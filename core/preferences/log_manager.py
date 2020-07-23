import inspect
import logging

import core.preferences.corepreferences as selenapreferences
import core.preferences.x_dir_configs as _selena_directory_

__selena_preferences__ = selenapreferences.fetch_core_preferences()


def diary_logger(log_level):
    _selena_directory_.SelenaDir().init_log_diary()
    objective = __selena_preferences__['ops_objective']
    ops_objective_dir = _selena_directory_.SelenaDir().fetch_log_ops_objective_dir(objective)
    ops_alias = f"selena Log - {__selena_preferences__['ops_objective']} Ops"
    log_name = inspect.stack()[1][3]
    logger = logging.getLogger(log_name)
    # DEBUG default level to log all messages
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(f"{ops_objective_dir}/{ops_alias}.log", mode='a')
    file_handler.setLevel(log_level)
    log_formatter = logging.Formatter('%(asctime)s -%(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)
    return logger


class selenaLogger:
    log = diary_logger(logging.DEBUG)

    def debug(self, log_message):
        self.log.debug(log_message)
        logging.shutdown()

    def info(self, log_message):
        self.log.info(log_message)
        logging.shutdown()

    def warn(self, log_message):
        self.log.warning(log_message)
        logging.shutdown()

    def error(self, log_message):
        self.log.error(log_message)
        logging.shutdown()

    def critical(self, log_message):
        self.log.critical(log_message)
        logging.shutdown()
