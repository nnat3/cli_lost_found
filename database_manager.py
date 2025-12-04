import sqlite3
from models import LostItem, FoundItem

class DatabaseManager:
    def __init__(self, db_name="lost_found.db"):
        self.db_name = db_name
        self.init_db()
    
    def init_db(self):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''CREATE TABLE IF NOT EXISTS lost_items (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                contact_info TEXT,
                date_lost TEXT,
                returned INTEGER DEFAULT 0
            )''')
            
            conn.execute('''CREATE TABLE IF NOT EXISTS found_items (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                contact_info TEXT,
                date_found TEXT,
                returned INTEGER DEFAULT 0
            )''')

    def add_lost_item (self, item):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''INSERT INTO lost_items (name, description, contact_info, date_lost)
                           VALUES (?, ?, ?, ?)''',
                        (item.name, item.description, item.contact_info, item.date))

    def add_found_item (self, item):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute('''INSERT INTO found_items (name, description, contact_info, date_found)
                           VALUES (?, ?, ?, ?)''',
                        (item.name, item.description, item.contact_info, item.date))  

    def get_lost_items(self):
        with sqlite3.connect(self.db_name) as conn:
            return conn.execute('SELECT * FROM lost_items').fetchall()

    def get_found_items(self):
        with sqlite3.connect(self.db_name) as conn:
            return conn.execute('SELECT * FROM found_items').fetchall()

    def search_lost_items(self, query):
        with sqlite3.connect(self.db_name) as conn:
            return conn.execute('''SELECT * FROM lost_items 
                                  WHERE name LIKE ? OR date_lost LIKE ?''',
                               (f'%{query}%', f'%{query}%')).fetchall()

    def search_found_items(self, query):
        with sqlite3.connect(self.db_name) as conn:
            return conn.execute('''SELECT * FROM found_items 
                                  WHERE name LIKE ? OR date_found LIKE ?''',
                               (f'%{query}%', f'%{query}%')).fetchall()
                     
    def update_item_status(self, item_id, table, returned=True):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(f'UPDATE {table} SET returned = ? WHERE id = ?',
                        (1 if returned else 0, item_id))
    
    def delete_item(self, item_id, table):
        with sqlite3.connect(self.db_name) as conn:
            conn.execute(f'DELETE FROM {table} WHERE id = ?', (item_id,))
                   