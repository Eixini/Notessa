# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_paintnote_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)


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

        self.paintnote_label = QLabel(ShowPaintNoteWidget)
        self.paintnote_label.setObjectName(u"paintnote_label")

        self.verticalLayout.addWidget(self.paintnote_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ShowPaintNoteWidget)

        QMetaObject.connectSlotsByName(ShowPaintNoteWidget)
    # setupUi

    def retranslateUi(self, ShowPaintNoteWidget):
        ShowPaintNoteWidget.setWindowTitle(QCoreApplication.translate("ShowPaintNoteWidget", u"Form", None))
        self.paintnote_name_label.setText(QCoreApplication.translate("ShowPaintNoteWidget", u"Paint note label", None))
        self.paintnote_label.setText("")
    # retranslateUi

