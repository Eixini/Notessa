# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note_list_gadget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_NoteListGadget(object):
    def setupUi(self, NoteListGadget):
        if not NoteListGadget.objectName():
            NoteListGadget.setObjectName(u"NoteListGadget")
        NoteListGadget.resize(397, 505)
        self.verticalLayout = QVBoxLayout(NoteListGadget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.create_note_button = QPushButton(NoteListGadget)
        self.create_note_button.setObjectName(u"create_note_button")
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(14)
        font.setBold(True)
        self.create_note_button.setFont(font)

        self.horizontalLayout.addWidget(self.create_note_button)

        self.horizontalSpacer = QSpacerItem(138, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pin_gadget_button = QPushButton(NoteListGadget)
        self.pin_gadget_button.setObjectName(u"pin_gadget_button")
        self.pin_gadget_button.setFont(font)

        self.horizontalLayout.addWidget(self.pin_gadget_button)

        self.close_button = QPushButton(NoteListGadget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setFont(font)

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableView = QTableView(NoteListGadget)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)


        self.retranslateUi(NoteListGadget)

        QMetaObject.connectSlotsByName(NoteListGadget)
    # setupUi

    def retranslateUi(self, NoteListGadget):
        NoteListGadget.setWindowTitle(QCoreApplication.translate("NoteListGadget", u"Form", None))
        self.create_note_button.setText(QCoreApplication.translate("NoteListGadget", u"+", None))
        self.pin_gadget_button.setText(QCoreApplication.translate("NoteListGadget", u"P", None))
        self.close_button.setText(QCoreApplication.translate("NoteListGadget", u"x", None))
    # retranslateUi

