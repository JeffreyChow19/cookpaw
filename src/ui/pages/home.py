from ui.components.card.recipe_card import *
from ui.components.card.article_card import *
from ui.components.cardscarousel.cards_carousel import *
from ui.utils import getFont
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class Home(QtWidgets.QWidget):
    def __init__(self,articles, recipes, parent=None):
        super().__init__(parent)

        # MAKE REFERENCE TO SIDEBAR AND STACKED WIDGET
        self.sidebar = parent.sidebar
        self.stacked_widget = parent.stacked_widget
        self.last_page_index = parent.last_page_index
        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        #set dashboard size
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(int(0.04 * parentWidth), 0, 0, 0)
        self.layout.addStretch()

        ## HEADER ##
        # home title
        home_title = QtWidgets.QLabel()
        home_title.setFont(getFont("Bold", 28))
        home_title.setFixedHeight(int(0.053 * parentHeight))
        home_title.setText("Welcome to CookPaw!")
        home_title.setObjectName("home_title")
        home_title.setStyleSheet("#home_title{color: #FFCF52;}")

        self.layout.addWidget(home_title)

        ## RECIPE SECTION ##
        # recipe heading #
        recipe_heading = QtWidgets.QLabel()
        recipe_heading.setFont(getFont("Bold", 20))
        recipe_heading.setObjectName("recipe_heading")
        recipe_heading.setStyleSheet("#recipe_heading{color: #F15D36;}")
        recipe_heading.setText("Check out our latest recipe collection")

        # see all recipe #
        see_all_recipe_button = QtWidgets.QPushButton()
        see_all_recipe_button.setFont(getFont("Bold", 12))
        see_all_recipe_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        see_all_recipe_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        see_all_recipe_button.setAutoFillBackground(False)
        see_all_recipe_button.setText("See All Recipes")
        see_all_recipe_button.setObjectName("see_all_recipe_button")
        see_all_recipe_button.setStyleSheet("""
            #see_all_recipe_button{
                color:#F15D36;
                background-color:transparent;
            }
            #see_all_recipe_button:hover{
                color:#b52100;
            }
        """)
        see_all_recipe_button.clicked.connect(self.on_see_all_recipes_clicked)

        ## RECIPE LAYOUT
        recipe_layout = QtWidgets.QVBoxLayout()

        recipe_heading_layout = QtWidgets.QHBoxLayout()
        recipe_heading_layout.addWidget(recipe_heading)
        recipe_heading_layout.addStretch()
        recipe_heading_layout.addWidget(see_all_recipe_button)
        recipe_layout.addLayout(recipe_heading_layout)

        recipe_carousel = CardsCarousel('recipe', recipes, 3, self)
        recipe_layout.addWidget(recipe_carousel)

        self.layout.addLayout(recipe_layout)
        
        ## ARTICLE SECTION ##
        # article heading #
        article_heading = QtWidgets.QLabel()
        article_heading.setFont(getFont("Bold", 20))
        article_heading.setObjectName("article_heading")
        article_heading.setStyleSheet("#article_heading{color: #29B067;}")
        article_heading.setText("Check out our latest article collection")

        # see all article #
        see_all_article_button = QtWidgets.QPushButton()
        see_all_article_button.setFont(getFont("Bold", 12))
        see_all_article_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        see_all_article_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        see_all_article_button.setAutoFillBackground(False)
        see_all_article_button.setText("See All Articles")
        see_all_article_button.setObjectName("see_all_article_button")
        see_all_article_button.setStyleSheet("""
            #see_all_article_button{
                color:#29B067;
                background-color:transparent;
            }
            #see_all_article_button:hover{
                color:#00742b;
            }
        """)
        see_all_article_button.clicked.connect(self.on_see_all_articles_clicked)

        ## ARTICLE LAYOUT   
        article_layout = QtWidgets.QVBoxLayout()

        article_heading_layout = QtWidgets.QHBoxLayout()
        article_heading_layout.addWidget(article_heading)
        article_heading_layout.addStretch()
        article_heading_layout.addWidget(see_all_article_button)
        article_layout.addLayout(article_heading_layout)

        article_carousel = CardsCarousel('article', articles, 3, self)
        article_layout.addWidget(article_carousel)

        self.layout.addLayout(article_layout)
        self.layout.addStretch()

        self.setLayout(self.layout)
    
    def on_see_all_articles_clicked(self):
        self.stacked_widget.setCurrentIndex(2)
        self.sidebar.update_sidebar(2)

    def on_see_all_recipes_clicked(self):
        self.stacked_widget.setCurrentIndex(1)
        self.sidebar.update_sidebar(1)
    
   