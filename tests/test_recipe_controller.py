# Change path directory to root
import sys
import os
root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir + '/src')

from controller.controller import *
from models.recipe import *

def test_recipe_controller():
    # make a new controller
    controller = Controller("src/database/cookpaw.db")
    
    # insert new recipe
    recipe = {
        "title" : "Recipe Title",
        "utensils" : "Recipe Utensils",
        "ingredients" : "Recipe Ingredients",
        "steps" : "Recipe Steps"
    }
    controller.create_recipe(recipe)

    # get all recipes
    recipes = controller.get_all_recipes()

    # get recently inserted recipe
    last_recipe = recipes[-1]
    last_recipe_by_id = controller.get_recipe_by_id(last_recipe.recipe_id)

    # TEST: get_recipe_by_id
    assert last_recipe_by_id[0] == last_recipe.recipe_id

    # delete last recipe
    controller.delete_recipe(last_recipe.recipe_id)

    # get last recipe after deletion of last_recipe
    recipes = controller.get_all_recipes()
    last_recipe_after_del = recipes[-1]

    # TEST: create_recipe, get_all_recipes, delete_recipe
    assert last_recipe.title == recipe["title"]
    assert last_recipe.utensils == recipe["utensils"]
    assert last_recipe.ingredients == recipe["ingredients"]
    assert last_recipe.steps == recipe["steps"]
    assert last_recipe_after_del.title != recipe["title"]
    assert last_recipe_after_del.utensils != recipe["utensils"]
    assert last_recipe_after_del.ingredients != recipe["ingredients"]
    assert last_recipe_after_del.steps != recipe["steps"]

    # TEST: create_user_recipe
    controller.create_user_recipe(recipe)
    recipes = controller.get_all_recipes()      # insert user recipe
    last_recipe = recipes[-1]
    assert last_recipe.author == "user"

    # TEST: update_recipe
    updated_recipe = {
        "title" : "Updated Recipe Title",
        "utensils" : "Updated Recipe Utensils",
        "ingredients" : "Recipe Ingredients",
        "steps" : "Recipe Steps"
    }
    controller.update_recipe(last_recipe.recipe_id, updated_recipe)
    recipes = controller.get_all_recipes()
    last_recipe = recipes[-1]
    assert last_recipe.title == updated_recipe["title"]
    assert last_recipe.utensils == updated_recipe["utensils"]
    assert last_recipe.ingredients == updated_recipe["ingredients"]
    assert last_recipe.steps == updated_recipe["steps"]
    
    # delete and reset db after testing
    controller.delete_recipe(last_recipe.recipe_id)
