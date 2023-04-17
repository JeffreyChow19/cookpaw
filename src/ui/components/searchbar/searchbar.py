from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import getFont

class SearchBar(QtWidgets.QWidget):
    def __init__(self, placeholder, parent=None):
        super().__init__(parent)

        self.parent = parent

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        # SET SIZE
        self.setFixedWidth(int(0.25 * parentWidth))
        self.setFixedHeight(int(0.05 * parentHeight))

        # SEARCH FIELD
        search_field = QtWidgets.QLineEdit()
        search_field.setPlaceholderText(placeholder)
        search_field.setFont(getFont("Regular", 11))
        search_field.setAlignment(QtCore.Qt.AlignVCenter)
        search_field.setFixedWidth(int(0.8 * self.width()))
        search_field.setFixedHeight(int(0.8 *self.height()))
        search_field.setObjectName("search_field")
        search_field.setStyleSheet("""
            #search_field { 
                padding-left: 15px; 
                border: none;
                border-radius: 15px;
            }
        """)
        search_field.textChanged.connect(self.update_content_list)

        # SPACER BETWEEN SEARCH FIELD AND SEARCH BUTTON
        search_button = QtWidgets.QPushButton()
        search_icon = QtGui.QIcon("assets/icons/icon_search.svg")
        search_button.setIcon(search_icon)
        search_button.setFixedWidth(int(0.8 *self.height()))
        search_button.setFixedHeight(int(0.8 *self.height()))
        search_button.setObjectName("search_button")
        search_button.setStyleSheet("""
            #search_button { 
                background-color: none; 
                border: none; 
            } 
        """)
        search_button.setIconSize(search_button.size())
        search_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(search_field, 0, 0, 1, 1)
        self.layout.addWidget(search_button, 0, 1, 1, 1)

        self.setLayout(self.layout)

    def update_content_list(self, search_query):
        self.parent.update_content_by_title(search_query)

