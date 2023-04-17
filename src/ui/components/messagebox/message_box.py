from PyQt5 import QtWidgets, QtGui, QtCore
from ui.utils import *

class MessageBox(QtWidgets.QDialog):
    def __init__(self, title, message, parent=None):
        super().__init__(parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle(title)

        # Create the message label
        message_label = QtWidgets.QLabel(message)
        message_label.setFont(getFont('Bold', 14))
        message_label.setContentsMargins(0,50,0,50)
        message_label.setStyleSheet("color: #29B067;")

        # Create the OK button
        ok_button = QtWidgets.QPushButton("OK")
        ok_button.setFont(getFont('Bold', 14))
        ok_button.clicked.connect(self.accept)
        ok_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        ok_button.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 20px;
                background-color: #FFCF52;
                padding: 10px 0;
            }

            QPushButton:hover {
                background-color: #D8AA2E;
            }
        """)

        # Create the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(message_label)
        layout.addWidget(ok_button)
        layout.setContentsMargins(50, 20, 50, 20)
        self.setLayout(layout)
