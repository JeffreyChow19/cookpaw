from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import getFont

class ArticleCard(QtWidgets.QWidget):
    """
    This is a card component for articles.
    """
    def __init__(self, index, width, article, parent=None):
        """
        image_path: the path of the image
        index: the index (relative to the list the article is in)
        width: the width of the screen
        article_title: article title
        artice_content: article content
        """
        self.article = article
        article_title = article.title
        article_content = article.content
        
        super().__init__(parent)

        self.stacked_widget = parent.stacked_widget
        
        # CARD SIZE
        height = int(0.75 * width)

        self.setFixedHeight(height)
        self.setFixedWidth(width)
        
        self.article_image = QtWidgets.QLabel()
        self.article_image.setPixmap(QtGui.QPixmap("assets/images/"+self.article.image_path))
        self.article_image.setObjectName("article_image_" + str(index))
        self.article_image.setMargin(0)
        self.article_image.setFixedWidth(width)
        self.article_image.setScaledContents(True)
        # Make article_image clickable
        self.article_image.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.article_image.mousePressEvent = self.handle_article_title_image_clicked
        
        self.article_title = QtWidgets.QPushButton()
        self.article_title.setFont(getFont("Bold", 14))
        self.article_title.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        if(len(article_title)>28):
            article_title = article_title[:28]+"..."
        self.article_title.setText(article_title)
        self.article_title.setObjectName("article_title_" + str(index))
        self.article_title.setStyleSheet("#article_title_" + str(index) + """{
            text-align:left; 
            background-color: transparent;
            padding-left: 12px;
            color: #29B067;
        }""")
        # Connect the clicked signal of the article_title button to a slot
        self.article_title.clicked.connect(self.handle_article_title_image_clicked)

        self.article_desc = QtWidgets.QLabel()
        article_content = article_content.lstrip('\n')
        if(len(article_content)>50):
            article_content = article_content[:50]+"..."
        self.article_desc.setText(article_content)
        self.article_desc.setFont(getFont("Regular", 8))
        self.article_desc.setContentsMargins(12, 0, 0, 0)
        self.article_desc.setObjectName("article_desc")

        article_title_container = QtWidgets.QWidget()
        article_title_container.setFixedWidth(width)
        article_title_container.setObjectName("article_title_container_"+str(index))
        article_title_container.setStyleSheet("#article_title_container_"+str(index)+"""{
            background-color:white;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
            border-top-left-radius: 0;
            border-top-right-radius: 0;
        }""")
        article_title_container_layout = QtWidgets.QVBoxLayout()
        article_title_container_layout.addWidget(self.article_title)
        article_title_container_layout.addWidget(self.article_desc)
        article_title_container_layout.setSpacing(0)
        article_title_container.setLayout(article_title_container_layout)

        article_card_layout = QtWidgets.QVBoxLayout()
        article_card_layout.setContentsMargins(0, 0, 0, 0)
        article_card_layout.setSpacing(0)
        article_card_layout.addWidget(self.article_image)
        article_card_layout.addWidget(article_title_container)
        self.setLayout(article_card_layout)

    def handle_article_title_image_clicked(self, event):
        """
        Handle the click event for the article title and image.
        """
        print("Article title or image clicked!")
    
        self.stacked_widget.article_detail_widget.update_article_detail(self.article)
        self.stacked_widget.setCurrentIndex(3)
        # CHANGE STACKED WIDGET