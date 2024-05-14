from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QDir, QFile
from Notessa.paint_note.ui_gen.ui_show_paintnote_widget import Ui_ShowPaintNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker


class ShowPaintNoteWidget(QWidget):
    def __init__(self, parent, note_data: list):
        super().__init__(parent)
        self.ui = Ui_ShowPaintNoteWidget()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self._note_data = note_data

        self.ui.paintnote_name_label.setText(self._note_data[1])

        _dir_checker = DirectoryChecker()
        self._file_path = f'{_dir_checker.paint_notes_directory()}{QDir.separator()}{self._note_data[1]}.{self._note_data[0]}'
        print(f'{self._file_path}: {QFile.exists(self._file_path)}')

        self._pixmap = QPixmap()
        self._pixmap.load(f'{QDir.toNativeSeparators(self._file_path)}')
        self._pixmap = self._pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio)

        self.ui.paintnote_label.setPixmap(self._pixmap)

        # Signal - Slot
        self.ui.close_button.clicked.connect(self.close_note)

    def close_note(self):
        self.close()
