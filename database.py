import sqlite3

def init_db():
    conn = sqlite3.connect("notes.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            tag TEXT,
            timestamp TEXT NOT NULL,
            version INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    return sqlite3.connect("notes.db")
