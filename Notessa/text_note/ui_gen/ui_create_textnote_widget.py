# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_textnote_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QFontComboBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_CreateTextNoteWidget(object):
    def setupUi(self, CreateTextNoteWidget):
        if not CreateTextNoteWidget.objectName():
            CreateTextNoteWidget.setObjectName(u"CreateTextNoteWidget")
        CreateTextNoteWidget.resize(851, 737)
        self.verticalLayout = QVBoxLayout(CreateTextNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textnote_name_horizontal_layout = QHBoxLayout()
        self.textnote_name_horizontal_layout.setObjectName(u"textnote_name_horizontal_layout")
        self.textnote_name_label = QLabel(CreateTextNoteWidget)
        self.textnote_name_label.setObjectName(u"textnote_name_label")
        font = QFont()
        font.setBold(True)
        self.textnote_name_label.setFont(font)

        self.textnote_name_horizontal_layout.addWidget(self.textnote_name_label)

        self.textnote_name_lineedit = QLineEdit(CreateTextNoteWidget)
        self.textnote_name_lineedit.setObjectName(u"textnote_name_lineedit")

        self.textnote_name_horizontal_layout.addWidget(self.textnote_name_lineedit)


        self.verticalLayout.addLayout(self.textnote_name_horizontal_layout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.indefinite_checkbox = QCheckBox(CreateTextNoteWidget)
        self.indefinite_checkbox.setObjectName(u"indefinite_checkbox")

        self.horizontalLayout_2.addWidget(self.indefinite_checkbox)

        self.note_deadline_label = QLabel(CreateTextNoteWidget)
        self.note_deadline_label.setObjectName(u"note_deadline_label")

        self.horizontalLayout_2.addWidget(self.note_deadline_label)

        self.note_date_time_edit = QDateTimeEdit(CreateTextNoteWidget)
        self.note_date_time_edit.setObjectName(u"note_date_time_edit")
        self.note_date_time_edit.setMinimumDateTime(QDateTime(QDate(1970, 1, 1), QTime(0, 0, 0)))
        self.note_date_time_edit.setCalendarPopup(False)

        self.horizontalLayout_2.addWidget(self.note_date_time_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.font_size_label = QLabel(CreateTextNoteWidget)
        self.font_size_label.setObjectName(u"font_size_label")

        self.horizontalLayout_3.addWidget(self.font_size_label)

        self.font_size_spinbox = QSpinBox(CreateTextNoteWidget)
        self.font_size_spinbox.setObjectName(u"font_size_spinbox")

        self.horizontalLayout_3.addWidget(self.font_size_spinbox)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.font_label = QLabel(CreateTextNoteWidget)
        self.font_label.setObjectName(u"font_label")

        self.horizontalLayout_4.addWidget(self.font_label)

        self.font_combobox = QFontComboBox(CreateTextNoteWidget)
        self.font_combobox.setObjectName(u"font_combobox")

        self.horizontalLayout_4.addWidget(self.font_combobox)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.textnote_contents = QTextEdit(CreateTextNoteWidget)
        self.textnote_contents.setObjectName(u"textnote_contents")
        self.textnote_contents.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.textnote_contents)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_button = QPushButton(CreateTextNoteWidget)
        self.save_button.setObjectName(u"save_button")
        icon = QIcon()
        icon.addFile(u":/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon)
        self.save_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.save_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CreateTextNoteWidget)

        QMetaObject.connectSlotsByName(CreateTextNoteWidget)
    # setupUi

    def retranslateUi(self, CreateTextNoteWidget):
        CreateTextNoteWidget.setWindowTitle(QCoreApplication.translate("CreateTextNoteWidget", u"Form", None))
        self.textnote_name_label.setText(QCoreApplication.translate("CreateTextNoteWidget", u"Enter a note title", None))
        self.textnote_name_lineedit.setPlaceholderText(QCoreApplication.translate("CreateTextNoteWidget", u"Enter a note name...", None))
        self.indefinite_checkbox.setText(QCoreApplication.translate("CreateTextNoteWidget", u"Indefinite", None))
        self.note_deadline_label.setText(QCoreApplication.translate("CreateTextNoteWidget", u"Note deadline", None))
        self.font_size_label.setText(QCoreApplication.translate("CreateTextNoteWidget", u"Font size", None))
        self.font_label.setText(QCoreApplication.translate("CreateTextNoteWidget", u"Font", None))
        self.textnote_contents.setPlaceholderText(QCoreApplication.translate("CreateTextNoteWidget", u"Here you can start writing your note...", None))
        self.save_button.setText(QCoreApplication.translate("CreateTextNoteWidget", u"Save", None))
    # retranslateUi

