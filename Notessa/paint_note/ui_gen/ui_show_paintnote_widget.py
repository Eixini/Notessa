# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_paintnote_widget.ui'
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
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
# from Notessa.resource import icons_rc

class Ui_ShowPaintNoteWidget(object):
    def setupUi(self, ShowPaintNoteWidget):
        if not ShowPaintNoteWidget.objectName():
            ShowPaintNoteWidget.setObjectName(u"ShowPaintNoteWidget")
        ShowPaintNoteWidget.resize(943, 648)
        self.verticalLayout = QVBoxLayout(ShowPaintNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.paintnote_name_label = QLabel(ShowPaintNoteWidget)
        self.paintnote_name_label.setObjectName(u"paintnote_name_label")

        self.verticalLayout.addWidget(self.paintnote_name_label)

        self.show_paintnote_vertical_layout = QVBoxLayout()
        self.show_paintnote_vertical_layout.setObjectName(u"show_paintnote_vertical_layout")
        self.paintnote_label = QLabel(ShowPaintNoteWidget)
        self.paintnote_label.setObjectName(u"paintnote_label")

        self.show_paintnote_vertical_layout.addWidget(self.paintnote_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.show_paintnote_vertical_layout.addItem(self.verticalSpacer)


        self.verticalLayout.addLayout(self.show_paintnote_vertical_layout)

        self.buttons_panel_horizonal_layout = QHBoxLayout()
        self.buttons_panel_horizonal_layout.setObjectName(u"buttons_panel_horizonal_layout")
        self.close_button = QPushButton(ShowPaintNoteWidget)
        self.close_button.setObjectName(u"close_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setIconSize(QSize(32, 32))

        self.buttons_panel_horizonal_layout.addWidget(self.close_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttons_panel_horizonal_layout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.buttons_panel_horizonal_layout)


        self.retranslateUi(ShowPaintNoteWidget)

        QMetaObject.connectSlotsByName(ShowPaintNoteWidget)
    # setupUi

    def retranslateUi(self, ShowPaintNoteWidget):
        ShowPaintNoteWidget.setWindowTitle(QCoreApplication.translate("ShowPaintNoteWidget", u"Form", None))
        self.paintnote_name_label.setText(QCoreApplication.translate("ShowPaintNoteWidget", u"Paint note label", None))
        self.paintnote_label.setText("")
        self.close_button.setText(QCoreApplication.translate("ShowPaintNoteWidget", u"Close", None))
    # retranslateUi

