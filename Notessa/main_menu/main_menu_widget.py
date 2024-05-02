from PySide6.QtCore import QTranslator, QFile, QSettings
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QAction, QIcon, QPixmap
from Notessa.main_menu.ui_gen.ui_main_menu_widget import Ui_MainMenuWidget


class MainMenuWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_MainMenuWidget()
        self.ui.setupUi(self)
