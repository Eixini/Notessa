from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtWidgets import (QFrame,QLabel, QLayout, QPushButton, QSizePolicy,
                               QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(761, 562)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.showNotesButton = QPushButton(self.centralwidget)
        self.showNotesButton.setObjectName(u"showNotesButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showNotesButton.sizePolicy().hasHeightForWidth())
        self.showNotesButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.showNotesButton)

        self.verticalSpacer = QSpacerItem(20, 68, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.createNoteLabel = QLabel(self.centralwidget)
        self.createNoteLabel.setObjectName(u"createNoteLabel")
        self.createNoteLabel.setFrameShape(QFrame.NoFrame)
        self.createNoteLabel.setFrameShadow(QFrame.Plain)
        self.createNoteLabel.setLineWidth(3)
        self.createNoteLabel.setScaledContents(False)

        self.verticalLayout.addWidget(self.createNoteLabel)

        self.createTextNoteButton = QPushButton(self.centralwidget)
        self.createTextNoteButton.setObjectName(u"createTextNoteButton")
        sizePolicy.setHeightForWidth(self.createTextNoteButton.sizePolicy().hasHeightForWidth())
        self.createTextNoteButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.createTextNoteButton)

        self.createVoiceNoteButton = QPushButton(self.centralwidget)
        self.createVoiceNoteButton.setObjectName(u"createVoiceNoteButton")
        sizePolicy.setHeightForWidth(self.createVoiceNoteButton.sizePolicy().hasHeightForWidth())
        self.createVoiceNoteButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.createVoiceNoteButton)

        self.createVideoNoteButton = QPushButton(self.centralwidget)
        self.createVideoNoteButton.setObjectName(u"createVideoNoteButton")
        sizePolicy.setHeightForWidth(self.createVideoNoteButton.sizePolicy().hasHeightForWidth())
        self.createVideoNoteButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.createVideoNoteButton)

        self.createPaintNoteButton = QPushButton(self.centralwidget)
        self.createPaintNoteButton.setObjectName(u"createPaintNoteButton")
        sizePolicy.setHeightForWidth(self.createPaintNoteButton.sizePolicy().hasHeightForWidth())
        self.createPaintNoteButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.createPaintNoteButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.closeApplicationButton = QPushButton(self.centralwidget)
        self.closeApplicationButton.setObjectName(u"closeApplicationButton")
        sizePolicy.setHeightForWidth(self.closeApplicationButton.sizePolicy().hasHeightForWidth())
        self.closeApplicationButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.closeApplicationButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Notessa", None))
        self.showNotesButton.setText(QCoreApplication.translate("MainWindow", u"Show notes", None))
        self.createNoteLabel.setText(QCoreApplication.translate("MainWindow", u"Create a note", None))
        self.createTextNoteButton.setText(QCoreApplication.translate("MainWindow", u"Text note", None))
        self.createVoiceNoteButton.setText(QCoreApplication.translate("MainWindow", u"Voice note", None))
        self.createVideoNoteButton.setText(QCoreApplication.translate("MainWindow", u"Video note", None))
        self.createPaintNoteButton.setText(QCoreApplication.translate("MainWindow", u"Paint note", None))
        self.closeApplicationButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

