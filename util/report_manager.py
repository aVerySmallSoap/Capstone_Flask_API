#TODO: Complete this report manager
#TODO: NOTE! THIS IS NOT A REPLACEMENT FOR THE DATABASE, INSTEAD IT MANAGES THE NAMING AND PATHS OF THE REPORTS FOR REFERENCE AND STORAGE
class ReportManager:
    """Manages the naming and local paths of generated reports."""
    local_path:str = "./reports/" # Reference path in which reports are stored
    reports:dict = {} # The dictionary should only store a dict that has two values, name and path, wherein name is the name of the report

    def __init__(self, args):
        pass

    def generate(self):
        """Generates a name and path for the report. The naming scheme is: DDMMYY-HH-SS"""
        pass