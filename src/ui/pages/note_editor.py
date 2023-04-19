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
    def __init__(self, editor_mode, note_data, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.stacked_widget = parent.stacked_widget
        # PARENT SIZE
        parentWidth = parent.width()
        parentHeight = parent.height()

        # Set dashboard size
        self.setFixedWidth(int(0.9 * parentWidth))
        self.setFixedHeight(parentHeight)
        self.file_name=""

        # SCROLL AREA
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)

        # CONTENT WIDGET
        content_widget = QtWidgets.QWidget(scroll_area)
        content_widget.setMinimumWidth(scroll_area.width())
        scroll_area.setWidget(content_widget)

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
        note_editor_title = QtWidgets.QLabel()
        note_editor_title.setFont(getFont("Bold", 24))
        note_editor_title.setFixedHeight(int(0.06 * parentHeight))
            
        note_editor_title.setObjectName("note_editor_title")
        note_editor_title.setStyleSheet("#note_editor_title{color: #F15D36;}")
        note_editor_title.setContentsMargins(int(0.04 * parentWidth), 0, 0, 0)
        title_container.addStretch()
        title_container.addWidget(note_editor_title)
        title_container.addStretch()
        
        self.note_title = FormQuestion("Note Title", "Write note title", True, parent)
        self.note_text = FormQuestion("Notes", "Write Something..", False, parent, height_=0.3)

        if editor_mode == "input":
            note_editor_title.setText("Input Your Note")
            submit_button = FormButton("Add Note", "submit", parent=parent)
        else:
            note_editor_title.setText("Edit Your Note")
            submit_button = FormButton("Save Changes", "submit", parent=parent)
        
        # FORM CONTAINER
        ## FORM QUESTIONS ##
        form_container.addWidget(self.note_title)
        form_container.addWidget(self.note_text)

        ## FORM BUTTONS ##
        upload_photos_button = FormButton("Upload Photos", "upload", parent=parent)
        
        upload_photos_button.setFixedWidth(int(0.7*parentWidth))

        # IMAGE
        self.note_image = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap("assets/images/empty.jpg")
        scaled_pixmap = pixmap.scaled(400, 300, QtCore.Qt.KeepAspectRatio)
        self.note_image.setPixmap(scaled_pixmap)
        self.note_image.setObjectName("note_image")
        self.note_image.setAlignment(QtCore.Qt.AlignCenter)

        # PHOTO CONTAINER
        photo_container = QtWidgets.QHBoxLayout()
        self.photo_file_title = QtWidgets.QLabel()
        self.photo_file_title.setFont(getFont("Bold", 12))
        self.photo_file_title.setFixedHeight(int(0.06 * parent.height()))
        self.photo_file_title.setFixedWidth(upload_photos_button.width())
        self.photo_file_title.setText("No File Selected")
        self.photo_file_title.setObjectName("photo_file_title")
        self.photo_file_title.setStyleSheet("#photo_file_title {color: #1E202C;}")
        self.photo_file_title.setContentsMargins(40, 10, 0, 0)
        self.photo_changed = False
        
        if editor_mode =="input":
            submit_button.form_button.clicked.connect(self.handle_add_notes)
        else:
            submit_button.form_button.clicked.connect(self.handle_edit_notes)
        upload_photos_button.form_button.clicked.connect(self.handle_upload_photo)

        photo_container.addWidget(upload_photos_button)
        photo_container.addWidget(self.photo_file_title)
        buttons_container.addLayout(photo_container)
        buttons_container.addStretch()
        buttons_container.addWidget(submit_button)

        self.layout.addLayout(header_container)
        self.layout.addLayout(title_container)

        content_layout = QtWidgets.QVBoxLayout(content_widget)
        content_layout.setObjectName("content_layout")
        content_layout.addLayout(form_container)
        content_layout.addWidget(self.note_image)
        content_layout.addLayout(buttons_container)
        content_layout = self.findChild(QtWidgets.QVBoxLayout, "content_layout")

        self.layout.addWidget(scroll_area)

        self.setLayout(self.layout)


    def handle_upload_photo(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Upload Image', '', 'Image files (*.jpg *.png *.gif);;All files (*.*)')
        if file_path == "":     # return if file dialog is cancelled
            return

        self.file_name = file_path
        self.photo_file_title.setText(Path(self.file_name).name)
        self.photo_changed = True
        pixmapNew = QtGui.QPixmap(file_path)
        scaled_pixmapNew = pixmapNew.scaled(400,300, QtCore.Qt.KeepAspectRatio)
        self.note_image.setPixmap(scaled_pixmapNew)

    def on_back_button_click(self):
        self.stacked_widget.setCurrentIndex(4)
    
    def update_edit_notes(self, note:Note):
        self.note = note
        self.last_page_index = self.parent.last_page_index
        self.note_title.question_text_field.text_field.setText(note.note_title)
        self.note_text.question_text_field.text_field.setText(note.note_content)
        if (len(note.image_paths)>0):
            self.photo_file_title.setText(note.image_paths[-1][13:])
            pixmap = QtGui.QPixmap("assets/images/"+note.image_paths[-1])
            scaled_pixmap = pixmap.scaled(400,300, QtCore.Qt.KeepAspectRatio)
            self.note_image.setPixmap(scaled_pixmap)
        else:
            self.photo_file_title.setText("No File Selected")
            pixmap = QtGui.QPixmap("assets/images/empty.jpg")
            scaled_pixmap = pixmap.scaled(400,300, QtCore.Qt.KeepAspectRatio)
            self.note_image.setPixmap(scaled_pixmap)
    
    def set_recipe_id(self, recipe_id):
        self.recipe_id = recipe_id

    def handle_add_notes(self):
        note = {
            "title" : (self.note_title.question_text_field.text_field.toPlainText()),
            "content" : (self.note_text.question_text_field.text_field.toPlainText()),
            "recipe_id" : self.recipe_id
        }

        if(note["title"]==""):
            err_msg_box = MessageBox("FAILED!", "Failed To Add Note!", False)
            err_msg_box.message_label.setStyleSheet("color: #F15D36")
            err_msg_box.exec_()
            return
        
        controller = Controller("src/database/cookpaw.db")
        note_id = controller.add_note(note)
        if (self.file_name!=""):
            self.image_path = save_image_to_assets(self.file_name, "notes")
            note_photo = {
                "note_id" : note_id,
                "path" : 'images_notes/'+ os.path.basename(self.file_name)
            }
            controller.add_note_photo(note_photo)
        
        msgBox = MessageBox("Success!", f"NOTE {note['title']} SUCCESSFULLY SAVED!", False)
        msgBox.exec_()

        # RELOAD DATA FROM DB
        CollectionButton.active_button = None
        self.parent.refresh_after_recipe_added()
        self.parent.sidebar.update_sidebar(1)
        c = self.parent.controller
        updated_recipe = c.get_recipe_by_id(self.recipe_id)
        self.parent.stacked_widget.recipe_detail_widget.update_recipe_detail(updated_recipe)
        self.parent.stacked_widget.setCurrentIndex(4)
    
    def handle_edit_notes(self):
        new_note = {
            "title" : (self.note_title.question_text_field.text_field.toPlainText()),
            "content" : (self.note_text.question_text_field.text_field.toPlainText()),
            "note_id" : self.note.note_id
        }

        if(new_note["title"]==""):
            err_msg_box = MessageBox("FAILED!", "Failed To Save Changes!", False, "Note title cannot be empty!")
            err_msg_box.message_label.setStyleSheet("color: #F15D36")
            err_msg_box.exec_()
            return
        
        controller = self.parent.controller
        note_id = controller.update_note(new_note)
        if (self.file_name!=""):
            self.image_path = save_image_to_assets(self.file_name, "notes")
            note_photo = {
                "note_id" : note_id,
                "path" : 'images_notes/'+ os.path.basename(self.file_name)
            }
            if len(self.note.image_paths) > 0:
                if (note_photo["path"] != self.note.image_paths[-1]):
                    controller.add_note_photo(note_photo)
            else:
                controller.add_note_photo(note_photo)
        
        msgBox = MessageBox("Success!", f"NOTE {new_note['title']} SUCCESSFULLY EDITED!", False)
        msgBox.exec_()

        # RELOAD DATA FROM DB
        CollectionButton.active_button = None
        self.parent.refresh_after_recipe_added()
        self.parent.sidebar.update_sidebar(1)
        c = self.parent.controller
        updated_recipe = c.get_recipe_by_id(self.note.recipe_id)
        self.parent.stacked_widget.recipe_detail_widget.update_recipe_detail(updated_recipe)
        self.parent.stacked_widget.setCurrentIndex(4)
