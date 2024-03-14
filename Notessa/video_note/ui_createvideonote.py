from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout)

class Ui_CreateVideoNoteWindow(object):
    def setupUi(self, CreateVideoNoteWindow):
        if not CreateVideoNoteWindow.objectName():
            CreateVideoNoteWindow.setObjectName(u"CreateVideoNoteWindow")
        CreateVideoNoteWindow.setWindowModality(Qt.NonModal)
        CreateVideoNoteWindow.resize(538, 432)
        self.gridLayout = QGridLayout(CreateVideoNoteWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.stateLabel = QLabel(CreateVideoNoteWindow)
        self.stateLabel.setObjectName(u"stateLabel")

        self.horizontalLayout_3.addWidget(self.stateLabel)

        self.durationLabel = QLabel(CreateVideoNoteWindow)
        self.durationLabel.setObjectName(u"durationLabel")

        self.horizontalLayout_3.addWidget(self.durationLabel)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.videoNoteName = QLineEdit(CreateVideoNoteWindow)
        self.videoNoteName.setObjectName(u"videoNoteName")

        self.horizontalLayout_3.addWidget(self.videoNoteName)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.videoLabel = QLabel(CreateVideoNoteWindow)
        self.videoLabel.setObjectName(u"videoLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoLabel.sizePolicy().hasHeightForWidth())
        self.videoLabel.setSizePolicy(sizePolicy)
        self.videoLabel.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.videoLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.recordButton = QPushButton(CreateVideoNoteWindow)
        self.recordButton.setObjectName(u"recordButton")

        self.horizontalLayout.addWidget(self.recordButton)

        self.pauseButton = QPushButton(CreateVideoNoteWindow)
        self.pauseButton.setObjectName(u"pauseButton")

        self.horizontalLayout.addWidget(self.pauseButton)

        self.stopButton = QPushButton(CreateVideoNoteWindow)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout.addWidget(self.stopButton)

        self.muteButton = QPushButton(CreateVideoNoteWindow)
        self.muteButton.setObjectName(u"muteButton")

        self.horizontalLayout.addWidget(self.muteButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.backButton = QPushButton(CreateVideoNoteWindow)
        self.backButton.setObjectName(u"backButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.backButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(CreateVideoNoteWindow)

        QMetaObject.connectSlotsByName(CreateVideoNoteWindow)
    # setupUi

    def retranslateUi(self, CreateVideoNoteWindow):
        CreateVideoNoteWindow.setWindowTitle(QCoreApplication.translate("CreateVideoNoteWindow", u"Create video note", None))
        self.stateLabel.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"STATE", None))
        self.durationLabel.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"00:00", None))
        self.videoNoteName.setPlaceholderText(QCoreApplication.translate("CreateVideoNoteWindow", u"Enter video note name ...", None))
        self.videoLabel.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"TextLabel", None))
        self.recordButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Record", None))
        self.pauseButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Pause", None))
        self.stopButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Stop", None))
        self.muteButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Mute", None))
        self.backButton.setText(QCoreApplication.translate("CreateVideoNoteWindow", u"Back", None))
    # retranslateUi

