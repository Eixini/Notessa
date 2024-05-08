from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QTranslator, QSettings, QFile
from Notessa.settings.ui_gen.ui_settings_widget import Ui_SettingsWidget


class SettingsWidget(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)
