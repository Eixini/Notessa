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
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_CreateVideoNoteWindow(object):
    def setupUi(self, CreateVideoNoteWindow):
        if not CreateVideoNoteWindow.objectName():
            CreateVideoNoteWindow.setObjectName(u"CreateVideoNoteWindow")
        CreateVideoNoteWindow.setWindowModality(Qt.NonModal)
        CreateVideoNoteWindow.resize(957, 697)
        self.gridLayout = QGridLayout(CreateVideoNoteWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cameraLabel = QLabel(CreateVideoNoteWindow)
        self.cameraLabel.setObjectName(u"cameraLabel")

        self.horizontalLayout_4.addWidget(self.cameraLabel)

        self.cameraList = QComboBox(CreateVideoNoteWindow)
        self.cameraList.setObjectName(u"cameraList")

        self.horizontalLayout_4.addWidget(self.cameraList)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.microphoneLabel = QLabel(CreateVideoNoteWindow)
        self.microphoneLabel.setObjectName(u"microphoneLabel")

        self.horizontalLayout_4.addWidget(self.microphoneLabel)

        self.microphoneList = QComboBox(CreateVideoNoteWindow)
        self.microphoneList.setObjectName(u"microphoneList")

        self.horizontalLayout_4.addWidget(self.microphoneList)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stateLabel = QLabel(CreateVideoNoteWindow)
        self.stateLabel.setObjectName(u"stateLabel")

        self.horizontalLayout_3.addWidget(self.stateLabel)

        self.durationLabel = QLabel(CreateVideoNoteWindow)
        self.durationLabel.setObjectName(u"durationLabel")

        self.horizontalLayout_3.addWidget(self.durationLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.videoNoteName = QLineEdit(CreateVideoNoteWindow)
        self.videoNoteName.setObjectName(u"videoNoteName")

        self.horizontalLayout_3.addWidget(self.videoNoteName)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.videoDisplay = QVideoWidget(CreateVideoNoteWindow)
        self.videoDisplay.setObjectName(u"videoDisplay")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoDisplay.sizePolicy().hasHeightForWidth())
        self.videoDisplay.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.videoDisplay)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.recordButton = QPushButton(CreateVideoNoteWindow)
        self.recordButton.setObjectName(u"recordButton")

        self.horizontalLayout.addWidget(self.recordButton)

        self.stopButton = QPushButton(CreateVideoNoteWindow)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout.addWidget(self.stopButton)

        self.muteButton = QPushButton(CreateVideoNoteWindow)
        self.muteButton.setObjectName(u"muteButton")

        self.horizontalLayout.addWidget(self.muteButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.backButton = QPushButton(CreateVideoNoteWindow)
        self.backButton.setObjectName(u"backButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy1)

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
        self.cameraLabel.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Camera", None))
        self.cameraList.setPlaceholderText(QCoreApplication.translate("CreateVideoNoteWindow", u"Select camera", None))
        self.microphoneLabel.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Microphone", None))
        self.microphoneList.setPlaceholderText(QCoreApplication.translate("CreateVideoNoteWindow", u"Select microphone", None))
        self.stateLabel.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"STATE", None))
        self.durationLabel.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"00:00", None))
        self.videoNoteName.setPlaceholderText(QCoreApplication.translate("CreateVideoNoteWindow", u"Enter video note name ...", None))
        self.recordButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Record", None))
        self.stopButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Stop", None))
        self.muteButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Mute", None))
        self.backButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Back", None))
    # retranslateUi

