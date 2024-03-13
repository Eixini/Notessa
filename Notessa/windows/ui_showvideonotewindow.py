# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowVideoNoteWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)

class Ui_ShowVideoNoteWindow(object):
    def setupUi(self, ShowVideoNoteWindow):
        if not ShowVideoNoteWindow.objectName():
            ShowVideoNoteWindow.setObjectName(u"ShowVideoNoteWindow")
        ShowVideoNoteWindow.resize(996, 704)
        self.gridLayout = QGridLayout(ShowVideoNoteWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.videoWidget = QVideoWidget(ShowVideoNoteWindow)
        self.videoWidget.setObjectName(u"videoWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoWidget.sizePolicy().hasHeightForWidth())
        self.videoWidget.setSizePolicy(sizePolicy)

        self.mainLayout.addWidget(self.videoWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.positionLabel = QLabel(ShowVideoNoteWindow)
        self.positionLabel.setObjectName(u"positionLabel")

        self.horizontalLayout_3.addWidget(self.positionLabel)

        self.durationSlider = QSlider(ShowVideoNoteWindow)
        self.durationSlider.setObjectName(u"durationSlider")
        self.durationSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.durationSlider)

        self.durationLabel = QLabel(ShowVideoNoteWindow)
        self.durationLabel.setObjectName(u"durationLabel")

        self.horizontalLayout_3.addWidget(self.durationLabel)


        self.mainLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.backButton = QPushButton(ShowVideoNoteWindow)
        self.backButton.setObjectName(u"backButton")

        self.horizontalLayout.addWidget(self.backButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.playButton = QPushButton(ShowVideoNoteWindow)
        self.playButton.setObjectName(u"playButton")

        self.horizontalLayout.addWidget(self.playButton)

        self.pauseButton = QPushButton(ShowVideoNoteWindow)
        self.pauseButton.setObjectName(u"pauseButton")

        self.horizontalLayout.addWidget(self.pauseButton)

        self.stopButton = QPushButton(ShowVideoNoteWindow)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout.addWidget(self.stopButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(ShowVideoNoteWindow)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.volumeSlider = QSlider(ShowVideoNoteWindow)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.volumeSlider)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)


        self.mainLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.mainLayout, 0, 0, 1, 1)


        self.retranslateUi(ShowVideoNoteWindow)

        QMetaObject.connectSlotsByName(ShowVideoNoteWindow)
    # setupUi

    def retranslateUi(self, ShowVideoNoteWindow):
        ShowVideoNoteWindow.setWindowTitle(QCoreApplication.translate("ShowVideoNoteWindow", u"Dialog", None))
        self.positionLabel.setText(QCoreApplication.translate("ShowVideoNoteWindow", u"00:00", None))
        self.durationLabel.setText(QCoreApplication.translate("ShowVideoNoteWindow", u"00:00", None))
        self.backButton.setText(QCoreApplication.translate("ShowVideoNoteWindow", u"Back", None))
        self.playButton.setText(QCoreApplication.translate("ShowVideoNoteWindow", u"Play", None))
        self.pauseButton.setText(QCoreApplication.translate("ShowVideoNoteWindow", u"Pause", None))
        self.stopButton.setText(QCoreApplication.translate("ShowVideoNoteWindow", u"Stop", None))
        self.label.setText(QCoreApplication.translate("ShowVideoNoteWindow", u"Volume", None))
    # retranslateUi

