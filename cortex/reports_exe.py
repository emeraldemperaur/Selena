import os
from datetime import datetime
from time import sleep
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import tostring

import core.preferences.corepreferences as selenapreferences
import core.preferences.log_manager as selena_logger
import core.preferences.x_dir_configs as _selena_directory
from core.webclient_tools import browser_agent

_current_time = datetime.now()
# x_driver = xDriver.initXDriver().init_driver()
time_stamp = _current_time.strftime("%I:%M %p")
temp_xml = "c:\\Selena\\Reports\\Sanctum\\selenaReports.xml"


class selenaReporter:
    def __init__(self):
        self.commit_state = False
        self.reports_event_list = []
        self.__selena_preferences__ = selenapreferences.fetch_core_preferences()
        self.selena_log_listener = selena_logger.selenaLogger()
        self.browser_tools_ = browser_agent.browserAgent()
        self.xml_path = temp_xml

    def add_report_data(self, synopsis, result, resource=None):
        report_entry = {
            "synopsis": synopsis,
            "result": result,
            "resource": resource,
            "time": time_stamp
        }
        self.reports_event_list.append(report_entry)
        report_data_count = len(self.reports_event_list)
        selena_output_str = f"-->| Added Report Data ({report_data_count}) >> Synopsis: '{synopsis}' | Result: {result} | Resource: {resource}"
        self.selena_log_listener.info(selena_output_str)
        if self.__selena_preferences__['narrator'] == "enabled":
            print(selena_output_str)
        return True

    def commit_report_file(self):
        reports_raw = self.reports_event_list
        report_xml_list = []
        for reports_dict in reports_raw:
            # convert reportData dictionary object to XML node object
            xml_node = raw_report_to_xml_node("reportData", reports_dict)
            # convert reportData XML node object to decoded byte String
            xml_node_str = tostring(xml_node).decode('utf8')
            # append xml byte String to report_xml_list
            report_xml_list.append(xml_node_str)
        try:
            _selena_directory.SelenaDir().init_reports()
            ops_alias = self.__selena_preferences__['ops_objective']
            ops_objective_dir = _selena_directory.SelenaDir().fetch_ops_objective_dir("Reports", ops_alias)
            # writes reportData XML nodes into selenaReport XML
            output_file = xml_file_template(report_xml_list)
            reports_xml_name = "selenaReports.xml"
            report_xml_path = os.path.join(ops_objective_dir, reports_xml_name)
            # create selenaReports.xml file in Ops Objective Directory
            reports_xml_file = open(report_xml_path, "w+", encoding="utf-8")
            reports_xml_file.write(output_file)
            reports_xml_file.close()
            selena_str_output = f"-->| Selena Reports XML created, output file location: {report_xml_path}"
            render_prompt = f"\n-->| New selenaReport committed...REMEMBER to update reportRenderer XML path to: {report_xml_path} |<--\n"
            self.selena_log_listener.info(selena_str_output)
            self.selena_log_listener.info(render_prompt)
            if self.__selena_preferences__['narrator'] == "enabled":
                print(selena_str_output)
                print(render_prompt)
            # set commit state to True to be read by corresponding generateHTML class
            self.commit_state = True
            self.xml_path = report_xml_path
            # returns path to report_xml to be used by corresponding generateHTML class method to find XML source file
            return report_xml_path
        except AttributeError:
            # print Error Log Output
            return False

    def generate_pdf_report(self, x_driver):
        if self.commit_state:
            report_html_path = self.browser_tools_.report_html_sourcecode(x_driver)
            xml_path = self.xml_path
            # generator method will take a path returned for report_html to create pdf report w/ pdfkit
            pass
        elif not self.commit_state:
            pass


def xml_file_template(iterated_xml_list):
    head = "<selenaReport>\n"
    body = ''.join(xml for xml in iterated_xml_list)
    foot = "\n</selenaReport>"
    xml_text_output = f"{head}{body}{foot}"
    # print(xml_text_output)
    return xml_text_output


def raw_report_to_xml_node(xml_tag, report_dict):
    node = Element(xml_tag)
    for key, val in report_dict.items():
        child = Element(key)
        child.text = str(val)
        node.append(child)
    return node


reports_test = selenaReporter()
reports_test.add_report_data("Test1", "PASSED", "C:/FilePath.exe")
reports_test.add_report_data("Test2", "FAILED", "C:/NewFilePath")
reports_test.add_report_data("Test3", "PASSED", "FilePath")
reports_test.add_report_data("Test4", "FAILED")
reports_test.add_report_data("Prometheus", "UNDETERMINED", "No File Found")
sleep(4)
reports_test.commit_report_file()
sleep(4)
# x_driver.get('http://localhost:5000/')
# bt = selenaReporter().browser_tools_
# report_snap = bt.report_html_sourcecode(x_driver)
# if report_snap:
#     selena_output = f"-->| Report HTML source code snapshot created,  output file location: {report_snap}"
#     print(selena_output)
# else:
#     selena_output = f"-->| Oh Crap!...Report HTML source code capture failed"
#     print(selena_output)
# x_driver.quit()
