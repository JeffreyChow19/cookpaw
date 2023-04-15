from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import *

class BackButton(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
    
        # CREATE BACK BUTTON
        self.setText("< Back")
        self.setObjectName('back_button')
        self.setFont(getFont("Medium", 12))
        self.setStyleSheet("""
            #back_button{
                background-color: none;
                border: none;
                padding: 0px 10px;
                color:#FFCF52;
            }
        """)
        self.setCursor(QtCore.Qt.PointingHandCursor)
        
        # self.layout = QtWidgets.QHBoxLayout(self)
        # self.layout.setContentsMargins(0, 0, 0, 0)
        # self.layout.addWidget(back_button)