import datetime

from PySide6.QtCore import QTranslator, QFile, QSettings
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QAction, QIcon, QPixmap
from Notessa.resources.icons import common_icons_rc
from Notessa.main_menu.main_menu_widget import MainMenuWidget
from Notessa.note_list_gadget.note_list_gadget import NoteListGadget


class TrayMenu(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.app = QApplication.instance()

        self.main_menu = MainMenuWidget(self)
        self.note_list_gadget = NoteListGadget(self)

        # Actions
        self.open_main_menu_action = QAction(u'Main menu')
        self.open_main_menu_action.triggered.connect(self.open_main_menu)

        self.open_note_list_gadget_action = QAction(u'Note list gadget')
        self.open_note_list_gadget_action.triggered.connect(self.open_note_list_gadget)

        self.quit_action = QAction(u'Quit')
        self.quit_action.triggered.connect(self.app.quit)

        # Tray Menu
        self.menu = QMenu()
        self.menu.addAction(self.open_main_menu_action)
        self.menu.addAction(self.open_note_list_gadget_action)
        self.menu.addAction(self.quit_action)

        # Tray
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QPixmap(':/common/notessa_logo.png'))
        self.tray.setVisible(True)
        self.tray.show()
        self.tray.setContextMenu(self.menu)

    def open_main_menu(self):
        self.main_menu.setVisible(True)

    def open_note_list_gadget(self):
        self.note_list_gadget.setVisible(True)
