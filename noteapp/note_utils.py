import json
import os
from string import ascii_lowercase
import random


DB_FILENAME = 'database.json'

def _generate_id():
    return ''.join([
        random.choice(ascii_lowercase + '1234567890') 
        for i in range(16)
    ])

def get_notes():
    if not os.path.isfile(DB_FILENAME):
        return []

    return json.loads(open(DB_FILENAME).read())

def get_note_by_id(note_id):
    notes = list(filter(lambda x: x['id'] == note_id, get_notes()))
    return notes[0] if notes else None

def create_note(title, content):
    notes = get_notes()
    note = dict(
        id=_generate_id(),
        title=title, 
        content=content
    )
    notes.append(note)

    open(DB_FILENAME, 'w+').write(json.dumps(notes))
    return note


def delete_note():
    pass
