import sys
import sqlite3
import os.path
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from ui.ui_main import Ui_MainWindow
from controller.controller import *
from models.article import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        controller = Controller("src/database/cookpaw.db")
        articles_row = controller.get_all_articles()

        # create a list of Article objects from the rows
        articles = [Article.from_row(row) for row in articles_row]

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, articles)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


