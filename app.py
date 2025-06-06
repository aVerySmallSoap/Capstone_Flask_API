from datetime import datetime
from glob import escape
from flask import Flask, request
from flask_cors import CORS

from managers.report_manager import ReportManager
from parsers.history_parser import history_parse, fetch_reports, fetch_report
from parsers.wapiti_parser import parse
from scanners.wapiti_scan import scan
from util.db import Database

_report_manager = ReportManager()
_db = Database()

app = Flask(__name__)
cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})

# Scanning

# Wapiti
@app.route('/v1/wapiti/scan', methods=['POST'])
def wapiti_scan():
    """Scan using Wapiti3's python package"""
    # scan_manager.spawn("wapiti", "some_ID", "SomeURL")
    _scan_start = datetime.now()
    _date_formated = _scan_start.strftime("%Y%m%d_%I-%M-%S")
    _report_manager.generate(_date_formated)
    path = _report_manager.build()
    scan(request.get_json()['url'], path)
    parsed = parse(path)
    _db.insert_wapiti_report(_scan_start, path)
    return parsed

# Zap
@app.route('/v1/zap/scan', methods=['POST', 'GET'])
def zap_scan():
    return "Zap scanning is not implemented yet! (-w-;)"

# Arachni
@app.route('/v1/arachni/scan', methods=['POST', 'GET'])
def arachni_scan():
    return "Arachni scanning is not implemented yet! (-w-;)"

# Settings
@app.route('/v1/settings/save')
def save_settings():
    #TODO: Save setting to SettingManager
    return "Settings are not implemented yet! (-w-;)"
@app.route('/v1/settings/load')
def load_settings():
    return "Settings are not implemented yet! (-w-;)"

# Wapiti
@app.route('/v1/wapiti/settings/save')
def wapiti_save_settings():
    return "Wapiti settings are not implemented yet! (-w-;)"
@app.route('/v1/wapiti/settings/load')
def wapiti_load_settings():
    return "Wapiti settings are not implemented yet! (-w-;)"

# Fetch data
@app.route('/v1/history/load')
def load_history():
    return history_parse()

@app.route('/v1/report/<report_id>')
def get_report(report_id):
    return f"{escape(report_id)} should not exist! We have not even implemented this yet! (-w-;)"

@app.route('/v1/report/fetch/<report_id>')
def report_fetch(report_id):
    return fetch_report(report_id)

# Wapiti
@app.route('/v1/wapiti/report/<report_id>')
def wapiti_report(report_id):
    report = fetch_reports(report_id)
    return parse(report)


@app.route('/v1/wapiti/status/<user>')
def wapiti_check(userid):
    return "Not implemented yet! (-w-;)"

if __name__ == '__main__':
    app.run(host="192.168.100.99")
