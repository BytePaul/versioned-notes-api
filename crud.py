import sqlite3
import datetime
from models import Note, NoteCreate
from typing import List
from database import get_db_connection

def get_latest_version(title: str) -> int:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT MAX(version) FROM notes WHERE title = ?", (title,))
    result = c.fetchone()
    conn.close()
    return result[0] if result[0] else 0

def create_note_in_db(note: NoteCreate) -> Note:
    version = get_latest_version(note.title) + 1
    timestamp = datetime.datetime.now().isoformat()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO notes (title, content, tag, timestamp, version)
        VALUES (?, ?, ?, ?, ?)
    ''', (note.title, note.content, note.tag, timestamp, version))
    conn.commit()
    note_id = c.lastrowid
    conn.close()
    return Note(id=note_id, title=note.title, content=note.content, tag=note.tag, timestamp=timestamp, version=version)

def get_notes_by_title(title: str) -> List[Note]:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM notes WHERE title = ? ORDER BY version DESC", (title,))
    rows = c.fetchall()
    conn.close()
    return [Note(id=row[0], title=row[1], content=row[2], tag=row[3], timestamp=row[4], version=row[5]) for row in rows]

def get_all_notes() -> List[Note]:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM notes ORDER BY timestamp DESC")
    rows = c.fetchall()
    conn.close()
    return [Note(id=row[0], title=row[1], content=row[2], tag=row[3], timestamp=row[4], version=row[5]) for row in rows]

def delete_note_by_id(note_id: int) -> None:
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
