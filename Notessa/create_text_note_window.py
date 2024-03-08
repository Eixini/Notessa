from PySide6.QtWidgets import QDialog, QWidget
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, Slot, QFile, QDateTime, QDir
from windows.ui_createtextnote import Ui_CreateTextNoteWindow
from settings.directory_checker import DirectoryChecker
import rc_icons

class CreateTextNote(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateTextNoteWindow()
        self.ui.setupUi(self)

        #Signal-Slot
        self.ui.cancelButton.clicked.connect(lambda: self.reject())
        self.ui.saveButton.clicked.connect(self.save_text_note)


    def save_text_note(self):
        dirCheck = DirectoryChecker()
        dirCheck.text_notes_directory_checker()

        if not self.ui.textNoteName.text() == '':
            datetime = QDateTime.currentDateTime()
            file = str(f'{self.ui.textNoteName.text()}_'
                         f'{datetime.date().day()}-{datetime.date().month()}-{datetime.date().year()}_'
                         f'{datetime.time().hour()}-{datetime.time().minute()}-{datetime.time().second()}.txt')

            with open(f'{dirCheck.text_notes_directory()}{QDir.separator()}{file}', 'w') as fp:
                fp.write(self.ui.textNoteField.toPlainText())

            print('Text note create!')
            self.accept()
