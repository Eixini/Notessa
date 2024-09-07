import json, uuid

from PySide6.QtCore import QDir, Qt, QDateTime
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from Notessa.todo_notes.ui_gen.ui_create_todo_note_widget import Ui_CreateTodoNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.common_modules.forming_note_name import forming_note_file_name
from Notessa.save_dialog.save_dialog import SaveDialog


class CreateTodoNoteWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_CreateTodoNoteWidget()
        self.ui.setupUi(self)

        # Set a default note deadline -
        self.note_deadline = 'None'

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
        save_dialog = SaveDialog(self)
        _, note_name, deadline_datetime = save_dialog.exec()

        dir_checker = DirectoryChecker()

        file_name = forming_note_file_name('TodoNote')

        file_path = str(f"{dir_checker.todo_notes_directory()}{QDir.separator()}{file_name}.json")

        json_data = dict()

        item_list = list()
        for it in range(self.ui.note_items_list_widget.count()):
            item_list.append((self.ui.note_items_list_widget.item(it).text(), False))

        json_data.update({'note_data': item_list})

        # Meta-data
        meta_data = {'note_name': note_name}

        if not self.note_deadline == 'None':
            meta_data.update({'deadline': deadline_datetime.toString()})
        else:
            meta_data.update({'deadline': None})

        note_uuid = uuid.uuid1()
        meta_data.update({'uuid': f'{note_uuid}'})

        json_data.update({'meta_data': meta_data})

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(json_data, file, indent=4)

        self.close()
        self.parent().close()
