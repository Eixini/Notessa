# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note_list_gadget.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableView,
    QVBoxLayout, QWidget)
from Notessa.resources.icons.button import button_icons_rc

class Ui_NoteListGadget(object):
    def setupUi(self, NoteListGadget):
        if not NoteListGadget.objectName():
            NoteListGadget.setObjectName(u"NoteListGadget")
        NoteListGadget.resize(557, 511)
        self.verticalLayout = QVBoxLayout(NoteListGadget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.create_note_button = QPushButton(NoteListGadget)
        self.create_note_button.setObjectName(u"create_note_button")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_note_button.sizePolicy().hasHeightForWidth())
        self.create_note_button.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(14)
        font.setBold(True)
        self.create_note_button.setFont(font)
        icon = QIcon()
        icon.addFile(u":/button/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.create_note_button.setIcon(icon)
        self.create_note_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.create_note_button)

        self.refresh_button = QPushButton(NoteListGadget)
        self.refresh_button.setObjectName(u"refresh_button")
        sizePolicy.setHeightForWidth(self.refresh_button.sizePolicy().hasHeightForWidth())
        self.refresh_button.setSizePolicy(sizePolicy)
        self.refresh_button.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/button/refresh.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.refresh_button.setIcon(icon1)
        self.refresh_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.refresh_button)

        self.calendar_button = QPushButton(NoteListGadget)
        self.calendar_button.setObjectName(u"calendar_button")
        sizePolicy.setHeightForWidth(self.calendar_button.sizePolicy().hasHeightForWidth())
        self.calendar_button.setSizePolicy(sizePolicy)
        self.calendar_button.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/button/calendar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.calendar_button.setIcon(icon2)
        self.calendar_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.calendar_button)

        self.horizontalSpacer = QSpacerItem(138, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.filter_combobox = QComboBox(NoteListGadget)
        self.filter_combobox.setObjectName(u"filter_combobox")

        self.horizontalLayout.addWidget(self.filter_combobox)

        self.pin_gadget_button = QPushButton(NoteListGadget)
        self.pin_gadget_button.setObjectName(u"pin_gadget_button")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(11)
        font1.setBold(False)
        self.pin_gadget_button.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/button/pin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pin_gadget_button.setIcon(icon3)
        self.pin_gadget_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pin_gadget_button)

        self.close_button = QPushButton(NoteListGadget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/button/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.close_button.setIcon(icon4)
        self.close_button.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.close_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.table_view = QTableView(NoteListGadget)
        self.table_view.setObjectName(u"table_view")

        self.verticalLayout.addWidget(self.table_view)


        self.retranslateUi(NoteListGadget)

        QMetaObject.connectSlotsByName(NoteListGadget)
    # setupUi

    def retranslateUi(self, NoteListGadget):
        NoteListGadget.setWindowTitle(QCoreApplication.translate("NoteListGadget", u"Note list", None))
#if QT_CONFIG(tooltip)
        self.create_note_button.setToolTip(QCoreApplication.translate("NoteListGadget", u"Add note", None))
#endif // QT_CONFIG(tooltip)
        self.create_note_button.setText("")
#if QT_CONFIG(tooltip)
        self.refresh_button.setToolTip(QCoreApplication.translate("NoteListGadget", u"Refresh notes list", None))
#endif // QT_CONFIG(tooltip)
        self.refresh_button.setText("")
#if QT_CONFIG(tooltip)
        self.calendar_button.setToolTip(QCoreApplication.translate("NoteListGadget", u"Calendar", None))
#endif // QT_CONFIG(tooltip)
        self.calendar_button.setText("")
        self.filter_combobox.setPlaceholderText(QCoreApplication.translate("NoteListGadget", u"Show note types", None))
#if QT_CONFIG(tooltip)
        self.pin_gadget_button.setToolTip(QCoreApplication.translate("NoteListGadget", u"Pin/Unpin", None))
#endif // QT_CONFIG(tooltip)
        self.pin_gadget_button.setText("")
#if QT_CONFIG(tooltip)
        self.close_button.setToolTip(QCoreApplication.translate("NoteListGadget", u"Hide", None))
#endif // QT_CONFIG(tooltip)
        self.close_button.setText("")
    # retranslateUi

