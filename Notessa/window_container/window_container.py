from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QMenu, QDialog
from PySide6.QtCore import QSortFilterProxyModel, Qt, QEvent, QSettings, QPoint
from PySide6.QtGui import QIcon, QPixmap, QMouseEvent, QAction, QCursor

from Notessa.window_container.ui_gen.ui_window_container import Ui_WindowContainer

from Notessa.text_note.show_textnote_widget import ShowTextNoteWidget
from Notessa.voice_note.show_voicenote_widget import ShowVoiceNoteWidget
from Notessa.video_note.show_videonote_widget import ShowVideoNoteWidget
from Notessa.paint_note.show_paint_note_widget import ShowPaintNoteWidget
from Notessa.todo_notes.show_todo_note_widget import ShowTodoNoteWidget

from Notessa.text_note.create_textnote_widget import CreateTextNoteWidget
from Notessa.voice_note.create_voice_note_widget import CreateVoiceNoteWidget
from Notessa.video_note.create_video_note_widget import CreateVideoNoteWidget
from Notessa.paint_note.create_paint_note_window import CreatePaintNoteWindow
from Notessa.todo_notes.create_todo_note_widget import CreateTodoNoteWidget

from Notessa.resources.icons.button import button_icons_rc
from Notessa.resources.icons.common import common_icons_rc

class WindowContainer(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_WindowContainer()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(':/common/notessa_logo.png'))

        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self._parent = parent

        self._old_position = None

        self.ui.collapse_button.setIcon(QIcon(':/button/minimized.png'))
        self.ui.close_button.setIcon(QIcon(':/button/close.png'))

        # Signal - Slot
        self.ui.collapse_button.clicked.connect(self.minimize_window)
        self.ui.close_button.clicked.connect(self.close_window)

    def show_note(self, note_type, data):
        if note_type == 'text':
            text_note_widget = ShowTextNoteWidget(self, data)
            self.ui.verticalLayout.addWidget(text_note_widget)
            text_note_widget.show()
        elif note_type == 'voice':
            voice_note_widget = ShowVoiceNoteWidget(self, data)
            self.ui.verticalLayout.addWidget(voice_note_widget)
            voice_note_widget.show()
        elif note_type == 'video':
            video_note_widget = ShowVideoNoteWidget(self, data)
            self.ui.verticalLayout.addWidget(video_note_widget)
            video_note_widget.show()
        elif note_type == 'paint':
            paint_note_widget = ShowPaintNoteWidget(self, data)
            self.ui.verticalLayout.addWidget(paint_note_widget)
            paint_note_widget.show()
        elif note_type == 'todo':
            todo_note_widget = ShowTodoNoteWidget(self, data)
            self.ui.verticalLayout.addWidget(todo_note_widget)
            todo_note_widget.show()

    def create_note(self, note_type):
        if note_type == 'text':
            text_note_widget = CreateTextNoteWidget(self.parent())
            self.ui.verticalLayout.addWidget(text_note_widget)
            text_note_widget.show()
        elif note_type == 'voice':
            voice_note_widget = CreateVoiceNoteWidget(self.parent())
            self.ui.verticalLayout.addWidget(voice_note_widget)
            voice_note_widget.show()
        elif note_type == 'video':
            video_note_widget = CreateVideoNoteWidget(self.parent())
            self.ui.verticalLayout.addWidget(video_note_widget)
            video_note_widget.show()
        elif note_type == 'paint':
            pass
            # paint_note_widget = CreatePaintNoteWindow(self.parent())
            # self.ui.verticalLayout.addWidget(paint_note_widget)
            # paint_note_widget.show()
        elif note_type == 'todo':
            todo_note_widget = CreateTodoNoteWidget(self.parent())
            self.ui.verticalLayout.addWidget(todo_note_widget)
            todo_note_widget.show()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton and event.modifiers() == Qt.KeyboardModifier.NoModifier:
            self._old_position = event.pos()

    def mouseMoveEvent(self, event):
        if not self._old_position:
            return
        delta = event.pos() - self._old_position
        self.move(self.pos() + delta)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._old_position = None

    def closeEvent(self, *args):
        self._parent.update_view()

    def minimize_window(self):
        self.showMinimized()

    def close_window(self):
        self.close()
