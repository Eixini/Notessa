# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_textnote_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
from Notessa.resource import icons_rc

class Ui_ShowTextNoteWidget(object):
    def setupUi(self, ShowTextNoteWidget):
        if not ShowTextNoteWidget.objectName():
            ShowTextNoteWidget.setObjectName(u"ShowTextNoteWidget")
        ShowTextNoteWidget.resize(727, 544)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ShowTextNoteWidget.sizePolicy().hasHeightForWidth())
        ShowTextNoteWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(ShowTextNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textnote_name_label = QLabel(ShowTextNoteWidget)
        self.textnote_name_label.setObjectName(u"textnote_name_label")

        self.verticalLayout.addWidget(self.textnote_name_label)

        self.show_textnote_field = QTextEdit(ShowTextNoteWidget)
        self.show_textnote_field.setObjectName(u"show_textnote_field")
        self.show_textnote_field.setReadOnly(True)

        self.verticalLayout.addWidget(self.show_textnote_field)

        self.buttons_panel_horizontal_layout = QHBoxLayout()
        self.buttons_panel_horizontal_layout.setObjectName(u"buttons_panel_horizontal_layout")
        self.backButton = QPushButton(ShowTextNoteWidget)
        self.backButton.setObjectName(u"backButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backButton.setIcon(icon)
        self.backButton.setIconSize(QSize(32, 32))

        self.buttons_panel_horizontal_layout.addWidget(self.backButton)

        self.horizontalSpacer = QSpacerItem(128, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttons_panel_horizontal_layout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.buttons_panel_horizontal_layout)


        self.retranslateUi(ShowTextNoteWidget)

        QMetaObject.connectSlotsByName(ShowTextNoteWidget)
    # setupUi

    def retranslateUi(self, ShowTextNoteWidget):
        ShowTextNoteWidget.setWindowTitle(QCoreApplication.translate("ShowTextNoteWidget", u"Form", None))
        self.textnote_name_label.setText(QCoreApplication.translate("ShowTextNoteWidget", u"Note name", None))
        self.backButton.setText(QCoreApplication.translate("ShowTextNoteWidget", u"Back", None))
    # retranslateUi

