from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSlider, QVBoxLayout)

class Ui_ShowVoiceNoteWindow(object):
    def setupUi(self, ShowVoiceNoteWindow):
        if not ShowVoiceNoteWindow.objectName():
            ShowVoiceNoteWindow.setObjectName(u"ShowVoiceNoteWindow")
        ShowVoiceNoteWindow.resize(404, 192)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ShowVoiceNoteWindow.sizePolicy().hasHeightForWidth())
        ShowVoiceNoteWindow.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(ShowVoiceNoteWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.voiceNoteName = QLabel(ShowVoiceNoteWindow)
        self.voiceNoteName.setObjectName(u"voiceNoteName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.voiceNoteName.sizePolicy().hasHeightForWidth())
        self.voiceNoteName.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.voiceNoteName)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.currentPositionLabel = QLabel(ShowVoiceNoteWindow)
        self.currentPositionLabel.setObjectName(u"currentPositionLabel")

        self.horizontalLayout.addWidget(self.currentPositionLabel)

        self.positionSlider = QSlider(ShowVoiceNoteWindow)
        self.positionSlider.setObjectName(u"positionSlider")
        self.positionSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.positionSlider)

        self.durationLabel = QLabel(ShowVoiceNoteWindow)
        self.durationLabel.setObjectName(u"durationLabel")

        self.horizontalLayout.addWidget(self.durationLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.volumeLabel = QLabel(ShowVoiceNoteWindow)
        self.volumeLabel.setObjectName(u"volumeLabel")

        self.horizontalLayout_3.addWidget(self.volumeLabel)

        self.volumeSlider = QSlider(ShowVoiceNoteWindow)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.volumeSlider)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.playButton = QPushButton(ShowVoiceNoteWindow)
        self.playButton.setObjectName(u"playButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.playButton)

        self.pauseButton = QPushButton(ShowVoiceNoteWindow)
        self.pauseButton.setObjectName(u"pauseButton")
        sizePolicy2.setHeightForWidth(self.pauseButton.sizePolicy().hasHeightForWidth())
        self.pauseButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.pauseButton)

        self.stopButton = QPushButton(ShowVoiceNoteWindow)
        self.stopButton.setObjectName(u"stopButton")
        sizePolicy2.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.stopButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.backButton = QPushButton(ShowVoiceNoteWindow)
        self.backButton.setObjectName(u"backButton")

        self.verticalLayout_2.addWidget(self.backButton)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.retranslateUi(ShowVoiceNoteWindow)

        QMetaObject.connectSlotsByName(ShowVoiceNoteWindow)
    # setupUi

    def retranslateUi(self, ShowVoiceNoteWindow):
        ShowVoiceNoteWindow.setWindowTitle(QCoreApplication.translate("ShowVoiceNoteWindow", u"Voice note", None))
        self.voiceNoteName.setText(QCoreApplication.translate("ShowVoiceNoteWindow", u"Voice note name", None))
        self.currentPositionLabel.setText(QCoreApplication.translate("ShowVoiceNoteWindow", u"00:00", None))
        self.durationLabel.setText(QCoreApplication.translate("ShowVoiceNoteWindow", u"00:00", None))
        self.volumeLabel.setText(QCoreApplication.translate("ShowVoiceNoteWindow", u"Volume", None))
        self.playButton.setText(QCoreApplication.translate("ShowVoiceNoteWindow", u"Play", None))
        self.pauseButton.setText(QCoreApplication.translate("ShowVoiceNoteWindow", u"Pause", None))
        self.stopButton.setText(QCoreApplication.translate("ShowVoiceNoteWindow", u"Stop", None))
        self.backButton.setText(QCoreApplication.translate("ShowVoiceNoteWindow", u"Back", None))
    # retranslateUi

