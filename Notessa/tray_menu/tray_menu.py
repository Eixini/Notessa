import datetime, uuid

from PySide6.QtCore import QTranslator, QFile, QSettings, QDateTime, QSortFilterProxyModel
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QAction, QIcon, QPixmap
from Notessa.model.notelist_table_model.notes_model import NotesModel
from Notessa.note_list_gadget.note_list_gadget import NoteListGadget
from Notessa.settings.settings_widget import SettingsWidget
from Notessa.common_modules.directory_checker import DirectoryChecker

from Notessa.resources.icons.common import common_icons_rc


class TrayMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.app = QApplication.instance()

        # Checking directories for storing notes
        self.checking_directories()

        # Setting View
        self.view_model = NotesModel()

        # Proxy model
        self._proxy_model = QSortFilterProxyModel()
        self._proxy_model.setDynamicSortFilter(False)
        self._proxy_model.setSourceModel(self.view_model)

        # Core elements
        self.note_list_gadget = NoteListGadget(self, self.view_model)
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

        self.settings = QSettings(self)

        try:
            if self.settings.value('AutoShowNoteListGadget') == 'True':
                self.note_list_gadget.setVisible(True)
            else:
                self.note_list_gadget.setVisible(False)
        except Exception as err:
            print(err)

        # TEST
        # self.check_notes_deadline()

    def update_model(self):
        """
        Method for reloading data into a model.
        """
        view_model = NotesModel()

        # Proxy model
        self._proxy_model = QSortFilterProxyModel()
        self._proxy_model.setDynamicSortFilter(False)
        self._proxy_model.setSourceModel(view_model)

    def open_settings_widget(self):
        self.settings_widget.setVisible(True)

    def open_note_list_gadget(self):
        self.note_list_gadget.setVisible(True)

    def check_notes_deadline(self):
        """
        This method is needed to check the current time and the deadline time of notes.
        If a deadline is approaching, the user must be notified about this.
        """
        # 1. Получение списка заметок, у которых имеется дедлайн
        # 2. Сравнение текущего времени и времени дедлайна заметок
        # 3. Если подходит время дедлайна заметки, то необходимо уведомить об этом пользователя.
        # * Возможно пользователь может настроить время уведомления (например, 1, 5, 10 мин и т.д)

        # for item in self.view_model._data:
        #     print(item[2])
        # print(uuid.uuid4())
        pass

    def checking_directories(self):
        # Checking application data directories
        directory_checker = DirectoryChecker()
        # directory_checker.application_data_directory_checker()
        # directory_checker.style_directory_checker()

        # Checking directories with notes
        directory_checker.notes_location_directory_checker()
        directory_checker.notes_directory_checker()
        directory_checker.text_notes_directory_checker()
        directory_checker.voice_notes_directory_checker()
        directory_checker.video_notes_directory_checker()
        directory_checker.paint_notes_directory_checker()
        directory_checker.todo_notes_directory_checker()

    # Work with model
    def delete_note(self, proxy_index):
        self.view_model.removeRows(proxy_index.row(), 1, proxy_index)
        self.view_model.submit()
        print('Call delete note')
