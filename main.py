from lost_found_manager import LostFoundManager

def main():
    manager = LostFoundManager()
    
    while True:
        print("\n=== LOST & FOUND MANAGER ===")
        print("1. Add Lost Item")
        print("2. Add Found Item")
        print("3. View Lost Items")
        print("4. View Found Items")
        print("5. Search Items")
        print("6. Mark Item as Returned")
        print("7. Delete Item")
        print("8. Exit")
        
        choice = input("\nSelect option (1-8): ").strip()
        
        if choice == '1':
            name = input("Item name: ")
            description = input("Description: ")
            contact = input("Your contact info: ")
            date_lost = input("Date lost (YYYY-MM-DD, or press Enter for today): ").strip()
            manager.add_lost_item(name, description, contact, date_lost or None)
        
        elif choice == '2':
            name = input("Item name: ")
            description = input("Description: ")
            contact = input("Your contact info: ")
            date_found = input("Date found (YYYY-MM-DD, or press Enter for today): ").strip()
            manager.add_found_item(name, description, contact, date_found or None)
        
        elif choice == '3':
            manager.display_lost_items()
        
        elif choice == '4':
            manager.display_found_items()
        
        elif choice == '5':
            query = input("Search by name or date: ")
            manager.search_items(query)
        
        elif choice == '6':
            item_id = int(input("Item ID: "))
            item_type = input("Item type (lost/found): ").lower()
            manager.mark_as_returned(item_id, item_type)
        
        elif choice == '7':
            item_id = int(input("Item ID: "))
            item_type = input("Item type (lost/found): ").lower()
            manager.delete_item(item_id, item_type)
        
        elif choice == '8':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()