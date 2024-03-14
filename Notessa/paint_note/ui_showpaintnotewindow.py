from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout)

class Ui_ShowPaintNoteWindow(object):
    def setupUi(self, ShowPaintNoteWindow):
        if not ShowPaintNoteWindow.objectName():
            ShowPaintNoteWindow.setObjectName(u"ShowPaintNoteWindow")
        ShowPaintNoteWindow.resize(786, 531)
        self.gridLayout = QGridLayout(ShowPaintNoteWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.paintNoteLabel = QLabel(ShowPaintNoteWindow)
        self.paintNoteLabel.setObjectName(u"paintNoteLabel")

        self.verticalLayout.addWidget(self.paintNoteLabel)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.backButton = QPushButton(ShowPaintNoteWindow)
        self.backButton.setObjectName(u"backButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.backButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(ShowPaintNoteWindow)

        QMetaObject.connectSlotsByName(ShowPaintNoteWindow)
    # setupUi

    def retranslateUi(self, ShowPaintNoteWindow):
        ShowPaintNoteWindow.setWindowTitle(QCoreApplication.translate("ShowPaintNoteWindow", u"Dialog", None))
        self.paintNoteLabel.setText("")
        self.backButton.setText(QCoreApplication.translate("ShowPaintNoteWindow", u"Back", None))
    # retranslateUi

