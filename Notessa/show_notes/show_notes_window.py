from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QScrollBar
from PySide6.QtCore import QSortFilterProxyModel, QRegularExpression, Qt, QEvent
from Notessa.show_notes.ui_gen.ui_show_notes_widget import Ui_ShowNotesWidget

from Notessa.model.show_notes_model.notes_model import NotesModel
from Notessa.model.show_notes_model.note_item_delegate import NoteItemDelegate
from Notessa.text_note.show_textnote_widget import ShowTextNoteWidget
from Notessa.voice_note.show_voicenote_widget import ShowVoiceNoteWidget
from Notessa.video_note.show_videonote_widget import ShowVideoNoteWidget
from Notessa.paint_note.show_paint_note_widget import ShowPaintNoteWidget
from Notessa.todo_notes.show_todo_note_widget import ShowTodoNoteWidget


class ShowNotesWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_ShowNotesWidget()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        # ComboBox
        self.ui.filter_combobox.addItem('All notes')
        self.ui.filter_combobox.addItem('Text notes')
        self.ui.filter_combobox.addItem('Voice notes')
        self.ui.filter_combobox.addItem('Video notes')
        self.ui.filter_combobox.addItem('Paint notes')
        self.ui.filter_combobox.addItem('Todo notes')

        # Model
        self._note_model = NotesModel()

        # Sorting
        self._proxy_model = QSortFilterProxyModel()
        self._proxy_model.setDynamicSortFilter(False)
        self._proxy_model.setSourceModel(self._note_model)

        # TableView
        self.ui.notes_tableview.setModel(self._proxy_model)
        self.ui.notes_tableview.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.notes_tableview.setItemDelegateForColumn(0, NoteItemDelegate())
        self.ui.notes_tableview.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.notes_tableview.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.notes_tableview.setSortingEnabled(True)
        self.ui.notes_tableview.verticalHeader().hide()

        # Signal-Slot
        self.ui.close_button.clicked.connect(self.close_show_notes)
        self.ui.delete_note_button.clicked.connect(self.delete_note)
        self.ui.show_note_button.clicked.connect(self.show_note)
        self.ui.filter_combobox.currentIndexChanged.connect(self.filter_notes)

    def delete_note(self):
        index = self.ui.notes_tableview.currentIndex()
        proxy_index = self._proxy_model.mapToSource(index)
        self._note_model.removeRows(proxy_index.row(), 1, proxy_index)
        self._note_model.submit()

    def show_note(self):
        """
        Method for displaying a note.
        The note type is obtained and based on this,
        the appropriate representation is selected.

        The widget itself contains a central widget (self.ui.show_notes_main_widget).
        This is some kind of container.
        Thanks to this solution,it is possible to “replace” the current widget with
        the one being opened and there is no need to create an additional QStackedWidget or QMdiArea.
        This is necessary so that when using the hide() method,
        the "QEvent::HideToParent" event does not fire and the current widget, i.e. displaying a list of notes,
        does not close due to a false positive.
        """

        index = self.ui.notes_tableview.currentIndex()
        sort_note_type = self._note_model.getNoteType(self._proxy_model.mapToSource(index))
        sort_index = self._proxy_model.mapToSource(index)

        data = self._note_model.getCurrentData(sort_index)
        if sort_note_type == 'txt':
            text_note_widget = ShowTextNoteWidget(self, data)
            self.ui.show_notes_main_widget.hide()
            text_note_widget.show()
            text_note_widget.resize(self.width(), self.height())
        elif sort_note_type == 'wav':
            voice_note_widget = ShowVoiceNoteWidget(self, data)
            self.ui.show_notes_main_widget.hide()
            voice_note_widget.show()
            voice_note_widget.resize(self.width(), self.height())
        elif sort_note_type == 'mp4':
            video_note_widget = ShowVideoNoteWidget(self, data)
            self.ui.show_notes_main_widget.hide()
            video_note_widget.show()
            video_note_widget.resize(self.width(), self.height())
        elif sort_note_type == 'png':
            paint_note_widget = ShowPaintNoteWidget(self, data)
            self.ui.show_notes_main_widget.hide()
            paint_note_widget.show()
            paint_note_widget.resize(self.width(), self.height())
        elif sort_note_type == 'json':
            todo_note_widget = ShowTodoNoteWidget(self, data)
            self.ui.show_notes_main_widget.hide()
            todo_note_widget.show()
            todo_note_widget.resize(self.width(), self.height())

    def eventFilter(self, watched, event):
        """
        The event filter handles closing the "replaced" widget.
        After processing, everything falls into place, i.e. the main widget is displayed again.
        """
        # QEvent::HideToParent
        if event.type() == QEvent.Type.HideToParent:
            self.ui.show_notes_main_widget.show()
            return True
        else:
            return False

    def filter_notes(self):
        """ Filter allows you to display notes of the selected type """
        index = self.ui.filter_combobox.currentIndex()
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
        elif index == 5:
            self._proxy_model.setFilterRegularExpression(QRegularExpression('json'))
            self._proxy_model.setFilterKeyColumn(0)

    def close_show_notes(self):
        self.close()

    def __del__(self):
        # Disconnect Signal - Slot
        self.ui.close_button.clicked.disconnect(self.close_show_notes)
        self.ui.delete_note_button.clicked.disconnect(self.delete_note)
        self.ui.show_note_button.clicked.disconnect(self.show_note)
        self.ui.filter_combobox.currentIndexChanged.disconnect(self.filter_notes)
