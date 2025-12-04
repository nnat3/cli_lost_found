from database_manager import DatabaseManager
from models import LostItem, FoundItem

class LostFoundManager:
    def __init__(self):
        self.db = DatabaseManager()
    
    def add_lost_item(self, name, description, contact_info, date_lost=None):
        item = LostItem(name, description, contact_info, date_lost)
        self.db.add_lost_item(item)
        print(f"Lost item '{name}' added successfully!")
    
    def add_found_item(self, name, description, contact_info, date_found=None):
        item = FoundItem(name, description, contact_info, date_found)
        self.db.add_found_item(item)
        print(f"Found item '{name}' added successfully!")