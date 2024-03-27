from PySide6.QtCore import QDir, Qt, QUrl, QFile
from PySide6.QtWidgets import QWidget
from Notessa.todo_notes.ui_gen.ui_show_todo_note_widget import Ui_ShowTodoNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.model.todo_note_model.todo_model import TodoModel
import json
import os


class ShowTodoNoteWidget(QWidget):
    def __init__(self, parent, note_data: list):
        super().__init__(parent)
        self.ui = Ui_ShowTodoNoteWidget()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self._note_data = note_data

        self.ui.todo_note_name_label.setText(self._note_data[1])

        self._dir_checker = DirectoryChecker()
        self._file_path = f'{self._dir_checker.todo_notes_directory()}{QDir.separator()}{self._note_data[1]}.{self._note_data[0]}'

        self._todos = None
        self.load_data()

        self._todo_model = TodoModel(self._todos)
        self.ui.todo_items_list_view.setModel(self._todo_model)
        self.ui.todo_items_list_view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ui.todo_items_list_view.setWordWrap(True)

        # Signal - Slot
        self.ui.close_button.clicked.connect(self.close_note)
        self.ui.todo_items_list_view.clicked.connect(self.mark)

    def mark(self):
        current_index = self.ui.todo_items_list_view.currentIndex()
        current_index_row = current_index.row()
        if not current_index == None:
            print(f'Clicked in ListView: {current_index_row}')
            text, status = self._todo_model._todos[current_index_row]
            self._todo_model._todos[current_index_row] = (text, not status)
            self._todo_model.dataChanged.emit(current_index, current_index)
            self.save_data()

    def load_data(self):
        with open(self._file_path, 'r') as file:
            self._todos = json.load(file)

    def save_data(self):
        dir_check = DirectoryChecker()
        with open(self._file_path, 'w') as file:
            json.dump(self._todo_model._todos, file, indent=4)

    def close_note(self):
        self.close()
