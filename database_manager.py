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