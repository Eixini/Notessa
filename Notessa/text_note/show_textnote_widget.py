from PySide6.QtWidgets import QWidget, QDialog
from PySide6.QtCore import QDir, Qt
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.text_note.ui_gen.ui_show_textnote_widget import Ui_ShowTextNoteWidget


class ShowTextNoteWidget(QDialog):
    def __init__(self, parent, note_data: list):
        super().__init__(parent)
        self.ui = Ui_ShowTextNoteWidget()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        # self.installEventFilter(self.parent())

        self._note_data = note_data

        self.ui.textnote_name_label.setText(self._note_data[1])

        dir_checker = DirectoryChecker()
        with open(f'{dir_checker.text_notes_directory()}{QDir.separator()}{self._note_data[1]}.{self._note_data[0]}', 'r') as file:
            text_note = file.readlines()
        self.ui.show_textnote_field.setText(' '.join(text_note))
        self.setWindowTitle(self._note_data[1])
