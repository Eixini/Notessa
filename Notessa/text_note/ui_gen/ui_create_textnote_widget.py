# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_textnote_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_CreateTextNoteWidget(object):
    def setupUi(self, CreateTextNoteWidget):
        if not CreateTextNoteWidget.objectName():
            CreateTextNoteWidget.setObjectName(u"CreateTextNoteWidget")
        CreateTextNoteWidget.resize(851, 737)
        self.verticalLayout = QVBoxLayout(CreateTextNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.textnote_contents = QTextEdit(CreateTextNoteWidget)
        self.textnote_contents.setObjectName(u"textnote_contents")
        self.textnote_contents.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout.addWidget(self.textnote_contents)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_button = QPushButton(CreateTextNoteWidget)
        self.save_button.setObjectName(u"save_button")
        icon = QIcon()
        icon.addFile(u":/icons/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
#if QT_CONFIG(tooltip)
        self.textnote_contents.setToolTip(QCoreApplication.translate("CreateTextNoteWidget", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.textnote_contents.setPlaceholderText(QCoreApplication.translate("CreateTextNoteWidget", u"Here you can start writing your note...", None))
        self.save_button.setText("")
    # retranslateUi

