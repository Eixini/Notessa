# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_textnote_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)
from Notessa.resource import icons_rc

class Ui_CreateTextNoteWidget(object):
    def setupUi(self, CreateTextNoteWidget):
        if not CreateTextNoteWidget.objectName():
            CreateTextNoteWidget.setObjectName(u"CreateTextNoteWidget")
        CreateTextNoteWidget.resize(975, 737)
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

        self.textnote_contents = QTextEdit(CreateTextNoteWidget)
        self.textnote_contents.setObjectName(u"textnote_contents")
        self.textnote_contents.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.textnote_contents)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.back_button = QPushButton(CreateTextNoteWidget)
        self.back_button.setObjectName(u"back_button")
        icon = QIcon()
        icon.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_button.setIcon(icon)
        self.back_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.back_button)

        self.horizontalSpacer = QSpacerItem(408, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_button = QPushButton(CreateTextNoteWidget)
        self.save_button.setObjectName(u"save_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon1)
        self.save_button.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(CreateTextNoteWidget)

        QMetaObject.connectSlotsByName(CreateTextNoteWidget)
    # setupUi

    def retranslateUi(self, CreateTextNoteWidget):
        CreateTextNoteWidget.setWindowTitle(QCoreApplication.translate("CreateTextNoteWidget", u"Form", None))
        self.textnote_name_label.setText(QCoreApplication.translate("CreateTextNoteWidget", u"Enter a note title", None))
        self.textnote_name_lineedit.setPlaceholderText(QCoreApplication.translate("CreateTextNoteWidget", u"Enter a note name...", None))
        self.textnote_contents.setPlaceholderText(QCoreApplication.translate("CreateTextNoteWidget", u"Here you can start writing your note...", None))
        self.back_button.setText(QCoreApplication.translate("CreateTextNoteWidget", u"Back", None))
        self.save_button.setText(QCoreApplication.translate("CreateTextNoteWidget", u"Save", None))
    # retranslateUi

