from models.model import *
class Note(Model):
    def __init__(self, notes_id, note_title, note_content, publish_date, recipe_id):
        self.notes_id = notes_id
        self.note_title = note_title
        self.note_content = note_content
        self.publish_date = publish_date
        self.recipe_id = recipe_id