from ui.components.card.recipe_card import *
from ui.components.card.article_card import *
from ui.components.searchbar.searchbar import *
from ui.components.collectionbutton.collection_button import *
from ui.components.cardscarousel.cards_carousel import *
from ui.components.messagebox.message_box import *
from ui.utils import getFont
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

from ui.components.textbox.textbox import *
from ui.components.forms.form_question import *
from ui.components.forms.form_button import *
from ui.components.backbutton.back_button import *
from controller.controller import *

from models.recipe import *

from pathlib import Path 


class RecipeEditor(QtWidgets.QWidget):
    def __init__(self, editor_mode, recipe_data : Recipe, parent=None):
        super().__init__(parent)
        
        self.parent = parent
        self.recipe_data = recipe_data

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        # Set dashboard size
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

        # SCROLL AREA
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)

        # CONTENT WIDGET
        content_widget = QtWidgets.QWidget(scroll_area)
        content_widget.setMinimumWidth(scroll_area.width())
        scroll_area.setWidget(content_widget)

        self.file_name = ""
        self.stacked_widget = parent.stacked_widget
        # LAYOUT
        self.layout = QtWidgets.QVBoxLayout()
        header_container = QtWidgets.QHBoxLayout()
        title_container = QtWidgets.QHBoxLayout()
        form_container = QtWidgets.QVBoxLayout()
        buttons_container = QtWidgets.QVBoxLayout()

        # BACK BUTTON CONTAINER
        back_button = BackButton(parent)
        back_button.clicked.connect(self.on_back_button_click)
        header_container.addWidget(back_button)
        header_container.addStretch()

        ## FORM HEADER ##
        recipe_editor_title = QtWidgets.QLabel()
        recipe_editor_title.setFont(getFont("Bold", 24))
        recipe_editor_title.setFixedHeight(int(0.06 * parentHeight))

        recipe_editor_title.setObjectName("editor_form_title")
        recipe_editor_title.setStyleSheet("#editor_form_title{color: #F15D36;}")
        recipe_editor_title.setContentsMargins(int(0.04 * parentWidth), 0, 0, 0)
        title_container.addStretch()
        title_container.addWidget(recipe_editor_title)
        title_container.addStretch()
        
        # SET PLACEHOLDER TEXT AND UPLOAD PHOTOS BUTTON
        self.recipe_title = FormQuestion("Recipe Title", "Recipe Title e.g. Crispy Pork Belly", True, parent)
        self.utensils = FormQuestion("Utensils", "Utensils e.g. Large skillet, wooden spoon, cutting board", True, parent, height_=0.15)
        self.ingredients = FormQuestion("Ingredients", "Ingredients e.g. 1 lb boneless chicken thighs; 1 cup fresh basil leaves;", True, parent,height_=0.2)
        self.steps = FormQuestion("Steps", "Steps e.g. 1. Heat the stock in a medium pot and keep it at a simmer. \n2. In a large pot, heat olive oil over medium heat.", True, parent, height_=0.2)
        upload_photos_button = FormButton("Upload Photos", "upload", parent=parent)
    
        if editor_mode =="input":
            recipe_editor_title.setText("Input Your Recipe")
            submit_button = FormButton("Add Recipe", "submit", parent=parent)
            self.edit_mode = False

        else:
            recipe_editor_title.setText("Edit Your Recipe")
            submit_button = FormButton("Save Changes", "submit", parent=parent)
            self.edit_mode = True

            # LOAD RECIPE TO EDITOR
            self.load_recipe(recipe_data)
        
        # FORM CONTAINER
        ## FORM QUESTIONS ##
        form_container.addWidget(self.recipe_title)
        form_container.addWidget(self.utensils)
        form_container.addWidget(self.ingredients)
        form_container.addWidget(self.steps)

        ## FORM BUTTONS ##
        photo_container = QtWidgets.QHBoxLayout()
        self.photo_file_title = QtWidgets.QLabel()
        self.photo_file_title.setFont(getFont("Bold", 12))
        self.photo_file_title.setFixedHeight(int(0.06 * parent.height()))
        self.photo_file_title.setFixedWidth(upload_photos_button.width())
        self.photo_file_title.setText("No File Selected")
        self.photo_file_title.setObjectName("photo_file_title")
        self.photo_file_title.setStyleSheet("#photo_file_title {color: #1E202C;}")
        self.photo_file_title.setContentsMargins(int(0.035*parent.width()), 10, 0, 0)

        submit_button.form_button.clicked.connect(self.handle_save_recipe)
        upload_photos_button.form_button.clicked.connect(self.handle_upload_photo)

        upload_photos_button.setFixedWidth(int(0.7*parentWidth))
       
        # IMAGE
        self.image_container = QtWidgets.QHBoxLayout()
        self.recipe_image = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("assets/images/empty.jpg")
        scaled_pixmap = pixmap.scaled(int(0.7*self.parent.width()),300, QtCore.Qt.KeepAspectRatio)
        self.recipe_image.setPixmap(scaled_pixmap)
        self.recipe_image.setObjectName("recipe_image")
        self.recipe_image.setAlignment(QtCore.Qt.AlignCenter)
        self.image_container.addStretch(100)
        self.image_container.addWidget(self.recipe_image)
        self.image_container.addStretch(88)

        # PHOTO CONTAINER
        photo_container.addWidget(upload_photos_button)
        photo_container.addWidget(self.photo_file_title)
        buttons_container.addLayout(photo_container)
        buttons_container.addWidget(submit_button)
        
        # CONTENT LAYOUT
        content_layout = QtWidgets.QVBoxLayout(content_widget)
        content_layout.setObjectName("content_layout")
        self.layout.addLayout(header_container)
        self.layout.addLayout(title_container)
        content_layout.addLayout(form_container)
        content_layout.addLayout(self.image_container)
        content_layout.addLayout(buttons_container)
        content_layout = self.findChild(QtWidgets.QVBoxLayout, "content_layout")

        self.layout.addWidget(scroll_area)

        self.setLayout(self.layout)

    def handle_save_recipe(self):
        recipe = {
            "title" : (self.recipe_title.question_text_field.text_field.toPlainText()),
            "utensils" : (self.utensils.question_text_field.text_field.toPlainText()),
            "ingredients" : (self.ingredients.question_text_field.text_field.toPlainText()),
            "steps" : (self.steps.question_text_field.text_field.toPlainText())
        }

        if(recipe["title"]=="" or recipe["utensils"] =="" or recipe["ingredients"]=="" or recipe["steps"]==""):
            err_msg = "Failed To Add Recipe!" if self.edit_mode is False else "Failed To Save Changes!"
            caption=""
            if(recipe["title"]==""):
                caption+="Recipe title can't be empty!\n"
            if(recipe["utensils"]==""):
                caption+="Utensils can't be empty!\n"
            if(recipe["ingredients"]==""):
                caption+="Ingredients can't be empty!\n"
            if(recipe["steps"]==""):
                caption+="Steps can't be empty!\n"
            err_msg_box = MessageBox("FAILED!", err_msg, False, caption)
            err_msg_box.message_label.setStyleSheet("color: #F15D36")
            err_msg_box.exec_()
            return

        controller = self.parent.controller
        if self.edit_mode is False:
            recipe_id = controller.create_user_recipe(recipe)
        else:
            recipe_id = controller.update_recipe(self.recipe_data.recipe_id, recipe)

        if (self.file_name!=""):
            self.image_path = save_image_to_assets(self.file_name, "recipe")
            recipe_photo = {
                "recipe_id" : recipe_id,
                "path" : 'images_recipe/'+ os.path.basename(self.file_name)
            }
            controller.add_recipe_photo(recipe_photo)
        
        msg_action = "SAVED" if self.edit_mode is False else "EDITED"
        msg_box = MessageBox("Success!", f"RECIPE {recipe['title']} SUCCESSFULLY {msg_action}!", False)
        msg_box.exec_()

        # RELOAD DATA FROM DB
        CollectionButton.active_button = None
        self.parent.refresh_after_recipe_added()
        self.parent.sidebar.update_sidebar(1)
        c = self.parent.controller
        updated_recipe = c.get_recipe_by_id(recipe_id)
        self.parent.stacked_widget.recipe_detail_widget.update_recipe_detail(updated_recipe)
        self.parent.stacked_widget.setCurrentIndex(4)
        
    
    def handle_upload_photo(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image files (*.jpg *.png *.gif);;All files (*.*)')
        if file_path == "":     # return if file dialog is cancelled
            return

        self.file_name = file_path
        self.photo_file_title.setText(Path(self.file_name).name)
        pixmapNew = QtGui.QPixmap(file_path)
        scaled_pixmapNew = pixmapNew.scaled(int(0.7*self.parent.width()),300, QtCore.Qt.KeepAspectRatio)
        self.recipe_image.setPixmap(scaled_pixmapNew)
        # to do handle update carousel
    
    def on_back_button_click(self):
        self.stacked_widget.setCurrentIndex(self.parent.last_page_index)
    
    def load_recipe(self, recipe_data):
        self.recipe_data = recipe_data

        # LOAD EXISTING DATA TO TEXTBOXES
        if self.recipe_data is not None:
            self.recipe_title.question_text_field.text_field.setText(self.recipe_data.title)
            self.utensils.question_text_field.text_field.setText(self.recipe_data.utensils)
            self.ingredients.question_text_field.text_field.setText(self.recipe_data.ingredients)
            self.steps.question_text_field.text_field.setText(self.recipe_data.steps)

            if (recipe_data.image_path != "empty.jpg"):
                self.photo_file_title.setText(recipe_data.image_path[14:])
                pixmap = QtGui.QPixmap("assets/images/"+recipe_data.image_path)
                scaled_pixmap = pixmap.scaled(int(0.7*self.parent.width()),300, QtCore.Qt.KeepAspectRatio)
                self.recipe_image.setPixmap(scaled_pixmap)
            else:
                self.photo_file_title.setText("No File Selected")
                pixmap = QtGui.QPixmap("assets/images/empty.jpg")
                scaled_pixmap = pixmap.scaled(int(0.7*self.parent.width()),300, QtCore.Qt.KeepAspectRatio)
                self.recipe_image.setPixmap(scaled_pixmap)