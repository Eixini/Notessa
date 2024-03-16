from PySide6.QtWidgets import QDialog, QHeaderView, QAbstractItemView
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSortFilterProxyModel, QRegularExpression
from Notessa.show_notes.ui_shownoteswindow import Ui_ShowNotesWindow

from Notessa.model.NotesModel import NotesModel
from Notessa.model.NoteItemDelegate import NoteItemDelegate
from Notessa.text_note.ShowTextNoteWindow import ShowTextNoteWindow
from Notessa.voice_note.ShowVoiceNoteWindow import ShowVoiceNoteWindow
from Notessa.video_note.ShowVideoNoteWindow import ShowVideoNoteWindow
from Notessa.paint_note.show_paint_note_window import ShowPaintNoteWindow
from Notessa.resource import rc_icons


class ShowNotesWindow(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_ShowNotesWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(':/resource/icons/list.png'))
        self.ui.toMainMenuButton.setIcon(QIcon(':/resource/icons/back.png'))
        self.ui.showNoteButton.setIcon(QIcon(':/resource/icons/info.png'))
        self.ui.deleteNoteButton.setIcon(QIcon(':/resource/icons/garbage.png'))

        # ComboBox
        self.ui.filterList.addItem('All notes')
        self.ui.filterList.addItem('Text notes')
        self.ui.filterList.addItem('Voice notes')
        self.ui.filterList.addItem('Video notes')
        self.ui.filterList.addItem('Paint notes')

        # Model
        self._note_model = NotesModel()

        # Sorting
        self._proxy_model = QSortFilterProxyModel()
        self._proxy_model.setDynamicSortFilter(False)
        self._proxy_model.setSourceModel(self._note_model)

        #TableView
        self.ui.notesTableView.setModel(self._proxy_model)
        self.ui.notesTableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.notesTableView.setItemDelegateForColumn(0, NoteItemDelegate())
        self.ui.notesTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.notesTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.notesTableView.setSortingEnabled(True)

        #Signal-Slot
        self.ui.toMainMenuButton.clicked.connect(lambda: self.accept())
        self.ui.deleteNoteButton.clicked.connect(self.delete_note)
        self.ui.showNoteButton.clicked.connect(self.show_note)
        self.ui.filterList.currentIndexChanged.connect(self.filter_notes)


    def delete_note(self):
        index = self.ui.notesTableView.currentIndex()
        proxy_index = self._proxy_model.mapToSource(index)
        self._note_model.removeRows(proxy_index.row(), 1, proxy_index)
        self._note_model.submit()

    def show_note(self):
        """Method for displaying a note.
        The note type is obtained and based on this,
        the appropriate representation is selected."""

        index = self.ui.notesTableView.currentIndex()
        sort_note_type = self._note_model.getNoteType(self._proxy_model.mapToSource(index))
        sort_index = self._proxy_model.mapToSource(index)

        data = self._note_model.getCurrentData(sort_index)
        if sort_note_type == 'txt':
            textNoteWindow = ShowTextNoteWindow(self, data)
            textNoteWindow.exec()
        elif sort_note_type == 'wav':
            voiceNoteWindow = ShowVoiceNoteWindow(self, data)
            voiceNoteWindow.exec()
        elif sort_note_type == 'mp4':
            videoNoteWindow = ShowVideoNoteWindow(self, data)
            videoNoteWindow.exec()
        elif sort_note_type == 'png':
            paintNoteWindow = ShowPaintNoteWindow(self, data)
            paintNoteWindow.exec()

    def filter_notes(self):
        index = self.ui.filterList.currentIndex()
        if index == 0:
            self._proxy_model.setFilterRegularExpression(QRegularExpression('\\w'))
            self._proxy_model.setFilterKeyColumn(0)
        elif index == 1:
            self._proxy_model.setFilterRegularExpression(QRegularExpression('txt'))
            self._proxy_model.setFilterKeyColumn(0)
        elif index == 2:
            self._proxy_model.setFilterRegularExpression(QRegularExpression('wav'))
            self._proxy_model.setFilterKeyColumn(0)
        elif index == 3:
            self._proxy_model.setFilterRegularExpression(QRegularExpression('mp4'))
            self._proxy_model.setFilterKeyColumn(0)
        elif index == 4:
            self._proxy_model.setFilterRegularExpression(QRegularExpression('png'))
            self._proxy_model.setFilterKeyColumn(0)
