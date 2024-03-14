from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout,
    QLayout, QMdiArea, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout)

class Ui_CreatePaintNote(object):
    def setupUi(self, CreatePaintNote):
        if not CreatePaintNote.objectName():
            CreatePaintNote.setObjectName(u"CreatePaintNote")
        CreatePaintNote.resize(1081, 710)
        self.gridLayout = QGridLayout(CreatePaintNote)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.mdiArea = QMdiArea(CreatePaintNote)
        self.mdiArea.setObjectName(u"mdiArea")

        self.mainLayout.addWidget(self.mdiArea)

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
        self.saveButton.setText(QCoreApplication.translate("CreatePaintNote", u"Save", None))
        self.openButton.setText(QCoreApplication.translate("CreatePaintNote", u"Open", None))
        self.backButton.setText(QCoreApplication.translate("CreatePaintNote", u"Back", None))
    # retranslateUi

