import shutil
from ui.components.messagebox.message_box import MessageBox
from ui.components.card.recipe_card import *
from ui.components.card.article_card import *
from ui.components.searchbar.searchbar import *
from ui.components.collectionbutton.collection_button import *
from ui.components.cardscarousel.cards_carousel import *
from ui.utils import getFont
from PyQt5 import QtCore, QtGui, QtWidgets, QtSvg

from ui.components.textbox.textbox import *
from ui.components.forms.form_question import *
from ui.components.forms.form_button import *
from ui.components.backbutton.back_button import *
from controller.controller import *

from pathlib import Path 

class NoteEditor(QtWidgets.QWidget):
    def __init__(self, type, note_data, parent=None):
        super().__init__(parent)

        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        # Set dashboard size
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)

        # LAYOUT
        self.layout = QtWidgets.QVBoxLayout()
        header_container = QtWidgets.QHBoxLayout()
        title_container = QtWidgets.QHBoxLayout()
        form_container = QtWidgets.QVBoxLayout()
        buttons_container = QtWidgets.QVBoxLayout()

        # BACK BUTTON CONTAINER
        back_button = BackButton(parent)
        header_container.addWidget(back_button)
        header_container.addStretch()


        ## FORM HEADER ##
        note_editor_title = QtWidgets.QLabel()
        note_editor_title.setFont(getFont("Bold", 24))
        note_editor_title.setFixedHeight(int(0.06 * parentHeight))
            
        note_editor_title.setObjectName("note_editor_title")
        note_editor_title.setStyleSheet("#note_editor_title{color: #F15D36;}")
        note_editor_title.setContentsMargins(int(0.04 * parentWidth), 0, 0, 0)
        title_container.addStretch()
        title_container.addWidget(note_editor_title)
        title_container.addStretch()
        if type =="input":
            note_editor_title.setText("Input Your Notes")
            self.note_title = FormQuestion("Note Title", "Write note title", True, parent)
            self.note_text = FormQuestion("Notes", "Write Something..", False, parent)
            submit_button = FormButton("Add Notes", "submit", parent=parent)
        else:
            note_editor_title.setText("Edit Your Notes")
            self.note_title = FormQuestion("Note Title", "Write note title", True, parent)
            self.note_text = FormQuestion("Notes", "Write Something..", False, parent)
            submit_button = FormButton("Save Changes", "submit", parent=parent)
            # todo: logic for editting existing note

        # FORM CONTAINER
        ## FORM QUESTIONS ##
        form_container.addWidget(self.note_title)
        form_container.addWidget(self.note_text)

        ## FORM BUTTONS ##
        upload_photos_button = FormButton("Upload Photos", "upload", parent=parent)
        
        upload_photos_button.setFixedWidth(int(0.7*parentWidth))

        photo_container = QtWidgets.QHBoxLayout()
        self.photo_file_title = QtWidgets.QLabel()
        self.photo_file_title.setFont(getFont("Bold", 12))
        self.photo_file_title.setFixedHeight(int(0.06 * parent.height()))
        self.photo_file_title.setFixedWidth(upload_photos_button.width())
        self.photo_file_title.setText("No File Selected")
        self.photo_file_title.setObjectName("photo_file_title")
        self.photo_file_title.setStyleSheet("#photo_file_title {color: #1E202C;}")
        self.photo_file_title.setContentsMargins(20, 10, 0, 0)


        submit_button.form_button.clicked.connect(self.handle_add_notes)
        upload_photos_button.form_button.clicked.connect(self.handle_upload_photo)

        photo_container.addWidget(upload_photos_button)
        photo_container.addWidget(self.photo_file_title)
        buttons_container.addLayout(photo_container)
        buttons_container.addStretch()
        buttons_container.addWidget(submit_button)

        self.layout.addLayout(header_container)
        self.layout.addLayout(title_container)
        self.layout.addLayout(form_container)
        self.layout.addLayout(buttons_container)
        self.layout.addStretch()

        self.setLayout(self.layout)


    def handle_upload_photo(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image files (*.jpg *.png *.gif);;All files (*.*)')
        self.file_name = file_path
        self.photo_file_title.setText(Path(self.file_name).name)
        # to do handle update carousel
    
    def on_back_button_click(self):
        self.stacked_widget.setCurrentIndex(1)
   
    def handle_add_notes(self):
        note = {
            "title" : (self.note_title.question_text_field.text_field.toPlainText()),
            "content" : (self.note_text.question_text_field.text_field.toPlainText())
        }

        if(note["title"]==""):
            err_msg_box = MessageBox("FAILED!", f"Failed To Add Note!", False)
            err_msg_box.message_label.setStyleSheet("color: #F15D36")
            err_msg_box.exec_()
            return
        
        controller = Controller("src/database/cookpaw.db")
        note_id = controller.add_note(note)
        if (self.file_name!=""):
            destination_path = 'assets/images/images_notes/' + os.path.basename(self.file_name)
            print(destination_path)
            shutil.copy(self.file_name, destination_path)
            self.image_path = destination_path
            note_photo = {
                "note_id" : note_id,
                "path" : 'images_notes/'+ os.path.basename(self.file_name)
            }
            controller.add_note_photo(note_photo)
        
        msgBox = MessageBox("Success!", f"NOTE {note['title']} SUCCESSFULLY SAVED!")
        msgBox.exec_()

        # RELOAD DATA FROM DB
        self.parent.refresh_after_recipe_added()

        self.stacked_widget.setCurrentIndex(1)
    
    def handle_edit_notes(self):
        note = {
            "title" : (self.note_title.question_text_field.text_field.toPlainText()),
            "content" : (self.note_text.question_text_field.text_field.toPlainText())
        }

        if(note["title"]==""):
            err_msg_box = MessageBox("FAILED!", f"Failed To Add Note!", False)
            err_msg_box.message_label.setStyleSheet("color: #F15D36")
            err_msg_box.exec_()
            return
        
        controller = Controller("src/database/cookpaw.db")
        note_id = controller.add_note(note)
        if (self.file_name!=""):
            destination_path = 'assets/images/images_notes/' + os.path.basename(self.file_name)
            print(destination_path)
            shutil.copy(self.file_name, destination_path)
            self.image_path = destination_path
            note_photo = {
                "note_id" : note_id,
                "path" : 'images_notes/'+ os.path.basename(self.file_name)
            }
            controller.add_note_photo(note_photo)
        
        msgBox = MessageBox("Success!", f"NOTE {note['title']} SUCCESSFULLY SAVED!")
        msgBox.exec_()

        # RELOAD DATA FROM DB
        self.parent.refresh_after_recipe_added()

        self.stacked_widget.setCurrentIndex(1)