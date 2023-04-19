# Change path directory to root
import sys
import os
root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir + '/src')

from models.note import *

def test_note_model():
    id = 15
    title = "Note Title"
    content = "First Try!"
    publish_date = "Now"
    recipe_id = 30

    note = Note(id, title, content, publish_date, recipe_id)

    assert note.note_id == id
    assert note.note_title == title
    assert note.note_content == content
    assert note.publish_date == publish_date
    assert note.recipe_id == recipe_id

