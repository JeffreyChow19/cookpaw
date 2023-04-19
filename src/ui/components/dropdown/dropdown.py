from ui.utils import getFont
from PyQt5 import QtWidgets, QtGui, QtCore


class DropdownButton(QtWidgets.QWidget):
    def __init__(self, type: str, parent=None):
        super().__init__(parent)

        self.layout = QtWidgets.QHBoxLayout()

        # Dropdown button
        self.dropdown_button = QtWidgets.QPushButton()
        self.dropdown_button.setCursor(QtCore.Qt.PointingHandCursor)
        self.dropdown_button.setStyleSheet("QPushButton { border: none; background-color: transparent; }")
        icon_size = QtCore.QSize(32, 32)
        icon = QtGui.QIcon("img/icons/icon_union.svg")
        icon = icon.pixmap(icon_size)
        self.dropdown_button.setIcon(QtGui.QIcon(icon))
        self.dropdown_button.clicked.connect(self.show_menu)
        self.layout.addWidget(self.dropdown_button)

        # Options menu
        self.option_menu = QtWidgets.QMenu(self)
        self.option_menu.setFont(getFont("Medium", 10))
        self.option_menu.setStyleSheet("""
            QMenu {
                border: 1px solid #D9DDEA;
            }
            QMenu::item {
                background-color: white;
                color:black;
                padding: 5px 16px 5px 12px;
            }
            QMenu::icon {
                max-width: 16px;
                max-height: 16px;
                padding-left: 16px;
            }
            QMenu::item:hover, QMenu::item:selected { 
                background-color: #F5F5F5;
                color: black; }
        """)
        self.option_menu.setObjectName("option_menu")
        self.edit_option = QtWidgets.QAction(QtGui.QIcon("img/icons/icon_edit.svg"), "Edit" + " " +type, self)
        self.delete_option = QtWidgets.QAction(QtGui.QIcon("img/icons/icon_delete.svg"), "Delete"+ " " +type, self)
        self.edit_option.setObjectName("edit_" + type + "_option")
        self.delete_option.setObjectName("delete_" + type + "_option")
        self.option_menu.addAction(self.edit_option)
        self.option_menu.addAction(self.delete_option)

        self.setLayout(self.layout)

    def show_menu(self):
        pos = self.mapToGlobal(QtCore.QPoint(self.dropdown_button.width() - self.option_menu.width(), self.dropdown_button.height()))
        pos.setY(pos.y() + self.dropdown_button.height())
        self.option_menu.exec_(pos)
