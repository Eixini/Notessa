from PySide6.QtWidgets import QDialog, QFileDialog,  QColorDialog
from PySide6.QtGui import QIcon, QResizeEvent
from PySide6.QtCore import QSize, QDir, QStandardPaths
from Notessa.paint_note.ui_createpaintnote import Ui_CreatePaintNote
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.paint_note.painter_widget import PainterWidget
from Notessa.paint_note.save_messagebox import SaveMessageBox
from Notessa.paint_note.create_canvas_window import CreateCanvasWindow

from Notessa.resource import rc_icons

class CreatePaintNote(QDialog):
    def __init__(self, canvas_size):
        super().__init__()

        self.ui = Ui_CreatePaintNote()
        self.ui.setupUi(self)

        # The resulting size value for the canvas
        self._canvas_size = canvas_size
        print(canvas_size)

        # WINDOW_FIXED_SIZE = ENTERED_CANVAS_SIZE + (WINDOW_SIZE - ENTERED_CANVAS_SIZE)
        self.size_diff = QSize(22, 90)

        # Icon set
        self.setWindowIcon(QIcon(':/resource/icons/brush.png'))

        self._painter_widget = PainterWidget(self._canvas_size)
        self.ui.drawingLayout.addWidget(self._painter_widget)

        """ 
            The recommended minimum window width is 250 px, since there are buttons in the panel.
        """
        self.setFixedSize(self._canvas_size + self.size_diff)
        self.ui.penWidth.setValue(5.0)

        # Color
        self._color_dialog = QColorDialog(self)

        # Signal - Slot
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.openButton.clicked.connect(self.open)
        self.ui.backButton.clicked.connect(self.back)

        self.ui.penWidth.valueChanged.connect(self.pen_width_change)
        self.ui.colorButton.clicked.connect(self.select_color)

    def resizeEvent(self, event: QResizeEvent):
        """
        Designed to obtain the window size.
        This method was needed in order to calculate the parameters for fixing the window size.
        To the left of the equal sign, the value that was set after resizing using this event handler.
        WINDOW_FIXED_SIZE = ENTERED_CANVAS_SIZE + (WINDOW_SIZE - ENTERED_CANVAS_SIZE)
        """
        # print(event)
        pass

    def pen_width_change(self):
        self._painter_widget.set_pen_width(self.ui.penWidth.value())

    def select_color(self):
        color = self._color_dialog.getColor()
        if color.isValid():
            self._painter_widget.set_pen_color(color)

    def save(self):
        note_name = self.enter_note_name()

        dirChecker = DirectoryChecker()
        file = f'{dirChecker.paint_notes_directory()}{QDir.separator()}{note_name}.png'
        url = f'{QDir.toNativeSeparators(file)}'

        self._painter_widget.save(url)
        self.accept()

    def open(self):
        """ Selecting a file for subsequent installation """
        file_dialog = QFileDialog(self)
        file_dialog.setDirectory(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.HomeLocation))
        file_dialog.setWindowTitle('Select image')
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Images (*.png *.jpeg *.jpg *.bmp *.pbm *.xbm *.xpm *.ppm)")
        file_dialog.setViewMode(QFileDialog.ViewMode.List)

        filename = None

        if file_dialog.exec():
            filename = file_dialog.selectedFiles()[0]

        self._painter_widget.load(filename)

        self.setFixedSize(self._painter_widget.size() + self.size_diff)

    def enter_note_name(self):
        """ Method for entering a note name, which will then be used for the note file namea """
        message_box = SaveMessageBox()
        _, note_name = message_box.exec()
        return note_name

    def back(self):
        self.reject()
