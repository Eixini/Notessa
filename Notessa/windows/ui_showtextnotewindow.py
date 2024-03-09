from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_ShowTextNoteWindow(object):
    def setupUi(self, ShowTextNoteWindow):
        if not ShowTextNoteWindow.objectName():
            ShowTextNoteWindow.setObjectName(u"ShowTextNoteWindow")
        ShowTextNoteWindow.setWindowModality(Qt.NonModal)
        ShowTextNoteWindow.resize(534, 454)
        self.gridLayout = QGridLayout(ShowTextNoteWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.showTextNoteField = QTextEdit(ShowTextNoteWindow)
        self.showTextNoteField.setObjectName(u"showTextNoteField")
        self.showTextNoteField.setReadOnly(True)

        self.verticalLayout.addWidget(self.showTextNoteField)

        self.backButton = QPushButton(ShowTextNoteWindow)
        self.backButton.setObjectName(u"backButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.backButton)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(ShowTextNoteWindow)

        QMetaObject.connectSlotsByName(ShowTextNoteWindow)
    # setupUi

    def retranslateUi(self, ShowTextNoteWindow):
        ShowTextNoteWindow.setWindowTitle(QCoreApplication.translate("ShowTextNoteWindow", u"Text note", None))
        self.backButton.setText(QCoreApplication.translate("ShowTextNoteWindow", u"Back", None))
    # retranslateUi

