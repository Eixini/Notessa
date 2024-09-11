from pathlib import Path
from zipfile import ZipFile
import shutil
import os

from PySide6.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QTranslator, QSettings, QFile, QDateTime, QDir

from Notessa.settings.ui_gen.ui_settings_widget import Ui_SettingsWidget
from Notessa.common_modules.directory_checker import DirectoryChecker

from Notessa.resources.icons.button import button_icons_rc
from Notessa.resources.icons.flags import flags_rc
from Notessa.resources.translations import translations_rc


class SettingsWidget(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)

        self.app = QApplication.instance()

        # Temporary solution !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.ui.start_at_system_startup_checkbox.hide()
        self.ui.style_combobox.hide()
        self.ui.style_label.hide()
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.setWindowIcon(QIcon(':/button/gear.png'))

        self.identification_comment = 'Notessa notes'.encode('utf-8')

        self.settings = QSettings(self)
        self.translator = QTranslator(self.app)

        try:
            if self.settings.value('AutoShowNoteListGadget') == 'True':
                self.ui.show_note_list_gadget_checkbox.setCheckState(Qt.CheckState.Checked)
            else:
                self.ui.show_note_list_gadget_checkbox.setCheckState(Qt.CheckState.Unchecked)

            if self.settings.value('WaitingTimeBeforeDeadline'):
                self.ui.deadline_time_spinbox.setValue(self.settings.value('WaitingTimeBeforeDeadline'))
        except Exception as err:
            print(err)

        try:
            self.ui.language_combobox.setPlaceholderText(self.settings.value('Language'))
            # self.ui.style_combo_box.setPlaceholderText(self.settings.value('StyleName'))
        except Exception as err:
            print(err)

        # Translate
        self.ui.language_combobox.addItem(QIcon(':/flags/american.png'), 'English', ':/qm/en.qm')
        self.ui.language_combobox.addItem(QIcon(':/flags/russian.png'), 'Русский', ':/qm/ru.qm')

        # Signal - Slot
        self.ui.show_note_list_gadget_checkbox.checkStateChanged.connect(self.show_note_list_gadget_change)
        self.ui.deadline_time_spinbox.valueChanged.connect(self.waiting_time_before_deadline_change)
        self.ui.import_notes_button.clicked.connect(self.import_notes)
        self.ui.export_notes_button.clicked.connect(self.export_notes)

        # Signal - Slot
        self.ui.language_combobox.currentIndexChanged.connect(self.change_translation)

    def change_translation(self):
        data = self.ui.language_combobox.currentData()
        self.app.removeTranslator(self.translator)
        self.translator.load(data)
        self.app.installTranslator(self.translator)
        self.settings.remove('LanguagePath')
        self.settings.remove('Language')
        self.settings.setValue('Language', self.ui.language_combobox.currentText())
        self.settings.setValue('LanguagePath', self.ui.language_combobox.currentData())

    def show_note_list_gadget_change(self):
        if self.ui.show_note_list_gadget_checkbox.isChecked():
            self.settings.remove('AutoShowNoteListGadget')
            self.settings.setValue('AutoShowNoteListGadget', 'True')
        else:
            self.settings.remove('AutoShowNoteListGadget')
            self.settings.setValue('AutoShowNoteListGadget', 'False')

    def waiting_time_before_deadline_change(self):
        # Setting the waiting time before the deadline
        self.settings.remove('WaitingTimeBeforeDeadline')
        self.settings.setValue('WaitingTimeBeforeDeadline', self.ui.deadline_time_spinbox.value())

    def import_notes(self):

        file_dialog = QFileDialog.getOpenFileName(self, u"Select Notessa zip file")
        # print(file_dialog[0])

        dir_checker = DirectoryChecker()

        if file_dialog[0]:
            with ZipFile(file_dialog[0], 'r') as zip:
                if zip.comment.decode('utf-8') == self.identification_comment:
                    zip.extractall(dir_checker.notes_directory_checker())
                else:
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle(QTranslator.tr(u'Import error'))
                    msg_box.setText(self.tr(u'An error occurred while importing notes. '
                                    u'The archive file is damaged or belongs to an old version of the application. '
                                    u'If you are sure that the specified archive contains the necessary notes, please import manually.'))
                    msg_box.exec()

    def export_notes(self):
        current_datetime = QDateTime.currentDateTime()
        zip_file_name = (f'Notessa_Notes_{current_datetime.date().day()}-{current_datetime.date().month()}-{current_datetime.date().year()}_'
                         f'{current_datetime.time().hour()}-{current_datetime.time().minute()}-{current_datetime.time().second()}.zip')

        file_dialog = QFileDialog.getExistingDirectory(self, self.tr(u"Select directory"))

        full_path = QDir.toNativeSeparators(f'{file_dialog}{QDir.separator()}{zip_file_name}')

        dir_checker = DirectoryChecker()

        with ZipFile(full_path, "w") as zip:
            for root, dirs, files in os.walk(dir_checker.notes_directory_checker()):
                for file in files:
                    file_path = os.path.join(root, file)
                    archive_path = os.path.relpath(file_path, dir_checker.notes_directory_checker())
                    zip.write(file_path, archive_path)
            zip.comment = self.identification_comment

        # shutil.make_archive(full_path, 'zip', dir_checker.notes_directory_checker())
