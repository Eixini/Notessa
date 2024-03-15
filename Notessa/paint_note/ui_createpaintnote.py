# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreatePaintNote.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_CreatePaintNote(object):
    def setupUi(self, CreatePaintNote):
        if not CreatePaintNote.objectName():
            CreatePaintNote.setObjectName(u"CreatePaintNote")
        CreatePaintNote.resize(848, 638)
        self.gridLayout = QGridLayout(CreatePaintNote)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.drawingLayout = QVBoxLayout()
        self.drawingLayout.setObjectName(u"drawingLayout")

        self.mainLayout.addLayout(self.drawingLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.colorButton = QPushButton(CreatePaintNote)
        self.colorButton.setObjectName(u"colorButton")

        self.horizontalLayout.addWidget(self.colorButton)

        self.label = QLabel(CreatePaintNote)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.penWidth = QDoubleSpinBox(CreatePaintNote)
        self.penWidth.setObjectName(u"penWidth")

        self.horizontalLayout.addWidget(self.penWidth)

        self.toolPanelLayout = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.toolPanelLayout)


        self.mainLayout.addLayout(self.horizontalLayout)

        self.panelLayout = QHBoxLayout()
        self.panelLayout.setSpacing(0)
        self.panelLayout.setObjectName(u"panelLayout")
        self.panelLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.saveButton = QPushButton(CreatePaintNote)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)

        self.panelLayout.addWidget(self.saveButton)

        self.openButton = QPushButton(CreatePaintNote)
        self.openButton.setObjectName(u"openButton")
        sizePolicy.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy)

        self.panelLayout.addWidget(self.openButton)

        self.pa = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.panelLayout.addItem(self.pa)

        self.backButton = QPushButton(CreatePaintNote)
        self.backButton.setObjectName(u"backButton")
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        self.backButton.setAutoFillBackground(False)

        self.panelLayout.addWidget(self.backButton)


        self.mainLayout.addLayout(self.panelLayout)


        self.gridLayout.addLayout(self.mainLayout, 0, 0, 1, 1)


        self.retranslateUi(CreatePaintNote)

        QMetaObject.connectSlotsByName(CreatePaintNote)
    # setupUi

    def retranslateUi(self, CreatePaintNote):
        CreatePaintNote.setWindowTitle(QCoreApplication.translate("CreatePaintNote", u"Create paint note", None))
        self.colorButton.setText(QCoreApplication.translate("CreatePaintNote", u"Color", None))
        self.label.setText(QCoreApplication.translate("CreatePaintNote", u"Width", None))
        self.saveButton.setText(QCoreApplication.translate("CreatePaintNote", u"Save", None))
        self.openButton.setText(QCoreApplication.translate("CreatePaintNote", u"Open", None))
        self.backButton.setText(QCoreApplication.translate("CreatePaintNote", u"Back", None))
    # retranslateUi

