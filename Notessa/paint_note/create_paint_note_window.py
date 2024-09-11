import json, uuid

from PySide6.QtWidgets import QMainWindow, QWidget, QColorDialog, QSizePolicy, QLabel, QSpinBox, QPushButton, QDialog, QCheckBox, QInputDialog, QDateTimeEdit, QLineEdit
from PySide6.QtGui import QAction, QIcon, QUndoStack
from PySide6.QtCore import Qt, QSize, QPoint, QDateTime, QDir
from Notessa.paint_note.ui_gen.ui_create_paintnote_window import Ui_CreatePaintNoteWindow
from Notessa.paint_note.PaintingArea import PaintingArea
from Notessa.save_dialog.save_dialog import SaveDialog

from Notessa.resources.icons.button import button_icons_rc
from Notessa.resources.icons.note_type import note_type_icons_rc

from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.common_modules.forming_note_name import forming_note_file_name


class CreatePaintNoteWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_CreatePaintNoteWindow()
        self.ui.setupUi(self)

        self._parent = parent

        # self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.setWindowTitle('Create paint note')
        self.setWindowIcon(QIcon(':/note_type/paint.png'))

        # Set a default note deadline -
        self.note_deadline = 'None'

        # Save
        self.save_button = QPushButton(QIcon(':/button/save.png'), '', self.ui.toolbar)
        self.ui.toolbar.addWidget(self.save_button)

        # Spacer 1
        self.spacer1 = QWidget()
        self.spacer1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.ui.toolbar.addWidget(self.spacer1)

        # Set pen color
        self.pen_color_button = QPushButton(QIcon(':/button/colors.png'), '', self.ui.toolbar)
        self.ui.toolbar.addWidget(self.pen_color_button)

        # Set pen size
        self.pen_size_label = QLabel()
        self.pen_size_label.setText('Pen size:')
        self.ui.toolbar.addWidget(self.pen_size_label)

        self.pen_size_spinbox = QSpinBox()
        self.pen_size_spinbox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.pen_size_spinbox.setMinimumSize(QSize(75, 24))
        self.pen_size_spinbox.setMinimum(1)
        self.ui.toolbar.addWidget(self.pen_size_spinbox)

        # Spacer 2
        self.spacer2 = QWidget()
        self.spacer2.setMinimumWidth(40)
        self.spacer2.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.ui.toolbar.addWidget(self.spacer2)

        # Clip
        self.clip_button = QPushButton(QIcon(':/button/frame.png'), '', self.ui.toolbar)
        self.clip_button_checked = False
        self.clip_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.ui.toolbar.addWidget(self.clip_button)

        # Spacer 3
        self.spacer3 = QWidget()
        self.spacer3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.ui.toolbar.addWidget(self.spacer3)

        # Undo
        self.undo_button = QPushButton(QIcon(':/button/back.png'), '', self.ui.toolbar)
        self.ui.toolbar.addWidget(self.undo_button)

        # Redo
        self.redo_button = QPushButton(QIcon(':/button/forward.png'), '', self.ui.toolbar)
        self.ui.toolbar.addWidget(self.redo_button)

        # Spacer 4
        self.spacer4 = QWidget()
        self.spacer4.setMinimumWidth(40)
        self.spacer4.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.ui.toolbar.addWidget(self.spacer4)

        # Clear canvas
        self.clear_button = QPushButton(QIcon(':/button/garbage.png'), '', self.ui.toolbar)
        self.ui.toolbar.addWidget(self.clear_button)

        # Spacer 5
        self.spacer5 = QWidget()
        self.spacer5.setMinimumWidth(40)
        self.spacer5.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        self.ui.toolbar.addWidget(self.spacer5)

        # Note deadline
        # self.indefinite_checkbox = QCheckBox(self.ui.toolbar)
        # self.indefinite_checkbox.setText('Indefinite')
        # self.ui.toolbar.addWidget(self.indefinite_checkbox)
        #
        # self.note_date_time_edit = QDateTimeEdit(QDateTime.currentDateTime())
        # self.note_date_time_edit.setMinimumWidth(170)
        # self.ui.toolbar.addWidget(self.note_date_time_edit)

        # ----------------- Undo/Redo -----------------
        self.undoStack = QUndoStack(self)
        self.undoStack.setUndoLimit(30)

        # ======================== StatusBar settings ========================

        self.cursor_coordinates_label = QLabel()
        self.ui.statusbar.addWidget(self.cursor_coordinates_label)

        # Signal - slot

        self.save_button.clicked.connect(self.save)
        self.pen_color_button.clicked.connect(self.set_pen_color)
        self.clip_button.clicked.connect(self.clip_active_state_change)
        self.undo_button.clicked.connect(self.undo)
        self.redo_button.clicked.connect(self.redo)
        self.pen_size_spinbox.valueChanged.connect(self.set_pen_size)
        self.clear_button.clicked.connect(self.clear_canvas)
        # self.note_date_time_edit.dateTimeChanged.connect(self.select_date_time_change)
        # self.indefinite_checkbox.checkStateChanged.connect(self.indefinite_change)

    # def indefinite_change(self):
    #     if self.indefinite_checkbox.isChecked():
    #         self.note_deadline = 'None'
    #         self.note_date_time_edit.setDisabled(True)
    #     else:
    #         self.note_deadline = self.note_date_time_edit.dateTime().toLocalTime()
    #         self.note_date_time_edit.setEnabled(True)

    # def select_date_time_change(self):
    #     self.note_deadline = self.note_date_time_edit.dateTime().toLocalTime()

    def save(self):

        save_dialog = SaveDialog(self)
        _, note_name, deadline_datetime = save_dialog.exec()

        dir_checker = DirectoryChecker()

        file_name = forming_note_file_name('PaintNote')
        file_path = str(f"{dir_checker.paint_notes_directory()}{QDir.separator()}{file_name}.png")
        meta_data_file_path = str(f'{dir_checker.paint_notes_directory()}{QDir.separator()}{file_name}.json')

        self.ui.canvas.image.save(file_path)

        meta_data_content = {'note_name': note_name}

        if not deadline_datetime == "None":
            meta_data_content.update({'deadline': deadline_datetime.toString()})
        else:
            meta_data_content.update({'deadline': None})

        note_uuid = uuid.uuid1()
        meta_data_content.update({'uuid': f'{note_uuid}'})

        with open(meta_data_file_path, 'w', encoding='utf-8') as file:
            json.dump(meta_data_content, file, indent=4)

        self.clear_canvas()
        self.close()

    def set_pen_size(self):
        self.ui.canvas.pen_size = self.pen_size_spinbox.value()

    def set_pen_color(self):
        color_dialog = QColorDialog()
        color = color_dialog.getColor()
        if color.isValid():
            self.ui.canvas.pen_color = color

    def clip_active_state_change(self):
        if self.clip_button_checked:
            self.clip_button_checked = False
            self.ui.canvas.clip = False
            self.clip_button.setText('')
        else:
            self.clip_button_checked = True
            self.ui.canvas.clip = True
            self.clip_button.setText('✔')

    def undo(self):
        self.ui.canvas.undo()

    def redo(self):
        self.ui.canvas.redo()

    def clear_canvas(self):
        # Clear canvas
        self.ui.canvas.clear()

    def get_clip_button_state(self) -> bool:
        return self.clip_button_checked

    def showEvent(self, event):

        '''
        Until the issue of closing the note creation window and deleting it is resolved,
        this handler clears the canvas and sets the current time for the deadline.
        '''

        # self.note_date_time_edit.setDateTime(QDateTime.currentDateTime())
        self.ui.canvas.image.fill(Qt.GlobalColor.white)

    def closeEvent(self, *args):
        self._parent.update_view()
