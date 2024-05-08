from PySide6.QtCore import QTranslator, QFile, QSettings
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QAction, QIcon, QPixmap
from Notessa.note_creation_menu.ui_gen.ui_note_creation_menu_widget import Ui_NoteCreationMenuWidget


class NoteCreationMenuWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_NoteCreationMenuWidget()
        self.ui.setupUi(self)
