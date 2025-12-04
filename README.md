# Lost and Found Manager

A simple CLI application for managing lost and found items. Users can post lost items and browse found items to help reunite people with their belongings.

## Features (MVP)

 **Add Lost Items** - Record name, description, date lost & contact info  
 **Add Found Items** - Record name, description, date found & contact info  
 **Item Overview** - Display items in formatted tables (separate for lost/found)  
 **Search Feature** - Search items by name or date  
 **Update Status** - Mark items as 'returned' when recovered  
 **Delete Items** - Remove items from records  

## Quick Start

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Follow the menu prompts:**
   ```
   === LOST & FOUND MANAGER ===
   1. Add Lost Item
   2. Add Found Item
   3. View Lost Items
   4. View Found Items
   5. Search Items
   6. Mark Item as Returned
   7. Delete Item
   8. Exit
   ```

## Project Structure

```
cli_sample/
  ─ main.py                 # CLI entry point
  ─ lost_found_manager.py   # Handle user-interaction
  ─ database_manager.py     # SQLite operations
  ─ models.py              # Data models (Item, LostItem, FoundItem)
 README.md              # Project Overview
 lost_found.db          # SQLite database (auto-created)
```

## Architecture

- **Object-Oriented Design**: Uses inheritance with Item parent class
- **Separation of Concerns**: Each file has single responsibility
- **Database Cls Handler**: DatabaseManager handles all SQL operations
- **Clean CLI Interface**: Menu-driven user experience

## Database Components

**Tables:** `lost_items` and `found_items`


## Usage Examples

**Adding a Lost Item:**
```
Item name: iPhone 13
Description: Black iPhone with cracked screen
Your contact info: john@email.com
Date lost: 2024-01-15
```

**Searching Items:**
```
Search by name or date: iPhone
# Returns all items matching "iPhone"
```

## Requirements

- Python 3
- SQLite3 (included with Python)
- No external dependencies

## Notes

- All data is stored locally in `lost_found.db`
- Use Ctrl+C to exit at any time
- Ensure Python 3 is installed on your system to run the application

## License