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

        def display_lost_items(self):
        items = self.db.get_lost_items()
        if not items:
            print("No lost items found.")
            return
        
        print("\n--- LOST ITEMS ---")
        print(f"{'ID':<3} {'Name':<15} {'Description':<20} {'Contact':<15} {'Date Lost':<12} {'Status':<10}")
        print("-" * 80)
        for item in items:
            status = "Returned" if item[5] else "Lost"
            print(f"{item[0]:<3} {item[1]:<15} {item[2]:<20} {item[3]:<15} {item[4]:<12} {status:<10}")
    
    def display_found_items(self):
        items = self.db.get_found_items()
        if not items:
            print("No found items.")
            return
        
        print("\n--- FOUND ITEMS ---")
        print(f"{'ID':<3} {'Name':<15} {'Description':<20} {'Contact':<15} {'Date Found':<12} {'Status':<10}")
        print("-" * 80)
        for item in items:
            status = "Returned" if item[5] else "Available"
            print(f"{item[0]:<3} {item[1]:<15} {item[2]:<20} {item[3]:<15} {item[4]:<12} {status:<10}")
    
    def search_items(self, query):
        lost_results = self.db.search_lost_items(query)
        found_results = self.db.search_found_items(query)
        
        if lost_results:
            print(f"\n--- LOST ITEMS MATCHING '{query}' ---")
            for item in lost_results:
                status = "Returned" if item[5] else "Lost"
                print(f"ID: {item[0]}, Name: {item[1]}, Description: {item[2]}, Contact: {item[3]}, Date: {item[4]}, Status: {status}")
        
        if found_results:
            print(f"\n--- FOUND ITEMS MATCHING '{query}' ---")
            for item in found_results:
                status = "Returned" if item[5] else "Available"
                print(f"ID: {item[0]}, Name: {item[1]}, Description: {item[2]}, Contact: {item[3]}, Date: {item[4]}, Status: {status}")
        
        if not lost_results and not found_results:
            print(f"No items found matching '{query}'")
    
    def mark_as_returned(self, item_id, item_type):
        table = "lost_items" if item_type == "lost" else "found_items"
        self.db.update_item_status(item_id, table, True)
        print(f"Item ID {item_id} marked as returned!")
    
    def delete_item(self, item_id, item_type):
        table = "lost_items" if item_type == "lost" else "found_items"
        self.db.delete_item(item_id, table)
        print(f"Item ID {item_id} deleted successfully!")