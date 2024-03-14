from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QDir, QStandardPaths
from Notessa.paint_note.ui_createpaintnote import Ui_CreatePaintNote
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.paint_note.painter_widget import PainterWidget
from Notessa.paint_note.save_messagebox import SaveMessageBox
from Notessa.resource import rc_icons

class CreatePaintNote(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreatePaintNote()
        self.ui.setupUi(self)

        self._painter_widget = PainterWidget()
        self.ui.mdiArea.addSubWindow(self._painter_widget)
        self.ui.mdiArea.currentSubWindow().setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedWidth(self._painter_widget.width())
        self.setFixedHeight(self._painter_widget.height() + self.ui.backButton.height() + self.ui.mainLayout.spacing())

        # Icon set
        self.setWindowIcon(QIcon(':/resource/icons/brush.png'))

        # Signal - Slot
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.openButton.clicked.connect(self.open)
        self.ui.backButton.clicked.connect(self.back)

    def save(self):
        note_name = self.enter_note_name()

        dirChecker = DirectoryChecker()
        file = f'{dirChecker.paint_notes_directory()}{QDir.separator()}{note_name}.png'
        url = f'{QDir.toNativeSeparators(file)}'

        self._painter_widget.save(url)
        self.accept()

    def open(self):
        """ Selecting a file for subsequent installation """
        file_dialog = QFileDialog(self)
        file_dialog.setDirectory(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.HomeLocation))
        file_dialog.setWindowTitle('Select image')
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.jpeg)")
        file_dialog.setViewMode(QFileDialog.ViewMode.List)

        filename = None

        if file_dialog.exec():
            filename = file_dialog.selectedFiles()[0]

        self._painter_widget.load(filename)

        self.setFixedWidth(self._painter_widget.width())
        self.setFixedHeight(self._painter_widget.height() + self.ui.backButton.height() + self.ui.mainLayout.spacing())

    def enter_note_name(self):
        message_box = SaveMessageBox()
        _, note_name = message_box.exec()
        return note_name

    def back(self):
        self.reject()
