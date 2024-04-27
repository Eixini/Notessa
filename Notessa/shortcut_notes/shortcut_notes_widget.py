from PySide6.QtCore import QSettings, QDir, QUrl, Qt, QEvent
from PySide6.QtGui import QIcon, QPixmap, QMouseEvent
from PySide6.QtWidgets import QWidget
from Notessa.shortcut_notes.ui_gen.ui_shortcut_notes_widget import Ui_ShortcutNotesWidget
from Notessa.model.shortcut_notes_model.shortcut_notes_model import TreeModel
from Notessa.resource import rc_icons

class ShortcutNotesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShortcutNotesWidget()
        self.ui.setupUi(self)

        #  Settings for frameless window and components for it
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        # self.setAttribute(Qt.WA_NoSystemBackground)
        self._old_position = None

        self.settings = QSettings('Notessa')
        self.position = None
        self.gadget_fix = False

        self.ui.fix_position_button.setText('')
        self.ui.close_button.setText('')
        self.ui.close_button.setIcon(QPixmap(':/icons/close.png').scaledToWidth(50).scaledToHeight(50))

        try:
            if self.settings.value('PinState') == 'true':
                self.gadget_fix = True
                self.move(self.settings.value('GadgetPosition'))
            elif self.settings.value('PinState') == 'false':
                self.gadget_fix = False
                self.move(self.settings.value('GadgetPosition'))
        except Exception as err:
            print(err)

        if self.gadget_fix:
            self.ui.fix_position_button.setIcon(QPixmap(':/icons/pin.png').scaledToWidth(50).scaledToHeight(50))
        else:
            self.ui.fix_position_button.setIcon(QPixmap(':/icons/unpin.png').scaledToWidth(50).scaledToHeight(50))

        self.model = TreeModel()
        self.ui.notes_treeview.setModel(self.model)

        self.ui.fix_position_button.clicked.connect(self.fix_widget_position)
        self.ui.close_button.clicked.connect(self.close_widget)

    def fix_widget_position(self):
        self.gadget_fix = not self.gadget_fix
        self.settings.remove('PinState')

        if self.gadget_fix:
            self.settings.setValue('PinState', 'false')
            self.ui.fix_position_button.setIcon(QPixmap(':/icons/pin.png').scaledToWidth(50).scaledToHeight(50))
        else:
            self.settings.setValue('PinState', 'true')
            self.ui.fix_position_button.setIcon(QPixmap(':/icons/unpin.png').scaledToWidth(50).scaledToHeight(50))

    def close_widget(self):
        self.close()

    def mousePressEvent(self, event: QMouseEvent):
        if self.gadget_fix:
            if event.button() == Qt.MouseButton.LeftButton and event.modifiers() == Qt.KeyboardModifier.NoModifier:
                self._old_position = event.pos()

    def mouseMoveEvent(self, event):
        if not self._old_position:
            return
        if self.gadget_fix:
            delta = event.pos() - self._old_position
            self.move(self.pos() + delta)

            self.settings.remove('GadgetPosition')
            self.settings.setValue('GadgetPosition', self.pos() + delta)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self._old_position = None
