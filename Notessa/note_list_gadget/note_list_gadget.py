from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QScrollBar
from PySide6.QtCore import QSortFilterProxyModel, QRegularExpression, Qt, QEvent
from Notessa.note_list_gadget.ui_gen.ui_note_list_gadget import Ui_NoteListGadget


class NoteListGadget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_NoteListGadget()
        self.ui.setupUi(self)
