# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateCanvasWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_CreateCanvasWindow(object):
    def setupUi(self, CreateCanvasWindow):
        if not CreateCanvasWindow.objectName():
            CreateCanvasWindow.setObjectName(u"CreateCanvasWindow")
        CreateCanvasWindow.resize(452, 110)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateCanvasWindow.sizePolicy().hasHeightForWidth())
        CreateCanvasWindow.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(CreateCanvasWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.descriptionLabel = QLabel(CreateCanvasWindow)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widthLabel = QLabel(CreateCanvasWindow)
        self.widthLabel.setObjectName(u"widthLabel")

        self.horizontalLayout.addWidget(self.widthLabel)

        self.widthSize = QSpinBox(CreateCanvasWindow)
        self.widthSize.setObjectName(u"widthSize")
        self.widthSize.setMaximum(1920)

        self.horizontalLayout.addWidget(self.widthSize)

        self.heightLabel = QLabel(CreateCanvasWindow)
        self.heightLabel.setObjectName(u"heightLabel")

        self.horizontalLayout.addWidget(self.heightLabel)

        self.heightSize = QSpinBox(CreateCanvasWindow)
        self.heightSize.setObjectName(u"heightSize")
        self.heightSize.setMaximum(1080)

        self.horizontalLayout.addWidget(self.heightSize)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.okButton = QPushButton(CreateCanvasWindow)
        self.okButton.setObjectName(u"okButton")

        self.horizontalLayout_2.addWidget(self.okButton)

        self.cancelButton = QPushButton(CreateCanvasWindow)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(CreateCanvasWindow)

        QMetaObject.connectSlotsByName(CreateCanvasWindow)
    # setupUi

    def retranslateUi(self, CreateCanvasWindow):
        CreateCanvasWindow.setWindowTitle(QCoreApplication.translate("CreateCanvasWindow", u"Create canvas", None))
        self.descriptionLabel.setText(QCoreApplication.translate("CreateCanvasWindow", u"Set canvas size. Maximum 1920x1080", None))
        self.widthLabel.setText(QCoreApplication.translate("CreateCanvasWindow", u"Width", None))
        self.heightLabel.setText(QCoreApplication.translate("CreateCanvasWindow", u"Height", None))
        self.okButton.setText(QCoreApplication.translate("CreateCanvasWindow", u"Ok", None))
        self.cancelButton.setText(QCoreApplication.translate("CreateCanvasWindow", u"Cancel", None))
    # retranslateUi

