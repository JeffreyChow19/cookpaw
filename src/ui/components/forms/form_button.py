from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import *

class FormButton(QtWidgets.QWidget):
    def __init__(self, title, button_type, parent=None):
        super().__init__(parent)

        # SET WIDTH & REQUIRED
        self.setFixedWidth(int(0.9*parent.width()))

        self.button_container = QtWidgets.QHBoxLayout()

        if(button_type == "submit"):
            # RECIPE COLLECTIONS AND SEARCH BAR
            form_button = QtWidgets.QPushButton()
            form_button.setFont(getFont("Bold", 11))
            form_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            form_button.setAutoFillBackground(False)
            form_button.setText(title)
            form_button.setObjectName("form_button")
            form_button.setStyleSheet( """
                #form_button { 
                    text-align: center; 
                    color: black;
                    border: none;
                    border-radius: 15px;
                    background-color: #FFCF52;
                } 
            """)
            form_button.setFixedHeight(int(0.06 * parent.height()))
            form_button.setFixedWidth(int(0.4 * parent.width()))
        else:
            # RECIPE COLLECTIONS AND SEARCH BAR
            form_button = QtWidgets.QPushButton()
            attach_logo_path = "assets/icons/icon_attach.svg"
            form_button.setIcon(QtGui.QIcon(attach_logo_path))
            form_button.setFont(getFont("Bold", 11))
            form_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            form_button.setAutoFillBackground(False)
            form_button.setText(title)
            form_button.setObjectName("form_button")
            form_button.setStyleSheet( """
                #form_button { 
                    text-align: center; 
                    color: black;
                    border: none;
                    border-radius: 15px;
                    background-color: #FFCF52;
                } 
            """)
            form_button.setFixedHeight(int(0.06 * parent.height()))
            form_button.setFixedWidth(int(0.2 * parent.width()))

        self.button_container.addStretch()
        self.button_container.addWidget(form_button)
        self.button_container.addStretch()

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 10, 0, 0)
        self.layout.addLayout(self.button_container)