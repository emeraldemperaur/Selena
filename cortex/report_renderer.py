from flask import Flask, render_template

import core.preferences.corepreferences as selenapreferences
import core.preferences.log_manager as selena_logger
from core.webclient_tools import browser_agent
from cortex.reports_exe import selenaReporter

_browser_tools = browser_agent.browserAgent()
_selena_preferences = selenapreferences.fetch_core_preferences()
_selena_log_listener = selena_logger.selenaLogger()


class reportRenderer:
    def __init__(self):
        self.pdf_options = {
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
        }
        self.app = Flask(__name__, template_folder='../cortex/templates')
        self.xml_temp = selenaReporter().xml_path


app = reportRenderer().app


@app.route('/')
def index():
    # input xml_temp path to be used by templates for report rendering
    return render_template('selenaReport.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # create HTML output file from template render in Ops Objective Directory
