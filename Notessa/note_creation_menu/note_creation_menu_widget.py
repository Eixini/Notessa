from PySide6.QtCore import Qt, QTranslator, QFile, QSettings
from PySide6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QWidget
from PySide6.QtGui import QAction, QIcon, QPixmap
from Notessa.note_creation_menu.ui_gen.ui_note_creation_menu_widget import Ui_NoteCreationMenuWidget
from Notessa.window_container.window_container import WindowContainer


class NoteCreationMenuWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_NoteCreationMenuWidget()
        self.ui.setupUi(self)

        # self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self._parent = parent

        # Signal - Slot
        self.ui.create_text_note_button.clicked.connect(self.create_text_note)
        self.ui.create_voice_note_button.clicked.connect(self.create_voice_note)
        self.ui.create_video_note_button.clicked.connect(self.create_video_note)
        self.ui.create_paint_note_button.clicked.connect(self.create_paint_note)
        self.ui.create_todo_note_button.clicked.connect(self.create_todo_note)

    def create_text_note(self):
        create_note_window = WindowContainer(self._parent)
        create_note_window.create_note('text')
        self.close()
        create_note_window.exec()

    def create_voice_note(self):
        create_note_window = WindowContainer(self._parent)
        create_note_window.create_note('voice')
        self.close()
        create_note_window.exec()

    def create_video_note(self):
        create_note_window = WindowContainer(self._parent)
        create_note_window.create_note('video')
        self.close()
        create_note_window.exec()

    def create_paint_note(self):
        create_note_window = WindowContainer(self._parent)
        create_note_window.create_note('paint')
        self.close()
        create_note_window.exec()

    def create_todo_note(self):
        create_note_window = WindowContainer(self._parent)
        create_note_window.create_note('todo')
        self.close()
        create_note_window.exec()
