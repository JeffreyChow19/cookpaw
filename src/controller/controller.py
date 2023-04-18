import sqlite3
import os
from datetime import datetime
from models.article import *
from models.recipe import *
from models.note import *

class Controller:
    def __init__(self, db_name):
        """Controller class constructor, connects instance to specified db_name"""
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    # ## RECIPE CONTROLLERS ##
    def get_all_recipes(self):
        """RECIPE CONTROLLER: get list of recipes"""
        self.cursor.execute("SELECT recipe_id, title, utensils, ingredients, steps, last_modified, author, path FROM recipes NATURAL LEFT JOIN recipe_photos NATURAL LEFT JOIN photos")
        recipe_row = self.cursor.fetchall()
        recipes = [Recipe.from_row(row) for row in recipe_row]
        for recipe in recipes:
            recipe.notes = self.get_recipe_note(recipe.recipe_id)
        return recipes

    def get_recipe_by_id(self, recipe_id):
        """RECIPE CONTROLLER: get a recipe by recipe_id"""
        self.cursor.execute("SELECT * FROM recipes WHERE recipe_id=?", (recipe_id,))
        recipe = self.cursor.fetchone()
        return recipe

    def create_recipe(self, recipe):
        """RECIPE CONTROLLER: insert new recipe, auto increment recipe_id"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO recipes (title, utensils, ingredients, steps, last_modified) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(query, (recipe['title'], recipe['utensils'], recipe['ingredients'], recipe['steps'], now))
        self.commit()
        return self.cursor.lastrowid
    
    def create_user_recipe(self, recipe):
        """RECIPE CONTROLLER: insert new user recipe, auto increment recipe_id"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO recipes (title, utensils, ingredients, steps, last_modified, author) VALUES (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (recipe['title'], recipe['utensils'], recipe['ingredients'], recipe['steps'], now, "user"))
        self.commit()
        return self.cursor.lastrowid
    
    def update_recipe(self, recipe_id, recipe):
        """RECIPE CONTROLLER: update existing recipe with ID recipe_id"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "UPDATE recipes SET title=?, utensils=?, ingredients=?, steps=?, last_modified=? WHERE recipe_id=?"
        self.cursor.execute(query, (recipe['title'], recipe['utensils'], recipe['ingredients'], recipe['steps'], now, recipe_id))
        self.commit()
        return recipe_id

    def delete_recipe(self, recipe_id):
        """RECIPE CONTROLLER: delete a recipe by recipe_id"""
        self.cursor.execute("DELETE FROM recipes WHERE recipe_id=?", (recipe_id,))
        self.commit()

    # ## ARTICLE CONTROLLERS ##
    def get_all_articles(self):
        """ARTICLE CONTROLLER: get list of article"""
        self.cursor.execute("SELECT article_id, title, content, author, publish_date, path FROM articles NATURAL LEFT JOIN article_photos NATURAL LEFT JOIN photos")
        articles = self.cursor.fetchall()
        return [Article.from_row(row) for row in articles]

    def get_article_by_id(self, article_id):
        """ARTICLE CONTROLLER: get an article with ID article_id"""
        self.cursor.execute("SELECT * FROM articles WHERE article_id=?", (article_id,))
        article = self.cursor.fetchone()
        return article

    def create_article(self, article):
        """ARTICLE CONTROLLER: insert a new article, auto increment article_id"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO articles (title, content, publish_date) VALUES (?, ?, ?)"
        self.cursor.execute(query, (article['title'], article['content'], now))
        self.commit()
        return self.cursor.lastrowid

    def update_article(self, article_id, article):
        """ARTICLE CONTROLLER: update existing article"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "UPDATE articles SET title=?, content=?, publish_date=? WHERE article_id=?"
        self.cursor.execute(query, (article['title'], article['content'], now, article_id))
        self.commit()
        return article_id

    def delete_article(self, article_id):
        """ARTICLE CONTROLLER: delete an article with ID article_id"""
        self.cursor.execute("DELETE FROM articles WHERE article_id=?", (article_id,))
        self.commit()
    
    def add_photo(self, path):
        self.cursor.execute("INSERT INTO photos (path) VALUES (?)", (path,))
        self.commit()
        return self.cursor.lastrowid
    
    def get_photo_id(self, path):
        self.cursor.execute("SELECT photo_id FROM photos WHERE path=?", (path,))
        self.commit()
        photo_id = self.cursor.fetchone()
        return photo_id[0]

    def add_recipe_photo(self, recipe_photo):
        self.add_photo(recipe_photo["path"])
        photo_id = self.get_photo_id(recipe_photo["path"])
        self.cursor.execute("INSERT INTO recipe_photos (recipe_id, photo_id) VALUES (?, ?)", (int(recipe_photo["recipe_id"]), int(photo_id),))
        self.commit()

    def add_article_photo(self, article_photo):
        self.add_photo(article_photo["path"])
        photo_id = self.get_photo_id(article_photo["path"])
        self.cursor.execute("INSERT INTO article_photos (article_id, photo_id) VALUES (?, ?)", (int(article_photo["article_id"]), int(photo_id),))
        self.commit()
    
    def add_note_photo(self, notes_photo):
        photo_id = self.add_photo(notes_photo["path"])
        self.cursor.execute("INSERT INTO notes_photos (note_id, photo_id) VALUES (?, ?)", (int(notes_photo["note_id"]), int(photo_id),))
        self.commit()
    
    # ## NOTES CONTROLLERS ##
    def add_note(self, note):
        """NOTES CONTROLLER: insert new note to db"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO notes (title, content, publish_date, recipe_id) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (note['title'], note['content'], now, note["recipe_id"]))
        self.commit()
        return self.cursor.lastrowid

    def get_note_photos(self, note_id):
        """NOTES CONTROLLER: get paths to photos of note_photos"""
        self.cursor.execute("SELECT path FROM notes_photos NATURAL LEFT JOIN photos WHERE note_id=?", (note_id,))
        photos = self.cursor.fetchall()
        photo_paths = [path_tuple[0] for path_tuple in photos]
        return photo_paths
    
    def get_recipe_note(self, recipe_id):
        """NOTES CONTROLLER: get notes and notes' photos of a recipe"""
        self.cursor.execute("SELECT * FROM notes WHERE recipe_id=?", (recipe_id,))
        notes_row = self.cursor.fetchall()
        notes = [Note.from_row(row) for row in notes_row]
        for note in notes:
            note.image_paths = self.get_note_photos(note.note_id)
        return notes

    def get_note_by_id(self, note_id):
        """NOTES CONTROLLER: get a note by note_id"""
        self.cursor.execute("SELECT * FROM notes WHERE note_id=?", (note_id,))
        note = self.cursor.fetchone()
        return note

    def update_note(self, note):
        """NOTES CONTROLLER: update a note"""
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "UPDATE notes SET title=?, content=?, publish_date=? WHERE note_id=?"
        self.cursor.execute(query, (note['title'], note['content'], now, note["note_id"]))
        self.commit()
        return note["note_id"]

    def delete_note(self, note_id):
        """NOTES CONTROLLER: delete a note by note_id"""
        self.cursor.execute("DELETE FROM notes WHERE note_id=?", (note_id,))
        self.commit()

    # ## UTILITY ##
    def __del__(self):
        """INSTANCE DELETION: close db connection"""
        self.conn.close()

    def commit(self):
        """commit db modification"""
        self.conn.commit()
