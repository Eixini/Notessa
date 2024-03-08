from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)


class Ui_CreateTextNoteWindow(object):
    def setupUi(self, Ui_CreateTextNoteWindow):
        if not Ui_CreateTextNoteWindow.objectName():
            Ui_CreateTextNoteWindow.setObjectName(u"Ui_CreateTextNoteWindow")
        Ui_CreateTextNoteWindow.resize(896, 504)
        icon = QIcon()
        icon.addFile(u":/resource/icons/text.png", QSize(), QIcon.Normal, QIcon.Off)
        Ui_CreateTextNoteWindow.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Ui_CreateTextNoteWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.textNoteName = QLineEdit(Ui_CreateTextNoteWindow)
        self.textNoteName.setObjectName(u"textNoteName")
        self.textNoteName.setMaxLength(256)

        self.verticalLayout.addWidget(self.textNoteName)

        self.textNoteField = QTextEdit(Ui_CreateTextNoteWindow)
        self.textNoteField.setObjectName(u"textNoteField")

        self.verticalLayout.addWidget(self.textNoteField)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.saveButton = QPushButton(Ui_CreateTextNoteWindow)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u":/resource/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.saveButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.cancelButton = QPushButton(Ui_CreateTextNoteWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        sizePolicy.setHeightForWidth(self.cancelButton.sizePolicy().hasHeightForWidth())
        self.cancelButton.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u":/resource/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.cancelButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Ui_CreateTextNoteWindow)

        QMetaObject.connectSlotsByName(Ui_CreateTextNoteWindow)
    # setupUi

    def retranslateUi(self, Ui_CreateTextNoteWindow):
        Ui_CreateTextNoteWindow.setWindowTitle(QCoreApplication.translate("Ui_CreateTextNoteWindow", u"Dialog", None))
        self.textNoteName.setPlaceholderText(QCoreApplication.translate("Ui_CreateTextNoteWindow", u"Enter note name...", None))
        self.textNoteField.setPlaceholderText(QCoreApplication.translate("Ui_CreateTextNoteWindow", u"Here you can write your note...", None))
        self.saveButton.setText(QCoreApplication.translate("Ui_CreateTextNoteWindow", u"Save", None))
        self.cancelButton.setText(QCoreApplication.translate("Ui_CreateTextNoteWindow", u"Cancel", None))
    # retranslateUi

