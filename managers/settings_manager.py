

class SettingManager:
    """Manages each user's settings and saves them into a database"""
     # This single dictionary will not be scalable and will block async IO operations as its mutable

    def __init__(self):
        self.managed_settings: dict = {}
        self._dirty = False

    def save_settings(self, settings):

        pass

    def load_settings(self, db):
        pass

    #This function is expensive to call so do it sparingly
    def push_to_db(self, ):
        """Asynchronously pushes settings to the database by periodically checking if the in memory db is updated or not."""
        pass