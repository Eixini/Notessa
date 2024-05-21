# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_textnote_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_ShowTextNoteWidget(object):
    def setupUi(self, ShowTextNoteWidget):
        if not ShowTextNoteWidget.objectName():
            ShowTextNoteWidget.setObjectName(u"ShowTextNoteWidget")
        ShowTextNoteWidget.resize(860, 582)
        self.verticalLayout = QVBoxLayout(ShowTextNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textnote_name_label = QLabel(ShowTextNoteWidget)
        self.textnote_name_label.setObjectName(u"textnote_name_label")

        self.verticalLayout.addWidget(self.textnote_name_label)

        self.show_textnote_field = QTextEdit(ShowTextNoteWidget)
        self.show_textnote_field.setObjectName(u"show_textnote_field")
        self.show_textnote_field.setReadOnly(True)

        self.verticalLayout.addWidget(self.show_textnote_field)


        self.retranslateUi(ShowTextNoteWidget)

        QMetaObject.connectSlotsByName(ShowTextNoteWidget)
    # setupUi

    def retranslateUi(self, ShowTextNoteWidget):
        ShowTextNoteWidget.setWindowTitle(QCoreApplication.translate("ShowTextNoteWidget", u"Dialog", None))
        self.textnote_name_label.setText(QCoreApplication.translate("ShowTextNoteWidget", u"Note name", None))
    # retranslateUi

