# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_videonote_widget.ui'
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
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)


class Ui_CreateVideoNoteWidget(object):
    def setupUi(self, CreateVideoNoteWidget):
        if not CreateVideoNoteWidget.objectName():
            CreateVideoNoteWidget.setObjectName(u"CreateVideoNoteWidget")
        CreateVideoNoteWidget.resize(944, 709)
        self.verticalLayout = QVBoxLayout(CreateVideoNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.select_camera_label = QLabel(CreateVideoNoteWidget)
        self.select_camera_label.setObjectName(u"select_camera_label")

        self.horizontalLayout_4.addWidget(self.select_camera_label)

        self.cameras_combobox = QComboBox(CreateVideoNoteWidget)
        self.cameras_combobox.setObjectName(u"cameras_combobox")

        self.horizontalLayout_4.addWidget(self.cameras_combobox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)

        self.select_microphone_label = QLabel(CreateVideoNoteWidget)
        self.select_microphone_label.setObjectName(u"select_microphone_label")

        self.horizontalLayout_4.addWidget(self.select_microphone_label)

        self.microphones_combobox = QComboBox(CreateVideoNoteWidget)
        self.microphones_combobox.setObjectName(u"microphones_combobox")

        self.horizontalLayout_4.addWidget(self.microphones_combobox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.state_label = QLabel(CreateVideoNoteWidget)
        self.state_label.setObjectName(u"state_label")

        self.horizontalLayout_3.addWidget(self.state_label)

        self.duration_label = QLabel(CreateVideoNoteWidget)
        self.duration_label.setObjectName(u"duration_label")

        self.horizontalLayout_3.addWidget(self.duration_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.videonote_name_lineedit = QLineEdit(CreateVideoNoteWidget)
        self.videonote_name_lineedit.setObjectName(u"videonote_name_lineedit")

        self.horizontalLayout_3.addWidget(self.videonote_name_lineedit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.video_display = QVideoWidget(CreateVideoNoteWidget)
        self.video_display.setObjectName(u"video_display")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_display.sizePolicy().hasHeightForWidth())
        self.video_display.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.video_display)

        self.media_buttons_horizontal_layout = QHBoxLayout()
        self.media_buttons_horizontal_layout.setObjectName(u"media_buttons_horizontal_layout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.media_buttons_horizontal_layout.addItem(self.horizontalSpacer_4)

        self.record_button = QPushButton(CreateVideoNoteWidget)
        self.record_button.setObjectName(u"record_button")
        icon = QIcon()
        icon.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.record_button.setIcon(icon)
        self.record_button.setIconSize(QSize(32, 32))

        self.media_buttons_horizontal_layout.addWidget(self.record_button)

        self.stop_button = QPushButton(CreateVideoNoteWidget)
        self.stop_button.setObjectName(u"stop_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_button.setIcon(icon1)
        self.stop_button.setIconSize(QSize(32, 32))

        self.media_buttons_horizontal_layout.addWidget(self.stop_button)

        self.mute_button = QPushButton(CreateVideoNoteWidget)
        self.mute_button.setObjectName(u"mute_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/microphone_off.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mute_button.setIcon(icon2)
        self.mute_button.setIconSize(QSize(32, 32))

        self.media_buttons_horizontal_layout.addWidget(self.mute_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.media_buttons_horizontal_layout.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.media_buttons_horizontal_layout)


        self.retranslateUi(CreateVideoNoteWidget)

        QMetaObject.connectSlotsByName(CreateVideoNoteWidget)
    # setupUi

    def retranslateUi(self, CreateVideoNoteWidget):
        CreateVideoNoteWidget.setWindowTitle(QCoreApplication.translate("CreateVideoNoteWidget", u"Form", None))
        self.select_camera_label.setText(QCoreApplication.translate("CreateVideoNoteWidget", u"Camera", None))
        self.cameras_combobox.setPlaceholderText(QCoreApplication.translate("CreateVideoNoteWidget", u"Select camera", None))
        self.select_microphone_label.setText(QCoreApplication.translate("CreateVideoNoteWidget", u"Microphone", None))
        self.microphones_combobox.setPlaceholderText(QCoreApplication.translate("CreateVideoNoteWidget", u"Select microphone", None))
        self.state_label.setText(QCoreApplication.translate("CreateVideoNoteWidget", u"STATE", None))
        self.duration_label.setText(QCoreApplication.translate("CreateVideoNoteWidget", u"00:00", None))
        self.videonote_name_lineedit.setPlaceholderText(QCoreApplication.translate("CreateVideoNoteWidget", u"Enter video note name ...", None))
        self.record_button.setText("")
        self.stop_button.setText("")
        self.mute_button.setText("")
    # retranslateUi

