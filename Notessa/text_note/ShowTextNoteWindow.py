from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QDir
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.text_note.ui_showtextnotewindow import Ui_ShowTextNoteWindow
from Notessa.resource import rc_icons

class ShowTextNoteWindow(QDialog):
    def __init__(self, noteData: list):
        super().__init__()
        self.ui = Ui_ShowTextNoteWindow()
        self.ui.setupUi(self)

        self.noteData = noteData

        dirChecker = DirectoryChecker()
        with open(f'{dirChecker.text_notes_directory()}{QDir.separator()}{self.noteData[1]}.txt', 'r') as file:
            textNote = file.readlines()
        self.ui.showTextNoteField.setText(' '.join(textNote))
        self.setWindowTitle(self.noteData[1])

        # Signal-Slot
        self.ui.backButton.clicked.connect(lambda: self.accept())
