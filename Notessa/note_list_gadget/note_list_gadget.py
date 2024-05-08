from PySide6.QtWidgets import QWidget, QHeaderView, QAbstractItemView, QMenu
from PySide6.QtCore import QSortFilterProxyModel, Qt, QEvent, QSettings, QPoint
from PySide6.QtGui import QIcon, QPixmap, QMouseEvent, QAction, QCursor
from Notessa.note_list_gadget.ui_gen.ui_note_list_gadget import Ui_NoteListGadget
from Notessa.note_creation_menu.note_creation_menu_widget import NoteCreationMenuWidget
from Notessa.model.notelist_tree_model.shortcut_notes_model import TreeModel
from Notessa.model.notelist_table_model.notes_model import NotesModel
from Notessa.model.notelist_table_model.note_item_delegate import NoteItemDelegate
from Notessa.resources.icons.button import button_icons_rc


class NoteListGadget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.ui = Ui_NoteListGadget()
        self.ui.setupUi(self)

        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)

        self.gadget_position = None
        self._old_position = None
        self.gadget_pin = False

        self.settings = QSettings(self)

        try:
            # Position of the note list window
            if self.settings.value('PinState') == 'true':
                self.gadget_pin = True
                self.move(self.settings.value('GadgetPosition'))
            elif self.settings.value('PinState') == 'false':
                self.gadget_pin = False
                self.move(self.settings.value('GadgetPosition'))

            # Setting View
            if self.settings.value('ViewMode') == 'TreeView':
                self.ui.tree_view.setVisible(True)
                self.ui.table_view.setVisible(False)
                self.view_model = TreeModel()
                self.ui.tree_view.setModel(self.view_model)

                self.ui.view_mode_button.setIcon(QPixmap(':/button/table_view.png').scaledToWidth(25).scaledToHeight(25))
            elif self.settings.value('ViewMode') == 'TableView':
                self.ui.table_view.setVisible(True)
                self.ui.tree_view.setVisible(False)
                self.view_model = NotesModel()
                self.ui.table_view.setModel(self.view_model)

                self.ui.view_mode_button.setIcon(QPixmap(':/button/tree_view.png').scaledToWidth(25).scaledToHeight(25))
            else:
                # Default
                self.ui.tree_view.setVisible(True)
                self.ui.table_view.setVisible(False)
                self.view_model = TreeModel()
                self.ui.tree_view.setModel(self.view_model)

                self.settings.setValue('ViewMode', 'TreeView')

                self.ui.view_mode_button.setIcon(QPixmap(':/button/table_view.png').scaledToWidth(25).scaledToHeight(25))

        except Exception as err:
            print(err)

        # Set Icon
        if self.gadget_pin:
            self.ui.pin_gadget_button.setIcon(QPixmap(':/button/unpin.png').scaledToWidth(25).scaledToHeight(25))
        else:
            self.ui.pin_gadget_button.setIcon(QPixmap(':/button/pin.png').scaledToWidth(25).scaledToHeight(25))

        # Sorting
        self._proxy_model = QSortFilterProxyModel()
        self._proxy_model.setDynamicSortFilter(False)
        self._proxy_model.setSourceModel(self.view_model)

        # TableView
        self.ui.table_view.setModel(self._proxy_model)
        self.ui.table_view.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.table_view.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.ui.table_view.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.table_view.setItemDelegateForColumn(0, NoteItemDelegate())
        self.ui.table_view.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.ui.table_view.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.ui.table_view.setSortingEnabled(True)
        self.ui.table_view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.table_view.verticalHeader().hide()

        # Create new note Widget
        self.note_creation_menu = NoteCreationMenuWidget(parent)

        # Signal - Slot
        self.ui.create_note_button.clicked.connect(self.open_note_creation_menu)
        self.ui.view_mode_button.clicked.connect(self.change_view_mode)
        self.ui.pin_gadget_button.clicked.connect(self.pin_widget_position)
        self.ui.close_button.clicked.connect(self.gadget_close)
        self.ui.table_view.customContextMenuRequested.connect(self.contex_menu)

    def open_note_creation_menu(self):
        self.note_creation_menu.setVisible(True)

    def change_view_mode(self):
        if self.settings.value('ViewMode') == 'TableView':
            self.ui.tree_view.setVisible(True)
            self.ui.table_view.setVisible(False)
            self.view_model = TreeModel()
            self.ui.tree_view.setModel(self.view_model)

            self.settings.remove('ViewMode')
            self.settings.setValue('ViewMode', 'TreeView')

            self.ui.view_mode_button.setIcon(QPixmap(':/button/table_view.png'))

        elif self.settings.value('ViewMode') == 'TreeView':
            self.ui.table_view.setVisible(True)
            self.ui.tree_view.setVisible(False)
            self.view_model = NotesModel()
            self.ui.table_view.setModel(self.view_model)

            self.settings.remove('ViewMode')
            self.settings.setValue('ViewMode', 'TableView')

            self.ui.view_mode_button.setIcon(QPixmap(':/button/tree_view.png'))

    def pin_widget_position(self):
        self.gadget_pin = not self.gadget_pin
        self.settings.remove('PinState')

        if self.gadget_pin:
            self.settings.setValue('PinState', self.gadget_pin)
            self.ui.pin_gadget_button.setIcon(QPixmap(':/button/unpin.png').scaledToWidth(25).scaledToHeight(25))
        else:
            self.settings.setValue('PinState', self.gadget_pin)
            self.ui.pin_gadget_button.setIcon(QPixmap(':/button/pin.png').scaledToWidth(25).scaledToHeight(25))

    def mousePressEvent(self, event: QMouseEvent):
        if not self.gadget_pin:
            if event.button() == Qt.MouseButton.LeftButton and event.modifiers() == Qt.KeyboardModifier.NoModifier:
                self._old_position = event.pos()

    def mouseMoveEvent(self, event):
        if not self._old_position:
            return
        if not self.gadget_pin:
            delta = event.pos() - self._old_position
            self.move(self.pos() + delta)

            self.settings.remove('GadgetPosition')
            self.settings.setValue('GadgetPosition', self.pos() + delta)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._old_position = None

    def contex_menu(self):
        print(f'Contex menu method called!')
        if self.ui.table_view.underMouse():
            print(f'self.ui.table_view.underMouse(): called!')
            self.table_item_context_menu = QMenu(self)
            open_note_action = QAction(u'Open', self)

            self.table_item_context_menu.addAction(open_note_action)
            open_note_action.triggered.connect(self.open_note)

            self.table_item_context_menu.popup(QCursor.pos())

    def open_note(self):
        if self.settings.value('ViewMode') == 'TableView':
            index = self.ui.table_view.currentIndex()
            sort_note_type = self.view_model.getNoteType(self._proxy_model.mapToSource(index))
            sort_index = self._proxy_model.mapToSource(index)

            data = self.view_model.getCurrentData(sort_index)

            print(data)

    def gadget_close(self):
        self.close()
