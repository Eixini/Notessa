import datetime, uuid

from PySide6.QtCore import QTranslator, QFile, QSettings, QDateTime, QSortFilterProxyModel, QTimer, QEvent
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QAction, QIcon, QPixmap
from Notessa.model.notelist_table_model.notes_model import NotesModel
from Notessa.note_list_gadget.note_list_gadget import NoteListGadget
from Notessa.settings.settings_widget import SettingsWidget
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.common_modules import constants

from Notessa.resources.icons.common import common_icons_rc


class TrayMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.app = QApplication.instance()

        # Checking directories for storing notes
        self.checking_directories()

        # Setting View
        self.view_model = NotesModel()

        # List of corrupted meta data files
        self.corrupted_files = self.view_model.get_corrupted_files()
        # print(self.corrupted_files)

        # Proxy model
        self._proxy_model = QSortFilterProxyModel()
        self._proxy_model.setDynamicSortFilter(False)
        self._proxy_model.setSourceModel(self.view_model)

        # Core elements
        self.note_list_gadget = NoteListGadget(self, self.view_model)
        self.settings_widget = SettingsWidget(self)

        # Actions
        self.open_note_list_gadget_action = QAction(QTranslator.tr(u'Note list gadget'))
        self.open_note_list_gadget_action.triggered.connect(self.open_note_list_gadget)

        self.open_settings_widget_action = QAction(QTranslator.tr(u'Settings'))
        self.open_settings_widget_action.triggered.connect(self.open_settings_widget)

        self.quit_action = QAction(QTranslator.tr(u'Quit'))
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
        # Default value (min * 60 * 1000 = msec (5 min = 300000 msec))
        self.waiting_time_before_deadline = 300000

        try:
            if self.settings.value('AutoShowNoteListGadget') == 'True':
                self.note_list_gadget.setVisible(True)
            else:
                self.note_list_gadget.setVisible(False)

            if self.settings.value('WaitingTimeBeforeDeadline'):
                self.waiting_time_before_deadline = self.settings.value('WaitingTimeBeforeDeadline') * 60 * 1000
        except Exception as err:
            print(err)

        self.note_deadline_list = dict()

        # Timer check deadline note
        note_deadline_timer = QTimer(self)
        note_deadline_timer.timeout.connect(self.check_notes_deadline)
        # note_deadline_timer.start(60000)
        note_deadline_timer.start(600)

    def update_model(self):
        """
        Method for reloading data into a model.
        """
        self.view_model = NotesModel()

        # List of corrupted meta data files
        self.corrupted_files.clear()
        self.corrupted_files = self.view_model.get_corrupted_files()
        # print(self.corrupted_files)

        # Proxy model
        self._proxy_model = QSortFilterProxyModel()
        self._proxy_model.setDynamicSortFilter(False)
        self._proxy_model.setSourceModel(self.view_model)

        # self.check_notes_deadline()

    def open_settings_widget(self):
        self.settings_widget.setVisible(True)

    def open_note_list_gadget(self):
        self.note_list_gadget.setVisible(True)

    def check_notes_deadline(self):
        """
        This method is needed to check the current time and the deadline time of notes.
        If a deadline is approaching, the user must be notified about this.
        """
        for item in self.view_model._data:
            if item[constants.NOTE_DEADLINE]:
                if not item[constants.NOTE_UUID] in self.note_deadline_list:
                    temp_dict = dict()
                    temp_dict.update({'note_name': item[constants.NOTE_NAME]})
                    temp_dict.update({'deadline': item[constants.NOTE_DEADLINE]})
                    temp_dict.update({'checked': False})

                    self.note_deadline_list.update({item[constants.NOTE_UUID]: temp_dict})

        for k, v in self.note_deadline_list.items():
            # Obtaining the necessary note data by its UUID
            current_note = self.note_deadline_list[k]

            deadline_msec = QDateTime.fromString(current_note['deadline']).toMSecsSinceEpoch()
            time_diff = deadline_msec - QDateTime.currentDateTime().toMSecsSinceEpoch()

            # min * 60 * 1000 = msec (5 min = 300000 msec)
            if time_diff <= self.waiting_time_before_deadline and time_diff >= 0 and current_note['checked'] == False:
                msg = QTranslator.tr(f"The deadline for note \"{current_note['note_name']}\" is approaching")
                self.tray.showMessage(QTranslator.tr(u'Timeout'), msg)
                print(msg)

                # Set to "Checked" to avoid duplicate messages about a specific note's deadline.
                current_note['checked'] = True
                self.note_deadline_list.update({k: current_note})

    def eventFilter(self, watched, event):
        # QEvent::HideToParent
        print(event.type())
        if event.type() == QEvent.Type.Close and watched.objectName() == 'WindowContainer':
            self.note_list_gadget.update_view()
            return True
        else:
            return False

    def checking_directories(self):
        # Checking application data directories
        directory_checker = DirectoryChecker()
        directory_checker.application_data_directory_checker()
        # directory_checker.style_directory_checker()
        directory_checker.logs_directory_checker()

        # Checking directories with notes
        directory_checker.notes_location_directory_checker()
        directory_checker.notes_directory_checker()
        directory_checker.text_notes_directory_checker()
        directory_checker.voice_notes_directory_checker()
        directory_checker.video_notes_directory_checker()
        directory_checker.paint_notes_directory_checker()
        directory_checker.todo_notes_directory_checker()
