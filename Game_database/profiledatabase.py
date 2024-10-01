import sqlite3

class NameDatabase:
    def __init__(self, filename='name_database.db'):
        self.conn = sqlite3.connect(filename)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS name_database (
                            id INTEGER PRIMARY KEY,
                            name TEXT
                        )''')
        self.conn.commit()

    def get_name(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM name_database WHERE id = 1")
        row = cursor.fetchone()
        return row[0] if row else None

    def add_name(self, name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO name_database (name) VALUES (?)", (name,))
        self.conn.commit()
