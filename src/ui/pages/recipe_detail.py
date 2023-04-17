from ui.utils import getFont
from controller.controller import *
from ui.components.dropdown.dropdown import *
from ui.components.backbutton.back_button import *
from ui.components.messagebox.message_box import *
from models.note import *
from models.recipe import *
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

class RecipeDetail(QtWidgets.QWidget):
    def __init__(self, recipe: Recipe, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.last_page_index = parent.last_page_index
        self.stacked_widget = parent.stacked_widget
        self.sidebar = parent.sidebar
        self.controller = parent.controller
        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        #set dashboard size
        self.setMinimumWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)
        self.recipe = recipe
        # SCROLL AREA
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)

        # CONTENT WIDGET
        content_widget = QtWidgets.QWidget(scroll_area)
        content_widget.setMinimumWidth(scroll_area.width())
        scroll_area.setWidget(content_widget)

        # HEAD BUTTONS
        back_button = BackButton()
        back_button.clicked.connect(self.on_back_button_click)
        head_button_container = QtWidgets.QHBoxLayout()
        head_button_container.addWidget(back_button)
        head_button_container.addStretch()
        if(recipe.author == "system"): # inget ubah jadi ! system
            recipe_dropdown = DropdownButton("recipe")
            head_button_container.addWidget(recipe_dropdown)
            recipe_dropdown.edit_option.triggered.connect(self.on_edit_recipe_clicked)
            recipe_dropdown.delete_option.triggered.connect(self.on_delete_recipe_clicked)

        # TITLE
        recipe_title = QtWidgets.QLabel()
        recipe_title.setText(recipe.title)
        recipe_title.setObjectName("recipe_title")
        recipe_title.setFont(getFont("Bold", 24))
        recipe_title.setStyleSheet("#recipe_title{color: #29B067;}")
        recipe_title.setAlignment(QtCore.Qt.AlignCenter)

        # AUTHOR
        author_container = QtWidgets.QHBoxLayout()
        author_logo_path = "assets/icons/icon_author.svg"
        author_logo_widget = QtSvg.QSvgWidget(author_logo_path, parent=self)
        author_logo_widget.setFixedSize(32, 32)
        author_container.addWidget(author_logo_widget, alignment=QtCore.Qt.AlignCenter)
        recipe_author = QtWidgets.QLabel()
        if recipe.author == "user":
            recipe_author.setText("User")
        else:
            recipe_author.setText("Cookpaw\'s Team")
        recipe_author.setObjectName("recipe_author")
        recipe_author.setFont(getFont("Regular", 10))
        author_container.addWidget(recipe_author)

        # LAST MODIFIED
        last_modified_container = QtWidgets.QHBoxLayout()
        last_modified_logo_path = "assets/icons/icon_time.svg"
        last_modified_logo_widget = QtSvg.QSvgWidget(last_modified_logo_path, parent=self)
        last_modified_logo_widget.setFixedSize(32, 32)
        last_modified_container.addWidget(last_modified_logo_widget, alignment=QtCore.Qt.AlignCenter)
        recipe_last_modified = QtWidgets.QLabel()
        recipe_last_modified.setText(recipe.last_modified)
        recipe_last_modified.setObjectName("recipe_last_modified")
        recipe_last_modified.setFont(getFont("Regular", 10))
        last_modified_container.addWidget(recipe_last_modified)

        # RECIPE DETAIL
        recipe_detail_container = QtWidgets.QHBoxLayout()
        recipe_detail_container.addStretch()
        recipe_detail_container.addLayout(author_container)
        recipe_detail_container.addLayout(last_modified_container)
        recipe_detail_container.addStretch()

        # IMAGE
        recipe_image = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("assets/images/" + recipe.image_path)
        scaled_pixmap = pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
        recipe_image.setPixmap(scaled_pixmap)
        recipe_image.setObjectName("recipe_image")
        recipe_image.setAlignment(QtCore.Qt.AlignCenter)

        # INGREDIENTS
        ingredients_container = QtWidgets.QVBoxLayout()
        ingredients_label = QtWidgets.QLabel()
        ingredients_label.setText("Ingredients")
        ingredients_label.setFont(getFont("Bold", 14))
        ingredients_container.addWidget(ingredients_label)

        if recipe.author == 'user':
            ingredients_list = recipe.ingredients
        else:
            recipe_ingredients = recipe.ingredients.split(';')
            ingredients_list = "<ul>"
            for ingredient in recipe_ingredients:
                ingredients_list += f"<li>{ingredient.strip()}</li>"
            ingredients_list += "</ul>"

        recipe_ingredients_label = QtWidgets.QLabel()
        recipe_ingredients_label.setTextFormat(QtCore.Qt.RichText)
        recipe_ingredients_label.setText(ingredients_list)
        recipe_ingredients_label.setObjectName("recipe_ingredients")
        recipe_ingredients_label.setFont(getFont("Regular", 12))
        recipe_ingredients_label.setWordWrap(True)
        recipe_ingredients_label.setAlignment(QtCore.Qt.AlignJustify)

        ingredients_container.addWidget(recipe_ingredients_label)
        
        # UTENSILS
        utensils_container = QtWidgets.QVBoxLayout()
        utensils_label = QtWidgets.QLabel()
        utensils_label.setText("Utensils")
        utensils_label.setFont(getFont("Bold", 14))
        utensils_container.addWidget(utensils_label)

        if recipe.author == 'user':
            utensils_list = recipe.utensils
        else:
            recipe_utensils = recipe.utensils.split(',')
            utensils_list = "<ul>"
            for utensil in recipe_utensils:
                utensils_list += f"<li>{utensil.strip()}</li>"
            utensils_list += "</ul>"

        recipe_utensils_label = QtWidgets.QLabel()
        recipe_utensils_label.setTextFormat(QtCore.Qt.RichText)
        recipe_utensils_label.setText(utensils_list)
        recipe_utensils_label.setObjectName("recipe_utensils")
        recipe_utensils_label.setFont(getFont("Regular", 12))
        recipe_utensils_label.setWordWrap(True)
        recipe_utensils_label.setAlignment(QtCore.Qt.AlignJustify)

        utensils_container.addWidget(recipe_utensils_label)

        
        # Ingredients and utensils
        ing_utensils_container = QtWidgets.QHBoxLayout()
        ing_utensils_container.addLayout(ingredients_container)
        ing_utensils_container.addLayout(utensils_container)
        ing_utensils_container.setAlignment(QtCore.Qt.AlignTop)

        # STEPS
        steps_container = QtWidgets.QVBoxLayout()
        steps_label = QtWidgets.QLabel()
        steps_label.setText("Steps")
        steps_label.setFont(getFont("Bold", 14))
        steps_container.addWidget(steps_label)
        recipe_steps = QtWidgets.QLabel()
        recipe_steps.setText(recipe.steps)
        recipe_steps.setObjectName("recipe_steps")
        recipe_steps.setFont(getFont("Regular", 12))
        recipe_steps.setWordWrap(True)
        recipe_steps.setAlignment(QtCore.Qt.AlignJustify)
        steps_container.addWidget(recipe_steps)

        # NOTEs
        notes_widget = QtWidgets.QWidget()
        notes_widget.setFixedWidth(int(0.8*parentWidth))
        notes_container = QtWidgets.QVBoxLayout(notes_widget)

        divider_line = QtWidgets.QFrame()
        divider_line.setFrameShape(QtWidgets.QFrame.VLine)
        divider_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        divider_line.setMinimumHeight(1)
        divider_line.setContentsMargins(0, 8, 0, 8)
        notes_container.addWidget(divider_line)

        notes = recipe.notes
        if len(notes) == 0:
            empty_notes = QtWidgets.QLabel()
            empty_notes.setText("You don\'t have any note yet for this recipe.")
            empty_notes.setFont(getFont("Regular", 14))
            notes_container.addWidget(empty_notes)
            notes_container.addWidget(divider_line)
        else:
            for i in range (len(notes)):
                notes_card = QtWidgets.QVBoxLayout()

                notes_title_container = QtWidgets.QHBoxLayout()
                notes_title = QtWidgets.QLabel()
                notes_title.setText(notes[i].note_title)
                notes_title.setFont(getFont("Bold", 12))
                notes_title_container.addWidget(notes_title)
                notes_title_container.addStretch()
                notes_dropdown = DropdownButton("note")
                notes_title_container.addWidget(notes_dropdown)
                notes_card.addLayout(notes_title_container)

                notes_content = QtWidgets.QLabel()
                notes_content.setText(notes[i].note_content)
                notes_content.setFont(getFont("Regular", 12))
                notes_content.setWordWrap(True)
                notes_content.setAlignment(QtCore.Qt.AlignJustify)
                notes_card.addWidget(notes_content)

                notes_published_container = QtWidgets.QHBoxLayout()
                notes_published_container.addStretch()
                notes_published_icon = QtSvg.QSvgWidget("assets/icons/icon_time.svg", parent=self)
                notes_published_icon.setFixedSize(24, 24)
                notes_published_container.addWidget(notes_published_icon, alignment=QtCore.Qt.AlignCenter)
                notes_published_time = QtWidgets.QLabel()
                notes_published_time.setText(notes[i].publish_date)
                notes_published_time.setFont(getFont("Regular", 10))
                notes_published_container.addWidget(notes_published_time)
                notes_card.addLayout(notes_published_container)

                notes_container.addLayout(notes_card)
                notes_container.addWidget(divider_line)

        # LAYOUT
        content_layout = QtWidgets.QVBoxLayout(content_widget)
        content_layout.addLayout(head_button_container)
        content_layout.addWidget(recipe_title)
        content_layout.addLayout(recipe_detail_container)
        content_layout.addWidget(recipe_image)
        content_layout.addLayout(ing_utensils_container)
        content_layout.addLayout(steps_container)
        content_layout.addWidget(notes_widget)
        # content_layout.addWidget()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(scroll_area)

        self.setLayout(self.layout)

    def on_back_button_click(self):
        self.stacked_widget.setCurrentIndex(self.last_page_index)
        self.sidebar.update_sidebar(self.last_page_index)
    
    def on_edit_recipe_clicked(self):
        self.stacked_widget.setCurrentIndex(7)
    
    def on_delete_recipe_clicked(self):
        self.msg_box_resp = False
        msg_box = MessageBox("Delete Recipe Confirmation", f"Are you sure you want to delete\n {self.recipe.title} from your recipes?", True, self)
        msg_box.exec_()
        # print(self.msg_box_resp)
        if(self.msg_box_resp):
            self.controller.delete_recipe(self.recipe.recipe_id)
            msg_box = MessageBox("Success!", f"SUCCESSFULLY DELETED \n {self.recipe.title} from recipes", False, self)
            msg_box.exec_()
            self.parent.refresh_after_recipe_added()
    
    def update_recipe_detail(self, recipe:Recipe):
        self.last_page_index = self.parent.last_page_index
        self.recipe = recipe
        # Update the title label
        self.findChild(QtWidgets.QLabel, "recipe_title").setText(recipe.title)

        # Update the author label
        if recipe.author == "user":
            self.findChild(QtWidgets.QLabel, "recipe_author").setText("User")
        else:
            self.findChild(QtWidgets.QLabel, "recipe_author").setText("Cookpaw\'s Team")

        # Update the publish date label
        self.findChild(QtWidgets.QLabel, "recipe_last_modified").setText(recipe.last_modified)

        # Update the image
        pixmap = QtGui.QPixmap("assets/images/" + recipe.image_path)
        scaled_pixmap = pixmap.scaled(500, 375, QtCore.Qt.KeepAspectRatio)
        self.findChild(QtWidgets.QLabel, "recipe_image").setPixmap(scaled_pixmap)

        if recipe.author == 'user':
            ingredients_list = recipe.ingredients
        else:
            recipe_ingredients = recipe.ingredients.split(';')
            ingredients_list = "<ul>"
            for ingredient in recipe_ingredients:
                ingredients_list += f"<li>{ingredient.strip()}</li>"
            ingredients_list += "</ul>"

        self.findChild(QtWidgets.QLabel, "recipe_ingredients").setText(ingredients_list)

        if recipe.author == 'user':
            utensils_list = recipe.utensils
        else:
            recipe_utensils = recipe.utensils.split(',')
            utensils_list = "<ul>"
            for utensil in recipe_utensils:
                utensils_list += f"<li>{utensil.strip()}</li>"
            utensils_list += "</ul>"

        self.findChild(QtWidgets.QLabel, "recipe_utensils").setText(utensils_list)

        self.findChild(QtWidgets.QLabel, "recipe_steps").setText(recipe.steps)

        # Redraw all widgets
        self.update()
