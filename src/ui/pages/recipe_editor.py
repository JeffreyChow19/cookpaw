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

from pathlib import Path 

import shutil

class RecipeEditor(QtWidgets.QWidget):
    def __init__(self, type, recipe_data, parent=None):
        super().__init__(parent)
        
        self.parent = parent

        # to do : if recipe_data != None (artinya ini edit), show recipe data dlm textbox
        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        # Set dashboard size
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

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
        if type =="input":
            recipe_editor_title.setText("Input Your Recipe")
            self.recipe_title = FormQuestion("Recipe Title", "Recipe Title e.g. Crispy Pork Belly", True, parent)
            self.utensils = FormQuestion("Utensils", "Utensils e.g. Large skillet, wooden spoon, cutting board", True, parent)
            self.ingredients = FormQuestion("Ingredients", "Ingredients e.g. 1 lb boneless chicken thighs; 1 cup fresh basil leaves;", True, parent)
            self.steps = FormQuestion("Steps", "Steps e.g. 1. Heat the stock in a medium pot and keep it at a simmer. \n2. In a large pot, heat olive oil over medium heat.", True, parent)
        
            upload_photos_button = FormButton("Upload Photos", "upload", parent=parent)
            submit_button = FormButton("Add Recipe", "submit", parent=parent)

        else:
            recipe_editor_title.setText("Edit Your Recipe")
            self.recipe_title = FormQuestion("Recipe Title", "Recipe Title e.g. Crispy Pork Belly", True, parent)
            self.utensils = FormQuestion("Utensils", "Utensils e.g. Large skillet, wooden spoon, cutting board", True, parent)
            self.ingredients = FormQuestion("Ingredients", "Ingredients e.g. 1 lb boneless chicken thighs; 1 cup fresh basil leaves;", True, parent)
            self.steps = FormQuestion("Steps", "Steps e.g. 1. Heat the stock in a medium pot and keep it at a simmer. \n2. In a large pot, heat olive oil over medium heat.", True, parent)
            # todo: implement update existing recipe

            upload_photos_button = FormButton("Upload Photos", "upload", parent=parent)
            submit_button = FormButton("Save Changes", "submit", parent=parent)

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
        self.photo_file_title.setContentsMargins(20, 10, 0, 0)

        if (type=="input"):
            submit_button.form_button.clicked.connect(self.handle_add_recipe)
        else:
            submit_button.form_button.clicked.connect(self.handle_edit_recipe)
        upload_photos_button.form_button.clicked.connect(self.handle_upload_photo)

        upload_photos_button.setFixedWidth(int(0.7*parentWidth))
        photo_container.addWidget(upload_photos_button)
        photo_container.addWidget(self.photo_file_title)
        buttons_container.addLayout(photo_container)
        buttons_container.addWidget(submit_button)
        
        self.layout.addLayout(header_container)
        self.layout.addLayout(title_container)
        self.layout.addLayout(form_container)
        self.layout.addLayout(buttons_container)
        self.layout.addStretch()

        self.setLayout(self.layout)

    def handle_edit_recipe(self):
        recipe = {
            "title" : (self.recipe_title.question_text_field.text_field.toPlainText()),
            "utensils" : (self.utensils.question_text_field.text_field.toPlainText()),
            "ingredients" : (self.ingredients.question_text_field.text_field.toPlainText()),
            "steps" : (self.steps.question_text_field.text_field.toPlainText())
        }

        if(recipe["title"]=="" or recipe["utensils"] =="" or recipe["ingredients"]=="" or recipe["steps"]==""):
            err_msg_box = MessageBox("FAILED!", f"Failed To Save Changes!", False)
            err_msg_box.message_label.setStyleSheet("color: #F15D36")
            err_msg_box.exec_()
            return

        controller = self.parent.controller
        recipe_id = controller.create_user_recipe(recipe)
        if (self.file_name!=""):
            destination_path = 'assets/images/images_recipe/' + os.path.basename(self.file_name)
            print(destination_path)
            shutil.copy(self.file_name, destination_path)
            self.image_path = destination_path
            recipe_photo = {
                "recipe_id" : recipe_id,
                "path" : 'images_recipe/'+ os.path.basename(self.file_name)
            }
            controller.add_recipe_photo(recipe_photo)
        
        msg_box = MessageBox("Success!", f"RECIPE {recipe['title']} SUCCESSFULLY SAVED!", False)
        msg_box.exec_()

        # RELOAD DATA FROM DB
        self.parent.refresh_after_recipe_added()

        self.stacked_widget.setCurrentIndex(1)
    
    def handle_add_recipe(self):
        recipe = {
            "title" : (self.recipe_title.question_text_field.text_field.toPlainText()),
            "utensils" : (self.utensils.question_text_field.text_field.toPlainText()),
            "ingredients" : (self.ingredients.question_text_field.text_field.toPlainText()),
            "steps" : (self.steps.question_text_field.text_field.toPlainText())
        }

        if(recipe["title"]=="" or recipe["utensils"] =="" or recipe["ingredients"]=="" or recipe["steps"]==""):
            err_msg_box = MessageBox("FAILED!", f"Failed To Add Recipe!", False)
            err_msg_box.message_label.setStyleSheet("color: #F15D36")
            err_msg_box.exec_()
            return

        controller = self.parent.controller
        recipe_id = controller.create_user_recipe(recipe)
        if (self.file_name!=""):
            destination_path = 'assets/images/images_recipe/' + os.path.basename(self.file_name)
            print(destination_path)
            shutil.copy(self.file_name, destination_path)
            self.image_path = destination_path
            recipe_photo = {
                "recipe_id" : recipe_id,
                "path" : 'images_recipe/'+ os.path.basename(self.file_name)
            }
            controller.add_recipe_photo(recipe_photo)
        
        msg_box = MessageBox("Success!", f"RECIPE {recipe['title']} SUCCESSFULLY SAVED!", False)
        msg_box.exec_()

        # RELOAD DATA FROM DB
        self.parent.refresh_after_recipe_added()

        self.stacked_widget.setCurrentIndex(1)
        
    
    def handle_upload_photo(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image files (*.jpg *.png *.gif);;All files (*.*)')
        self.file_name = file_path
        self.photo_file_title.setText(Path(self.file_name).name)
        # to do handle update carousel
    
    def on_back_button_click(self):
        self.stacked_widget.setCurrentIndex(self.parent.last_page_index)

   