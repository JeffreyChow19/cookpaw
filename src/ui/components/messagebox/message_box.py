from PyQt5 import QtWidgets, QtGui, QtCore
from ui.utils import *

class MessageBox(QtWidgets.QDialog):
    def __init__(self, title, message, warning, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowTitle(title)

        # Create the message label
        self.message_label = QtWidgets.QLabel(message)
        self.message_label.setFont(getFont('Bold', 14))
        self.message_label.setContentsMargins(0,50,0,50)
        self.message_label.setStyleSheet("color: #29B067;")
        self.message_label.setAlignment(QtCore.Qt.AlignCenter)
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
        layout.addWidget(self.message_label)
        if(warning):
            # Create the cancel button
            self.message_label.setStyleSheet("color: #F15D36;")
            option_layout = QtWidgets.QHBoxLayout()
            ok_button.setText("YES")
            ok_button.clicked.connect(self.on_yes_button_click)
            cancel_button = QtWidgets.QPushButton("CANCEL")
            cancel_button.clicked.connect(self.accept)
            cancel_button.setFont(getFont('Bold', 14))
            cancel_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            cancel_button.setStyleSheet("""
                QPushButton {
                    border: 2px solid #FFA500;
                    border-radius: 20px;
                    background-color: white;
                    padding: 10px 0;
                }

                QPushButton:hover {
                    background-color: #D8AA2E;
                }
            """)
            option_layout.addWidget((ok_button))
            option_layout.addWidget(cancel_button)
            layout.addLayout(option_layout)
        else:
            layout.addWidget(ok_button)

        layout.setContentsMargins(50, 20, 50, 20)
        self.setLayout(layout)
    
    def on_yes_button_click(self):
        self.parent.msg_box_resp = True
        self.accept()
