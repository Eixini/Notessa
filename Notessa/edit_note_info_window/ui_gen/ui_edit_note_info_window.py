# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_note_info_window.ui'
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

class Ui_EditNoteInfoWindow(object):
    def setupUi(self, EditNoteInfoWindow):
        if not EditNoteInfoWindow.objectName():
            EditNoteInfoWindow.setObjectName(u"EditNoteInfoWindow")
        EditNoteInfoWindow.resize(540, 596)
        self.verticalLayout_5 = QVBoxLayout(EditNoteInfoWindow)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.old_name_label = QLabel(EditNoteInfoWindow)
        self.old_name_label.setObjectName(u"old_name_label")

        self.verticalLayout.addWidget(self.old_name_label)

        self.old_name_line_edit = QLineEdit(EditNoteInfoWindow)
        self.old_name_line_edit.setObjectName(u"old_name_line_edit")
        self.old_name_line_edit.setEnabled(True)
        self.old_name_line_edit.setReadOnly(True)

        self.verticalLayout.addWidget(self.old_name_line_edit)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.rename_checkbox = QCheckBox(EditNoteInfoWindow)
        self.rename_checkbox.setObjectName(u"rename_checkbox")

        self.verticalLayout_2.addWidget(self.rename_checkbox)

        self.new_name_label = QLabel(EditNoteInfoWindow)
        self.new_name_label.setObjectName(u"new_name_label")

        self.verticalLayout_2.addWidget(self.new_name_label)

        self.new_name_line_edit = QLineEdit(EditNoteInfoWindow)
        self.new_name_line_edit.setObjectName(u"new_name_line_edit")

        self.verticalLayout_2.addWidget(self.new_name_line_edit)

        self.new_name_error_label = QLabel(EditNoteInfoWindow)
        self.new_name_error_label.setObjectName(u"new_name_error_label")

        self.verticalLayout_2.addWidget(self.new_name_error_label)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.old_deadline_label = QLabel(EditNoteInfoWindow)
        self.old_deadline_label.setObjectName(u"old_deadline_label")

        self.verticalLayout_3.addWidget(self.old_deadline_label)

        self.old_deadline_line_edit = QLineEdit(EditNoteInfoWindow)
        self.old_deadline_line_edit.setObjectName(u"old_deadline_line_edit")
        self.old_deadline_line_edit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.old_deadline_line_edit)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.change_deadline_checkbox = QCheckBox(EditNoteInfoWindow)
        self.change_deadline_checkbox.setObjectName(u"change_deadline_checkbox")

        self.verticalLayout_4.addWidget(self.change_deadline_checkbox)

        self.new_deadline_label = QLabel(EditNoteInfoWindow)
        self.new_deadline_label.setObjectName(u"new_deadline_label")

        self.verticalLayout_4.addWidget(self.new_deadline_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.indefinite_checkbox = QCheckBox(EditNoteInfoWindow)
        self.indefinite_checkbox.setObjectName(u"indefinite_checkbox")

        self.horizontalLayout.addWidget(self.indefinite_checkbox)

        self.new_deadline_datetime_edit = QDateTimeEdit(EditNoteInfoWindow)
        self.new_deadline_datetime_edit.setObjectName(u"new_deadline_datetime_edit")
        self.new_deadline_datetime_edit.setMinimumSize(QSize(175, 0))

        self.horizontalLayout.addWidget(self.new_deadline_datetime_edit)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.new_deadline_error_label = QLabel(EditNoteInfoWindow)
        self.new_deadline_error_label.setObjectName(u"new_deadline_error_label")

        self.verticalLayout_4.addWidget(self.new_deadline_error_label)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 188, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.apply_button = QPushButton(EditNoteInfoWindow)
        self.apply_button.setObjectName(u"apply_button")

        self.horizontalLayout_2.addWidget(self.apply_button)

        self.cancel_button = QPushButton(EditNoteInfoWindow)
        self.cancel_button.setObjectName(u"cancel_button")

        self.horizontalLayout_2.addWidget(self.cancel_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.retranslateUi(EditNoteInfoWindow)

        QMetaObject.connectSlotsByName(EditNoteInfoWindow)
    # setupUi

    def retranslateUi(self, EditNoteInfoWindow):
        EditNoteInfoWindow.setWindowTitle(QCoreApplication.translate("EditNoteInfoWindow", u"Edit note info", None))
#if QT_CONFIG(tooltip)
        EditNoteInfoWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.old_name_label.setText(QCoreApplication.translate("EditNoteInfoWindow", u"Old name:", None))
        self.rename_checkbox.setText(QCoreApplication.translate("EditNoteInfoWindow", u"Rename", None))
        self.new_name_label.setText(QCoreApplication.translate("EditNoteInfoWindow", u"New name:", None))
        self.new_name_error_label.setText(QCoreApplication.translate("EditNoteInfoWindow", u"Error! New name cannot be empty.", None))
        self.old_deadline_label.setText(QCoreApplication.translate("EditNoteInfoWindow", u"Old deadline:", None))
        self.change_deadline_checkbox.setText(QCoreApplication.translate("EditNoteInfoWindow", u"Change deadline", None))
        self.new_deadline_label.setText(QCoreApplication.translate("EditNoteInfoWindow", u"New deadline:", None))
        self.indefinite_checkbox.setText(QCoreApplication.translate("EditNoteInfoWindow", u"Indefinite", None))
        self.new_deadline_error_label.setText(QCoreApplication.translate("EditNoteInfoWindow", u"Error! The new deadline cannot be less than the current time.", None))
#if QT_CONFIG(tooltip)
        self.apply_button.setToolTip(QCoreApplication.translate("EditNoteInfoWindow", u"Apply", None))
#endif // QT_CONFIG(tooltip)
        self.apply_button.setText(QCoreApplication.translate("EditNoteInfoWindow", u"Apply", None))
#if QT_CONFIG(tooltip)
        self.cancel_button.setToolTip(QCoreApplication.translate("EditNoteInfoWindow", u"Cancel", None))
#endif // QT_CONFIG(tooltip)
        self.cancel_button.setText(QCoreApplication.translate("EditNoteInfoWindow", u"Cancel", None))
    # retranslateUi

