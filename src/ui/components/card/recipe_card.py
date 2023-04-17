from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import getFont

class RecipeCard(QtWidgets.QWidget):
    def __init__(self, index, width, recipe, parent=None):
        super().__init__(parent)

        recipe_title = recipe.title
        self.recipe = recipe
        self.stacked_widget = parent.stacked_widget
           
        # CARD SIZE
        height = int(0.75 * width)

        self.setFixedHeight(height)
        self.setFixedWidth(width)
        self.recipe_image = QtWidgets.QLabel()
        if (recipe.image_path == None):
            recipe.image_path = "empty.jpg"
        self.recipe_image.setPixmap(QtGui.QPixmap("assets/images/"+recipe.image_path))
        self.recipe_image.setObjectName("recipe_image_" + str(index))
        self.recipe_image.setMargin(0)
        self.recipe_image.setFixedWidth(width)
        self.recipe_image.setScaledContents(True)
        self.recipe_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.recipe_image.mousePressEvent = self.handle_recipe_title_image_clicked

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
        self.recipe_title.clicked.connect(self.handle_recipe_title_image_clicked)
        
        recipe_card_layout = QtWidgets.QVBoxLayout()
        recipe_card_layout.setContentsMargins(0, 0, 0, 0)
        recipe_card_layout.setSpacing(0)
        recipe_card_layout.setAlignment(QtCore.Qt.AlignLeft) 
        recipe_card_layout.addWidget(self.recipe_image)
        recipe_card_layout.addWidget(self.recipe_title)
        
        self.setLayout(recipe_card_layout)
    
    def handle_recipe_title_image_clicked(self, event):
        """
        Handle the click event for the recipe title and image.
        """

        # UPDATE RECIPE DETAIL WIDGET
        # self.stacked_widget.recipe_detail_widget.recipe_detail(self.recipe)

        # CHANGE STACKED WIDGET TO RECIPE DETAIL
        self.stacked_widget.setCurrentIndex(1)