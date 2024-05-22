# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_voicenote_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)


class Ui_ShowVoiceNoteWidget(object):
    def setupUi(self, ShowVoiceNoteWidget):
        if not ShowVoiceNoteWidget.objectName():
            ShowVoiceNoteWidget.setObjectName(u"ShowVoiceNoteWidget")
        ShowVoiceNoteWidget.resize(877, 507)
        self.verticalLayout = QVBoxLayout(ShowVoiceNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.voicenote_name_label = QLabel(ShowVoiceNoteWidget)
        self.voicenote_name_label.setObjectName(u"voicenote_name_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voicenote_name_label.sizePolicy().hasHeightForWidth())
        self.voicenote_name_label.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.voicenote_name_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.current_position_label = QLabel(ShowVoiceNoteWidget)
        self.current_position_label.setObjectName(u"current_position_label")

        self.horizontalLayout.addWidget(self.current_position_label)

        self.position_slider = QSlider(ShowVoiceNoteWidget)
        self.position_slider.setObjectName(u"position_slider")
        self.position_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.position_slider)

        self.duration_label = QLabel(ShowVoiceNoteWidget)
        self.duration_label.setObjectName(u"duration_label")

        self.horizontalLayout.addWidget(self.duration_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.volume_label = QLabel(ShowVoiceNoteWidget)
        self.volume_label.setObjectName(u"volume_label")

        self.horizontalLayout_3.addWidget(self.volume_label)

        self.volume_slider = QSlider(ShowVoiceNoteWidget)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMaximum(100)
        self.volume_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.volume_slider)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.play_button = QPushButton(ShowVoiceNoteWidget)
        self.play_button.setObjectName(u"play_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy1)
        icon = QIcon()
        icon.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_button.setIcon(icon)
        self.play_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.play_button)

        self.pause_button = QPushButton(ShowVoiceNoteWidget)
        self.pause_button.setObjectName(u"pause_button")
        sizePolicy1.setHeightForWidth(self.pause_button.sizePolicy().hasHeightForWidth())
        self.pause_button.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u":/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_button.setIcon(icon1)
        self.pause_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pause_button)

        self.stop_button = QPushButton(ShowVoiceNoteWidget)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy1.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_button.setIcon(icon2)
        self.stop_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.stop_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(ShowVoiceNoteWidget)

        QMetaObject.connectSlotsByName(ShowVoiceNoteWidget)
    # setupUi

    def retranslateUi(self, ShowVoiceNoteWidget):
        ShowVoiceNoteWidget.setWindowTitle(QCoreApplication.translate("ShowVoiceNoteWidget", u"Form", None))
        self.voicenote_name_label.setText(QCoreApplication.translate("ShowVoiceNoteWidget", u"Voice note name", None))
        self.current_position_label.setText(QCoreApplication.translate("ShowVoiceNoteWidget", u"00:00", None))
        self.duration_label.setText(QCoreApplication.translate("ShowVoiceNoteWidget", u"00:00", None))
        self.volume_label.setText(QCoreApplication.translate("ShowVoiceNoteWidget", u"Volume", None))
        self.play_button.setText("")
        self.pause_button.setText("")
        self.stop_button.setText("")
    # retranslateUi

