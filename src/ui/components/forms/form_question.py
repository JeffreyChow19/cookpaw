from PyQt5 import QtWidgets, QtCore
from ui.components.textbox.textbox import *
import math

class FormQuestion(QtWidgets.QWidget):
    def __init__(self, title_text, placeholder, required, parent=None):
        super().__init__(parent)

        # SET WIDTH & REQUIRED
        self.setFixedWidth(parent.width())
        self.required = required

        # QUESTION CONTAINERS
        self.question_title_container = QtWidgets.QHBoxLayout()
        self.question_text_box_container = QtWidgets.QHBoxLayout()

        # SET QUESTION FIELD
        question_text_field = TextBox(placeholder, parent)
        self.question_text_box_container.addStretch()
        self.question_text_box_container.addWidget(question_text_field)
        self.question_text_box_container.addStretch()

        # SET QUESTION TITLE
        question_title = QtWidgets.QLabel()
        question_title.setFont(getFont("Bold", 12))
        question_title.setFixedHeight(int(0.06 * parent.height()))
        question_title.setFixedWidth(question_text_field.width())
        if required is True:
            title_text += "*"
        question_title.setText(title_text)
        question_title.setObjectName("question_title")
        question_title.setStyleSheet("#question_title {color: #1E202C;}")
        question_title.setContentsMargins(0, 0, 0, 0)

        self.question_title_container.addStretch()
        self.question_title_container.addWidget(question_title)
        self.question_title_container.addStretch()


        # SET HEIGHT
        self.setFixedHeight(
            question_title.height() + question_text_field.height()
        )

        # CREATE MAIN LAYOUT
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addLayout(self.question_title_container)
        self.layout.addLayout(self.question_text_box_container)
        self.layout.setContentsMargins(0, 0, 0, 2)

        # todo: required flag

        self.setLayout(self.layout)
       