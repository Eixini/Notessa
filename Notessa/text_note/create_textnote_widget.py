from PySide6.QtWidgets import QWidget, QScrollBar
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QFile, QDateTime, QDir, Qt
from Notessa.text_note.ui_gen.ui_create_textnote_widget import Ui_CreateTextNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker

class CreateTextNoteWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_CreateTextNoteWidget()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self.ui.textnote_name_lineedit.setValidator(QRegularExpressionValidator('([a-zA-Zа-яА-Я0-9-_ ]){255}'))

        self.vertical_scrollbar = QScrollBar()
        self.ui.textnote_contents.setVerticalScrollBar(self.vertical_scrollbar)

        # Signal - Slot
        self.ui.back_button.clicked.connect(self.back)
        self.ui.save_button.clicked.connect(self.save_text_note)

    def save_text_note(self):
        dir_check = DirectoryChecker()
        dir_check.text_notes_directory_checker()

        if not self.ui.textnote_name_lineedit.text() == '':
            datetime = QDateTime.currentDateTime()
            file_name = str()

            if QFile(f'{dir_check.text_notes_directory()}{QDir.separator()}{self.ui.textnote_name_lineedit.text()}.txt').exists():
                print('A note with the same name already exists.')
                file_name = str(f'{dir_check.text_notes_directory()}{QDir.separator()}{self.ui.textnote_name_lineedit.text()}_'
                            f'{datetime.date().day()}-{datetime.date().month()}-{datetime.date().year()}_'
                            f'{datetime.time().hour()}-{datetime.time().minute()}-{datetime.time().second()}-{datetime.time().msec()}.txt')
            else:
                file_name = str(f'{dir_check.text_notes_directory()}{QDir.separator()}{self.ui.textnote_name_lineedit.text()}.txt')

            print(file_name)
            with open(file_name, 'w') as fp:
                fp.write(self.ui.textnote_contents.toPlainText())

            print('Text note create!')
            self.close()

    def back(self):
        self.close()
