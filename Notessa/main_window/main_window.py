from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon, QPixmap
from Notessa.main_window.ui_mainwindow import Ui_MainWindow
from Notessa.show_notes.show_notes_window import ShowNotesWindow
from Notessa.text_note.create_text_note_window import CreateTextNote
from Notessa.voice_note.create_voice_note_window import CreateVoiceNote
from Notessa.video_note.create_video_note_window import CreateVideoNote
from Notessa.paint_note.create_paint_note_window import CreatePaintNote

from Notessa.resource import rc_icons

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(QPixmap(':/resource/icons/notessa_logo.png')))

        # Setting icons for buttons
        self.ui.showNotesButton.setIcon(QIcon(QPixmap(':/resource/icons/list.png')))
        self.ui.createTextNoteButton.setIcon(QIcon(QPixmap(':/resource/icons/text.png')))
        self.ui.createVoiceNoteButton.setIcon(QIcon(QPixmap(':/resource/icons/microphone.png')))
        self.ui.createVideoNoteButton.setIcon(QIcon(QPixmap(':/resource/icons/video.png')))
        self.ui.createPaintNoteButton.setIcon(QIcon(QPixmap(':/resource/icons/brush.png')))
        self.ui.closeApplicationButton.setIcon(QIcon(QPixmap(':/resource/icons/exit.png')))

        # Signal - Slots
        self.ui.showNotesButton.clicked.connect(self.show_notes)
        self.ui.createTextNoteButton.clicked.connect(self.create_text_note)
        self.ui.createVoiceNoteButton.clicked.connect(self.create_voice_note)
        self.ui.createVideoNoteButton.clicked.connect(self.create_video_note)
        self.ui.createPaintNoteButton.clicked.connect(self.create_paint_note)
        self.ui.closeApplicationButton.clicked.connect(lambda: self.close())

    def show_notes(self):
        showNotes = ShowNotesWindow()
        showNotes.exec()

    def create_text_note(self):
        createTextNoteWindow = CreateTextNote()
        createTextNoteWindow.exec()

    def create_voice_note(self):
        createVoiceNoteWindow = CreateVoiceNote()
        createVoiceNoteWindow.exec()

    def create_video_note(self):
        createVideoNoteWindow = CreateVideoNote()
        createVideoNoteWindow.exec()

    def create_paint_note(self):
        createPaintNoteWindow = CreatePaintNote()
        createPaintNoteWindow.exec()
