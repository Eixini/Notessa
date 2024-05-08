# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note_creation_menu_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_NoteCreationMenuWidget(object):
    def setupUi(self, NoteCreationMenuWidget):
        if not NoteCreationMenuWidget.objectName():
            NoteCreationMenuWidget.setObjectName(u"NoteCreationMenuWidget")
        NoteCreationMenuWidget.resize(311, 300)
        self.verticalLayout = QVBoxLayout(NoteCreationMenuWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.create_text_note_button = QPushButton(NoteCreationMenuWidget)
        self.create_text_note_button.setObjectName(u"create_text_note_button")

        self.verticalLayout.addWidget(self.create_text_note_button)

        self.create_voice_note_button = QPushButton(NoteCreationMenuWidget)
        self.create_voice_note_button.setObjectName(u"create_voice_note_button")

        self.verticalLayout.addWidget(self.create_voice_note_button)

        self.create_video_note_button = QPushButton(NoteCreationMenuWidget)
        self.create_video_note_button.setObjectName(u"create_video_note_button")

        self.verticalLayout.addWidget(self.create_video_note_button)

        self.create_paint_note_button = QPushButton(NoteCreationMenuWidget)
        self.create_paint_note_button.setObjectName(u"create_paint_note_button")

        self.verticalLayout.addWidget(self.create_paint_note_button)

        self.create_todo_note_button = QPushButton(NoteCreationMenuWidget)
        self.create_todo_note_button.setObjectName(u"create_todo_note_button")

        self.verticalLayout.addWidget(self.create_todo_note_button)


        self.retranslateUi(NoteCreationMenuWidget)

        QMetaObject.connectSlotsByName(NoteCreationMenuWidget)
    # setupUi

    def retranslateUi(self, NoteCreationMenuWidget):
        NoteCreationMenuWidget.setWindowTitle(QCoreApplication.translate("NoteCreationMenuWidget", u"Note creation", None))
        self.create_text_note_button.setText(QCoreApplication.translate("NoteCreationMenuWidget", u"Create Text note", None))
        self.create_voice_note_button.setText(QCoreApplication.translate("NoteCreationMenuWidget", u"Create Voice note", None))
        self.create_video_note_button.setText(QCoreApplication.translate("NoteCreationMenuWidget", u"Create Video note", None))
        self.create_paint_note_button.setText(QCoreApplication.translate("NoteCreationMenuWidget", u"Create Paint note", None))
        self.create_todo_note_button.setText(QCoreApplication.translate("NoteCreationMenuWidget", u"Create Todo note", None))
    # retranslateUi

