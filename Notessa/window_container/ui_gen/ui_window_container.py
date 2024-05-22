# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_container.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_WindowContainer(object):
    def setupUi(self, WindowContainer):
        if not WindowContainer.objectName():
            WindowContainer.setObjectName(u"WindowContainer")
        WindowContainer.resize(1006, 600)
        WindowContainer.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.verticalLayout = QVBoxLayout(WindowContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.collapse_button = QPushButton(WindowContainer)
        self.collapse_button.setObjectName(u"collapse_button")

        self.horizontalLayout.addWidget(self.collapse_button)

        self.close_button = QPushButton(WindowContainer)
        self.close_button.setObjectName(u"close_button")

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(WindowContainer)

        QMetaObject.connectSlotsByName(WindowContainer)
    # setupUi

    def retranslateUi(self, WindowContainer):
        WindowContainer.setWindowTitle(QCoreApplication.translate("WindowContainer", u"Dialog", None))
        self.collapse_button.setText("")
        self.close_button.setText("")
    # retranslateUi

