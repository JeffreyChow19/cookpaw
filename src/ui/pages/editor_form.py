from ui.components.card.recipe_card import *
from ui.components.card.article_card import *
from ui.components.searchbar.searchbar import *
from ui.components.collectionbutton.collection_button import *
from ui.components.cardscarousel.cards_carousel import *
from ui.utils import getFont
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

from ui.components.textbox.textbox import *
from ui.components.forms.form_question import *
from ui.components.forms.form_button import *
from ui.components.backbutton.back_button import *

class EditorForm(QtWidgets.QWidget):
    """

    demo page for textbox

    """
    def __init__(self, parent=None):
        super().__init__(parent)

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        # Set dashboard size
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

        # LAYOUT
        self.layout = QtWidgets.QVBoxLayout()
        header_container = QtWidgets.QHBoxLayout()
        title_container = QtWidgets.QHBoxLayout()
        form_container = QtWidgets.QVBoxLayout()
        buttons_container = QtWidgets.QVBoxLayout()

        # BACK BUTTON CONTAINER
        back_button = BackButton(parent)
        header_container.addWidget(back_button)
        header_container.addStretch()


        ## FORM HEADER ##
        editor_form_title = QtWidgets.QLabel()
        editor_form_title.setFont(getFont("Bold", 32))
        editor_form_title.setFixedHeight(int(0.06 * parentHeight))
        editor_form_title.setText("Editor Form")
        editor_form_title.setObjectName("editor_form_title")
        editor_form_title.setStyleSheet("#editor_form_title{color: #F15D36;}")
        editor_form_title.setContentsMargins(int(0.04 * parentWidth), 0, 0, 0)
        title_container.addStretch()
        title_container.addWidget(editor_form_title)
        title_container.addStretch()

        # FORM CONTAINER
        ## FORM QUESTIONS ##
        question1 = FormQuestion("My Question", "Write Something..", True, parent)
        question2 = FormQuestion("My Question 2", "Also Write Something..", False, parent)
        form_container.addWidget(question1)
        form_container.addWidget(question2)

        ## FORM BUTTONS ##
        upload_photos_button = FormButton("Upload Photos", 0.2, parent=parent)
        submit_button = FormButton("Submit", 0.4, parent=parent)
        buttons_container.addWidget(upload_photos_button)
        buttons_container.addWidget(submit_button)


        self.layout.addLayout(header_container)
        self.layout.addLayout(title_container)
        self.layout.addLayout(form_container)
        self.layout.addLayout(buttons_container)
        self.layout.addStretch()

        self.setLayout(self.layout)

   