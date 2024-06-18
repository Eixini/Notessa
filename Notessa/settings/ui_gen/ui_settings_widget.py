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
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        if not SettingsWidget.objectName():
            SettingsWidget.setObjectName(u"SettingsWidget")
        SettingsWidget.resize(697, 585)
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

        self.show_note_list_gadget_checkbox = QCheckBox(SettingsWidget)
        self.show_note_list_gadget_checkbox.setObjectName(u"show_note_list_gadget_checkbox")

        self.verticalLayout.addWidget(self.show_note_list_gadget_checkbox)

        self.start_at_system_startup_checkbox = QCheckBox(SettingsWidget)
        self.start_at_system_startup_checkbox.setObjectName(u"start_at_system_startup_checkbox")

        self.verticalLayout.addWidget(self.start_at_system_startup_checkbox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.deadline_time_label = QLabel(SettingsWidget)
        self.deadline_time_label.setObjectName(u"deadline_time_label")

        self.horizontalLayout_3.addWidget(self.deadline_time_label)

        self.deadline_time_spinbox = QSpinBox(SettingsWidget)
        self.deadline_time_spinbox.setObjectName(u"deadline_time_spinbox")
        self.deadline_time_spinbox.setMinimum(1)
        self.deadline_time_spinbox.setMaximum(999999)

        self.horizontalLayout_3.addWidget(self.deadline_time_spinbox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(676, 340, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.import_notes_button = QPushButton(SettingsWidget)
        self.import_notes_button.setObjectName(u"import_notes_button")

        self.horizontalLayout_4.addWidget(self.import_notes_button)

        self.export_notes_button = QPushButton(SettingsWidget)
        self.export_notes_button.setObjectName(u"export_notes_button")

        self.horizontalLayout_4.addWidget(self.export_notes_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

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
        self.show_note_list_gadget_checkbox.setText(QCoreApplication.translate("SettingsWidget", u"Show notes gadget when app launches", None))
        self.start_at_system_startup_checkbox.setText(QCoreApplication.translate("SettingsWidget", u"Start at system startup", None))
        self.deadline_time_label.setText(QCoreApplication.translate("SettingsWidget", u"Notify me when a deadline is approaching (minutes)", None))
        self.deadline_time_spinbox.setSuffix("")
        self.import_notes_button.setText(QCoreApplication.translate("SettingsWidget", u"Import notes", None))
        self.export_notes_button.setText(QCoreApplication.translate("SettingsWidget", u"Export notes", None))
        self.label.setText(QCoreApplication.translate("SettingsWidget", u"Eixini (Roman R\u04d3ximov)", None))
    # retranslateUi

