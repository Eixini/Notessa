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

        print(self.data)

        self.ui.old_name_line_edit.setText(data['note_name'])
        self.ui.old_deadline_line_edit.setText(data['deadline'])

        # ============ Settings ============
        # Hide error messages
        self.ui.new_name_error_label.hide()
        self.ui.new_deadline_error_label.hide()

        self.ui.new_name_line_edit.setDisabled(True)

        self.ui.new_deadline_datetime_edit.setDisabled(True)

        self.ui.new_deadline_datetime_edit.setDateTime(QDateTime.currentDateTime())

        # ============ Signal - Slot ============
        self.ui.rename_checkbox.checkStateChanged.connect(self.rename_checkbox_state_change)
        self.ui.change_deadline_checkbox.checkStateChanged.connect(self.deadline_checkbox_state_change)

        self.ui.apply_button.clicked.connect(self.apply_button_press)
        self.ui.cancel_button.clicked.connect(self.cancel_button_press)

    def rename_checkbox_state_change(self):
        if self.ui.rename_checkbox.isChecked():
            pass
        else:
            pass

    def deadline_checkbox_state_change(self):
        if self.ui.change_deadline_checkbox.isChecked():
            pass
        else:
            pass

    def apply_button_press(self):
        pass

    def cancel_button_press(self):
        self.close()
