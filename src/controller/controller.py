import sqlite3
import os
from datetime import datetime
from models.article import *
from models.recipe import *
from models.note import *

class Controller:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def get_all_recipes(self):
        self.cursor.execute("SELECT recipe_id, title, utensils, ingredients, steps, last_modified, author, path FROM recipes NATURAL LEFT JOIN recipe_photos NATURAL LEFT JOIN photos")
        recipe_row = self.cursor.fetchall()
        recipes = [Recipe.from_row(row) for row in recipe_row]
        for recipe in recipes:
            recipe.notes = self.get_recipe_note(recipe.recipe_id)
        return recipes

    # def get_all_notes(self):
    #     self.cursor.execute("SELECT * FROM notes")
    #     notes = self.cursor.fetchall()
    #     return notes

    def get_recipe_by_id(self, recipe_id):
        self.cursor.execute("SELECT * FROM recipes WHERE recipe_id=?", (recipe_id,))
        recipe = self.cursor.fetchone()
        return recipe

    def create_recipe(self, recipe):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO recipes (title, utensils, ingredients, steps, last_modified) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(query, (recipe['title'], recipe['utensils'], recipe['ingredients'], recipe['steps'], now))
        self.commit()
        return self.cursor.lastrowid
    
    def create_user_recipe(self, recipe):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO recipes (title, utensils, ingredients, steps, last_modified, author) VALUES (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (recipe['title'], recipe['utensils'], recipe['ingredients'], recipe['steps'], now, "user"))
        self.commit()
        return self.cursor.lastrowid
    
    def update_recipe(self, recipe_id, recipe):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "UPDATE recipes SET title=?, utensils=?, ingredients=?, steps=?, last_modified=? WHERE recipe_id=?"
        self.cursor.execute(query, (recipe['title'], recipe['utensils'], recipe['ingredients'], recipe['steps'], now, recipe_id))
        self.commit()
        return recipe_id

    def delete_recipe(self, recipe_id):
        self.cursor.execute("DELETE FROM recipes WHERE recipe_id=?", (recipe_id,))
        self.commit()
    
    def get_all_articles(self):
        self.cursor.execute("SELECT article_id, title, content, author, publish_date, path FROM articles NATURAL LEFT JOIN article_photos NATURAL LEFT JOIN photos")
        articles = self.cursor.fetchall()
        return [Article.from_row(row) for row in articles]


    def get_article_by_id(self, article_id):
        self.cursor.execute("SELECT * FROM articles WHERE article_id=?", (article_id,))
        article = self.cursor.fetchone()
        return article

    def create_article(self, article):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO articles (title, content, publish_date) VALUES (?, ?, ?)"
        self.cursor.execute(query, (article['title'], article['content'], now))
        self.commit()
        return self.cursor.lastrowid

    def update_article(self, article_id, article):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "UPDATE articles SET title=?, content=?, publish_date=? WHERE article_id=?"
        self.cursor.execute(query, (article['title'], article['content'], now, article_id))
        self.commit()
        return article_id

    def delete_article(self, article_id):
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
        self.cursor.execute("INSERT INTO notes_photos (notes_id, photo_id) VALUES (?, ?)", (int(notes_photo["notes_id"]), int(photo_id),))
        self.commit()
    
    def add_note(self, note):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = "INSERT INTO notes (title, content, publish_date, recipe_id) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (note['title'], note['content'], now, note["recipe_id"]))
        self.commit()
        return self.cursor.lastrowid

    def get_note_photos(self, notes_id):
        self.cursor.execute("SELECT path FROM notes_photos NATURAL LEFT JOIN photos WHERE notes_id=?", (notes_id,))
        photos = self.cursor.fetchall()
        photo_paths = [path_tuple[0] for path_tuple in photos]
        return photo_paths
    
    def get_recipe_note(self, recipe_id):
        self.cursor.execute("SELECT * FROM notes WHERE recipe_id=?", (recipe_id,))
        notes_row = self.cursor.fetchall()
        notes = [Note.from_row(row) for row in notes_row]
        for note in notes:
            note.image_paths = self.get_note_photos(note.notes_id)
        return notes

    # def get_photos(self):
    #     self.cursor.execute("SELECT * FROM photos");
    #     res = (self.cursor.fetchall())
    #     print(res)
    # def get_recipe_photo(self):
    #     self.cursor.execute("SELECT * FROM recipe_photos");
    #     print(self.cursor.fetchall())
    
    def __del__(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

# if __name__ == "__main__":
#     c = Controller("src/database/cookpaw.db")
#     c.get_recipe_photo()
#     c.get_photos()