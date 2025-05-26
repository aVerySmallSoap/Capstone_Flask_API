# Installs all the project's dependencies
import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "wapiti3", "Flask", "flask-cors", "tz", "SQLAlchemy", "psycopg2"])