from ui.utils import getFont
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class RecipeDetail(QtWidgets.QWidget):
    def __init__(self, recipe, parent=None):
        super().__init__(parent)

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        #set dashboard size
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addStretch()

        # SCROLL AREA
        scrollArea = QtWidgets.QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(scrollArea)

        # CONTENT WIDGET
        contentWidget = QtWidgets.QWidget(scrollArea)
        contentWidget.setMinimumWidth(scrollArea.width())
        scrollArea.setWidget(contentWidget)

        # TITLE
        recipe_title = QtWidgets.QLabel()
        recipe_title.setText(recipe.title)
        recipe_title.setObjectName("recipe_title")
        recipe_title.setFont(getFont("Bold", 24))
        recipe_title.setStyleSheet("#recipe_title{color: #29B067;}")
        recipe_title.setAlignment(QtCore.Qt.AlignCenter)

        # AUTHOR
        author_container = QtWidgets.QHBoxLayout()
        author_logo_path = "assets/icons/icon_author.svg"
        author_logo_widget = QtSvg.QSvgWidget(author_logo_path, parent=self)
        author_logo_widget.setFixedSize(32, 32)
        author_container.addWidget(author_logo_widget, alignment=QtCore.Qt.AlignCenter)
        recipe_author = QtWidgets.QLabel()
        recipe_author.setText("Cookpaw\'s Team")
        recipe_author.setObjectName("recipe_author")
        recipe_author.setFont(getFont("Regular", 10))
        author_container.addWidget(recipe_author)

        # LAST MODIFIED
        last_modified_container = QtWidgets.QHBoxLayout()
        last_modified_logo_path = "assets/icons/icon_time.svg"
        last_modified_logo_widget = QtSvg.QSvgWidget(last_modified_logo_path, parent=self)
        last_modified_logo_widget.setFixedSize(32, 32)
        last_modified_container.addWidget(last_modified_logo_widget, alignment=QtCore.Qt.AlignCenter)
        recipe_last_modified = QtWidgets.QLabel()
        recipe_last_modified.setText(recipe.last_modified)
        recipe_last_modified.setObjectName("recipe_last_modified")
        recipe_last_modified.setFont(getFont("Regular", 10))
        last_modified_container.addWidget(recipe_last_modified)

        # RECIPE DETAIL
        recipe_detail_container = QtWidgets.QHBoxLayout()
        recipe_detail_container.addStretch()
        recipe_detail_container.addLayout(author_container)
        recipe_detail_container.addLayout(last_modified_container)
        recipe_detail_container.addStretch()

        # IMAGE
        recipe_image = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("assets/images/" + recipe.image_path)
        scaled_pixmap = pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
        recipe_image.setPixmap(scaled_pixmap)
        recipe_image.setObjectName("recipe_image")
        recipe_image.setAlignment(QtCore.Qt.AlignCenter)

        # INGREDIENTS
        ingredients_container = QtWidgets.QVBoxLayout()
        ingredients_label = QtWidgets.QLabel()
        ingredients_label.setText("Ingredients")
        ingredients_label.setFont(getFont("Bold", 14))
        ingredients_container.addWidget(ingredients_label)

        recipe_ingredients = recipe.ingredients.split(';')

        ingredients_list = "<ul>"
        for ingredient in recipe_ingredients:
            ingredients_list += f"<li>{ingredient.strip()}</li>"
        ingredients_list += "</ul>"

        recipe_ingredients_label = QtWidgets.QLabel()
        recipe_ingredients_label.setTextFormat(QtCore.Qt.RichText)
        recipe_ingredients_label.setText(ingredients_list)
        recipe_ingredients_label.setObjectName("recipe_ingredients")
        recipe_ingredients_label.setFont(getFont("Regular", 12))
        recipe_ingredients_label.setWordWrap(True)
        recipe_ingredients_label.setAlignment(QtCore.Qt.AlignJustify)

        ingredients_container.addWidget(recipe_ingredients_label)
        
        # UTENSILS
        utensils_container = QtWidgets.QVBoxLayout()
        utensils_label = QtWidgets.QLabel()
        utensils_label.setText("Utensils")
        utensils_label.setFont(getFont("Bold", 14))
        utensils_container.addWidget(utensils_label)

        recipe_utensils = recipe.utensils.split(',')

        utensils_list = "<ul>"
        for utensil in recipe_utensils:
            utensils_list += f"<li>{utensil.strip()}</li>"
        utensils_list += "</ul>"

        recipe_utensils_label = QtWidgets.QLabel()
        recipe_utensils_label.setTextFormat(QtCore.Qt.RichText)
        recipe_utensils_label.setText(utensils_list)
        recipe_utensils_label.setObjectName("recipe_utensils")
        recipe_utensils_label.setFont(getFont("Regular", 12))
        recipe_utensils_label.setWordWrap(True)
        recipe_utensils_label.setAlignment(QtCore.Qt.AlignJustify)

        utensils_container.addWidget(recipe_utensils_label)

        
        # Ingredients and utensils
        ing_utensils_container = QtWidgets.QHBoxLayout()
        ing_utensils_container.addLayout(ingredients_container)
        ing_utensils_container.addLayout(utensils_container)
        ing_utensils_container.setAlignment(QtCore.Qt.AlignTop)

        # STEPS
        steps_container = QtWidgets.QVBoxLayout()
        steps_label = QtWidgets.QLabel()
        steps_label.setText("Steps")
        steps_label.setFont(getFont("Bold", 14))
        steps_container.addWidget(steps_label)
        recipe_steps = QtWidgets.QLabel()
        recipe_steps.setText(recipe.steps)
        recipe_steps.setObjectName("recipe_steps")
        recipe_steps.setFont(getFont("Regular", 12))
        recipe_steps.setWordWrap(True)
        recipe_steps.setAlignment(QtCore.Qt.AlignJustify)
        steps_container.addWidget(recipe_steps)

        # LAYOUT
        self.layout = QtWidgets.QVBoxLayout(contentWidget)
        self.layout.addWidget(recipe_title)
        self.layout.addLayout(recipe_detail_container)
        self.layout.addWidget(recipe_image)
        self.layout.addLayout(ing_utensils_container)
        self.layout.addLayout(steps_container)

