import os
import platform
from datetime import datetime

import core.preferences.corepreferences as selenapreferences

_selena_preferences = selenapreferences.fetch_core_preferences()
_local_host = platform.system()
_current_time = datetime.now()

selena_root_dir = 'Selena'
selena_reports_dir = "Reports"
selena_assets_dir = "Assets"
selena_file_repo = "File Repository"
selena_snapshot_dir = "Snapshot"
selena_log_dir = "Log Diary"


# selena_directory_list = [selena_root_dir, selena_reports_dir, selena_assets_dir,
#                         selena_file_repo, selena_snapshot_dir, selena_log_dir]


class SelenaDir:
    def __init__(self):
        self.selena_root_dir = 'Selena'
        self.selena_reports_dir = 'Reports'
        self.selena_assets_dir = 'Assets'
        self.selena_file_repo = 'File Repository'
        self.selena_snapshot_dir = 'Snapshot'
        self.selena_log_dir = 'Log Diary'

    def init_root_dir(self):
        dir_init_path = x_dir_path_generator()
        return dir_init_path
        # returns True if Folder is Created or False if not Created/Already Exist

    def init_reports(self):
        init_reports_path = x_sub_dir_path_generator(self.selena_reports_dir)
        return init_reports_path

    def init_assets(self):
        init_assets_path = x_sub_dir_path_generator(self.selena_assets_dir)
        return init_assets_path

    def init_file_repo(self):
        init_file_repo_path = x_sub_dir_path_generator(self.selena_file_repo)
        return init_file_repo_path

    def init_snapshot_dir(self):
        init_snapshot_path = x_sub_dir_path_generator(self.selena_snapshot_dir)
        return init_snapshot_path

    def init_log_diary(self):
        init_log_diary_path = x_sub_dir_path_generator(self.selena_log_dir)
        return init_log_diary_path

    def fetch_ops_objective_dir(self, selena_sub_dir_path, ops_objective):
        ops_objective_dir_path = ops_objective_mkdir(selena_sub_dir_path, ops_objective)
        return ops_objective_dir_path

    def fetch_log_ops_objective_dir(self, ops_objective):
        log_dir_path = log_ops_objective_mkdir(ops_objective)
        return log_dir_path

    def fetch_assets_ops_objective_dir(self, ops_objective):
        assets_dir_path = log_ops_objective_mkdir(ops_objective, "Assets")
        return assets_dir_path


def x_sub_dir_path_generator(sub_directory):
    if _local_host == "Windows":
        sub_dir_path = os.path.join("c:\\Selena\\", sub_directory)
        try:
            os.makedirs(sub_dir_path)
            # returns sub_dir_path for use by browser agent
            return sub_dir_path
        except FileExistsError:
            return sub_dir_path
        except PermissionError:
            permissions_prompt()
            return False
        except NameError:
            permissions_prompt()
            return False
    elif _local_host == "Linux":
        pass
    elif _local_host == "Darwin":
        pass


def x_dir_path_generator():
    if _local_host == "Windows":
        dir_path = os.path.join("c:\\", selena_root_dir)
        try:
            os.makedirs(dir_path)
            # returns x_dir_path for use by browser agent
            return dir_path
        except FileExistsError:
            return False
        except PermissionError:
            permissions_prompt()
        except NameError:
            permissions_prompt()
    elif _local_host == "Linux":
        pass
    elif _local_host == "Darwin":
        pass


def ops_objective_mkdir(selena_sub_dir_name, ops_objective):
    time_stamp = _current_time.strftime("%b %d %Y - %H_%M")
    _ops_objective = dir_filename_validator(ops_objective)
    valid_ops_objective = _ops_objective.rstrip()
    if _local_host == "Windows":
        ops_objective_dir = f"c:\\Selena\\{selena_sub_dir_name}\\{valid_ops_objective}"
    else:
        ops_objective_dir = f"~/Selena/{selena_sub_dir_name}/{valid_ops_objective}"
    try:
        os.makedirs(ops_objective_dir)
        # returns sub directory ops_objective_path for use by browser agent to save file into
        return ops_objective_dir
    except FileExistsError:
        # returns unique sub directory ops_objective_path for use by browser agent to save file into
        unique_ops_dir_path = os.path.join(ops_objective_dir, time_stamp)
        # creates unique sub directory only if one with same name + timestamp doesnt exist already and returns path
        # for use by browser agent
        if not os.path.exists(unique_ops_dir_path):
            try:
                os.makedirs(unique_ops_dir_path)
            except FileExistsError:
                return ops_objective_dir
        return unique_ops_dir_path
    except PermissionError:
        permissions_prompt()
        return False


def log_ops_objective_mkdir(ops_objective, log_sub_dir=None):
    if log_sub_dir is None:
        log_sub_dir = "Log Diary"
    _ops_objective = dir_filename_validator(ops_objective)
    _valid_ops_objective = _ops_objective.rstrip()
    if _local_host == "Windows":
        log_ops_objective_dir = f"c:\\Selena\\{log_sub_dir}\\{_valid_ops_objective}"
    else:
        log_ops_objective_dir = f"~/Selena/{log_sub_dir}/{_valid_ops_objective}"
    try:
        os.makedirs(log_ops_objective_dir)
        # returns sub directory ops_objective_path for use by browser agent to save file into
        return log_ops_objective_dir
    except FileExistsError:
        return log_ops_objective_dir


def dir_filename_validator(invalid_file_dir_name):
    invalid_chars = ['*', '/', ':', '?', '"', "<", ">", "|"]
    valid_name = ''.join(a for a in invalid_file_dir_name if a not in invalid_chars)
    return valid_name


def permissions_prompt():
    selena_permission_output = "============================\n" \
                    "\t\t PERMISSION DENIED\n" \
                    "============================\n" \
                    "-->| Please run Selena as an administrator w/ Elevated Permission\n"
    print(selena_permission_output)
    exit(1)
