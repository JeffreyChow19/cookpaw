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

class NoteEditor(QtWidgets.QWidget):
    def __init__(self, note_data=None, parent=None):
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
        note_editor_title = QtWidgets.QLabel()
        note_editor_title.setFont(getFont("Bold", 24))
        note_editor_title.setFixedHeight(int(0.06 * parentHeight))
        if note_data is None:
            note_editor_title.setText("Input Your Notes")
        else:
            note_editor_title.setText("Edit Your Notes")
            # todo: logic for editting existing note
            
        note_editor_title.setObjectName("note_editor_title")
        note_editor_title.setStyleSheet("#note_editor_title{color: #F15D36;}")
        note_editor_title.setContentsMargins(int(0.04 * parentWidth), 0, 0, 0)
        title_container.addStretch()
        title_container.addWidget(note_editor_title)
        title_container.addStretch()

        # FORM CONTAINER
        ## FORM QUESTIONS ##
        question1 = FormQuestion("Note Title", "Write note title", True, parent)
        question2 = FormQuestion("Notes", "Write Something..", False, parent)
        form_container.addWidget(question1)
        form_container.addWidget(question2)

        ## FORM BUTTONS ##
        upload_photos_button = FormButton("Upload Photos", "upload", parent=parent)
        submit_button = FormButton("Submit", "submit", parent=parent)
        upload_photos_button.setFixedWidth(int(0.7*parentWidth))
        buttons_container.addStretch()
        buttons_container.addWidget(upload_photos_button, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        buttons_container.addWidget(submit_button)


        self.layout.addLayout(header_container)
        self.layout.addLayout(title_container)
        self.layout.addLayout(form_container)
        self.layout.addLayout(buttons_container)
        self.layout.addStretch()

        self.setLayout(self.layout)

   