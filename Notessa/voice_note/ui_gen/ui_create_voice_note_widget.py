# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_voice_note_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_CreateVoiceNoteWidget(object):
    def setupUi(self, CreateVoiceNoteWidget):
        if not CreateVoiceNoteWidget.objectName():
            CreateVoiceNoteWidget.setObjectName(u"CreateVoiceNoteWidget")
        CreateVoiceNoteWidget.resize(677, 613)
        self.verticalLayout = QVBoxLayout(CreateVoiceNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.up_horizontal_layout = QHBoxLayout()
        self.up_horizontal_layout.setObjectName(u"up_horizontal_layout")
        self.available_devices_label = QLabel(CreateVoiceNoteWidget)
        self.available_devices_label.setObjectName(u"available_devices_label")

        self.up_horizontal_layout.addWidget(self.available_devices_label)

        self.available_devices_combobox = QComboBox(CreateVoiceNoteWidget)
        self.available_devices_combobox.setObjectName(u"available_devices_combobox")

        self.up_horizontal_layout.addWidget(self.available_devices_combobox)


        self.verticalLayout.addLayout(self.up_horizontal_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 129, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.duration_horizontal_layout = QHBoxLayout()
        self.duration_horizontal_layout.setObjectName(u"duration_horizontal_layout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.duration_horizontal_layout.addItem(self.horizontalSpacer_2)

        self.duration_label = QLabel(CreateVoiceNoteWidget)
        self.duration_label.setObjectName(u"duration_label")
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(32)
        font.setBold(True)
        font.setItalic(True)
        font.setStrikeOut(False)
        self.duration_label.setFont(font)

        self.duration_horizontal_layout.addWidget(self.duration_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.duration_horizontal_layout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.duration_horizontal_layout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.media_buttons_horizontal_layout = QHBoxLayout()
        self.media_buttons_horizontal_layout.setObjectName(u"media_buttons_horizontal_layout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.media_buttons_horizontal_layout.addItem(self.horizontalSpacer_4)

        self.pause_button = QPushButton(CreateVoiceNoteWidget)
        self.pause_button.setObjectName(u"pause_button")
        self.pause_button.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pause_button.sizePolicy().hasHeightForWidth())
        self.pause_button.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 127))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush6 = QBrush(QColor(127, 127, 127, 127))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.pause_button.setPalette(palette)
        icon = QIcon()
        icon.addFile(u":/icons/pause.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pause_button.setIcon(icon)
        self.pause_button.setIconSize(QSize(32, 32))

        self.media_buttons_horizontal_layout.addWidget(self.pause_button)

        self.record_button = QPushButton(CreateVoiceNoteWidget)
        self.record_button.setObjectName(u"record_button")
        sizePolicy.setHeightForWidth(self.record_button.sizePolicy().hasHeightForWidth())
        self.record_button.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/icons/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.record_button.setIcon(icon1)
        self.record_button.setIconSize(QSize(32, 32))

        self.media_buttons_horizontal_layout.addWidget(self.record_button)

        self.stop_button = QPushButton(CreateVoiceNoteWidget)
        self.stop_button.setObjectName(u"stop_button")
        sizePolicy.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u":/icons/stop.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_button.setIcon(icon2)
        self.stop_button.setIconSize(QSize(32, 32))

        self.media_buttons_horizontal_layout.addWidget(self.stop_button)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.media_buttons_horizontal_layout.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.media_buttons_horizontal_layout)

        self.verticalSpacer = QSpacerItem(20, 129, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(CreateVoiceNoteWidget)

        QMetaObject.connectSlotsByName(CreateVoiceNoteWidget)
    # setupUi

    def retranslateUi(self, CreateVoiceNoteWidget):
        CreateVoiceNoteWidget.setWindowTitle(QCoreApplication.translate("CreateVoiceNoteWidget", u"Form", None))
        self.available_devices_label.setText(QCoreApplication.translate("CreateVoiceNoteWidget", u"Available devices", None))
        self.duration_label.setText(QCoreApplication.translate("CreateVoiceNoteWidget", u"0:00", None))
#if QT_CONFIG(tooltip)
        self.pause_button.setToolTip(QCoreApplication.translate("CreateVoiceNoteWidget", u"Pause", None))
#endif // QT_CONFIG(tooltip)
        self.pause_button.setText("")
#if QT_CONFIG(tooltip)
        self.record_button.setToolTip(QCoreApplication.translate("CreateVoiceNoteWidget", u"Record", None))
#endif // QT_CONFIG(tooltip)
        self.record_button.setText("")
#if QT_CONFIG(tooltip)
        self.stop_button.setToolTip(QCoreApplication.translate("CreateVoiceNoteWidget", u"Stop", None))
#endif // QT_CONFIG(tooltip)
        self.stop_button.setText("")
    # retranslateUi

