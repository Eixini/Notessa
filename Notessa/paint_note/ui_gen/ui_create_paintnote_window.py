# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_paintnote_window.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStatusBar,
    QToolBar, QVBoxLayout, QWidget)

from Notessa.paint_note.PaintingArea import PaintingArea

class Ui_CreatePaintNoteWindow(object):
    def setupUi(self, CreatePaintNoteWindow):
        if not CreatePaintNoteWindow.objectName():
            CreatePaintNoteWindow.setObjectName(u"CreatePaintNoteWindow")
        CreatePaintNoteWindow.resize(1036, 680)
        self.centralwidget = QWidget(CreatePaintNoteWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.canvas = PaintingArea(self.centralwidget)
        self.canvas.setObjectName(u"canvas")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy)
        self.canvas.setMinimumSize(QSize(200, 200))

        self.verticalLayout.addWidget(self.canvas)

        CreatePaintNoteWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(CreatePaintNoteWindow)
        self.statusbar.setObjectName(u"statusbar")
        CreatePaintNoteWindow.setStatusBar(self.statusbar)
        self.toolbar = QToolBar(CreatePaintNoteWindow)
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setMovable(False)
        self.toolbar.setIconSize(QSize(32, 32))
        self.toolbar.setFloatable(False)
        CreatePaintNoteWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolbar)

        self.retranslateUi(CreatePaintNoteWindow)

        QMetaObject.connectSlotsByName(CreatePaintNoteWindow)
    # setupUi

    def retranslateUi(self, CreatePaintNoteWindow):
        CreatePaintNoteWindow.setWindowTitle(QCoreApplication.translate("CreatePaintNoteWindow", u"MainWindow", None))
        self.toolbar.setWindowTitle(QCoreApplication.translate("CreatePaintNoteWindow", u"toolBar", None))
    # retranslateUi

