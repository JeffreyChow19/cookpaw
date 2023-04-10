class Recipe:
    def __init__(self, recipe_id, title, utensils, ingredients, steps, last_modified, author):
        self.recipe_id = recipe_id
        self.title = title
        self.utensils = utensils
        self.ingredients = ingredients
        self.steps = steps
        self.last_modified = last_modified
        self.author = author
    
    @classmethod
    def from_row(cls, row):
        return cls(*row)