# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_menu_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainMenuWidget(object):
    def setupUi(self, MainMenuWidget):
        if not MainMenuWidget.objectName():
            MainMenuWidget.setObjectName(u"MainMenuWidget")
        MainMenuWidget.resize(311, 300)
        self.verticalLayout = QVBoxLayout(MainMenuWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.show_notes_button = QPushButton(MainMenuWidget)
        self.show_notes_button.setObjectName(u"show_notes_button")

        self.verticalLayout.addWidget(self.show_notes_button)

        self.verticalSpacer = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.create_text_note_button = QPushButton(MainMenuWidget)
        self.create_text_note_button.setObjectName(u"create_text_note_button")

        self.verticalLayout.addWidget(self.create_text_note_button)

        self.create_voice_note_button = QPushButton(MainMenuWidget)
        self.create_voice_note_button.setObjectName(u"create_voice_note_button")

        self.verticalLayout.addWidget(self.create_voice_note_button)

        self.create_video_note_button = QPushButton(MainMenuWidget)
        self.create_video_note_button.setObjectName(u"create_video_note_button")

        self.verticalLayout.addWidget(self.create_video_note_button)

        self.create_paint_note_button = QPushButton(MainMenuWidget)
        self.create_paint_note_button.setObjectName(u"create_paint_note_button")

        self.verticalLayout.addWidget(self.create_paint_note_button)

        self.create_todo_note_button = QPushButton(MainMenuWidget)
        self.create_todo_note_button.setObjectName(u"create_todo_note_button")

        self.verticalLayout.addWidget(self.create_todo_note_button)

        self.verticalSpacer_2 = QSpacerItem(20, 16, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.settings_button = QPushButton(MainMenuWidget)
        self.settings_button.setObjectName(u"settings_button")

        self.verticalLayout.addWidget(self.settings_button)


        self.retranslateUi(MainMenuWidget)

        QMetaObject.connectSlotsByName(MainMenuWidget)
    # setupUi

    def retranslateUi(self, MainMenuWidget):
        MainMenuWidget.setWindowTitle(QCoreApplication.translate("MainMenuWidget", u"Form", None))
        self.show_notes_button.setText(QCoreApplication.translate("MainMenuWidget", u"Show Notes", None))
        self.create_text_note_button.setText(QCoreApplication.translate("MainMenuWidget", u"Create Text note", None))
        self.create_voice_note_button.setText(QCoreApplication.translate("MainMenuWidget", u"Create Voice note", None))
        self.create_video_note_button.setText(QCoreApplication.translate("MainMenuWidget", u"Create Video note", None))
        self.create_paint_note_button.setText(QCoreApplication.translate("MainMenuWidget", u"Create Paint note", None))
        self.create_todo_note_button.setText(QCoreApplication.translate("MainMenuWidget", u"Create Todo note", None))
        self.settings_button.setText(QCoreApplication.translate("MainMenuWidget", u"Settings", None))
    # retranslateUi

