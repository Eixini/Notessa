# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_todo_note_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_CreateTodoNoteWidget(object):
    def setupUi(self, CreateTodoNoteWidget):
        if not CreateTodoNoteWidget.objectName():
            CreateTodoNoteWidget.setObjectName(u"CreateTodoNoteWidget")
        CreateTodoNoteWidget.resize(906, 633)
        self.verticalLayout = QVBoxLayout(CreateTodoNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.todo_note_name_label = QLabel(CreateTodoNoteWidget)
        self.todo_note_name_label.setObjectName(u"todo_note_name_label")

        self.horizontalLayout.addWidget(self.todo_note_name_label)

        self.todo_note_name_lineedit = QLineEdit(CreateTodoNoteWidget)
        self.todo_note_name_lineedit.setObjectName(u"todo_note_name_lineedit")

        self.horizontalLayout.addWidget(self.todo_note_name_lineedit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.indefinite_checkbox = QCheckBox(CreateTodoNoteWidget)
        self.indefinite_checkbox.setObjectName(u"indefinite_checkbox")

        self.horizontalLayout_2.addWidget(self.indefinite_checkbox)

        self.note_deadline_label = QLabel(CreateTodoNoteWidget)
        self.note_deadline_label.setObjectName(u"note_deadline_label")

        self.horizontalLayout_2.addWidget(self.note_deadline_label)

        self.note_date_time_edit = QDateTimeEdit(CreateTodoNoteWidget)
        self.note_date_time_edit.setObjectName(u"note_date_time_edit")
        self.note_date_time_edit.setMinimumDateTime(QDateTime(QDate(1970, 1, 1), QTime(0, 0, 0)))
        self.note_date_time_edit.setCalendarPopup(False)

        self.horizontalLayout_2.addWidget(self.note_date_time_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.note_item_horizontal_layout = QHBoxLayout()
        self.note_item_horizontal_layout.setObjectName(u"note_item_horizontal_layout")
        self.note_item_label = QLabel(CreateTodoNoteWidget)
        self.note_item_label.setObjectName(u"note_item_label")

        self.note_item_horizontal_layout.addWidget(self.note_item_label)

        self.note_item_lineedit = QLineEdit(CreateTodoNoteWidget)
        self.note_item_lineedit.setObjectName(u"note_item_lineedit")
        self.note_item_lineedit.setFocusPolicy(Qt.StrongFocus)

        self.note_item_horizontal_layout.addWidget(self.note_item_lineedit)

        self.add_item_button = QPushButton(CreateTodoNoteWidget)
        self.add_item_button.setObjectName(u"add_item_button")
        icon = QIcon()
        icon.addFile(u":/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_item_button.setIcon(icon)
        self.add_item_button.setIconSize(QSize(32, 32))

        self.note_item_horizontal_layout.addWidget(self.add_item_button)


        self.verticalLayout.addLayout(self.note_item_horizontal_layout)

        self.note_items_list_widget = QListWidget(CreateTodoNoteWidget)
        self.note_items_list_widget.setObjectName(u"note_items_list_widget")

        self.verticalLayout.addWidget(self.note_items_list_widget)

        self.buttons_panel_horizontal_layout = QHBoxLayout()
        self.buttons_panel_horizontal_layout.setObjectName(u"buttons_panel_horizontal_layout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttons_panel_horizontal_layout.addItem(self.horizontalSpacer_2)

        self.delete_button = QPushButton(CreateTodoNoteWidget)
        self.delete_button.setObjectName(u"delete_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/garbage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_button.setIcon(icon1)
        self.delete_button.setIconSize(QSize(32, 32))

        self.buttons_panel_horizontal_layout.addWidget(self.delete_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttons_panel_horizontal_layout.addItem(self.horizontalSpacer)

        self.save_button = QPushButton(CreateTodoNoteWidget)
        self.save_button.setObjectName(u"save_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon2)
        self.save_button.setIconSize(QSize(32, 32))

        self.buttons_panel_horizontal_layout.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.buttons_panel_horizontal_layout)


        self.retranslateUi(CreateTodoNoteWidget)

        QMetaObject.connectSlotsByName(CreateTodoNoteWidget)
    # setupUi

    def retranslateUi(self, CreateTodoNoteWidget):
        CreateTodoNoteWidget.setWindowTitle(QCoreApplication.translate("CreateTodoNoteWidget", u"Form", None))
        self.todo_note_name_label.setText(QCoreApplication.translate("CreateTodoNoteWidget", u"Enter note name", None))
        self.todo_note_name_lineedit.setPlaceholderText(QCoreApplication.translate("CreateTodoNoteWidget", u"For example, \u201cTo-do list for today\u201d", None))
        self.indefinite_checkbox.setText(QCoreApplication.translate("CreateTodoNoteWidget", u"Indefinite", None))
        self.note_deadline_label.setText(QCoreApplication.translate("CreateTodoNoteWidget", u"Note deadline", None))
        self.note_item_label.setText(QCoreApplication.translate("CreateTodoNoteWidget", u"Enter note item", None))
        self.note_item_lineedit.setPlaceholderText(QCoreApplication.translate("CreateTodoNoteWidget", u"For example, \u201cOrder new food for the cat\u201d", None))
        self.add_item_button.setText("")
        self.delete_button.setText("")
        self.save_button.setText("")
    # retranslateUi

