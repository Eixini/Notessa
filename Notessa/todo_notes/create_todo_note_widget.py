import json, uuid

from PySide6.QtCore import QDir, Qt, QDateTime
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from Notessa.todo_notes.ui_gen.ui_create_todo_note_widget import Ui_CreateTodoNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.common_modules.forming_note_name import forming_note_file_name


class CreateTodoNoteWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_CreateTodoNoteWidget()
        self.ui.setupUi(self)

        # Set a default note deadline -
        self.note_deadline = ' '

        # Default value
        self.ui.indefinite_checkbox.setChecked(True)
        self.ui.note_deadline_label.setDisabled(True)
        self.ui.note_date_time_edit.setDisabled(True)
        self.ui.note_date_time_edit.setDateTime(QDateTime.currentDateTime())

        self._parent = parent

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self.ui.note_item_lineedit.setFocus()

        self.ui.note_items_list_widget.setWordWrap(True)
        self.ui.note_items_list_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Signal - Slot
        self.ui.add_item_button.clicked.connect(self.add_note_item)
        self.ui.delete_button.clicked.connect(self.delete_note_item)
        self.ui.save_button.clicked.connect(self.save_note)
        self.ui.indefinite_checkbox.checkStateChanged.connect(self.indefinite_change)
        self.ui.note_date_time_edit.dateTimeChanged.connect(self.select_date_time_change)

    def indefinite_change(self):
        if self.ui.indefinite_checkbox.isChecked():
            self.note_deadline = ' '
            self.ui.note_deadline_label.setDisabled(True)
            self.ui.note_date_time_edit.setDisabled(True)
        else:
            self.note_deadline = self.ui.note_date_time_edit.dateTime().toLocalTime()
            self.ui.note_deadline_label.setEnabled(True)
            self.ui.note_date_time_edit.setEnabled(True)

    def select_date_time_change(self):
        self.note_deadline = self.ui.note_date_time_edit.dateTime().toLocalTime()
        print(self.ui.note_date_time_edit.dateTime().toLocalTime())

    def add_note_item(self):
        if not self.ui.note_item_lineedit.text() == '':
            self.ui.note_items_list_widget.addItem(self.ui.note_item_lineedit.text())
            self.ui.note_item_lineedit.clear()

    def delete_note_item(self):
        items = self.ui.note_items_list_widget.selectedItems()
        if not items:
            return
        for item in items:
            self.ui.note_items_list_widget.takeItem(self.ui.note_items_list_widget.row(item))

    def save_note(self):
        if self.date_time_check() == 'Correct' or self.date_time_check() == 'None':
            dir_checker = DirectoryChecker()

            note_name = self.ui.todo_note_name_lineedit.text()
            file_name = forming_note_file_name('TodoNote')

            file_path = str(f"{dir_checker.todo_notes_directory()}{QDir.separator()}{file_name}.json")

            json_data = dict()

            item_list = list()
            for it in range(self.ui.note_items_list_widget.count()):
                item_list.append((self.ui.note_items_list_widget.item(it).text(), False))

            json_data.update({'note_data': item_list})

            # Meta-data
            meta_data = {'note_name': note_name}


            if not self.note_deadline == ' ':
                meta_data.update({'deadline': self.note_deadline.toString()})
            else:
                meta_data.update({'deadline': ' '})

            note_uuid = uuid.uuid1()
            meta_data.update({'uuid': f'{note_uuid}'})

            json_data.update({'meta_data': meta_data})

            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(json_data, file, indent=4)

            self.close()
            self.parent().close()
        else:
            msg_box = QMessageBox()
            msg_box.setText(u"The note's deadline date and time cannot be less than the current one")
            msg_box.setWindowTitle(u"Invalid value")
            msg_box.exec()
            return

    def date_time_check(self):
        """ To check the correctness of the note's deadline """
        if not self.note_deadline == ' ':
            if QDateTime.currentDateTime() < self.ui.note_date_time_edit.dateTime():
                return 'Correct'
            else:
                return 'Incorrect'
        else:
            return 'None'
