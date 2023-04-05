from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import getFont

class ArticleCard(QtWidgets.QWidget):
    def __init__(self, image_path, index, width, article_title, article_content, parent=None):
        super().__init__(parent)

        # CARD SIZE
        height = int(0.75 * width)

        self.setFixedHeight(height)
        self.setFixedWidth(width)
        
        self.article_image = QtWidgets.QLabel()
        self.article_image.setPixmap(QtGui.QPixmap(image_path))
        self.article_image.setObjectName("article_image_" + str(index))
        self.article_image.setMargin(0)
        self.article_image.setFixedWidth(width)
        self.article_image.setScaledContents(True)
        
        self.article_title = QtWidgets.QPushButton()
        self.article_title.setFont(getFont("Bold", 14))
        self.article_title.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        if(len(article_title)>28):
            article_title = article_title[:28]+"..."
        self.article_title.setText(article_title)
        self.article_title.setObjectName("article_title_" + str(index))
        self.article_title.setStyleSheet("#article_title_" + str(index) + "{text-align:left; background-color: transparent;padding-left: 20px;color: #29B067;}")
       
        self.article_desc = QtWidgets.QLabel()
        if(len(article_content)>50):
            article_content = article_content[:50]+"..."
        self.article_desc.setText(article_content)
        self.article_desc.setFont(getFont("Regular", 8))
        self.article_desc.setContentsMargins(20, 0, 0, 0)

        article_title_container = QtWidgets.QWidget()
        article_title_container.setFixedWidth(width)
        article_title_container.setObjectName("article_title_container_"+str(index))
        article_title_container.setStyleSheet("#article_title_container_"+str(index)+"{background-color:white;border-bottom-left-radius: 8px;border-bottom-right-radius: 8px;border-top-left-radius: 0;border-top-right-radius: 0;}")
        article_title_container_layout = QtWidgets.QVBoxLayout()
        article_title_container_layout.addWidget(self.article_title)
        article_title_container_layout.addWidget(self.article_desc)
        article_title_container_layout.setSpacing(0)
        article_title_container.setLayout(article_title_container_layout)

        article_card_layout = QtWidgets.QVBoxLayout()
        article_card_layout.setContentsMargins(5, 0, 5, 0)
        article_card_layout.setSpacing(0)
        article_card_layout.addWidget(self.article_image)
        article_card_layout.addWidget(article_title_container)
        self.setLayout(article_card_layout)