from datetime import datetime

class Item:
    def __init__(self, name, description, contact_info, date=None):
        self.name = name
        self.description = description
        self.contact_info = contact_info
        self.date = date or datetime.now().strftime('%Y-%m-%d')
        self.returned = False

class LostItem(Item):
    def __init__(self, name, description, contact_info, date_lost=None):
        super().__init__(name, description, contact_info, date_lost)

class FoundItem(Item):
    def __init__(self, name, description, contact_info, date_found=None):
        super().__init__(name, description, contact_info, date_found)