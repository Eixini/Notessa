import json, uuid
from PySide6.QtWidgets import QWidget, QScrollBar, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QFile, QDateTime, QDir, Qt, QIODevice
from Notessa.text_note.ui_gen.ui_create_textnote_widget import Ui_CreateTextNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.common_modules.forming_note_name import forming_note_file_name
from Notessa.save_dialog.save_dialog import SaveDialog


class CreateTextNoteWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_CreateTextNoteWidget()
        self.ui.setupUi(self)

        # Set a default note deadline -
        self.note_deadline = 'None'

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self.vertical_scrollbar = QScrollBar()
        self.ui.textnote_contents.setVerticalScrollBar(self.vertical_scrollbar)

        # Signal - Slot
        self.ui.save_button.clicked.connect(self.save_text_note)

    def save_text_note(self):
        dir_check = DirectoryChecker()
        dir_check.text_notes_directory_checker()

        save_dialog = SaveDialog(self)
        _, note_name, deadline_datetime = save_dialog.exec()

        file_name = forming_note_file_name('TextNote')
        file_path = str(f"{dir_check.text_notes_directory()}{QDir.separator()}{file_name}.txt")
        meta_data_file_path = str(f'{dir_check.text_notes_directory()}{QDir.separator()}{file_name}.json')

        meta_data_content = {'note_name': note_name}

        with open(file_path, 'w', encoding='utf-8') as fp:
            fp.write(self.ui.textnote_contents.toPlainText())

        if not self.note_deadline == 'None':
            meta_data_content.update({'deadline': deadline_datetime.toString()})
        else:
            meta_data_content.update({'deadline': None})

        note_uuid = uuid.uuid1()
        meta_data_content.update({'uuid': f'{note_uuid}'})

        with open(meta_data_file_path, 'w', encoding='utf-8') as file:
            json.dump(meta_data_content, file, indent=4)

        self.close()
        self.parent().close()
