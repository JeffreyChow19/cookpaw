from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import *

class BackButton(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
    
        # CREATE BACK BUTTON
        back_button = QtWidgets.QPushButton("< Back")
        back_button.setObjectName('back_button')
        back_button.setFont(getFont("Medium", 12))
        back_button.setStyleSheet("""
            #back_button{
                background-color: none;
                border: none;
                padding: 0px 10px;
                color:#FFCF52;
            }
        """)
        back_button.setCursor(QtCore.Qt.PointingHandCursor)
        
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(back_button)