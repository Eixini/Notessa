import json, uuid
from PySide6.QtWidgets import QWidget, QScrollBar, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QFile, QDateTime, QDir, Qt, QIODevice
from Notessa.text_note.ui_gen.ui_create_textnote_widget import Ui_CreateTextNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.common_modules.forming_note_name import forming_note_file_name


class CreateTextNoteWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_CreateTextNoteWidget()
        self.ui.setupUi(self)

        # Set a default note deadline -
        self.note_deadline = 'None'

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        # Default value
        self.ui.indefinite_checkbox.setChecked(True)
        self.ui.note_deadline_label.setDisabled(True)
        self.ui.note_date_time_edit.setDisabled(True)

        self.ui.note_date_time_edit.setDateTime(QDateTime.currentDateTime())

        self.vertical_scrollbar = QScrollBar()
        self.ui.textnote_contents.setVerticalScrollBar(self.vertical_scrollbar)

        # Signal - Slot
        self.ui.save_button.clicked.connect(self.save_text_note)
        self.ui.note_date_time_edit.dateTimeChanged.connect(self.select_date_time_change)
        self.ui.indefinite_checkbox.checkStateChanged.connect(self.indefinite_change)

    def indefinite_change(self):
        if self.ui.indefinite_checkbox.isChecked():
            self.note_deadline = 'None'
            self.ui.note_deadline_label.setDisabled(True)
            self.ui.note_date_time_edit.setDisabled(True)
        else:
            self.note_deadline = self.ui.note_date_time_edit.dateTime().toLocalTime()
            self.ui.note_deadline_label.setEnabled(True)
            self.ui.note_date_time_edit.setEnabled(True)

    def select_date_time_change(self):
        self.note_deadline = self.ui.note_date_time_edit.dateTime().toLocalTime()

    def save_text_note(self):
        dir_check = DirectoryChecker()
        dir_check.text_notes_directory_checker()

        if self.date_time_check() == 'Correct' or self.date_time_check() == 'None':

            if not self.ui.textnote_name_lineedit.text() == 'None':
                note_name = self.ui.textnote_name_lineedit.text()
                file_name = forming_note_file_name('TextNote')
                file_path = str(f"{dir_check.text_notes_directory()}{QDir.separator()}{file_name}.txt")
                meta_data_file_path = str(f'{dir_check.text_notes_directory()}{QDir.separator()}{file_name}.json')

                meta_data_content = {'note_name': note_name}

                with open(file_path, 'w', encoding='utf-8') as fp:
                    fp.write(self.ui.textnote_contents.toPlainText())

                if not self.note_deadline == 'None':
                    meta_data_content.update({'deadline': self.note_deadline.toString()})
                else:
                    meta_data_content.update({'deadline': None})

                note_uuid = uuid.uuid1()
                meta_data_content.update({'uuid': f'{note_uuid}'})

                with open(meta_data_file_path, 'w', encoding='utf-8') as file:
                    json.dump(meta_data_content, file, indent=4)

                self.close()
                self.parent().close()
        else:
            msg_box = QMessageBox()
            msg_box.setText(u"The note's deadline date and time cannot be less than the current one")
            msg_box.setWindowTitle(u"Invalid value")
            msg_box.exec()
            return

    def date_time_check(self):
        """ To check the correctness of the note's deadline """
        if not self.note_deadline == 'None':
            if QDateTime.currentDateTime() < self.ui.note_date_time_edit.dateTime():
                return 'Correct'
            else:
                return 'Incorrect'
        else:
            return 'None'
