from ui.utils import getFont
from ui.components.backbutton.back_button import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class ArticleDetail(QtWidgets.QWidget):
    def __init__(self, article, parent=None):
        super().__init__(parent)
        self.stacked_widget = parent.stacked_widget
        self.sidebar = parent.sidebar
        self.article = article

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        #set dashboard size
        self.setMinimumWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

        # SCROLL AREA
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)

        # CONTENT WIDGET
        contentWidget = QtWidgets.QWidget(scroll_area)
        contentWidget.setMinimumWidth(scroll_area.width())
        scroll_area.setWidget(contentWidget)

        # BACK
        back_button = BackButton(parent)
        back_button.clicked.connect(self.on_back_button_click)

        # TITLE
        article_title_container = QtWidgets.QHBoxLayout()
        article_title = QtWidgets.QLabel()
        article_title.setMinimumWidth(int(0.8*parentWidth))
        article_title.setText(self.article.title)
        article_title.setObjectName("article_title")
        article_title.setWordWrap(True)
        article_title.setFont(getFont("Bold", 24))
        article_title.setStyleSheet("#article_title{color: #29B067;}")
        article_title.setAlignment(QtCore.Qt.AlignCenter)
        article_title_container.addStretch()
        article_title_container.addWidget(article_title)
        article_title_container.addStretch()

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
        article_publish_date.setText(self.article.publish_date)
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
        pixmap = QtGui.QPixmap("assets/images/" + self.article.image_path)
        scaled_pixmap = pixmap.scaled(500, 375, QtCore.Qt.KeepAspectRatio)
        article_image.setPixmap(scaled_pixmap)
        article_image.setObjectName("article_image")
        article_image.setAlignment(QtCore.Qt.AlignCenter)

        # CONTENT
        article_content = QtWidgets.QLabel()
        article_content.setMaximumWidth(int(0.8*parentWidth))
        formatted_content = self.article.content.replace('\n', '\n         ')
        article_content.setText(formatted_content)
        article_content.setObjectName("article_content")
        article_content.setFont(getFont("Regular", 12))
        article_content.setWordWrap(True)
        article_content.setContentsMargins(0, 0, 0, 24)
        article_content.setAlignment(QtCore.Qt.AlignJustify)

        # LAYOUT
        content_layout = QtWidgets.QVBoxLayout(contentWidget)
        content_layout.setContentsMargins(0,0,0,0)
        content_layout.addWidget(back_button, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        content_layout.addLayout(article_title_container)
        content_layout.addLayout(article_detail_container)
        content_layout.addWidget(article_image, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        content_layout.addWidget(article_content, alignment=QtCore.Qt.AlignmentFlag.AlignHCenter)
        content_layout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(scroll_area)
        self.setLayout(self.layout)

    def update_article_detail(self, article):
        self.article = article

        # Update the title label
        self.findChild(QtWidgets.QLabel, "article_title").setText(self.article.title)

        # Update the author label
        self.findChild(QtWidgets.QLabel, "article_author").setText("Cookpaw\'s Team")

        # Update the publish date label
        self.findChild(QtWidgets.QLabel, "article_publish_date").setText(self.article.publish_date)

        # Update the image
        pixmap = QtGui.QPixmap("assets/images/" + self.article.image_path)
        scaled_pixmap = pixmap.scaled(500, 375, QtCore.Qt.KeepAspectRatio)
        self.findChild(QtWidgets.QLabel, "article_image").setPixmap(scaled_pixmap)

        # Update the content label
        formatted_content = self.article.content.replace('\n', '\n\n         ')
        self.findChild(QtWidgets.QLabel, "article_content").setText(formatted_content)

        # Redraw all widgets
        self.update()
    
    def on_back_button_click(self):
        self.stacked_widget.setCurrentIndex(2)
        self.update_sidebar("article_list_button")
    
    def update_sidebar(self, button_name):
        button = self.sidebar.findChild(QtWidgets.QPushButton, button_name)
        self.sidebar.on_button_clicked(button, True)