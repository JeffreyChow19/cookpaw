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
        self.parent = parent
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
        recipe_list_title.setText("Recipes Collection")
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
        add_button.setText("+")
        add_button.setFont(getFont("Medium", 20))
        add_button.setFixedWidth(int(0.085 *self.height()))
        add_button.setFixedHeight(int(0.085 *self.height()))
        add_button.setObjectName("add_button")
        add_button.setStyleSheet("""
            #add_button {
                color: white;
                text-align: center; 
                padding-top: 8px;
                background-color: #FFCF52; 
                border: none; 
                border-radius:40px;
            } 
            #add_button:hover{
                background-color: #F15D36; 
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
        self.parent.last_page_index = 1
        self.stacked_widget.setCurrentIndex(6)

    def update_content_by_title(self, search_query):
        if CollectionButton.active_button is not None:
            self.recipes_to_show = self.get_content_by_author(CollectionButton.active_button.type)
            self.recipes_to_show = [recipe for recipe in self.recipes_to_show if search_query.lower() in recipe.title.lower()]
        else :
            self.recipes_to_show = [recipe for recipe in self.recipes if search_query.lower() in recipe.title.lower()]
        self.recipe_carousel.update_data(self.recipes_to_show)
    
    def update_content_by_author(self, author):
        self.recipes_to_show = self.get_content_by_author(author)
        self.recipe_carousel.update_data(self.recipes_to_show)
    
    def get_content_by_author(self, author):
        return [recipe for recipe in self.recipes if author.lower() in recipe.author.lower()]
   