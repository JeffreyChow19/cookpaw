from PyQt5 import QtWidgets, QtCore
from ui.components.card.recipe_card import *
from ui.components.card.article_card import *
import math

class CardsCarousel(QtWidgets.QWidget):
    def __init__(self, type, data, num_show, parent=None):
        super().__init__(parent)

        self.stacked_widget = parent.stacked_widget

        # GET THE ITEMS DATA
        self.type = type
        self.data = data
        self.num_show = num_show
        self.setFixedWidth(parent.width())

        # CREATE THE DATA CARD LAYOUT
        self.data_card_widget = QtWidgets.QWidget()
        self.data_card_layout = QtWidgets.QGridLayout(self.data_card_widget)
        self.data_card_layout.setSpacing(50)
        self.data_card_layout.setContentsMargins(0, 0, 0, 0)
        if self.num_show > 3 :
            self.data_card_widget.setMinimumHeight(int(0.6 * parent.height()))

        # CREATE MAIN LAYOUT
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.data_card_widget)

        # SET CURRRENT PAGE
        self.current_page = 0

        # CREATE PAGINATION BUTTONS
        prev_button = QtWidgets.QPushButton("<")
        prev_button.setObjectName('prev_button')
        prev_button.setStyleSheet("""
            #prev_button{
                background-color: none;
                border: none;
                padding: 0px 10px;
                color:#FFCF52;
                font-weight: 900;
            }
        """)
        prev_button.setCursor(QtCore.Qt.PointingHandCursor)
        prev_button.clicked.connect(self.on_prev_button_clicked)

        next_button = QtWidgets.QPushButton(">")
        next_button.setObjectName('next_button')
        next_button.setStyleSheet("""
            #next_button{
                background-color: none;
                border: none;
                padding: 0 10px;
                color:#FFCF52;
                font-weight: 900;
            }
        """)
        next_button.setCursor(QtCore.Qt.PointingHandCursor)
        next_button.clicked.connect(self.on_next_button_clicked)

        # # CREATE LABEL TO DISPLAY CURRENT PAGE
        self.page_label = QtWidgets.QLabel()
        self.page_label.setFont(getFont('Bold', 12))
        self.page_label.setObjectName("page_label")
        self.page_label.setStyleSheet("""
            #page_label{
                color:#FFCF52;
            }
        """)
        self.update_page_label()

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(prev_button)
        button_layout.addWidget(self.page_label)
        button_layout.addWidget(next_button)
        button_layout.addStretch()
        button_layout.setContentsMargins(0, 0, 0, 0)
        
        self.layout.addLayout(button_layout)
        
        # UPDATE DISPLAYED DATA
        self.update_data()

        self.setLayout(self.layout)
       

    def update_data(self, data=None):
        if data is not None:
            self.data = data
            self.current_page = 0
            self.update_page_label()

        # CLEAR THE LAYOUT
        for i in reversed(range(self.data_card_layout.count())):
            self.data_card_layout.itemAt(i).widget().setParent(None)

        # ADD CURRENT DATA
        index_start = self.current_page * self.num_show
        index_end = ((self.current_page + 1) * self.num_show) if ((self.current_page + 1) * self.num_show) < len(self.data) else len(self.data)

        for i in range(index_start, index_end):
            if (self.type == 'recipe'):
                card = RecipeCard(i, int(0.8 * self.width() / 3), self.data[i], self)
            else :
                card = ArticleCard(i, int(0.8 * self.width() / 3), self.data[i], self)
            self.data_card_layout.addWidget(card, i // 3, i % 3, 1, 1)

    def on_prev_button_clicked(self):
        # GO TO PREVIOUS PAGE
        if self.current_page > 0:
            self.current_page -= 1
            self.update_data()
            self.update_page_label()

    def on_next_button_clicked(self):
        # GO TO NEXT PAGE
        if self.current_page < math.ceil(len(self.data) / self.num_show) - 1:
            self.current_page += 1
            self.update_data()
            self.update_page_label()

    def update_page_label(self):
        # UPDATE THE TEXT OF THE PAGE LABEL
        page_count = math.ceil(len(self.data) / self.num_show)
        self.page_label.setText(f"{self.current_page + 1} of {page_count if page_count != 0 else 1}")