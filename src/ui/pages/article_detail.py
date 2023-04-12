from ui.utils import getFont
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class ArticleDetail(QtWidgets.QWidget):
    def __init__(self, article, parent=None):
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
        article_title = QtWidgets.QLabel()
        article_title.setText(article.title)
        article_title.setObjectName("article_title")
        article_title.setFont(getFont("Bold", 24))
        article_title.setStyleSheet("#article_title{color: #29B067;}")
        article_title.setAlignment(QtCore.Qt.AlignCenter)

        # AUTHOR
        author_container = QtWidgets.QHBoxLayout()
        author_logo_path = "assets/icons/icon_author.svg"
        author_logo_widget = QtSvg.QSvgWidget(author_logo_path, parent=self)
        author_logo_widget.setFixedSize(32, 32)
        author_container.addWidget(author_logo_widget, alignment=QtCore.Qt.AlignCenter)
        article_author = QtWidgets.QLabel()
        article_author.setText("Cookpaw\'s Team")
        article_author.setObjectName("article_author")
        article_author.setFont(getFont("Regular", 10))
        author_container.addWidget(article_author)

        # PUBLISH DATE
        publish_date_container = QtWidgets.QHBoxLayout()
        publish_date_logo_path = "assets/icons/icon_time.svg"
        publish_date_logo_widget = QtSvg.QSvgWidget(publish_date_logo_path, parent=self)
        publish_date_logo_widget.setFixedSize(32, 32)
        publish_date_container.addWidget(publish_date_logo_widget, alignment=QtCore.Qt.AlignCenter)
        article_publish_date = QtWidgets.QLabel()
        article_publish_date.setText(article.publish_date)
        article_publish_date.setObjectName("article_publish_date")
        article_publish_date.setFont(getFont("Regular", 10))
        publish_date_container.addWidget(article_publish_date)

        # ARTICLE DETAIL
        article_detail_container = QtWidgets.QHBoxLayout()
        article_detail_container.addStretch()
        article_detail_container.addLayout(author_container)
        article_detail_container.addLayout(publish_date_container)
        article_detail_container.addStretch()

        # IMAGE
        article_image = QtWidgets.QLabel()
        article_image.setPixmap(QtGui.QPixmap("assets/images/" + article.image_path))
        article_image.setObjectName("article_image")
        article_image.setAlignment(QtCore.Qt.AlignCenter)

        # CONTENT
        article_content = QtWidgets.QLabel()
        article_content.setText(article.content)
        article_content.setObjectName("article_content")
        article_content.setFont(getFont("Regular", 12))
        article_content.setWordWrap(True)
        article_content.setAlignment(QtCore.Qt.AlignJustify)

        # LAYOUT
        self.layout = QtWidgets.QVBoxLayout(contentWidget)
        self.layout.addWidget(article_title)
        self.layout.addLayout(article_detail_container)
        self.layout.addWidget(article_image)
        self.layout.addWidget(article_content)

        self.setLayout(self.layout)