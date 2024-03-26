# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_paintnote_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from Notessa.paint_note.painter_widget import PainterWidget
from Notessa.resource import icons_rc

class Ui_CreatePaintNoteWidget(object):
    def setupUi(self, CreatePaintNoteWidget):
        if not CreatePaintNoteWidget.objectName():
            CreatePaintNoteWidget.setObjectName(u"CreatePaintNoteWidget")
        CreatePaintNoteWidget.resize(997, 728)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreatePaintNoteWidget.sizePolicy().hasHeightForWidth())
        CreatePaintNoteWidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(CreatePaintNoteWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.paintnote_name_horizontal_layout = QHBoxLayout()
        self.paintnote_name_horizontal_layout.setObjectName(u"paintnote_name_horizontal_layout")
        self.paintnote_name_label = QLabel(CreatePaintNoteWidget)
        self.paintnote_name_label.setObjectName(u"paintnote_name_label")

        self.paintnote_name_horizontal_layout.addWidget(self.paintnote_name_label)

        self.paintnote_name_lineedit = QLineEdit(CreatePaintNoteWidget)
        self.paintnote_name_lineedit.setObjectName(u"paintnote_name_lineedit")

        self.paintnote_name_horizontal_layout.addWidget(self.paintnote_name_lineedit)


        self.verticalLayout.addLayout(self.paintnote_name_horizontal_layout)

        self.painter_widget = PainterWidget(CreatePaintNoteWidget)
        self.painter_widget.setObjectName(u"painter_widget")
        sizePolicy.setHeightForWidth(self.painter_widget.sizePolicy().hasHeightForWidth())
        self.painter_widget.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.painter_widget)

        self.panel_horizontal_layout = QHBoxLayout()
        self.panel_horizontal_layout.setSpacing(0)
        self.panel_horizontal_layout.setObjectName(u"panel_horizontal_layout")
        self.panel_horizontal_layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.close_button = QPushButton(CreatePaintNoteWidget)
        self.close_button.setObjectName(u"close_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.close_button.sizePolicy().hasHeightForWidth())
        self.close_button.setSizePolicy(sizePolicy1)
        self.close_button.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close_button.setIcon(icon)
        self.close_button.setIconSize(QSize(32, 32))

        self.panel_horizontal_layout.addWidget(self.close_button)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.panel_horizontal_layout.addItem(self.horizontalSpacer)

        self.color_button = QPushButton(CreatePaintNoteWidget)
        self.color_button.setObjectName(u"color_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/colors.png", QSize(), QIcon.Normal, QIcon.Off)
        self.color_button.setIcon(icon1)
        self.color_button.setIconSize(QSize(32, 32))

        self.panel_horizontal_layout.addWidget(self.color_button)

        self.brush_widht_label = QLabel(CreatePaintNoteWidget)
        self.brush_widht_label.setObjectName(u"brush_widht_label")

        self.panel_horizontal_layout.addWidget(self.brush_widht_label)

        self.pen_width_double_spinbox = QDoubleSpinBox(CreatePaintNoteWidget)
        self.pen_width_double_spinbox.setObjectName(u"pen_width_double_spinbox")

        self.panel_horizontal_layout.addWidget(self.pen_width_double_spinbox)

        self.pa = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.panel_horizontal_layout.addItem(self.pa)

        self.save_button = QPushButton(CreatePaintNoteWidget)
        self.save_button.setObjectName(u"save_button")
        sizePolicy1.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_button.setIcon(icon2)
        self.save_button.setIconSize(QSize(32, 32))

        self.panel_horizontal_layout.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.panel_horizontal_layout)


        self.retranslateUi(CreatePaintNoteWidget)

        QMetaObject.connectSlotsByName(CreatePaintNoteWidget)
    # setupUi

    def retranslateUi(self, CreatePaintNoteWidget):
        CreatePaintNoteWidget.setWindowTitle(QCoreApplication.translate("CreatePaintNoteWidget", u"Form", None))
        self.paintnote_name_label.setText(QCoreApplication.translate("CreatePaintNoteWidget", u"Enter note name", None))
        self.close_button.setText(QCoreApplication.translate("CreatePaintNoteWidget", u"Back", None))
        self.color_button.setText("")
        self.brush_widht_label.setText(QCoreApplication.translate("CreatePaintNoteWidget", u"Width", None))
        self.save_button.setText("")
    # retranslateUi

