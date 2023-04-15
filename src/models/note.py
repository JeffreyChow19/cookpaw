class Note:
    def __init__(self, note_id, note_title, note_content, publish_date, recipe_id):
        self.note_id = note_id
        self.note_title = note_title
        self.note_content = note_content
        self.publish_date = publish_date
        self.recipe_id = recipe_id
    
    @classmethod
    def from_row(cls, row):
        return cls(*row)