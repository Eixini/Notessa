# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_todo_note_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from Notessa.resource import icons_rc

class Ui_ShowTodoNoteWidget(object):
    def setupUi(self, ShowTodoNoteWidget):
        if not ShowTodoNoteWidget.objectName():
            ShowTodoNoteWidget.setObjectName(u"ShowTodoNoteWidget")
        ShowTodoNoteWidget.resize(772, 678)
        self.verticalLayout = QVBoxLayout(ShowTodoNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.todo_note_name_label = QLabel(ShowTodoNoteWidget)
        self.todo_note_name_label.setObjectName(u"todo_note_name_label")

        self.verticalLayout.addWidget(self.todo_note_name_label)

        self.todo_items_list_view = QListView(ShowTodoNoteWidget)
        self.todo_items_list_view.setObjectName(u"todo_items_list_view")

        self.verticalLayout.addWidget(self.todo_items_list_view)

        self.buttons_panel_horizontal_layout = QHBoxLayout()
        self.buttons_panel_horizontal_layout.setObjectName(u"buttons_panel_horizontal_layout")
        self.close_button = QPushButton(ShowTodoNoteWidget)
        self.close_button.setObjectName(u"close_button")
        icon = QIcon()
        icon.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setIconSize(QSize(32, 32))

        self.buttons_panel_horizontal_layout.addWidget(self.close_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttons_panel_horizontal_layout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.buttons_panel_horizontal_layout)


        self.retranslateUi(ShowTodoNoteWidget)

        QMetaObject.connectSlotsByName(ShowTodoNoteWidget)
    # setupUi

    def retranslateUi(self, ShowTodoNoteWidget):
        ShowTodoNoteWidget.setWindowTitle(QCoreApplication.translate("ShowTodoNoteWidget", u"Form", None))
        self.todo_note_name_label.setText(QCoreApplication.translate("ShowTodoNoteWidget", u"Todo note name", None))
        self.close_button.setText(QCoreApplication.translate("ShowTodoNoteWidget", u"Close", None))
    # retranslateUi

