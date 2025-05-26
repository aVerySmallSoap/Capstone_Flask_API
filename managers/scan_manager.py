from scanners.wapiti_scan import scan

class ScanManager:
    """Manages scans from client requests"""
    _scans = {"wapiti":{}, "zap":{}, "arachni":{}} # Template: scanner:{USERID, SCANNER, STATUS}
    _SCANNING = 0
    _DONE = 1

    def __init__(self):
        pass

    def spawn(self, scanner, userid, url):
        if scanner == "wapiti":
            if userid not in self._scans["wapiti"]:
                self._scans['wapiti'] = {userid:{"scanner": "wapiti", "status": self._SCANNING}}
                # scan = scan() ; start the scan
                if scan == "done":
                    self._scans["wapiti"][userid].update({"status":self._DONE})
            elif self._scans["wapiti"][userid].get("status") == self._DONE:
                self._scans["wapiti"].pop(userid)
                # parse() ; parse the result here
                pass  # return the scan results

        elif scanner == "zap":
            pass
        else: #arachni
            pass