from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import getFont

class FormTextBox(QtWidgets.QWidget):
    def __init__(self, placeholder, parent=None):
        super().__init__(parent)
        # Parent Size 
        parentWidth = parent.width()
        parentHeight = parent.height()
        self.setFixedWidth(int(0.5*parentWidth))
        self.setFixedHeight(int(0.1*parentHeight))



        # DECLARE TEXT BOX
        text_box = QtWidgets.QWidget()

        text_field = QtWidgets.QTextEdit(text_box)
        text_field.setPlaceholderText(placeholder)
        text_field.setFont(getFont("Regular", 11))
        text_field.setAlignment(QtCore.Qt.AlignVCenter)
        text_box.setFixedWidth(int(0.8 * self.width()))
        text_box.setFixedHeight(int(0.8 * self.height()))
        text_box.setObjectName("text_box")
        text_box.setStyleSheet("""
            #text_box { 
                padding-left: 15px; 
                border: none;
                border-radius: 15px;
            }
        """)

        # todo: fix styling for rounded, size
        
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(text_box)
        self.setLayout(self.layout)

        