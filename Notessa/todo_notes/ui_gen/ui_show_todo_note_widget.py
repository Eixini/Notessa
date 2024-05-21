# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_todo_note_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QListView,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ShowTodoNoteWidget(object):
    def setupUi(self, ShowTodoNoteWidget):
        if not ShowTodoNoteWidget.objectName():
            ShowTodoNoteWidget.setObjectName(u"ShowTodoNoteWidget")
        ShowTodoNoteWidget.resize(841, 679)
        self.verticalLayout = QVBoxLayout(ShowTodoNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.todo_note_name_label = QLabel(ShowTodoNoteWidget)
        self.todo_note_name_label.setObjectName(u"todo_note_name_label")

        self.verticalLayout.addWidget(self.todo_note_name_label)

        self.todo_items_list_view = QListView(ShowTodoNoteWidget)
        self.todo_items_list_view.setObjectName(u"todo_items_list_view")

        self.verticalLayout.addWidget(self.todo_items_list_view)


        self.retranslateUi(ShowTodoNoteWidget)

        QMetaObject.connectSlotsByName(ShowTodoNoteWidget)
    # setupUi

    def retranslateUi(self, ShowTodoNoteWidget):
        ShowTodoNoteWidget.setWindowTitle(QCoreApplication.translate("ShowTodoNoteWidget", u"Dialog", None))
        self.todo_note_name_label.setText(QCoreApplication.translate("ShowTodoNoteWidget", u"Todo note name", None))
    # retranslateUi

