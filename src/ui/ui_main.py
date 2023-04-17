from .components.sidebar.sidebar import *
from .pages.home import *
from .pages.recipe_list import *
from .pages.article_list import *
from .pages.recipe_detail import *
from .pages.article_detail import *
from .pages.note_editor import *
from .pages.recipe_editor import *

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, articles, recipes):
        MainWindow.setObjectName("MainWindow")

        # SET MAIN WINDOW SIZE
        # Create a QApplication object
        app = QtWidgets.QApplication.instance()

        # Get the screen size
        screen = app.desktop().screenGeometry()
        screen_width = screen.width()

        # Calculate the width and height of the MainWindow
        width = int(screen_width * 0.8)
        height = int(width * 10 / 16)

        # Set the size of the MainWindow
        MainWindow.resize(width, height)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # content container
        content_container = QtWidgets.QStackedWidget()
        content_container.setFixedWidth(int(0.95 * width))
        MainWindow.stacked_widget = content_container

        ## sidebar container
        sidebar_container = QtWidgets.QWidget()
        sidebar_container.setFixedWidth(int(0.05 * width))
        sidebar_container.setStyleSheet("background-color: white;")
        sidebar = Sidebar(MainWindow)
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(sidebar, alignment=QtCore.Qt.AlignCenter)
        sidebar_container.setLayout(layout)

        # ADD STACKED_WIDGET TO MAIN WINDOW
        MainWindow.last_page_index = 0
        MainWindow.sidebar = sidebar
        home_widget = Home(articles, recipes, MainWindow)
        recipe_list_widget = RecipeList(recipes, MainWindow)
        article_list_widget = ArticleList(articles, MainWindow)

        recipe_detail_widget = RecipeDetail(recipes[0], MainWindow)
        # tester for article detail, note editor, recipe editor
        article_detail_widget = ArticleDetail(articles[0], MainWindow)
  
        note_page = NoteEditor(parent=MainWindow,type = "input", note_data=True)
        MainWindow.add_notes_page = note_page
        
        recipe_page = RecipeEditor(parent=MainWindow, type = "input", recipe_data =None)
        edit_recipe_page = RecipeEditor(parent=MainWindow, type = "edit", recipe_data =None)
        
        edit_notes_page = NoteEditor(parent=MainWindow,type = "edit", note_data=True)
        MainWindow.edit_notes_page = edit_notes_page
        # ADD ARTICLE DETAIL WIDGET TO MAIN WINDOW
        MainWindow.stacked_widget.article_detail_widget = article_detail_widget
        MainWindow.stacked_widget.recipe_detail_widget = recipe_detail_widget

        content_container.addWidget(home_widget) # INDEX 0
        content_container.addWidget(recipe_list_widget) # INDEX 1
        content_container.addWidget(article_list_widget) # INDEX 2

        # tester for article detail, note editor, recipe editor
        content_container.addWidget(article_detail_widget) # INDEX 3
        content_container.addWidget(recipe_detail_widget) # INDEX 4
        content_container.addWidget(note_page) # INDEX 5
        content_container.addWidget(recipe_page) # INDEX 6
        content_container.addWidget(edit_recipe_page) # INDEX 7
        content_container.addWidget(edit_notes_page) # INDEX 8

        self.layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.layout.setSpacing(0)
        self.layout.addWidget(sidebar_container)
        self.layout.addWidget(content_container)
        self.layout.setContentsMargins(0,0,0,0)
        MainWindow.setCentralWidget(self.centralwidget)

