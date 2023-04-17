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
        
        # create a list of Article objects from the rows
        self.articles = self.controller.get_all_articles()
        self.recipes = self.controller.get_all_recipes()
        # for recipe in self.recipes:
        #     print(recipe.title)
        #     print(recipe.notes)
        # print(self.controller.get_all_notes())
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, self.articles, self.recipes)

    def refresh_after_recipe_added(self):
        self.recipes = self.controller.get_all_recipes()
        self.ui.setupUi(self, self.articles, self.recipes)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


