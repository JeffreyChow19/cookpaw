from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg
from ui.utils import *

class CollectionButton(QtWidgets.QWidget):
    active_button = None

    def __init__(self, title, parent=None):
        super().__init__(parent)

        self.parent = parent
        self.title = title
        self.type = 'system' if 'cookpaw' in self.title.lower() else 'user'
        self.active = False

        self.active_stylesheet = """
            #collection_button { 
                text-align: center; 
                padding: 10px 25px;
                color: white;
                border-radius: 15px;
                background-color: #FFCF52;
            } 
        """
        self.passive_stylesheet = """
            #collection_button { 
                text-align: center; 
                padding: 10px 25px;
                color: #808080;
                border:none;
                border-radius: 15px;
                border-color: #808080;
                background-color: white;
            } 
            #collection_button:hover { 
                color: #FFCF52;
                border: 2px solid;
                border-color: #FFCF52;
            } 
        """ 

        # RECIPE COLLECTIONS AND SEARCH BAR
        self.collection_button = QtWidgets.QPushButton()
        self.collection_button.setFont(getFont("Regular", 11))
        self.collection_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.collection_button.setAutoFillBackground(False)
        self.collection_button.setText(title)
        self.collection_button.setObjectName("collection_button")
        self.collection_button.setStyleSheet(self.passive_stylesheet)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        self.collection_button.setSizePolicy(sizePolicy)
        self.collection_button.setFixedHeight(int(0.04 * parent.height()))
        self.collection_button.clicked.connect(self.on_clicked)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.collection_button)

    def on_clicked(self):
        # Check if the button is already active
        if self.active:
            CollectionButton.active_button = None
            self.active = False
            self.collection_button.setStyleSheet(self.passive_stylesheet)
            self.parent.update_content_by_author('')
            return

        # Deactivate the current active button
        if CollectionButton.active_button is not None:
            CollectionButton.active_button.active = False
            CollectionButton.active_button.collection_button.setStyleSheet(self.passive_stylesheet)

        # Set this button to be active and update the active_button attribute
        self.active = True
        CollectionButton.active_button = self
        self.collection_button.setStyleSheet(self.active_stylesheet)

        self.parent.update_content_by_author(self.type)

        
    
