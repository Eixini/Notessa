# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateVideoNote.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_CreateVideoNoteWindow(object):
    def setupUi(self, CreateVideoNoteWindow):
        if not CreateVideoNoteWindow.objectName():
            CreateVideoNoteWindow.setObjectName(u"CreateVideoNoteWindow")
        CreateVideoNoteWindow.setWindowModality(Qt.NonModal)
        CreateVideoNoteWindow.resize(895, 594)
        self.gridLayout = QGridLayout(CreateVideoNoteWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.videoLabel = QLabel(CreateVideoNoteWindow)
        self.videoLabel.setObjectName(u"videoLabel")
        self.videoLabel.setMinimumSize(QSize(854, 480))

        self.verticalLayout.addWidget(self.videoLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.recordButton = QPushButton(CreateVideoNoteWindow)
        self.recordButton.setObjectName(u"recordButton")

        self.horizontalLayout.addWidget(self.recordButton)

        self.pauseButton = QPushButton(CreateVideoNoteWindow)
        self.pauseButton.setObjectName(u"pauseButton")

        self.horizontalLayout.addWidget(self.pauseButton)

        self.stopButton = QPushButton(CreateVideoNoteWindow)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout.addWidget(self.stopButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.backButton = QPushButton(CreateVideoNoteWindow)
        self.backButton.setObjectName(u"backButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.backButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(CreateVideoNoteWindow)

        QMetaObject.connectSlotsByName(CreateVideoNoteWindow)
    # setupUi

    def retranslateUi(self, CreateVideoNoteWindow):
        CreateVideoNoteWindow.setWindowTitle(QCoreApplication.translate("CreateVideoNoteWindow", u"Create video note", None))
        self.videoLabel.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"TextLabel", None))
        self.recordButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Record", None))
        self.pauseButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Pause", None))
        self.stopButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Stop", None))
        self.backButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Back", None))
    # retranslateUi

