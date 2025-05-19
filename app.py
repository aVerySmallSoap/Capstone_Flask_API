from glob import escape
from flask import Flask
from flask_cors import CORS, cross_origin

from scripts.wapiti_parser import parse
from scripts.wapiti_scan import scan
from util.scan_manager import ScanManager

scan_manager = ScanManager()

app = Flask(__name__)
cors = CORS(app, resources={r"/v1/*": {"origins": "*"}})

# Scanning

# Wapiti
@app.route('/v1/wapiti/scan', methods=['POST', 'GET'])
def wapiti_scan():
    """Scan using Wapiti3's python package"""
    # scan_manager.spawn("wapiti", "some_ID", "SomeURL")
    scan()
    parsed = parse()
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
@app.route('/v1/report/load')
def load_report():
    return "Consolidated reports are not implemented yet! (-w-;)"

@app.route('/v1/report/<report_id>')
def get_report(report_id):
    return f"{escape(report_id)} should not exist! We have not even implemented this yet! (-w-;)"

# Wapiti
@app.route('/v1/wapiti/report')
def wapiti_report():
    report = parse()
    return report

@app.route('/v1/wapiti/status/<user>')
def wapiti_check(userid):
    return "Not implemented yet! (-w-;)"

if __name__ == '__main__':
    app.run(host="192.168.100.99")
