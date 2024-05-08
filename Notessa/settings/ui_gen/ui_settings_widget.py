# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(697, 598)
        self.verticalLayout = QVBoxLayout(SettingsWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.language_label = QLabel(SettingsWidget)
        self.language_label.setObjectName(u"language_label")

        self.horizontalLayout.addWidget(self.language_label)

        self.language_combobox = QComboBox(SettingsWidget)
        self.language_combobox.setObjectName(u"language_combobox")

        self.horizontalLayout.addWidget(self.language_combobox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.style_label = QLabel(SettingsWidget)
        self.style_label.setObjectName(u"style_label")

        self.horizontalLayout_2.addWidget(self.style_label)

        self.style_combobox = QComboBox(SettingsWidget)
        self.style_combobox.setObjectName(u"style_combobox")

        self.horizontalLayout_2.addWidget(self.style_combobox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.notelist_mode_label = QLabel(SettingsWidget)
        self.notelist_mode_label.setObjectName(u"notelist_mode_label")

        self.horizontalLayout_3.addWidget(self.notelist_mode_label)

        self.notelist_mode_combobox = QComboBox(SettingsWidget)
        self.notelist_mode_combobox.setObjectName(u"notelist_mode_combobox")

        self.horizontalLayout_3.addWidget(self.notelist_mode_combobox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.start_at_system_startup_checkbox = QCheckBox(SettingsWidget)
        self.start_at_system_startup_checkbox.setObjectName(u"start_at_system_startup_checkbox")

        self.verticalLayout.addWidget(self.start_at_system_startup_checkbox)

        self.verticalSpacer = QSpacerItem(20, 419, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(SettingsWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(SettingsWidget)

        QMetaObject.connectSlotsByName(SettingsWidget)
    # setupUi

    def retranslateUi(self, SettingsWidget):
        SettingsWidget.setWindowTitle(QCoreApplication.translate("SettingsWidget", u"Form", None))
        self.language_label.setText(QCoreApplication.translate("SettingsWidget", u"Language", None))
        self.style_label.setText(QCoreApplication.translate("SettingsWidget", u"Style", None))
        self.notelist_mode_label.setText(QCoreApplication.translate("SettingsWidget", u"Note list display mode", None))
        self.start_at_system_startup_checkbox.setText(QCoreApplication.translate("SettingsWidget", u"Start at system startup", None))
        self.label.setText(QCoreApplication.translate("SettingsWidget", u"Eixini (Roman R\u04d3ximov)", None))
    # retranslateUi

