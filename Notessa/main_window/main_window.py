from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QMouseEvent
from Notessa.main_window.ui_gen.ui_main_window import Ui_MainWindow
from Notessa.show_notes.show_notes_window import ShowNotesWidget
from Notessa.text_note.create_textnote_widget import CreateTextNoteWidget
from Notessa.voice_note.create_voice_note_widget import CreateVoiceNoteWidget
from Notessa.video_note.create_video_note_widget import CreateVideoNoteWidget
from Notessa.paint_note.create_paint_note_widget import CreatePaintNoteWidget
from Notessa.todo_notes.create_todo_note_widget import CreateTodoNoteWidget
from Notessa.settings.settings_widget import SettingsWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #  Settings for frameless window and components for it
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_NoSystemBackground)
        self._old_position = None

        self.ui.folded_sidebar.hide()

        # StatuBar is planned to be used instead of QMessageBox
        self.statusBar().hide()

        # To store the value of an open widget
        self._widget_stack = dict()

        # Signal - Slot
        self.ui.es_shownotes_button.clicked.connect(self.open_show_notes_widget)
        self.ui.fs_shownotes_button.clicked.connect(self.open_show_notes_widget)

        self.ui.es_create_textnote_button.clicked.connect(self.open_create_text_note_widget)
        self.ui.fs_create_textnote_button.clicked.connect(self.open_create_text_note_widget)

        self.ui.es_create_voicenote_button.clicked.connect(self.open_create_voice_note_widget)
        self.ui.fs_create_voicenote_button.clicked.connect(self.open_create_voice_note_widget)

        self.ui.es_create_videonote_button.clicked.connect(self.open_create_video_note_widget)
        self.ui.fs_create_videonote_button.clicked.connect(self.open_create_video_note_widget)

        self.ui.es_create_paintnote_button.clicked.connect(self.open_create_paint_note_widget)
        self.ui.fs_create_paintnote_button.clicked.connect(self.open_create_paint_note_widget)

        self.ui.es_create_todonote_button.clicked.connect(self.open_create_todo_note_widget)
        self.ui.fs_create_todonote_button.clicked.connect(self.open_create_todo_note_widget)

        self.ui.es_settings_button.clicked.connect(self.open_settings_widget)
        self.ui.fs_settings_button.clicked.connect(self.open_settings_widget)

        self.ui.es_exit_button.clicked.connect(self.close_app)
        self.ui.fs_exit_button.clicked.connect(self.close_app)

    def open_show_notes_widget(self):
        create_show_notes_widget = ShowNotesWidget(self)
        self._widget_stack['ShowNotesWidget'] = create_show_notes_widget
        self.ui.content_stacked.addWidget(self._widget_stack['ShowNotesWidget'])

        print(f'Widget add. Current count in stack: {self.ui.content_stacked.count()}')
        self.ui.expanded_sidebar.hide()
        self.ui.folded_sidebar.show()

    def open_create_text_note_widget(self):
        create_text_note_widget = CreateTextNoteWidget(self)
        self._widget_stack['CreateTextNoteWidget'] = create_text_note_widget
        self.ui.content_stacked.addWidget(self._widget_stack['CreateTextNoteWidget'])

        print(f'Widget add. Current count in stack: {self.ui.content_stacked.count()}')
        self.ui.expanded_sidebar.hide()
        self.ui.folded_sidebar.show()

    def open_create_voice_note_widget(self):
        create_voice_note_widget = CreateVoiceNoteWidget(self)
        self._widget_stack['CreateVoiceNoteWidget'] = create_voice_note_widget
        self.ui.content_stacked.addWidget(self._widget_stack['CreateVoiceNoteWidget'])

        print(f'Widget add. Current count in stack: {self.ui.content_stacked.count()}')
        self.ui.expanded_sidebar.hide()
        self.ui.folded_sidebar.show()

    def open_create_video_note_widget(self):
        create_video_note_widget = CreateVideoNoteWidget(self)
        self._widget_stack['CreateVideoNoteWidget'] = create_video_note_widget
        self.ui.content_stacked.addWidget(self._widget_stack['CreateVideoNoteWidget'])

        print(f'Widget add. Current count in stack: {self.ui.content_stacked.count()}')
        self.ui.expanded_sidebar.hide()
        self.ui.folded_sidebar.show()

    def open_create_paint_note_widget(self):
        create_video_note_widget = CreatePaintNoteWidget(self)
        self._widget_stack['CreatePaintNoteWidget'] = create_video_note_widget
        self.ui.content_stacked.addWidget(self._widget_stack['CreatePaintNoteWidget'])

        print(f'Widget add. Current count in stack: {self.ui.content_stacked.count()}')
        self.ui.expanded_sidebar.hide()
        self.ui.folded_sidebar.show()

    def open_create_todo_note_widget(self):
        create_todo_note_widget = CreateTodoNoteWidget(self)
        self._widget_stack['CreateTodoNoteWidget'] = create_todo_note_widget
        self.ui.content_stacked.addWidget(self._widget_stack['CreateTodoNoteWidget'])

        print(f'Widget add. Current count in stack: {self.ui.content_stacked.count()}')
        self.ui.expanded_sidebar.hide()
        self.ui.folded_sidebar.show()

    def open_settings_widget(self):
        settings_widget = SettingsWidget(self)
        self._widget_stack['SettingsWidget'] = settings_widget
        self.ui.content_stacked.addWidget(self._widget_stack['SettingsWidget'])

        print(f'Widget add. Current count in stack: {self.ui.content_stacked.count()}')
        self.ui.expanded_sidebar.hide()
        self.ui.folded_sidebar.show()

    def eventFilter(self, watched, event):
        # QEvent::HideToParent
        if event.type() == QEvent.Type.HideToParent and watched.objectName() == 'ShowNotesWidget':
            if 'ShowNotesWidget' in self._widget_stack:
                self.ui.content_stacked.removeWidget(self._widget_stack['ShowNotesWidget'])
                self._widget_stack.pop('ShowNotesWidget')
            print(f'Widget remove. Current count in stack: {self.ui.content_stacked.count()}')
            if self.ui.content_stacked.count() == 0:
                self.ui.folded_sidebar.hide()
                self.ui.expanded_sidebar.show()
            return True
        elif event.type() == QEvent.Type.HideToParent and watched.objectName() == 'CreateTextNoteWidget':
            if 'CreateTextNoteWidget' in self._widget_stack:
                self.ui.content_stacked.removeWidget(self._widget_stack['CreateTextNoteWidget'])
                self._widget_stack.pop('CreateTextNoteWidget')
            print(f'Widget remove. Current count in stack: {self.ui.content_stacked.count()}')
            if self.ui.content_stacked.count() == 0:
                self.ui.folded_sidebar.hide()
                self.ui.expanded_sidebar.show()
            return True
        elif event.type() == QEvent.Type.HideToParent and watched.objectName() == 'CreateVoiceNoteWidget':
            if 'CreateVoiceNoteWidget' in self._widget_stack:
                self.ui.content_stacked.removeWidget(self._widget_stack['CreateVoiceNoteWidget'])
                self._widget_stack.pop('CreateVoiceNoteWidget')
            print(f'Widget remove. Current count in stack: {self.ui.content_stacked.count()}')
            if self.ui.content_stacked.count() == 0:
                self.ui.folded_sidebar.hide()
                self.ui.expanded_sidebar.show()
            return True
        elif event.type() == QEvent.Type.HideToParent and watched.objectName() == 'CreateVideoNoteWidget':
            if 'CreateVideoNoteWidget' in self._widget_stack:
                self.ui.content_stacked.removeWidget(self._widget_stack['CreateVideoNoteWidget'])
                self._widget_stack.pop('CreateVideoNoteWidget')
            print(f'Widget remove. Current count in stack: {self.ui.content_stacked.count()}')
            if self.ui.content_stacked.count() == 0:
                self.ui.folded_sidebar.hide()
                self.ui.expanded_sidebar.show()
            return True
        elif event.type() == QEvent.Type.HideToParent and watched.objectName() == 'CreatePaintNoteWidget':
            if 'CreatePaintNoteWidget' in self._widget_stack:
                self.ui.content_stacked.removeWidget(self._widget_stack['CreatePaintNoteWidget'])
                self._widget_stack.pop('CreatePaintNoteWidget')
            print(f'Widget remove. Current count in stack: {self.ui.content_stacked.count()}')
            if self.ui.content_stacked.count() == 0:
                self.ui.folded_sidebar.hide()
                self.ui.expanded_sidebar.show()
            return True
        elif event.type() == QEvent.Type.HideToParent and watched.objectName() == 'CreateTodoNoteWidget':
            if 'CreateTodoNoteWidget' in self._widget_stack:
                self.ui.content_stacked.removeWidget(self._widget_stack['CreateTodoNoteWidget'])
                self._widget_stack.pop('CreateTodoNoteWidget')
            print(f'Widget remove. Current count in stack: {self.ui.content_stacked.count()}')
            if self.ui.content_stacked.count() == 0:
                self.ui.folded_sidebar.hide()
                self.ui.expanded_sidebar.show()
            return True
        elif event.type() == QEvent.Type.HideToParent and watched.objectName() == 'SettingsWidget':
            if 'SettingsWidget' in self._widget_stack:
                self.ui.content_stacked.removeWidget(self._widget_stack['SettingsWidget'])
                self._widget_stack.pop('SettingsWidget')
            print(f'Widget remove. Current count in stack: {self.ui.content_stacked.count()}')
            if self.ui.content_stacked.count() == 0:
                self.ui.folded_sidebar.hide()
                self.ui.expanded_sidebar.show()
            return True
        elif event and watched.objectName() == 'CreatePaintNoteWidget':
            # print(event)
            return True
        else:
            return False

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

    def close_app(self):
        self.close()
