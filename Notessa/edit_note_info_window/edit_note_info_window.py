import json

from PySide6.QtCore import QDateTime
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from Notessa.edit_note_info_window.ui_gen.ui_edit_note_info_window import Ui_EditNoteInfoWindow


class EditNoteInfoWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_EditNoteInfoWindow()
        self.ui.setupUi(self)

        self.data = data

        self.ui.old_name_line_edit.setText(data['note_name'])
        self.ui.old_deadline_line_edit.setText(data['deadline'])

        self.note_date_time = QDateTime(QDateTime.currentDateTime())

        # ============ Settings ============
        # Hide error messages
        self.ui.new_name_error_label.hide()
        self.ui.new_deadline_error_label.hide()

        self.ui.new_name_line_edit.setDisabled(True)

        self.ui.new_deadline_datetime_edit.setDisabled(True)
        self.ui.indefinite_checkbox.setDisabled(True)

        self.ui.new_deadline_datetime_edit.setDateTime(QDateTime.currentDateTime())

        # ============ Signal - Slot ============
        self.ui.rename_checkbox.checkStateChanged.connect(self.rename_checkbox_state_change)
        self.ui.change_deadline_checkbox.checkStateChanged.connect(self.deadline_checkbox_state_change)
        self.ui.indefinite_checkbox.checkStateChanged.connect(self.deadline_checkbox_state_change)
        self.ui.indefinite_checkbox.checkStateChanged.connect(self.indefinite_change)
        self.ui.new_name_line_edit.textChanged.connect(self.text_entered)

        self.ui.apply_button.clicked.connect(self.apply_button_press)
        self.ui.cancel_button.clicked.connect(self.cancel_button_press)

    def rename_checkbox_state_change(self):
        if self.ui.rename_checkbox.isChecked():
            self.ui.new_name_line_edit.setDisabled(False)
        else:
            self.ui.new_name_line_edit.setDisabled(True)

    def deadline_checkbox_state_change(self):
        if self.ui.change_deadline_checkbox.isChecked() and self.ui.indefinite_checkbox.isChecked():
            self.ui.new_deadline_datetime_edit.setDisabled(True)
            self.ui.indefinite_checkbox.setDisabled(False)
        elif self.ui.change_deadline_checkbox.isChecked() and not self.ui.indefinite_checkbox.isChecked():
            self.ui.new_deadline_datetime_edit.setDisabled(False)
            self.ui.indefinite_checkbox.setDisabled(False)
        elif not self.ui.change_deadline_checkbox.isChecked() and not self.ui.indefinite_checkbox.isChecked():
            self.ui.new_deadline_datetime_edit.setDisabled(True)
            self.ui.indefinite_checkbox.setDisabled(True)

    def apply_button_press(self):
        if (self.ui.new_name_line_edit.text() == '' and self.date_time_check() == 'Incorrect'
                and self.ui.rename_checkbox.isChecked() and self.ui.change_deadline_checkbox.isChecked()):
            self.ui.new_name_error_label.show()
            self.ui.new_deadline_error_label.show()
        elif self.ui.new_name_line_edit.text() == '' and self.ui.rename_checkbox.isChecked():
            self.ui.new_name_error_label.show()
        elif self.date_time_check() == 'Incorrect' and self.ui.change_deadline_checkbox.isChecked():
            self.ui.new_deadline_error_label.show()
        elif (self.date_time_check() == 'Correct' or self.date_time_check() == 'None'
              or self.ui.rename_checkbox.isChecked() or self.ui.change_deadline_checkbox.isChecked()):

            json_data = None

            with open(self.data['meta_data_file'], 'r') as file:
                json_data = json.load(file)

            if self.ui.rename_checkbox.isChecked():
                json_data['note_name'] = self.ui.new_name_line_edit.text()
            if self.ui.change_deadline_checkbox.isChecked() and self.date_time_check() == 'Correct':
                json_data['deadline'] = self.ui.new_deadline_datetime_edit.dateTime().toString()
            elif self.ui.change_deadline_checkbox.isChecked() and self.date_time_check() == 'None':
                json_data['deadline'] = None

            with open(self.data['meta_data_file'], 'w', encoding='utf-8') as file:
                json.dump(json_data, file, indent=4)

            self.accept()

    def cancel_button_press(self):
        self.close()

    def text_entered(self):
        if self.ui.new_name_line_edit.text() != '':
            self.ui.new_name_error_label.hide()

    def date_time_change(self):
        if not self.ui.indefinite_checkbox.isChecked():
            self.note_date_time = self.ui.new_deadline_datetime_edit.dateTime()
            self.ui.new_deadline_error_label.hide()
        else:
            self.note_date_time = None

    def indefinite_change(self):
        if self.ui.indefinite_checkbox.isChecked():
            self.note_date_time = 'None'
            self.ui.new_deadline_datetime_edit.setDisabled(True)
        else:
            self.note_date_time = self.ui.new_deadline_datetime_edit.dateTime().toLocalTime()
            self.ui.new_deadline_datetime_edit.setEnabled(True)

    def date_time_check(self):
        """ To check the correctness of the note's deadline """
        if not self.note_date_time == 'None':
            if QDateTime.currentDateTime().toSecsSinceEpoch() < self.ui.new_deadline_datetime_edit.dateTime().toSecsSinceEpoch():
                return 'Correct'
            else:
                return 'Incorrect'
        else:
            return 'None'
