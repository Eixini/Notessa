from PySide6.QtWidgets import QDialog, QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, Slot, QFile, QDateTime, QDir, QModelIndex
from Notessa.windows.ui_shownoteswindow import Ui_ShowNotesWindow
from Notessa.settings.directory_checker import DirectoryChecker
from Notessa.windows.ui_showtextnotewindow import Ui_ShowTextNoteWindow
import Notessa.rc_icons

class ShowTextNoteWindow(QDialog):
    def __init__(self, noteData: list):
        super().__init__()
        self.ui = Ui_ShowTextNoteWindow()
        self.ui.setupUi(self)

        self.noteData = noteData

        dirChecker = DirectoryChecker()
        textNote = str()
        with open(f'{dirChecker.text_notes_directory()}{QDir.separator()}{self.noteData[1]}.txt', 'r') as file:
            textNote = file.readlines()
        self.ui.showTextNoteField.setText(' '.join(textNote))
        self.setWindowTitle(self.noteData[1])

        # Signal-Slot
        self.ui.backButton.clicked.connect(lambda: self.accept())
