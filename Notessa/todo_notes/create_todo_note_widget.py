from PySide6.QtCore import QDir, Qt
from PySide6.QtWidgets import QWidget, QListWidgetItem
from PySide6.QtGui import QRegularExpressionValidator
from Notessa.todo_notes.ui_gen.ui_create_todo_note_widget import Ui_CreateTodoNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker
import json


class CreateTodoNoteWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_CreateTodoNoteWidget()
        self.ui.setupUi(self)

        self._parent = parent

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self.ui.todo_note_name_lineedit.setValidator(QRegularExpressionValidator('([a-zA-Zа-яА-Я0-9-_ ]){255}'))
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
        if not self.ui.todo_note_name_lineedit == '':
            dir_check = DirectoryChecker()
            file_name = f'{dir_check.todo_notes_directory()}{QDir.separator()}{self.ui.todo_note_name_lineedit.text()}.json'
            json_data = list()
            for it in range(self.ui.note_items_list_widget.count()):
                json_data.append((self.ui.note_items_list_widget.item(it).text(), False))
            with open(file_name, 'w') as file:
                json.dump(json_data, file, indent=4)
            self.close()
