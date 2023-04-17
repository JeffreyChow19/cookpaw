from ui.components.card.recipe_card import *
from ui.components.card.article_card import *
from ui.components.searchbar.searchbar import *
from ui.components.collectionbutton.collection_button import *
from ui.components.cardscarousel.cards_carousel import *
from ui.utils import getFont
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class RecipeList(QtWidgets.QWidget):
    def __init__(self, recipes, parent=None):
        super().__init__(parent)

        self.stacked_widget = parent.stacked_widget
        self.recipes = recipes
        self.recipes_to_show = self.recipes

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        #set dashboard size
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

        ## HEADER ##
        # RECIPE LIST TITLE
        recipe_list_title = QtWidgets.QLabel()
        recipe_list_title.setFont(getFont("Bold", 32))
        recipe_list_title.setFixedHeight(int(0.06 * parentHeight))
        recipe_list_title.setText("Recipe's Collection")
        recipe_list_title.setObjectName("recipe_list_title")
        recipe_list_title.setStyleSheet("#recipe_list_title{color: #F15D36;}")
        recipe_list_title.setContentsMargins(int(0.04 * parentWidth), 0, 0, 0)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addStretch()
        self.layout.addWidget(recipe_list_title)

        # RECIPE COLLECTIONS AND SEARCH BAR
        cookpaw_collection_button = CollectionButton("Cookpaw's Collection", self)
        user_collection_button = CollectionButton("User's Collection", self)

        search_bar = SearchBar("Search Recipe Title", self)

        collection_search_container = QtWidgets.QHBoxLayout()
        collection_search_container.setContentsMargins(int(0.04 * parentWidth), 0, 0, 0)
        collection_search_container.addWidget(cookpaw_collection_button)
        collection_search_container.addWidget(user_collection_button)
        collection_search_container.addStretch()
        collection_search_container.addWidget(search_bar)

        self.layout.addLayout(collection_search_container)

        # RECIPE CARDS CAROUSEL
        self.recipe_carousel = CardsCarousel('recipe', self.recipes_to_show, 6, self)
        self.layout.addWidget(self.recipe_carousel)
        self.layout.addStretch()

        # ADD RECIPE BUTTON
        add_button = QtWidgets.QToolButton(self)
        add_button.setIcon(QtGui.QIcon("assets/icons/icon_add.svg"))
        add_button.setFixedWidth(int(0.085 *self.height()))
        add_button.setFixedHeight(int(0.085 *self.height()))
        add_button.setObjectName("add_button")
        add_button.setStyleSheet("""
            #add_button { 
                background-color: none; 
                border: none; 
            } 
        """)
        add_button.setIconSize(add_button.size())
        add_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        add_button.clicked.connect(self.on_add_button_clicked)
        
        # MOVE TO THE BOTTOM RIGHT
        add_button.move(self.width() - add_button.width(), int(0.8 * self.height()))

        # Raise the button to the top of the parent widget's stack
        add_button.raise_()

        self.setLayout(self.layout)
    
    def on_add_button_clicked(self):
        self.stacked_widget.setCurrentIndex(5)

    def update_content(self, search_query):
        self.recipes_to_show = [recipe for recipe in self.recipes if search_query.lower() in recipe.title.lower()]
        self.recipe_carousel.update_data(self.recipes_to_show)

   