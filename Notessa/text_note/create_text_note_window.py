from PySide6.QtWidgets import QDialog, QWidget
from PySide6.QtGui import QIcon, QPixmap, QRegularExpressionValidator
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, Slot, QFile, QDateTime, QDir
from Notessa.text_note.ui_createtextnote import Ui_CreateTextNoteWindow
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.resource import rc_icons

class CreateTextNote(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateTextNoteWindow()
        self.ui.setupUi(self)

        self.ui.textNoteName.setValidator(QRegularExpressionValidator('([a-zA-Zа-яА-Я0-9-_ ]){255}'))

        #Signal-Slot
        self.ui.cancelButton.clicked.connect(lambda: self.reject())
        self.ui.saveButton.clicked.connect(self.save_text_note)


    def save_text_note(self):
        dirCheck = DirectoryChecker()
        dirCheck.text_notes_directory_checker()

        if not self.ui.textNoteName.text() == '':
            datetime = QDateTime.currentDateTime()
            fileName = str()

            if QFile(f'{dirCheck.text_notes_directory()}{QDir.separator()}{self.ui.textNoteName.text()}.txt').exists():
                print('A note with the same name already exists.')
                fileName = str(f'{dirCheck.text_notes_directory()}{QDir.separator()}{self.ui.textNoteName.text()}_'
                            f'{datetime.date().day()}-{datetime.date().month()}-{datetime.date().year()}_'
                            f'{datetime.time().hour()}-{datetime.time().minute()}-{datetime.time().second()}-{datetime.time().msec()}.txt')
            else:
                fileName = str(f'{dirCheck.text_notes_directory()}{QDir.separator()}{self.ui.textNoteName.text()}.txt')

            print(fileName)
            with open(fileName, 'w') as fp:
                fp.write(self.ui.textNoteField.toPlainText())

            print('Text note create!')
            self.accept()
