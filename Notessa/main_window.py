from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, Slot
from windows.ui_mainwindow import Ui_MainWindow
from show_notes_window import ShowNotesWindow
from create_text_note_window import CreateTextNote

import rc_icons

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
        self.ui.closeApplicationButton.clicked.connect(lambda: self.close())



    def show_notes(self):
        showNotes = ShowNotesWindow()
        showNotes.exec()

    def create_text_note(self):
        createTextNoteWindow = CreateTextNote()
        createTextNoteWindow.exec()
