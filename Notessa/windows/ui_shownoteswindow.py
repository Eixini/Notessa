from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_ShowNotesWindow(object):
    def setupUi(self, ShowNotesWindow):
        if not ShowNotesWindow.objectName():
            ShowNotesWindow.setObjectName(u"ShowNotesWindow")
        ShowNotesWindow.setWindowModality(Qt.NonModal)
        ShowNotesWindow.resize(1000, 674)
        self.gridLayout = QGridLayout(ShowNotesWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.notesTableView = QTableView(ShowNotesWindow)
        self.notesTableView.setObjectName(u"notesTableView")
        self.notesTableView.setFrameShape(QFrame.NoFrame)
        self.notesTableView.setFrameShadow(QFrame.Plain)
        self.notesTableView.setMidLineWidth(1)
        self.notesTableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.notesTableView.setGridStyle(Qt.NoPen)
        self.notesTableView.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.notesTableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.showNoteButton = QPushButton(ShowNotesWindow)
        self.showNoteButton.setObjectName(u"showNoteButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showNoteButton.sizePolicy().hasHeightForWidth())
        self.showNoteButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.showNoteButton)

        self.deleteNoteButton = QPushButton(ShowNotesWindow)
        self.deleteNoteButton.setObjectName(u"deleteNoteButton")

        self.horizontalLayout.addWidget(self.deleteNoteButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toMainMenuButton = QPushButton(ShowNotesWindow)
        self.toMainMenuButton.setObjectName(u"toMainMenuButton")
        sizePolicy.setHeightForWidth(self.toMainMenuButton.sizePolicy().hasHeightForWidth())
        self.toMainMenuButton.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.toMainMenuButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(ShowNotesWindow)

        QMetaObject.connectSlotsByName(ShowNotesWindow)
    # setupUi

    def retranslateUi(self, ShowNotesWindow):
        ShowNotesWindow.setWindowTitle(QCoreApplication.translate("ShowNotesWindow", u"Show notes", None))
        self.showNoteButton.setText(QCoreApplication.translate("ShowNotesWindow", u"Show note", None))
        self.deleteNoteButton.setText(QCoreApplication.translate("ShowNotesWindow", u"Delete note", None))
        self.toMainMenuButton.setText(QCoreApplication.translate("ShowNotesWindow", u"Main menu", None))
    # retranslateUi

