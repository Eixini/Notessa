from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QTranslator, QSettings, QFile
from Notessa.settings.ui_gen.ui_settings_widget import Ui_SettingsWidget


class SettingsWidget(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)

        self.settings = QSettings(self)

        try:
            if self.settings.value('AutoShowNoteListGadget') == 'True':
                self.ui.show_note_list_gadget_checkbox.setCheckState(Qt.CheckState.Checked)
            else:
                self.ui.show_note_list_gadget_checkbox.setCheckState(Qt.CheckState.Unchecked)
        except Exception as err:
            print(err)

        # Signal - Slot
        self.ui.show_note_list_gadget_checkbox.checkStateChanged.connect(self.show_note_list_gadget_change)

    def show_note_list_gadget_change(self):
        if self.ui.show_note_list_gadget_checkbox.isChecked():
            self.settings.remove('AutoShowNoteListGadget')
            self.settings.setValue('AutoShowNoteListGadget', 'True')
        else:
            self.settings.remove('AutoShowNoteListGadget')
            self.settings.setValue('AutoShowNoteListGadget', 'False')
