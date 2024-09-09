# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calendar_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDialog, QHeaderView,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_CalendarWindow(object):
    def setupUi(self, CalendarWindow):
        if not CalendarWindow.objectName():
            CalendarWindow.setObjectName(u"CalendarWindow")
        CalendarWindow.resize(779, 621)
        self.verticalLayout = QVBoxLayout(CalendarWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 3, 0, 0)
        self.calendar_widget = QCalendarWidget(CalendarWindow)
        self.calendar_widget.setObjectName(u"calendar_widget")

        self.verticalLayout.addWidget(self.calendar_widget)

        self.table_notes_widget = QTableWidget(CalendarWindow)
        self.table_notes_widget.setObjectName(u"table_notes_widget")

        self.verticalLayout.addWidget(self.table_notes_widget)


        self.retranslateUi(CalendarWindow)

        QMetaObject.connectSlotsByName(CalendarWindow)
    # setupUi

    def retranslateUi(self, CalendarWindow):
        CalendarWindow.setWindowTitle(QCoreApplication.translate("CalendarWindow", u"Calendar window", None))
    # retranslateUi

