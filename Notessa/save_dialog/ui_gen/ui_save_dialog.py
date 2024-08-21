# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QDialog,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_SaveDialog(object):
    def setupUi(self, SaveDialog):
        if not SaveDialog.objectName():
            SaveDialog.setObjectName(u"SaveDialog")
        SaveDialog.resize(471, 146)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SaveDialog.sizePolicy().hasHeightForWidth())
        SaveDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(SaveDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.note_name_lineedit = QLineEdit(SaveDialog)
        self.note_name_lineedit.setObjectName(u"note_name_lineedit")

        self.verticalLayout.addWidget(self.note_name_lineedit)

        self.warning_message_label = QLabel(SaveDialog)
        self.warning_message_label.setObjectName(u"warning_message_label")
        self.warning_message_label.setEnabled(True)
        self.warning_message_label.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.verticalLayout.addWidget(self.warning_message_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.indefinite_checkbox = QCheckBox(SaveDialog)
        self.indefinite_checkbox.setObjectName(u"indefinite_checkbox")

        self.horizontalLayout.addWidget(self.indefinite_checkbox)

        self.note_date_time_edit = QDateTimeEdit(SaveDialog)
        self.note_date_time_edit.setObjectName(u"note_date_time_edit")
        sizePolicy.setHeightForWidth(self.note_date_time_edit.sizePolicy().hasHeightForWidth())
        self.note_date_time_edit.setSizePolicy(sizePolicy)
        self.note_date_time_edit.setMinimumSize(QSize(175, 0))
        self.note_date_time_edit.setMinimumDateTime(QDateTime(QDate(1970, 1, 1), QTime(0, 0, 0)))
        self.note_date_time_edit.setCalendarPopup(False)

        self.horizontalLayout.addWidget(self.note_date_time_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.save_button = QPushButton(SaveDialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.save_button)

        self.cancel_button = QPushButton(SaveDialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.cancel_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(SaveDialog)

        QMetaObject.connectSlotsByName(SaveDialog)
    # setupUi

    def retranslateUi(self, SaveDialog):
        SaveDialog.setWindowTitle(QCoreApplication.translate("SaveDialog", u"Dialog", None))
        self.note_name_lineedit.setPlaceholderText(QCoreApplication.translate("SaveDialog", u"Enter note name ...", None))
        self.warning_message_label.setText(QCoreApplication.translate("SaveDialog", u"No note name entered!", None))
        self.indefinite_checkbox.setText(QCoreApplication.translate("SaveDialog", u"Indefinite", None))
#if QT_CONFIG(tooltip)
        self.save_button.setToolTip(QCoreApplication.translate("SaveDialog", u"Save", None))
#endif // QT_CONFIG(tooltip)
        self.save_button.setText("")
#if QT_CONFIG(tooltip)
        self.cancel_button.setToolTip(QCoreApplication.translate("SaveDialog", u"Cancel", None))
#endif // QT_CONFIG(tooltip)
        self.cancel_button.setText("")
    # retranslateUi

