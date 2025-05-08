from util.configurator import Configurator
import subprocess

# Update wapiti
#TODO: TRACK OF VULN DATABASE UPDATES
def scan() -> int:
    """Activate a scan using wapiti. Returns 1 if successful, 0 otherwise."""
    # process = subprocess.Popen(["wapiti", "--update"])
    # process.wait()
    # print("wapiti updated")

    # Start running config
    config = Configurator()
    config.set_url("https://google-gruyere.appspot.com/481794057459442987145926499918218457249/")
    test = config.configure()
    p = subprocess.Popen(test)
    p.wait()
    return 1 #TODO: find what the process returns or just return the status code