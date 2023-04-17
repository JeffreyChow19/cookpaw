from models.model import *
class Recipe(Model):
    def __init__(self, recipe_id, title, utensils, ingredients, steps, last_modified, author, path):
        self.recipe_id = recipe_id
        self.title = title
        self.utensils = utensils
        self.ingredients = ingredients
        self.steps = steps
        self.last_modified = last_modified
        self.author = author
        self.image_path = path