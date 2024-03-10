from PySide6.QtWidgets import QDialog, QWidget, QHeaderView, QAbstractItemView
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, Slot, QFile, QDateTime, QDir, QModelIndex
from Notessa.windows.ui_shownoteswindow import Ui_ShowNotesWindow
from Notessa.model.NotesModel import NotesModel
from Notessa.settings.directory_checker import DirectoryChecker
from Notessa.NoteItemDelegate import NoteItemDelegate
from Notessa.note_windows.ShowTextNoteWindow import ShowTextNoteWindow
from Notessa import rc_icons


class ShowNotesWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShowNotesWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(':/resource/icons/list.png'))
        self.ui.toMainMenuButton.setIcon(QIcon(':/resource/icons/back.png'))
        self.ui.showNoteButton.setIcon(QIcon(':/resource/icons/info.png'))
        self.ui.deleteNoteButton.setIcon(QIcon(':/resource/icons/garbage.png'))

        # Model
        self.noteModel = NotesModel()
        self.ui.notesTableView.setModel(self.noteModel)

        #TableView
        self.ui.notesTableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.notesTableView.setItemDelegateForColumn(0, NoteItemDelegate())
        self.ui.notesTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.notesTableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        #Signal-Slot
        self.ui.toMainMenuButton.clicked.connect(lambda: self.accept())
        self.ui.deleteNoteButton.clicked.connect(self.delete_note)
        self.ui.showNoteButton.clicked.connect(self.show_note)


    def delete_note(self):
        index = self.ui.notesTableView.currentIndex()
        self.noteModel.removeRows(index.row(), 1, index)


    def show_note(self):
        """Method for displaying a note.
        The note type is obtained and based on this,
        the appropriate representation is selected."""
        index = self.ui.notesTableView.currentIndex()
        noteType = self.noteModel.getNoteType(index)
        data = self.noteModel.getCurrentData(index)
        if noteType == 'txt':
            textNoteWindow = ShowTextNoteWindow(data)
            textNoteWindow.exec()
        elif noteType == 'wav':
            pass
