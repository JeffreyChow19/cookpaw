# Change path directory to root
import sys
import os
root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir + '/src')

from controller.controller import *
from models.recipe import *
from models.note import *

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

    # get recently inserted recipe
    recipes = controller.get_all_recipes()
    last_recipe = recipes[-1]

    # insert new notes to recipe
    note_1 = {
        "title" : "Note1",
        "content" : "Content1",
        "recipe_id" : last_recipe.recipe_id
    }
    note_2 = {
        "title" : "Note2",
        "content" : "Content2",
        "recipe_id" : last_recipe.recipe_id
    }
    note_1_id = controller.add_note(note_1)
    note_2_id = controller.add_note(note_2)

    # TEST: add_note, get_recipe_note
    recipe_notes = controller.get_recipe_note(last_recipe.recipe_id)
    for note in recipe_notes:
        print(note.note_id)
        print(note.note_title)
        print(note.note_content)
    print()
    assert len(recipe_notes) == 2
    assert recipe_notes[0].note_id == note_1_id
    assert recipe_notes[1].note_id == note_2_id
    assert recipe_notes[0].note_title == note_1["title"]
    assert recipe_notes[1].note_title == note_2["title"]
    assert recipe_notes[0].note_content == note_1["content"]
    assert recipe_notes[1].note_content == note_2["content"]
    
    # TEST: get_note_by_id
    note_1_by_id = controller.get_note_by_id(note_1_id)
    assert note_1_by_id[0] == note_1_id
    assert note_1_by_id[1] == note_1["title"]
    assert note_1_by_id[2] == note_1["content"]
    assert note_1_by_id[4] == note_1["recipe_id"]

    # TEST: update_note
    updated_note_1 = {
        "title" : "Update Note1",
        "content" : "Update Content1",
        "recipe_id" : last_recipe.recipe_id,
        "note_id" : note_1_id
    }
    controller.update_note(updated_note_1)
    updated_note_1_by_id = controller.get_note_by_id(note_1_id)
    recipe_notes = controller.get_recipe_note(last_recipe.recipe_id)
    for note in recipe_notes:
        print(note.note_id)
        print(note.note_title)
        print(note.note_content)
    print()
    assert len(recipe_notes) == 2
    assert updated_note_1_by_id[0] == note_1_id
    assert updated_note_1_by_id[1] == updated_note_1["title"]
    assert updated_note_1_by_id[2] == updated_note_1["content"]
    assert updated_note_1_by_id[4] == updated_note_1["recipe_id"]

    # TEST: delete_note
    controller.delete_note(note_1_id)
    recipe_notes = controller.get_recipe_note(last_recipe.recipe_id)
    for note in recipe_notes:
        print(note.note_id)
        print(note.note_title)
        print(note.note_content)
    print()
    assert len(recipe_notes) == 1


    # delete and reset db after testing
    controller.delete_recipe(last_recipe.recipe_id)
    recipe_notes = controller.get_recipe_note(last_recipe.recipe_id)
    for note in recipe_notes:
        print(note.note_id)
        print(note.note_title)
        print(note.note_content)
    print()
    assert len(recipe_notes) == 0

    recipes = controller.get_all_recipes()
