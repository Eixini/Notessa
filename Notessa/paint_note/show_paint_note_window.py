from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import Qt, QDir
from Notessa.paint_note.ui_showpaintnotewindow import Ui_ShowPaintNoteWindow
from Notessa.common_modules.directory_checker import DirectoryChecker

class ShowPaintNoteWindow(QDialog):
    def __init__(self, noteData: list):
        super().__init__()
        self.ui = Ui_ShowPaintNoteWindow()
        self.ui.setupUi(self)

        self.noteData = noteData

        # Icon set
        self.setWindowIcon(QIcon(':/resource/icons/brush.png'))
        self.ui.backButton.setIcon(QIcon(':/resource/icons/back.png'))

        self.setWindowTitle(self.noteData[1])

        _dir_checker = DirectoryChecker()
        self._file_path = f'{_dir_checker.paint_notes_directory()}{QDir.separator()}{self.noteData[1]}.{self.noteData[0]}'
        url = f'{QDir.toNativeSeparators(self._file_path)}'
        print(url)

        self._pixmap = QPixmap()
        self._pixmap.load(url)
        self._pixmap = self._pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio)

        self.ui.paintNoteLabel.setPixmap(self._pixmap)

        # Signal - Slot
        self.ui.backButton.clicked.connect(self.back)

    def back(self):
        self.reject()
