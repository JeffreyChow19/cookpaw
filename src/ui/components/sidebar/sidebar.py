from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class Sidebar(QtWidgets.QWidget):
    def __init__(self,parent=None, stacked_widget=None):
        super().__init__(parent)

        # MAKE REFERENCE TO STACKED WIDGET
        self.stacked_widget = stacked_widget

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()
        
        # SET SIZE
        self.setFixedWidth(int(0.05 * parentWidth))
        self.setFixedHeight(parentHeight)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(int(0.02 * parentHeight))
    
        # ADD LOGO
        logo_path = "assets/icons/icon_logo.svg"
        logo_label = QtWidgets.QLabel()
        logo_image = QtGui.QPixmap.fromImage(QtGui.QImage(logo_path)).scaled(int(0.5 * self.width()), int(0.5 * self.width()))
        logo_label.setPixmap(logo_image)
        logo_label.setFixedHeight(int(0.1 * parentHeight))
        self.layout.addWidget(logo_label, alignment=QtCore.Qt.AlignCenter)  # add alignment to addWidget call
        self.layout.setAlignment(logo_label, QtCore.Qt.AlignCenter)  # set alignment of logo_label to center

        # ADD SIDEBAR BUTTON
        self.addSideBarButton("home", "assets/icons/icon_home.svg")
        self.addSideBarButton("recipe_list", "assets/icons/icon_recipe.svg")
        self.addSideBarButton("article_list", "assets/icons/icon_article.svg")

        spacerItem = QtWidgets.QSpacerItem(20, 330, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.layout.addItem(spacerItem)
        self.setLayout(self.layout)
    
    def addSideBarButton(self, button_name, icon_path):
        icon = self.qiconFromSvg(icon_path, "#F15D36", int(0.5 * self.width()))
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
        button.setIconSize(QtCore.QSize(int(0.5 * self.width()), int(0.5 * self.width())))
        button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        button.clicked.connect(lambda checked, button=button: self.on_button_clicked(button, checked))
        self.layout.addWidget(button, alignment=QtCore.Qt.AlignCenter)

    
    def on_button_clicked(self, button, checked):
        # SET ICON COLOR
        for i in range(self.layout.count()):
            widget = self.layout.itemAt(i).widget()
            if isinstance(widget, QtWidgets.QPushButton):
                icon = self.qiconFromSvg(widget.icon_path, "#F15D36" if widget == button and checked else "#8C92AB", int(0.5 * self.width()))

                widget.setIcon(icon)
        
        # SET STACKED WIDGET PAGE
        if self.stacked_widget is not None:
            # SET DEFAULT TO HOME PAGE
            index = 0

            # IF ANOTHER BUTTON CLICKED
            if button.button_name == "recipe_list":
                index = 1
            elif button.button_name == "article_list":
                index = 2

            self.stacked_widget.setCurrentIndex(index)
        self.update()
    
    def qiconFromSvg(self, svg_filepath, color, size):
        img = QtGui.QPixmap(svg_filepath).scaled(size, size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        qp = QtGui.QPainter(img)
        qp.setCompositionMode(QtGui.QPainter.CompositionMode_SourceIn)
        qp.fillRect(img.rect(), QtGui.QColor(color))
        qp.end()
        return QtGui.QIcon(img)

