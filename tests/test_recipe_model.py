# Change path directory to root
import sys
import os
root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir + '/src')

from models.recipe import *

def test_recipe_model():
    id = 10
    title = "Recipe Title"
    utensils = "Spoon; Bowl"
    ingredients = "Cereal; Milk"
    steps = "Mix"
    last_modified = "Now"
    author = "Author"
    image_path = "Image Path"

    recipe = Recipe(id, title, utensils, ingredients, steps, last_modified, author, image_path)

    assert recipe.recipe_id == id
    assert recipe.title == title
    assert recipe.utensils == utensils
    assert recipe.ingredients == ingredients
    assert recipe.steps == steps
    assert recipe.last_modified == last_modified
    assert recipe.author == author
    assert recipe.image_path == image_path

