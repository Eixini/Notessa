from PySide6.QtWidgets import QWidget, QFileDialog,  QColorDialog
from PySide6.QtGui import QResizeEvent, QRegularExpressionValidator
from PySide6.QtCore import QSize, QDir, QStandardPaths, Qt
from Notessa.paint_note.ui_gen.ui_create_paintnote_widget import Ui_CreatePaintNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker


class CreatePaintNoteWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_CreatePaintNoteWidget()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self.ui.paintnote_name_lineedit.setValidator(QRegularExpressionValidator('([a-zA-Zа-яА-Я0-9-_ ]){255}'))

        self.ui.pen_width_double_spinbox.setValue(5.0)

        """ Calculating the width and height of a PainterWidget """
        # Width of the current widget - margins on the sides
        painter_width = self.width() - self.contentsMargins().left() - self.contentsMargins().right()
        # Current widget height - padding top and bottom
        # - number of spaces between layouts (excluding 1 main one) * by the size of spaces
        # - height of button and input line
        painter_height = (self.height() - self.contentsMargins().top() - self.contentsMargins().bottom()
                          - ((self.layout().count() - 1) * self.layout().spacing())
                          - (self.ui.paintnote_name_lineedit.height() + self.ui.save_button.height()))

        self.ui.painter_widget.set_pixmap(QSize(painter_width, painter_height))

        # Color
        self._color_dialog = QColorDialog(self)

        # Signal - Slot
        self.ui.save_button.clicked.connect(self.save)
        self.ui.close_button.clicked.connect(self.close_note)
        self.ui.pen_width_double_spinbox.valueChanged.connect(self.pen_width_change)
        self.ui.color_button.clicked.connect(self.select_color)

    def pen_width_change(self):
        self.ui.painter_widget.set_pen_width(self.ui.pen_width_double_spinbox.value())

    def select_color(self):
        color = self._color_dialog.getColor()
        if color.isValid():
            self.ui.painter_widget.set_pen_color(color)

    def save(self):
        if not self.ui.paintnote_name_lineedit.text() == '':
            note_name = self.ui.paintnote_name_lineedit.text()
            dir_checker = DirectoryChecker()
            file = f'{dir_checker.paint_notes_directory()}{QDir.separator()}{note_name}.png'
            url = f'{QDir.toNativeSeparators(file)}'

            self.ui.painter_widget.save(url)
            self.close()
    def close_note(self):
        self.close()
