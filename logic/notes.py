from .models import Note
import json
import os
import pandas as pd


NOTES_FILE = f"{os.getcwd()}/storage/notes.json"


def load_notes():
    try:
        with open(NOTES_FILE, "r") as file:
            return [Note.from_dict(note) for note in json.load(file)]
    except:
        return []


def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump([note.to_dict() for note in notes], file, indent=4)


def create_note():
    notes = load_notes()
    note_id = len(notes) + 1
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержимое заметки: ")
    note = Note(note_id, title, content)
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно создана.")


def list_notes():
    notes = load_notes()
    if not notes:
        print("Список заметок пуст.")
        return
    for note in notes:
        print(f"{note.id}. {note.title} ({note.timestamp})")


def export_notes_to_csv():
    notes = load_notes()
    df = pd.DataFrame([note.to_dict() for note in notes])
    df.to_csv(f"{os.getcwd()}/storage/notes.csv", index=False)
    print("Заметки успешно экспортированы в CSV.")


def import_notes_from_csv():
    df = pd.read_csv(f"{os.getcwd()}/storage/notes.csv")
    notes = [Note.from_dict(row) for index, row in df.iterrows()]
    save_notes(notes)
    print("Заметки успешно импортированы из CSV.")
