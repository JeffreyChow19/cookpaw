from ui.components.card.recipe_card import *
from ui.components.card.article_card import *
from ui.components.searchbar.searchbar import *
from ui.components.collectionbutton.collection_button import *
from ui.components.cardscarousel.cards_carousel import *
from ui.utils import getFont
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

from ui.components.textbox.textbox import *

class EditorForm(QtWidgets.QWidget):
    """

    demo page for textbox

    """
    def __init__(self, parent=None):
        super().__init__(parent)

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        #set dashboard size
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

        ## HEADER ##
        editor_form_title = QtWidgets.QLabel()
        editor_form_title.setFont(getFont("Bold", 32))
        editor_form_title.setFixedHeight(int(0.06 * parentHeight))
        editor_form_title.setText("Editor Form")
        editor_form_title.setObjectName("editor_form_title")
        editor_form_title.setStyleSheet("#editor_form_title{color: #F15D36;}")
        editor_form_title.setContentsMargins(int(0.04 * parentWidth), 0, 0, 0)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addStretch()
        self.layout.addWidget(editor_form_title)

        # Form
        form = FormTextBox("test", parent)
        self.layout.addWidget(form)
        self.layout.addStretch()

        self.setLayout(self.layout)

   