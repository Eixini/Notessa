# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_videonote_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QVBoxLayout, QWidget)
from Notessa.resource import icons_rc

class Ui_ShowVideoNoteWidget(object):
    def setupUi(self, ShowVideoNoteWidget):
        if not ShowVideoNoteWidget.objectName():
            ShowVideoNoteWidget.setObjectName(u"ShowVideoNoteWidget")
        ShowVideoNoteWidget.resize(926, 596)
        self.verticalLayout = QVBoxLayout(ShowVideoNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.videonote_name_label = QLabel(ShowVideoNoteWidget)
        self.videonote_name_label.setObjectName(u"videonote_name_label")

        self.verticalLayout.addWidget(self.videonote_name_label)

        self.play_videonote_widget = QVideoWidget(ShowVideoNoteWidget)
        self.play_videonote_widget.setObjectName(u"play_videonote_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_videonote_widget.sizePolicy().hasHeightForWidth())
        self.play_videonote_widget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.play_videonote_widget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.position_label = QLabel(ShowVideoNoteWidget)
        self.position_label.setObjectName(u"position_label")

        self.horizontalLayout_4.addWidget(self.position_label)

        self.duration_slider = QSlider(ShowVideoNoteWidget)
        self.duration_slider.setObjectName(u"duration_slider")
        self.duration_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_4.addWidget(self.duration_slider)

        self.duration_label = QLabel(ShowVideoNoteWidget)
        self.duration_label.setObjectName(u"duration_label")

        self.horizontalLayout_4.addWidget(self.duration_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.close_button = QPushButton(ShowVideoNoteWidget)
        self.close_button.setObjectName(u"close_button")
        icon = QIcon()
        icon.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.close_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.play_button = QPushButton(ShowVideoNoteWidget)
        self.play_button.setObjectName(u"play_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_button.setIcon(icon1)
        self.play_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.play_button)

        self.pause_button = QPushButton(ShowVideoNoteWidget)
        self.pause_button.setObjectName(u"pause_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_button.setIcon(icon2)
        self.pause_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pause_button)

        self.stop_button = QPushButton(ShowVideoNoteWidget)
        self.stop_button.setObjectName(u"stop_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_button.setIcon(icon3)
        self.stop_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.stop_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.volume_label = QLabel(ShowVideoNoteWidget)
        self.volume_label.setObjectName(u"volume_label")

        self.horizontalLayout_6.addWidget(self.volume_label)

        self.volume_slider = QSlider(ShowVideoNoteWidget)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMaximum(100)
        self.volume_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.volume_slider)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(ShowVideoNoteWidget)

        QMetaObject.connectSlotsByName(ShowVideoNoteWidget)
    # setupUi

    def retranslateUi(self, ShowVideoNoteWidget):
        ShowVideoNoteWidget.setWindowTitle(QCoreApplication.translate("ShowVideoNoteWidget", u"Form", None))
        self.videonote_name_label.setText(QCoreApplication.translate("ShowVideoNoteWidget", u"Video note name", None))
        self.position_label.setText(QCoreApplication.translate("ShowVideoNoteWidget", u"00:00", None))
        self.duration_label.setText(QCoreApplication.translate("ShowVideoNoteWidget", u"00:00", None))
        self.close_button.setText(QCoreApplication.translate("ShowVideoNoteWidget", u"Back", None))
        self.play_button.setText("")
        self.pause_button.setText("")
        self.stop_button.setText("")
        self.volume_label.setText(QCoreApplication.translate("ShowVideoNoteWidget", u"Volume", None))
    # retranslateUi

