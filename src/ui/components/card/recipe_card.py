from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import getFont

class RecipeCard(QtWidgets.QWidget):
    def __init__(self, image_path, index, width, recipe, parent=None):
        super().__init__(parent)

        # print(recipe)
        recipe_title = recipe.title
        # CARD SIZE
        height = int(0.75 * width)

        self.setFixedHeight(height)
        self.setFixedWidth(width)

        self.recipe_image = QtWidgets.QLabel()
        self.recipe_image.setPixmap(QtGui.QPixmap("assets/images/"+recipe.image_path))
        self.recipe_image.setObjectName("recipe_image_" + str(index))
        self.recipe_image.setMargin(0)
        self.recipe_image.setFixedWidth(width)
        self.recipe_image.setScaledContents(True)

        self.recipe_title = QtWidgets.QPushButton()
        self.recipe_title.setFixedWidth(width)
        self.recipe_title.setFont(getFont("Bold", 14))
        self.recipe_title.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recipe_title.setText(recipe_title)
        self.recipe_title.setObjectName("recipe_title_" + str(index))
        self.recipe_title.setStyleSheet("#recipe_title_" + str(index) + """{
            text-align: left;
            background-color: white;
            padding: 20px;
            color: #F15D36;
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
            border-top-left-radius: 0;
            border-top-right-radius: 0;
        }""")
        
        recipe_card_layout = QtWidgets.QVBoxLayout()
        recipe_card_layout.setContentsMargins(0, 0, 0, 0)
        recipe_card_layout.setSpacing(0)
        recipe_card_layout.setAlignment(QtCore.Qt.AlignLeft) 
        recipe_card_layout.addWidget(self.recipe_image)
        recipe_card_layout.addWidget(self.recipe_title)
        
        self.setLayout(recipe_card_layout)