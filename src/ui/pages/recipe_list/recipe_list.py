from ui.components.card.recipe_card import *
from ui.components.card.article_card import *
from ui.utils import getFont
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class RecipeList(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        #set dashboard size
        self.setFixedWidth(int(0.95 * parentWidth))
        self.setFixedHeight(parentHeight)

        ## HEADER ##
        # recipe list title
        recipe_list_title = QtWidgets.QLabel()
        recipe_list_title.setFont(getFont("Bold", 32))
        recipe_list_title.setFixedHeight(int(0.053 * parentHeight))
        recipe_list_title.setText("Recipe's Collection")
        recipe_list_title.setObjectName("recipe_list_title")
        recipe_list_title.setStyleSheet("#recipe_list_title{color: #FFCF52;}")

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(recipe_list_title)

        self.setLayout(self.layout)
    

   