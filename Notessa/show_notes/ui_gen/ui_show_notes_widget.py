# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_notes_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)
from Notessa.resource import icons_rc

class Ui_ShowNotesWidget(object):
    def setupUi(self, ShowNotesWidget):
        if not ShowNotesWidget.objectName():
            ShowNotesWidget.setObjectName(u"ShowNotesWidget")
        ShowNotesWidget.resize(1002, 648)
        self.verticalLayout_2 = QVBoxLayout(ShowNotesWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.show_notes_main_widget = QWidget(ShowNotesWidget)
        self.show_notes_main_widget.setObjectName(u"show_notes_main_widget")
        self.verticalLayout = QVBoxLayout(self.show_notes_main_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.up_horizontal_layout = QHBoxLayout()
        self.up_horizontal_layout.setObjectName(u"up_horizontal_layout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.up_horizontal_layout.addItem(self.horizontalSpacer_3)

        self.filter_label = QLabel(self.show_notes_main_widget)
        self.filter_label.setObjectName(u"filter_label")

        self.up_horizontal_layout.addWidget(self.filter_label)

        self.filter_combobox = QComboBox(self.show_notes_main_widget)
        self.filter_combobox.setObjectName(u"filter_combobox")

        self.up_horizontal_layout.addWidget(self.filter_combobox)


        self.verticalLayout.addLayout(self.up_horizontal_layout)

        self.notes_tableview = QTableView(self.show_notes_main_widget)
        self.notes_tableview.setObjectName(u"notes_tableview")
        self.notes_tableview.setFrameShape(QFrame.NoFrame)
        self.notes_tableview.setFrameShadow(QFrame.Plain)
        self.notes_tableview.setMidLineWidth(1)
        self.notes_tableview.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.notes_tableview.setGridStyle(Qt.NoPen)
        self.notes_tableview.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.notes_tableview)

        self.buttons_panel_horizontal_layout = QHBoxLayout()
        self.buttons_panel_horizontal_layout.setObjectName(u"buttons_panel_horizontal_layout")
        self.close_button = QPushButton(self.show_notes_main_widget)
        self.close_button.setObjectName(u"close_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setIconSize(QSize(32, 32))

        self.buttons_panel_horizontal_layout.addWidget(self.close_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttons_panel_horizontal_layout.addItem(self.horizontalSpacer_2)

        self.show_note_button = QPushButton(self.show_notes_main_widget)
        self.show_note_button.setObjectName(u"show_note_button")
        sizePolicy.setHeightForWidth(self.show_note_button.sizePolicy().hasHeightForWidth())
        self.show_note_button.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/icons/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.show_note_button.setIcon(icon1)
        self.show_note_button.setIconSize(QSize(32, 32))

        self.buttons_panel_horizontal_layout.addWidget(self.show_note_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttons_panel_horizontal_layout.addItem(self.horizontalSpacer)

        self.delete_note_button = QPushButton(self.show_notes_main_widget)
        self.delete_note_button.setObjectName(u"delete_note_button")
        self.delete_note_button.setFocusPolicy(Qt.StrongFocus)
        icon2 = QIcon()
        icon2.addFile(u":/icons/garbage.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_note_button.setIcon(icon2)
        self.delete_note_button.setIconSize(QSize(32, 32))

        self.buttons_panel_horizontal_layout.addWidget(self.delete_note_button)


        self.verticalLayout.addLayout(self.buttons_panel_horizontal_layout)


        self.verticalLayout_2.addWidget(self.show_notes_main_widget)


        self.retranslateUi(ShowNotesWidget)

        QMetaObject.connectSlotsByName(ShowNotesWidget)
    # setupUi

    def retranslateUi(self, ShowNotesWidget):
        ShowNotesWidget.setWindowTitle(QCoreApplication.translate("ShowNotesWidget", u"Form", None))
        self.filter_label.setText(QCoreApplication.translate("ShowNotesWidget", u"Show specific types of notes", None))
        self.filter_combobox.setPlaceholderText(QCoreApplication.translate("ShowNotesWidget", u"Show note types", None))
        self.close_button.setText(QCoreApplication.translate("ShowNotesWidget", u"Close", None))
        self.show_note_button.setText(QCoreApplication.translate("ShowNotesWidget", u"Show note", None))
        self.delete_note_button.setText(QCoreApplication.translate("ShowNotesWidget", u"Delete note", None))
    # retranslateUi

