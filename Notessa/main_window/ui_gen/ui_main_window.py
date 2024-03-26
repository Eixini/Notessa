# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)
from Notessa.resource import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1155, 675)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.folded_sidebar = QWidget(self.centralwidget)
        self.folded_sidebar.setObjectName(u"folded_sidebar")
        self.gridLayout = QGridLayout(self.folded_sidebar)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fs_buttons_vlayout = QVBoxLayout()
        self.fs_buttons_vlayout.setSpacing(10)
        self.fs_buttons_vlayout.setObjectName(u"fs_buttons_vlayout")
        self.fs_shownotes_button = QPushButton(self.folded_sidebar)
        self.fs_shownotes_button.setObjectName(u"fs_shownotes_button")
        icon = QIcon()
        icon.addFile(u":/icons/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fs_shownotes_button.setIcon(icon)
        self.fs_shownotes_button.setIconSize(QSize(32, 32))
        self.fs_shownotes_button.setCheckable(True)
        self.fs_shownotes_button.setAutoExclusive(True)

        self.fs_buttons_vlayout.addWidget(self.fs_shownotes_button)

        self.fs_create_textnote_button = QPushButton(self.folded_sidebar)
        self.fs_create_textnote_button.setObjectName(u"fs_create_textnote_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/text.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fs_create_textnote_button.setIcon(icon1)
        self.fs_create_textnote_button.setIconSize(QSize(32, 32))
        self.fs_create_textnote_button.setCheckable(True)
        self.fs_create_textnote_button.setAutoExclusive(True)

        self.fs_buttons_vlayout.addWidget(self.fs_create_textnote_button)

        self.fs_create_voicenote_button = QPushButton(self.folded_sidebar)
        self.fs_create_voicenote_button.setObjectName(u"fs_create_voicenote_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/microphone.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fs_create_voicenote_button.setIcon(icon2)
        self.fs_create_voicenote_button.setIconSize(QSize(32, 32))
        self.fs_create_voicenote_button.setCheckable(True)
        self.fs_create_voicenote_button.setAutoExclusive(True)

        self.fs_buttons_vlayout.addWidget(self.fs_create_voicenote_button)

        self.fs_create_videonote_button = QPushButton(self.folded_sidebar)
        self.fs_create_videonote_button.setObjectName(u"fs_create_videonote_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/video.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fs_create_videonote_button.setIcon(icon3)
        self.fs_create_videonote_button.setIconSize(QSize(32, 32))
        self.fs_create_videonote_button.setCheckable(True)
        self.fs_create_videonote_button.setAutoExclusive(True)

        self.fs_buttons_vlayout.addWidget(self.fs_create_videonote_button)

        self.fs_create_paintnote_button = QPushButton(self.folded_sidebar)
        self.fs_create_paintnote_button.setObjectName(u"fs_create_paintnote_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/brush.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fs_create_paintnote_button.setIcon(icon4)
        self.fs_create_paintnote_button.setIconSize(QSize(32, 32))
        self.fs_create_paintnote_button.setCheckable(True)
        self.fs_create_paintnote_button.setAutoExclusive(True)

        self.fs_buttons_vlayout.addWidget(self.fs_create_paintnote_button)

        self.fs_create_todonote_button = QPushButton(self.folded_sidebar)
        self.fs_create_todonote_button.setObjectName(u"fs_create_todonote_button")
        icon5 = QIcon()
        icon5.addFile(u":/icons/todo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fs_create_todonote_button.setIcon(icon5)
        self.fs_create_todonote_button.setIconSize(QSize(32, 32))
        self.fs_create_todonote_button.setCheckable(True)
        self.fs_create_todonote_button.setAutoExclusive(True)

        self.fs_buttons_vlayout.addWidget(self.fs_create_todonote_button)

        self.fs_vertical_spacer = QSpacerItem(20, 198, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fs_buttons_vlayout.addItem(self.fs_vertical_spacer)

        self.fs_settings_button = QPushButton(self.folded_sidebar)
        self.fs_settings_button.setObjectName(u"fs_settings_button")
        icon6 = QIcon()
        icon6.addFile(u":/icons/gear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fs_settings_button.setIcon(icon6)
        self.fs_settings_button.setIconSize(QSize(32, 32))
        self.fs_settings_button.setCheckable(True)
        self.fs_settings_button.setAutoExclusive(True)

        self.fs_buttons_vlayout.addWidget(self.fs_settings_button)

        self.fs_exit_button = QPushButton(self.folded_sidebar)
        self.fs_exit_button.setObjectName(u"fs_exit_button")
        icon7 = QIcon()
        icon7.addFile(u":/icons/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fs_exit_button.setIcon(icon7)
        self.fs_exit_button.setIconSize(QSize(32, 32))

        self.fs_buttons_vlayout.addWidget(self.fs_exit_button)


        self.gridLayout.addLayout(self.fs_buttons_vlayout, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.folded_sidebar)

        self.expanded_sidebar = QWidget(self.centralwidget)
        self.expanded_sidebar.setObjectName(u"expanded_sidebar")
        self.gridLayout_2 = QGridLayout(self.expanded_sidebar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.es_buttons_vlayout = QVBoxLayout()
        self.es_buttons_vlayout.setSpacing(10)
        self.es_buttons_vlayout.setObjectName(u"es_buttons_vlayout")
        self.es_shownotes_button = QPushButton(self.expanded_sidebar)
        self.es_shownotes_button.setObjectName(u"es_shownotes_button")
        self.es_shownotes_button.setMinimumSize(QSize(0, 30))
        self.es_shownotes_button.setIcon(icon)
        self.es_shownotes_button.setIconSize(QSize(32, 32))
        self.es_shownotes_button.setCheckable(True)
        self.es_shownotes_button.setAutoExclusive(True)

        self.es_buttons_vlayout.addWidget(self.es_shownotes_button)

        self.es_create_textnote_button = QPushButton(self.expanded_sidebar)
        self.es_create_textnote_button.setObjectName(u"es_create_textnote_button")
        self.es_create_textnote_button.setMinimumSize(QSize(0, 30))
        self.es_create_textnote_button.setIcon(icon1)
        self.es_create_textnote_button.setIconSize(QSize(32, 32))
        self.es_create_textnote_button.setCheckable(True)
        self.es_create_textnote_button.setAutoExclusive(True)

        self.es_buttons_vlayout.addWidget(self.es_create_textnote_button)

        self.es_create_voicenote_button = QPushButton(self.expanded_sidebar)
        self.es_create_voicenote_button.setObjectName(u"es_create_voicenote_button")
        self.es_create_voicenote_button.setMinimumSize(QSize(0, 30))
        self.es_create_voicenote_button.setIcon(icon2)
        self.es_create_voicenote_button.setIconSize(QSize(32, 32))
        self.es_create_voicenote_button.setCheckable(True)
        self.es_create_voicenote_button.setAutoExclusive(True)

        self.es_buttons_vlayout.addWidget(self.es_create_voicenote_button)

        self.es_create_videonote_button = QPushButton(self.expanded_sidebar)
        self.es_create_videonote_button.setObjectName(u"es_create_videonote_button")
        self.es_create_videonote_button.setMinimumSize(QSize(0, 30))
        self.es_create_videonote_button.setIcon(icon3)
        self.es_create_videonote_button.setIconSize(QSize(32, 32))
        self.es_create_videonote_button.setCheckable(True)
        self.es_create_videonote_button.setAutoExclusive(True)

        self.es_buttons_vlayout.addWidget(self.es_create_videonote_button)

        self.es_create_paintnote_button = QPushButton(self.expanded_sidebar)
        self.es_create_paintnote_button.setObjectName(u"es_create_paintnote_button")
        self.es_create_paintnote_button.setMinimumSize(QSize(0, 30))
        self.es_create_paintnote_button.setIcon(icon4)
        self.es_create_paintnote_button.setIconSize(QSize(32, 32))
        self.es_create_paintnote_button.setCheckable(True)
        self.es_create_paintnote_button.setAutoExclusive(True)

        self.es_buttons_vlayout.addWidget(self.es_create_paintnote_button)

        self.es_create_todonote_button = QPushButton(self.expanded_sidebar)
        self.es_create_todonote_button.setObjectName(u"es_create_todonote_button")
        self.es_create_todonote_button.setMinimumSize(QSize(0, 30))
        self.es_create_todonote_button.setIcon(icon5)
        self.es_create_todonote_button.setIconSize(QSize(32, 32))
        self.es_create_todonote_button.setCheckable(True)
        self.es_create_todonote_button.setAutoExclusive(True)

        self.es_buttons_vlayout.addWidget(self.es_create_todonote_button)

        self.es_vertical_spacer = QSpacerItem(20, 230, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.es_buttons_vlayout.addItem(self.es_vertical_spacer)

        self.es_settings_button = QPushButton(self.expanded_sidebar)
        self.es_settings_button.setObjectName(u"es_settings_button")
        self.es_settings_button.setMinimumSize(QSize(0, 30))
        self.es_settings_button.setIcon(icon6)
        self.es_settings_button.setIconSize(QSize(32, 32))
        self.es_settings_button.setCheckable(True)
        self.es_settings_button.setAutoExclusive(True)

        self.es_buttons_vlayout.addWidget(self.es_settings_button)

        self.es_exit_button = QPushButton(self.expanded_sidebar)
        self.es_exit_button.setObjectName(u"es_exit_button")
        self.es_exit_button.setMinimumSize(QSize(0, 30))
        self.es_exit_button.setIcon(icon7)
        self.es_exit_button.setIconSize(QSize(32, 32))

        self.es_buttons_vlayout.addWidget(self.es_exit_button)


        self.gridLayout_2.addLayout(self.es_buttons_vlayout, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.expanded_sidebar)

        self.content_area = QWidget(self.centralwidget)
        self.content_area.setObjectName(u"content_area")
        self.gridLayout_3 = QGridLayout(self.content_area)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.content_stacked = QStackedWidget(self.content_area)
        self.content_stacked.setObjectName(u"content_stacked")

        self.gridLayout_3.addWidget(self.content_stacked, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.content_area)

        MainWindow.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)

        self.content_stacked.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Notessa", None))
        self.fs_shownotes_button.setText("")
        self.fs_create_textnote_button.setText("")
        self.fs_create_voicenote_button.setText("")
        self.fs_create_videonote_button.setText("")
        self.fs_create_paintnote_button.setText("")
        self.fs_create_todonote_button.setText("")
        self.fs_settings_button.setText("")
        self.fs_exit_button.setText("")
        self.es_shownotes_button.setText(QCoreApplication.translate("MainWindow", u"Show notes", None))
        self.es_create_textnote_button.setText(QCoreApplication.translate("MainWindow", u"Create text note", None))
        self.es_create_voicenote_button.setText(QCoreApplication.translate("MainWindow", u"Create voice note", None))
        self.es_create_videonote_button.setText(QCoreApplication.translate("MainWindow", u"Create video note", None))
        self.es_create_paintnote_button.setText(QCoreApplication.translate("MainWindow", u"Create paint note", None))
        self.es_create_todonote_button.setText(QCoreApplication.translate("MainWindow", u"Create ToDo", None))
        self.es_settings_button.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.es_exit_button.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

