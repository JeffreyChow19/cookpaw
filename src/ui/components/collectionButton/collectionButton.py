from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import *

class CollectionButton(QtWidgets.QWidget):
    def __init__(self, title, parent=None):
        super().__init__(parent)

        # RECIPE COLLECTIONS AND SEARCH BAR
        collection_button = QtWidgets.QPushButton()
        collection_button.setFont(getFont("Regular", 12))
        collection_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        collection_button.setAutoFillBackground(False)
        collection_button.setText(title)
        collection_button.setObjectName( "collection_button")
        collection_button.setStyleSheet( """
            #collection_button { 
                text-align: center; 
                padding: 10px 25px;
            } 
        """)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        collection_button.setSizePolicy(sizePolicy)
        collection_button.setFixedHeight(int(0.04 * parent.height()))

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(collection_button)