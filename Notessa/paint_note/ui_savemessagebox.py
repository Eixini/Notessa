from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout)

class Ui_SaveMessageBox(object):
    def setupUi(self, SaveMessageBox):
        if not SaveMessageBox.objectName():
            SaveMessageBox.setObjectName(u"SaveMessageBox")
        SaveMessageBox.resize(327, 88)
        self.gridLayout = QGridLayout(SaveMessageBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.note_name_lineedit = QLineEdit(SaveMessageBox)
        self.note_name_lineedit.setObjectName(u"note_name_lineedit")
        self.note_name_lineedit.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.verticalLayout.addWidget(self.note_name_lineedit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.saveButton = QPushButton(SaveMessageBox)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.saveButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(SaveMessageBox)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(SaveMessageBox)

        QMetaObject.connectSlotsByName(SaveMessageBox)
    # setupUi

    def retranslateUi(self, SaveMessageBox):
        SaveMessageBox.setWindowTitle(QCoreApplication.translate("SaveMessageBox", u"Dialog", None))
        self.note_name_lineedit.setPlaceholderText(QCoreApplication.translate("SaveMessageBox", u"Enter note name...", None))
        self.saveButton.setText(QCoreApplication.translate("SaveMessageBox", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("SaveMessageBox", u"Cancel", None))
    # retranslateUi

