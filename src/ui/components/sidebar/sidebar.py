from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class Sidebar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(60)
        self.setFixedHeight(900)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(20)
        self.addSideBarButton("home", "assets/icons/icon_home.svg")
        self.addSideBarButton("recipe", "assets/icons/icon_recipe.svg")
        self.addSideBarButton("article", "assets/icons/icon_article.svg")
        spacerItem = QtWidgets.QSpacerItem(20, 330, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout.addItem(spacerItem)
        self.setLayout(self.layout)
    
    def addSideBarButton(self, button_name, icon_path):
        icon = self.qiconFromSvg(icon_path, "#F15D36")
        button = QtWidgets.QPushButton()
        button.setObjectName(button_name + "_button")
        button.setStyleSheet("#" + button_name + "_button {\n"
                            "    background: transparent;\n"
                            "}")
        button.button_name = button_name
        button.icon_path = icon_path
        button.setIcon(icon)
        button.setCheckable(True)
        button.setAutoExclusive(True)
        button.setIconSize(QtCore.QSize(32, 32))
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.clicked.connect(lambda checked, button=button: self.on_button_clicked(button, checked))
        self.layout.addWidget(button, alignment=QtCore.Qt.AlignCenter)

    
    def on_button_clicked(self, button, checked):
        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                icon = self.qiconFromSvg(widget.icon_path, "#F15D36" if widget == button and checked else "#8C92AB")
                widget.setIcon(icon)
        self.update()
    
    def qiconFromSvg(self, svg_filepath, color):
        img = QtGui.QPixmap(svg_filepath)
        qp = QtGui.QPainter(img)
        qp.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        qp.fillRect( img.rect(), QtGui.QColor(color) )
        qp.end()
        return QtGui.QIcon(img)

