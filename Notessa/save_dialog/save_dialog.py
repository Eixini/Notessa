from PySide6.QtWidgets import QDialog, QDateTimeEdit
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QDateTime

from Notessa.save_dialog.ui_gen.ui_save_dialog import Ui_SaveDialog

from Notessa.resources.icons.button import button_icons_rc


class SaveDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_SaveDialog()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        self.ui.warning_message_label.hide()

        self.ui.save_button.setIcon(QIcon(':/button/save.png'))
        self.ui.cancel_button.setIcon(QIcon(':/button/close.png'))

        self.note_name = ''
        self.note_date_time = QDateTime(QDateTime.currentDateTime())
        self.ui.note_date_time_edit.setDateTime(self.note_date_time)

        # Signal - slot
        self.ui.save_button.clicked.connect(self.save)
        self.ui.cancel_button.clicked.connect(self.cancel)
        self.ui.note_name_lineedit.textChanged.connect(self.text_entered)
        self.ui.note_date_time_edit.dateTimeChanged.connect(self.date_time_change)
        self.ui.indefinite_checkbox.checkStateChanged.connect(self.indefinite_change)

    def date_time_change(self):
        if not self.ui.indefinite_checkbox.isChecked():
            self.note_date_time = self.ui.note_date_time_edit.dateTime()
        else:
            self.note_date_time = None

    def indefinite_change(self):
        if self.ui.indefinite_checkbox.isChecked():
            self.note_date_time = 'None'
            self.ui.note_date_time_edit.setDisabled(True)
        else:
            self.note_date_time = self.ui.note_date_time_edit.dateTime().toLocalTime()
            self.ui.note_date_time_edit.setEnabled(True)

    def text_entered(self):
        if self.ui.note_name_lineedit.text() != '':
            self.ui.warning_message_label.hide()
            self.note_name = self.ui.note_name_lineedit.text()

    def save(self):
        if self.ui.note_name_lineedit.text() != '':
            self.accept()
        else:
            self.ui.warning_message_label.show()

    def exec(self):
        # self.note_name = self.ui.note_name_lineedit.text()
        # self.note_date_time = self.ui.note_date_time_edit.dateTime()
        if not self.note_date_time == 'None':
            return super().exec(), self.note_name, self.note_date_time
        else:
            return super().exec(), self.note_name, "None"

    def cancel(self):
        self.reject()
