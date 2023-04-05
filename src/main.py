import sys
import sqlite3
import os.path
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from ui.ui_main import Ui_MainWindow
from database.db import *
from models.article import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        if not os.path.exists("src/database/cookpaw.db"):
            database = Database()
        # create a connection to the database
        conn = sqlite3.connect("src/database/cookpaw.db")
        c = conn.cursor()
        # execute a SELECT statement to retrieve data from the articles table
        c.execute("SELECT * FROM articles")

        # fetch all the rows from the result set
        article_rows = c.fetchall()

        # create a list of Article objects from the rows
        articles = [Article.from_row(row) for row in article_rows]

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, articles)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


