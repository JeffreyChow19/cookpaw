from PyQt5 import QtCore, QtGui, QtWidgets

class Sidebar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("sidebar")
        self.setGeometry(QtCore.QRect(0, 0, 71, 1081))
        self.setStyleSheet("#sidebar {\n"
                            "    background: #FFFFFF;\n"
                            "    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.25);\n"
                            "}")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)

        logo = QtWidgets.QLabel(self)
        logo.setAlignment(QtCore.Qt.AlignCenter)
        logo.setObjectName("logo")
        self.verticalLayout.addWidget(logo)

        self.addSideBarButton("home", "")

        self.addSideBarButton("recipe", "")

        self.addSideBarButton("article", "")

        spacerItem = QtWidgets.QSpacerItem(20, 330, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
    
    def addSideBarButton(self, button_name, icon_path):
        button = QtWidgets.QPushButton(self)
        button.setObjectName(button_name + "_button")
        button.setStyleSheet("#" + button_name + "_button {\n"
                              "    background: transparent;\n"
                              "}")
        icon = QtGui.QIcon(icon_path)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(32, 32))
        self.verticalLayout.addWidget(button)

