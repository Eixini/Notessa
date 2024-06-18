from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QDir, Qt
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.text_note.ui_gen.ui_show_textnote_widget import Ui_ShowTextNoteWidget
from Notessa.common_modules import constants


class ShowTextNoteWidget(QWidget):
    def __init__(self, parent, note_data: list):
        super().__init__(parent)
        self.ui = Ui_ShowTextNoteWidget()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self._note_data = note_data

        self.ui.textnote_name_label.setText(self._note_data[constants.NOTE_NAME])
        self.setWindowTitle(self._note_data[constants.NOTE_NAME])

        dir_checker = DirectoryChecker()
        with open(f'{dir_checker.text_notes_directory()}{QDir.separator()}{self._note_data[constants.NOTE_FILE_BASENAME]}.{self._note_data[constants.NOTE_FILE_TYPE]}', 'r', encoding='utf-8') as file:
            text_note = file.readlines()
        self.ui.show_textnote_field.setText(' '.join(text_note))
