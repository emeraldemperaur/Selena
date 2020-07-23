import os
from time import sleep

import pandas as pd
from selenium.webdriver.common.by import By

import core.preferences.corepreferences as selenapreferences
import core.preferences.init_x_driver as xDriver
import core.preferences.log_manager as selena_logger
import core.preferences.x_dir_configs as __selena_directory__
from core.elementagent import element_agent

x_driver = xDriver.initXDriver().init_driver()


class dataAgent:
    def __init__(self):
        self.init_assets = __selena_directory__.SelenaDir().init_assets()
        self.log_listener = selena_logger.selenaLogger()
        self.selena_preference = selenapreferences.fetch_core_preferences()
        self.element_scout = element_agent.DOMElementAgent()

    def read_html_table(self, table_element_xpath_locator):
        table_element = self.element_scout.explicit_element_agent(x_driver, By.XPATH, table_element_xpath_locator)
        _selena_output_ = f"-->| HTML Table Element with XPATH: '{table_element_xpath_locator}' was found"
        if table_element.tag_name == "table":
            print(_selena_output_)
            self.log_listener.info(_selena_output_)
            html_table = table_element.get_attribute('outerHTML')
            raw_html_data_frame = pd.read_html(html_table)
            html_data_frame = raw_html_data_frame[0]
            # returns table data list object w/ table_element.text = [0] | html_data_frame = [1] | html_table_code = [2]
            return table_element.text, html_data_frame, html_table
        elif table_element.tag_name != "table":
            _selena_output_ = f"-->| Uh Oh...The XPATH: '{table_element_xpath_locator}' doesn't seem to reference a HTML table"
            print(_selena_output_)
            self.log_listener.warn(_selena_output_)
            # returns False boolean if the web element found doesn't refer to a HTML <table> Element
            return False

    def read_delimited_file(self, file_path, delimiter=None):
        # looks for file in Ops Objective Assets directory
        # returns False if not found and prompt to ensure file is in the target directory
        if delimiter is None:
            delimiter = ','
        delimited_file_path = file_path
        ops_objective_dir = __selena_directory__.SelenaDir().fetch_assets_ops_objective_dir(
            self.selena_preference['ops_objective'])
        delimited_asset = os.path.join(ops_objective_dir, delimited_file_path)
        try:
            __selena_output__ = f"-->| ...Reading '{delimiter}' Delimited File located in: {delimited_asset}"
            staged_file = open(delimited_asset, "r")
            df_data_frame = pd.read_csv(staged_file, sep=delimiter)
            if self.selena_preference['narrator'] == "enabled":
                print(__selena_output__)
            self.log_listener.info(__selena_output__)
            return df_data_frame
        except FileNotFoundError:
            __selena_output__ = f"-->| Uh Oh...I wasn't able to find the Delimited Asset file at the location: {delimited_asset}"
            if self.selena_preference['narrator'] == "enabled":
                print(__selena_output__)
            self.log_listener.warn(__selena_output__)
            return False

    def read_excel_file(self, excel_file_path, sheet_name=None):
        # optional sheet name argument to or returns spreadsheet data frame object for all sheets
        ops_objective_dir = __selena_directory__.SelenaDir().fetch_assets_ops_objective_dir(
            self.selena_preference['ops_objective'])
        excel_asset_file = os.path.join(ops_objective_dir, excel_file_path)
        try:
            __selena_output__ = f"-->| ...Reading Excel File located in: {excel_file_path}"
            excel_data_frame = pd.read_excel(excel_asset_file, sheet_name)
            if self.selena_preference['narrator'] == "enabled":
                print(__selena_output__)
            self.log_listener.info(__selena_output__)
            return excel_data_frame
        except FileNotFoundError:
            __selena_output__ = f"-->| Uh Oh...I wasn't able to find the Excel Asset file at the location: {excel_asset_file}"
            if self.selena_preference['narrator'] == "enabled":
                print(__selena_output__)
            self.log_listener.warn(__selena_output__)
            return False

    def read_json_file(self, json_file_path):
        ops_objective_dir = __selena_directory__.SelenaDir().fetch_assets_ops_objective_dir(
            self.selena_preference['ops_objective'])
        json_asset_file = os.path.join(ops_objective_dir, json_file_path)
        try:
            __selena_output__ = f"-->| ...Reading JSON File located in: {json_asset_file}"
            staged_file = open(json_asset_file, "r")
            json_data_frame = pd.read_json(staged_file)
            if self.selena_preference['narrator'] == "enabled":
                print(__selena_output__)
            self.log_listener.info(__selena_output__)
            return json_data_frame
        except FileNotFoundError:
            __selena_output__ = f"-->| Uh Oh...I wasn't able to find the JSON Asset file at the location: {json_asset_file}"
            if self.selena_preference['narrator'] == "enabled":
                print(__selena_output__)
            self.log_listener.warn(__selena_output__)
            return False


x_driver.get("https://www.w3schools.com/html/html_tables.asp")
sleep(3)
data_test = dataAgent()
table_element_xpath = "//*[@id='customers']"
non_table_element_xpath = "//*[@id='main']/div[3]/a"
table_found = data_test.read_html_table(table_element_xpath)
if table_found:
    table_text = table_found[0]
    data_frame = table_found[1]
    html_markup = table_found[2]
    print(table_text, "\n")
    print(data_frame, "\n")
    print(html_markup)
elif table_found is False:
    print("-->| Table Validation Successful")
sleep(3)
test_df = data_test.read_delimited_file("test.csv", "|")
if test_df is not None:
    print("\n", test_df)
elif test_df is False:
    print("-->| Asset File Not Found error handling was successful")
test_json = data_test.read_json_file("test.json")
if test_json is not None:
    print("\n", test_json)
elif test_df is False:
    print("-->| Asset File Not Found error handling was successful")
test_excel = data_test.read_excel_file("test.xlsx")
sleep(3)
test_excel_sheet = data_test.read_excel_file("test.xls", "Prometheus")
if test_excel and test_excel_sheet is not None:
    print("\n", test_excel)
    print("\n", test_excel_sheet)
elif test_excel and test_excel_sheet is False:
    print("-->| Asset File Not Found error handling was successful")
sleep(3)
x_driver.quit()
