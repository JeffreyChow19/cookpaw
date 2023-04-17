import sys
import sqlite3
import os.path
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from ui.ui_main import Ui_MainWindow
from controller.controller import *
from models.article import *
from models.recipe import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.controller = Controller("src/database/cookpaw.db")
        articles_row = self.controller.get_all_articles()
        recipes_row = self.controller.get_all_recipes()
        
        # create a list of Article objects from the rows
        self.articles = [Article.from_row(row) for row in articles_row]
        self.recipes = [Recipe.from_row(row) for row in recipes_row]
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, self.articles, self.recipes)

    def refresh_after_recipe_added(self):
        recipes_row = self.controller.get_all_recipes()
        self.recipes = [Recipe.from_row(row) for row in recipes_row]
        self.ui.setupUi(self, self.articles, self.recipes)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


