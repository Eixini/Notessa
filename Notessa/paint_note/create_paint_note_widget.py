import json, uuid

from PySide6.QtWidgets import QWidget, QColorDialog, QMessageBox
from PySide6.QtCore import QSize, QDir, Qt, QDateTime
from Notessa.paint_note.ui_gen.ui_create_paintnote_widget import Ui_CreatePaintNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.common_modules.forming_note_name import forming_note_file_name


class CreatePaintNoteWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_CreatePaintNoteWidget()
        self.ui.setupUi(self)

        # Set a default note deadline -
        self.note_deadline = ' '

        # Default value
        self.ui.indefinite_checkbox.setChecked(True)
        self.ui.note_deadline_label.setDisabled(True)
        self.ui.note_date_time_edit.setDisabled(True)
        self.ui.note_date_time_edit.setDateTime(QDateTime.currentDateTime())

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

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
        self.ui.pen_width_double_spinbox.valueChanged.connect(self.pen_width_change)
        self.ui.color_button.clicked.connect(self.select_color)
        self.ui.indefinite_checkbox.checkStateChanged.connect(self.indefinite_change)
        self.ui.note_date_time_edit.dateTimeChanged.connect(self.select_date_time_change)

    def indefinite_change(self):
        if self.ui.indefinite_checkbox.isChecked():
            self.note_deadline = ' '
            self.ui.note_deadline_label.setDisabled(True)
            self.ui.note_date_time_edit.setDisabled(True)
        else:
            self.note_deadline = self.ui.note_date_time_edit.dateTime().toLocalTime()
            self.ui.note_deadline_label.setEnabled(True)
            self.ui.note_date_time_edit.setEnabled(True)

    def select_date_time_change(self):
        self.note_deadline = self.ui.note_date_time_edit.dateTime().toLocalTime()
        print(self.ui.note_date_time_edit.dateTime().toLocalTime())

    def pen_width_change(self):
        self.ui.painter_widget.set_pen_width(self.ui.pen_width_double_spinbox.value())

    def select_color(self):
        color = self._color_dialog.getColor()
        if color.isValid():
            self.ui.painter_widget.set_pen_color(color)

    def save(self):
        if self.date_time_check() == 'Correct' or self.date_time_check() == 'None':

            dir_checker = DirectoryChecker()

            note_name = self.ui.paintnote_name_lineedit.text()
            file_name = forming_note_file_name('PaintNote')
            file_path = str(f"{dir_checker.paint_notes_directory()}{QDir.separator()}{file_name}.png")
            meta_data_file_path = str(f'{dir_checker.paint_notes_directory()}{QDir.separator()}{file_name}.json')

            url = f'{QDir.toNativeSeparators(file_path)}'

            meta_data_content = {'note_name': note_name}

            if not self.note_deadline == ' ':
                meta_data_content.update({'deadline': self.note_deadline.toString()})
            else:
                meta_data_content.update({'deadline': ' '})

            note_uuid = uuid.uuid1()
            meta_data_content.update({'uuid': f'{note_uuid}'})

            with open(meta_data_file_path, 'w', encoding='utf-8') as file:
                json.dump(meta_data_content, file, indent=4)

            self.ui.painter_widget.save(url)
            self.close()
        else:
            msg_box = QMessageBox()
            msg_box.setText(u"The note's deadline date and time cannot be less than the current one")
            msg_box.setWindowTitle(u"Invalid value")
            msg_box.exec()
            return

    def date_time_check(self):
        """ To check the correctness of the note's deadline """
        if not self.note_deadline == ' ':
            if QDateTime.currentDateTime() < self.ui.note_date_time_edit.dateTime():
                return 'Correct'
            else:
                return 'Incorrect'
        else:
            return 'None'
