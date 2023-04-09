from .components.sidebar.sidebar import *
from .pages.home.home import *
from .pages.recipe_list.recipe_list import *

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
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
        # MainWindow.resize(1440, 900)

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
        home_widget = Home(MainWindow)
        recipe_list_widget = RecipeList(MainWindow)
        
        content_container.addWidget(home_widget) # INDEX 0
        content_container.addWidget(recipe_list_widget) # INDEX 1

        ## sidebar container
        sidebar_container = QtWidgets.QWidget()
        sidebar_container.setFixedWidth(int(0.05 * width))
        sidebar_container.setStyleSheet("background-color: white;")
        sidebar = Sidebar(MainWindow, content_container)
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(sidebar, alignment=QtCore.Qt.AlignCenter)
        sidebar_container.setLayout(layout)

        self.layout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.layout.setSpacing(0)
        self.layout.addWidget(sidebar_container)
        self.layout.addWidget(content_container)
        self.layout.setContentsMargins(0,0,0,0)
        MainWindow.setCentralWidget(self.centralwidget)

