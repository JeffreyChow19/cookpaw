# Change path directory to root
import sys
import os
root_dir = os.path.abspath(os.path.join(os.getcwd()))
sys.path.append(root_dir)

from src.controller.controller import *
from src.models.recipe import *
from src.models.article import *

def test_recipe_model():
    # make a new controller
    controller = Controller("src/database/cookpaw.db")
    recipe = {
        "title" : "Recipe Title",
        "utensils" : "Recipe Utensils",
        "ingredients" : "Recipe Ingredients",
        "steps" : "Recipe Steps"
    }

    article = {
        "title" : "Article Title",
        "content" : "Article Content",
    }

    controller.create_recipe(recipe)
    controller.create_article(article)

    # test get all recipes
    recipe_row = controller.get_all_recipes()

    recipes = [Recipe.from_row(row) for row in recipe_row]

    last_recipe = recipes[-1]

    controller.delete_recipe(last_recipe.recipe_id)

    recipe_row = controller.get_all_recipes()

    recipes = [Recipe.from_row(row) for row in recipe_row]
    last_recipe_after_del = recipes[-1]

    # test get all recipes
    article_row = controller.get_all_articles()

    articles = [Article.from_row(row) for row in article_row]

    last_article = articles[-1]

    controller.delete_article(last_article.article_id)

    article_row = controller.get_all_articles()

    articles = [Article.from_row(row) for row in article_row]
    last_article_after_del = articles[-1]

    assert last_recipe.title == recipe["title"]
    assert last_recipe.utensils == recipe["utensils"]
    assert last_recipe.ingredients == recipe["ingredients"]
    assert last_recipe.steps == recipe["steps"]
    assert last_recipe_after_del.title != recipe["title"]
    assert last_recipe_after_del.utensils != recipe["utensils"]
    assert last_recipe_after_del.ingredients != recipe["ingredients"]
    assert last_recipe_after_del.steps != recipe["steps"]

    assert last_article.title == article["title"]
    assert last_article.content == article["content"]
    assert last_article_after_del.title != article["title"]
    assert last_article_after_del.content != article["content"]
