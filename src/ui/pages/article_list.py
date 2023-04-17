from ui.components.card.recipe_card import *
from ui.components.card.article_card import *
from ui.components.searchbar.searchbar import *
from ui.components.collectionbutton.collection_button import *
from ui.components.cardscarousel.cards_carousel import *
from ui.utils import getFont
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class ArticleList(QtWidgets.QWidget):
    def __init__(self, articles, parent=None):
        super().__init__(parent)

        self.stacked_widget = parent.stacked_widget
        self.articles = articles
        self.articles_to_show = self.articles

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        #set dashboard size
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addStretch()
        
        ## HEADER ##
        # ARTICLE LIST TITLE
        article_list_title = QtWidgets.QLabel()
        article_list_title.setFont(getFont("Bold", 32))
        article_list_title.setFixedHeight(int(0.06 * parentHeight))
        article_list_title.setText("Article's Collection")
        article_list_title.setObjectName("article_list_title")
        article_list_title.setStyleSheet("#article_list_title{color: #29B067;}")

        # SEARCH BAR
        search_bar = SearchBar("Search Article Title", self)

        title_search_container = QtWidgets.QHBoxLayout()
        title_search_container.setContentsMargins(int(0.04 * parentWidth), 0, 0, 0)
        title_search_container.addWidget(article_list_title)
        title_search_container.addStretch()
        title_search_container.addWidget(search_bar)

        self.layout.addLayout(title_search_container)

        # ARTICLE CARDS
        self.article_carousel = CardsCarousel('article', self.articles_to_show, 6, self)
        self.layout.addWidget(self.article_carousel)
        self.layout.addStretch()

        self.setLayout(self.layout)

    def update_content(self, search_query):
        self.articles_to_show = [article for article in self.articles if search_query.lower() in article.title.lower()]
        self.article_carousel.update_data(self.articles_to_show)
   