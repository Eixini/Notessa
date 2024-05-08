import datetime

from PySide6.QtCore import QTranslator, QFile, QSettings
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QAction, QIcon, QPixmap
from Notessa.resources.icons.common import common_icons_rc
from Notessa.note_creation_menu.note_creation_menu_widget import NoteCreationMenuWidget
from Notessa.note_list_gadget.note_list_gadget import NoteListGadget
from Notessa.settings.settings_widget import SettingsWidget
from Notessa.common_modules.directory_checker import DirectoryChecker


class TrayMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.app = QApplication.instance()

        # Checking directories for storing notes
        self.checking_directories()

        self.note_list_gadget = NoteListGadget(self)
        self.settings_widget = SettingsWidget(self)

        # Actions
        self.open_note_list_gadget_action = QAction(u'Note list gadget')
        self.open_note_list_gadget_action.triggered.connect(self.open_note_list_gadget)

        self.open_settings_widget_action = QAction(u'Settings')
        self.open_settings_widget_action.triggered.connect(self.open_settings_widget)

        self.quit_action = QAction(u'Quit')
        self.quit_action.triggered.connect(self.app.quit)

        # Tray Menu
        self.menu = QMenu()
        self.menu.addAction(self.open_note_list_gadget_action)
        self.menu.addAction(self.open_settings_widget_action)
        self.menu.addAction(self.quit_action)

        # Tray
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QPixmap(':/common/notessa_logo.png'))
        self.tray.setVisible(True)
        self.tray.show()
        self.tray.setContextMenu(self.menu)

    def open_settings_widget(self):
        self.settings_widget.setVisible(True)

    def open_note_list_gadget(self):
        self.note_list_gadget.setVisible(True)

    def checking_directories(self):
        # Checking application data directories
        directory_checker = DirectoryChecker()
        directory_checker.application_data_directory_checker()
        directory_checker.style_directory_checker()

        # Checking directories with notes
        directory_checker.notes_location_directory_checker()
        directory_checker.notes_directory_checker()
        directory_checker.text_notes_directory_checker()
        directory_checker.voice_notes_directory_checker()
        directory_checker.video_notes_directory_checker()
        directory_checker.paint_notes_directory_checker()
        directory_checker.todo_notes_directory_checker()
