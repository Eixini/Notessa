from PySide6.QtWidgets import QDialog, QWidget
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, Slot
from windows.ui_createtextnote import Ui_CreateTextNoteWindow
import rc_icons

class CreateTextNote(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateTextNoteWindow()
        self.ui.setupUi(self)

        #Signal-Slot
        self.ui.cancelButton.clicked.connect(lambda: self.reject())
