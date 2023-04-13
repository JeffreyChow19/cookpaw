from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import getFont

class TextBox(QtWidgets.QWidget):
    def __init__(self, placeholder, parent=None):
        super().__init__(parent)
        # Parent Size 
        parentWidth = parent.width()
        parentHeight = parent.height()
        self.setFixedWidth(int(0.5*parentWidth))
        self.setFixedHeight(int(0.1*parentHeight))

        # DECLARE TEXT BOX
        text_field = QtWidgets.QTextEdit()
        text_field.setPlaceholderText(placeholder)
        text_field.setFont(getFont("Regular", 11))
        text_field.setAlignment(QtCore.Qt.AlignVCenter)
        text_field.setFixedWidth(int(0.8 * self.width()))
        text_field.setFixedHeight(int(0.8 * self.height()))
        text_field.setObjectName("text_field")
        text_field.setStyleSheet("""
            #text_field { 
                padding-left: 15px; 
                border: 3px solid rgb(205,205,205);
                border-radius: 15px;
                background-color: palette(base);
            }
        """)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(text_field)
        self.setLayout(self.layout)
        