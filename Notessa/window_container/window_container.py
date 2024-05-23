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
from Notessa.paint_note.create_paint_note_widget import CreatePaintNoteWidget
from Notessa.todo_notes.create_todo_note_widget import CreateTodoNoteWidget


class WindowContainer(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_WindowContainer()
        self.ui.setupUi(self)

        # Signal - Slot

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
            text_note_widget = CreateTextNoteWidget(self)
            self.ui.verticalLayout.addWidget(text_note_widget)
            text_note_widget.show()
        elif note_type == 'voice':
            voice_note_widget = CreateVoiceNoteWidget(self)
            self.ui.verticalLayout.addWidget(voice_note_widget)
            voice_note_widget.show()
        elif note_type == 'video':
            video_note_widget = CreateVideoNoteWidget(self)
            self.ui.verticalLayout.addWidget(video_note_widget)
            video_note_widget.show()
        elif note_type == 'paint':
            paint_note_widget = CreatePaintNoteWidget(self)
            self.ui.verticalLayout.addWidget(paint_note_widget)
            paint_note_widget.show()
        elif note_type == 'todo':
            todo_note_widget = CreateTodoNoteWidget(self)
            self.ui.verticalLayout.addWidget(todo_note_widget)
            todo_note_widget.show()
