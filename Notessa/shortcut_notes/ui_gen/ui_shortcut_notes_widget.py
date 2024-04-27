# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shortcut_notes_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTreeView, QVBoxLayout,
    QWidget)

class Ui_ShortcutNotesWidget(object):
    def setupUi(self, ShortcutNotesWidget):
        if not ShortcutNotesWidget.objectName():
            ShortcutNotesWidget.setObjectName(u"ShortcutNotesWidget")
        ShortcutNotesWidget.resize(372, 596)
        ShortcutNotesWidget.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(ShortcutNotesWidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fix_position_button = QPushButton(ShortcutNotesWidget)
        self.fix_position_button.setObjectName(u"fix_position_button")

        self.horizontalLayout.addWidget(self.fix_position_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.close_button = QPushButton(ShortcutNotesWidget)
        self.close_button.setObjectName(u"close_button")

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.notes_treeview = QTreeView(ShortcutNotesWidget)
        self.notes_treeview.setObjectName(u"notes_treeview")

        self.verticalLayout.addWidget(self.notes_treeview)


        self.retranslateUi(ShortcutNotesWidget)

        QMetaObject.connectSlotsByName(ShortcutNotesWidget)
    # setupUi

    def retranslateUi(self, ShortcutNotesWidget):
        ShortcutNotesWidget.setWindowTitle(QCoreApplication.translate("ShortcutNotesWidget", u"Form", None))
        self.fix_position_button.setText(QCoreApplication.translate("ShortcutNotesWidget", u"Fix", None))
        self.close_button.setText(QCoreApplication.translate("ShortcutNotesWidget", u"Close", None))
    # retranslateUi

