from PyQt5 import QtWidgets, QtCore
from ui.components.textbox.textbox import *
import math

class FormQuestion(QtWidgets.QWidget):
    def __init__(self, title_text, placeholder, required, parent=None):
        super().__init__(parent)

        # SET WIDTH & REQUIRED
        self.setFixedWidth(parent.width())
        self.required = required

        # SET QUESTION TITLE
        self.question_title = QtWidgets.QLabel()
        self.question_title.setFont(getFont("Bold", 20))
        self.question_title.setFixedHeight(int(0.06 * parent.height()))
        if required is True:
            title_text += "*"
        self.question_title.setText(title_text)
        self.question_title.setObjectName("question_title")
        self.question_title.setStyleSheet("#question_title {color: #1E202C;}")
        self.question_title.setContentsMargins(0, 0, 0, 0)

        # SET QUESTION FIELD
        self.question_text_field = TextBox(placeholder, parent)

        # SET HEIGHT
        self.setFixedHeight(
            self.question_title.height() + self.question_text_field.height()
        )

        # CREATE MAIN LAYOUT
        self.layout = QtWidgets.QGridLayout()
        self.layout.addWidget(self.question_title, 0, 0, 1, 1)
        self.layout.addWidget(self.question_text_field, 1, 0, 1, 1)
        self.layout.setContentsMargins(0, 0, 0, 2)

        # todo: required flag

        self.setLayout(self.layout)
       