from PySide6.QtWidgets import QDialog, QTableWidgetItem, QHeaderView
from PySide6.QtGui import QIcon, QTextCharFormat, QBrush, QColor
from PySide6.QtCore import Qt, QDateTime, QDate

from Notessa.calendar_window.ui_gen.ui_calendar_window import Ui_CalendarWindow

from Notessa.resources.icons.button import button_icons_rc


class CalendarWindow(QDialog):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_CalendarWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(':/button/calendar.png'))

        self.data = data

        note_event_format = QTextCharFormat()
        note_event_format.setBackground(QBrush(QColor('#1D766F')))

        self.dates_and_times_strings = [res['deadline'] for res in self.data]
        self.dates_and_times = [QDateTime.fromString(res) for res in self.dates_and_times_strings]
        self.dates = [res.date() for res in self.dates_and_times]

        for date in self.dates:
            self.ui.calendar_widget.setDateTextFormat(date, note_event_format)

        # Signal - slot
        self.ui.calendar_widget.activated.connect(self.click_day)

    def click_day(self):

        self.ui.table_notes_widget.clear()

        self.ui.table_notes_widget.setColumnCount(2)
        self.ui.table_notes_widget.setHorizontalHeaderLabels(["Note name", "Time"])
        self.ui.table_notes_widget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.ui.table_notes_widget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.table_notes_widget.verticalHeader().hide()

        if self.ui.calendar_widget.selectedDate() in self.dates:

            list_events_in_day = list()

            for dt in self.dates_and_times:
                if dt.date() == self.ui.calendar_widget.selectedDate():
                    list_events_in_day.append(dt)

            self.ui.table_notes_widget.setRowCount(len(list_events_in_day))

            # Counter for insert row to table
            i = 0

            for note in self.data:
                for event_day in list_events_in_day:
                    if note['deadline'] == event_day.toString():

                        note_name_item = QTableWidgetItem(note['note_name'])
                        note_name_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
                        self.ui.table_notes_widget.setItem(i, 0, note_name_item)

                        note_deadline_time_item = QTableWidgetItem(event_day.time().toString())
                        note_deadline_time_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
                        self.ui.table_notes_widget.setItem(i, 1, note_deadline_time_item)

                        i += 1
