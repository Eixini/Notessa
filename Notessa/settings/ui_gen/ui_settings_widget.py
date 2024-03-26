# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from Notessa.resource import icons_rc

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(803, 596)
        self.verticalLayout = QVBoxLayout(SettingsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.language_horizontal_layout = QHBoxLayout()
        self.language_horizontal_layout.setObjectName(u"language_horizontal_layout")
        self.language_label = QLabel(SettingsWidget)
        self.language_label.setObjectName(u"language_label")

        self.language_horizontal_layout.addWidget(self.language_label)

        self.language_combo_box = QComboBox(SettingsWidget)
        self.language_combo_box.setObjectName(u"language_combo_box")

        self.language_horizontal_layout.addWidget(self.language_combo_box)


        self.verticalLayout.addLayout(self.language_horizontal_layout)

        self.style_horizontal_layout = QHBoxLayout()
        self.style_horizontal_layout.setObjectName(u"style_horizontal_layout")
        self.style_label = QLabel(SettingsWidget)
        self.style_label.setObjectName(u"style_label")

        self.style_horizontal_layout.addWidget(self.style_label)

        self.style_combo_box = QComboBox(SettingsWidget)
        self.style_combo_box.setObjectName(u"style_combo_box")

        self.style_horizontal_layout.addWidget(self.style_combo_box)


        self.verticalLayout.addLayout(self.style_horizontal_layout)

        self.verticalSpacer = QSpacerItem(20, 471, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttons_panel_horizonal_layout = QHBoxLayout()
        self.buttons_panel_horizonal_layout.setObjectName(u"buttons_panel_horizonal_layout")
        self.close_button = QPushButton(SettingsWidget)
        self.close_button.setObjectName(u"close_button")
        icon = QIcon()
        icon.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setIconSize(QSize(32, 32))

        self.buttons_panel_horizonal_layout.addWidget(self.close_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttons_panel_horizonal_layout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.buttons_panel_horizonal_layout)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Form", None))
        self.language_label.setText(QCoreApplication.translate("SettingsWidget", u"Select language", None))
        self.style_label.setText(QCoreApplication.translate("SettingsWidget", u"Select style", None))
        self.close_button.setText(QCoreApplication.translate("SettingsWidget", u"Close", None))
    # retranslateUi

