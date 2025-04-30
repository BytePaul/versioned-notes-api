from fastapi import APIRouter
from typing import List
from models import NoteCreate, Note
from crud import create_note_in_db, get_notes_by_title, get_all_notes, delete_note_by_id

router = APIRouter()

@router.post("/notes/", response_model=Note)
def create_note(note: NoteCreate):
    return create_note_in_db(note)

@router.get("/notes/{title}", response_model=List[Note])
def get_note_versions(title: str):
    return get_notes_by_title(title)

@router.get("/notes/", response_model=List[Note])
def list_all_notes():
    return get_all_notes()

@router.delete("/notes/{note_id}")
def delete_note(note_id: int):
    delete_note_by_id(note_id)
    return {"message": "Note deleted successfully"}
