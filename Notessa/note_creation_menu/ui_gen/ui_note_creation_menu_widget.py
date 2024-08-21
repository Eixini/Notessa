# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'note_creation_menu_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QPushButton,
    QSizePolicy, QWidget)

from Notessa.resources.icons.note_type import note_type_icons_rc
from Notessa.resources.icons.common import common_icons_rc


class Ui_NoteCreationMenuWidget(object):
    def setupUi(self, NoteCreationMenuWidget):
        if not NoteCreationMenuWidget.objectName():
            NoteCreationMenuWidget.setObjectName(u"NoteCreationMenuWidget")
        NoteCreationMenuWidget.resize(360, 70)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NoteCreationMenuWidget.sizePolicy().hasHeightForWidth())
        NoteCreationMenuWidget.setSizePolicy(sizePolicy)
        NoteCreationMenuWidget.setMinimumSize(QSize(360, 70))
        NoteCreationMenuWidget.setMaximumSize(QSize(360, 70))
        icon = QIcon()
        icon.addFile(u":/common/notessa_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        NoteCreationMenuWidget.setWindowIcon(icon)
        self.layoutWidget = QWidget(NoteCreationMenuWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(9, 9, 351, 58))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.create_text_note_button = QPushButton(self.layoutWidget)
        self.create_text_note_button.setObjectName(u"create_text_note_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.create_text_note_button.sizePolicy().hasHeightForWidth())
        self.create_text_note_button.setSizePolicy(sizePolicy1)
        self.create_text_note_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon1 = QIcon()
        icon1.addFile(u":/note_type/text.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.create_text_note_button.setIcon(icon1)
        self.create_text_note_button.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.create_text_note_button)

        self.create_voice_note_button = QPushButton(self.layoutWidget)
        self.create_voice_note_button.setObjectName(u"create_voice_note_button")
        sizePolicy1.setHeightForWidth(self.create_voice_note_button.sizePolicy().hasHeightForWidth())
        self.create_voice_note_button.setSizePolicy(sizePolicy1)
        self.create_voice_note_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon2 = QIcon()
        icon2.addFile(u":/note_type/voice.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.create_voice_note_button.setIcon(icon2)
        self.create_voice_note_button.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.create_voice_note_button)

        self.create_video_note_button = QPushButton(self.layoutWidget)
        self.create_video_note_button.setObjectName(u"create_video_note_button")
        sizePolicy1.setHeightForWidth(self.create_video_note_button.sizePolicy().hasHeightForWidth())
        self.create_video_note_button.setSizePolicy(sizePolicy1)
        self.create_video_note_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon3 = QIcon()
        icon3.addFile(u":/note_type/video.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.create_video_note_button.setIcon(icon3)
        self.create_video_note_button.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.create_video_note_button)

        self.create_paint_note_button = QPushButton(self.layoutWidget)
        self.create_paint_note_button.setObjectName(u"create_paint_note_button")
        sizePolicy1.setHeightForWidth(self.create_paint_note_button.sizePolicy().hasHeightForWidth())
        self.create_paint_note_button.setSizePolicy(sizePolicy1)
        self.create_paint_note_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon4 = QIcon()
        icon4.addFile(u":/note_type/paint.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.create_paint_note_button.setIcon(icon4)
        self.create_paint_note_button.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.create_paint_note_button)

        self.create_todo_note_button = QPushButton(self.layoutWidget)
        self.create_todo_note_button.setObjectName(u"create_todo_note_button")
        sizePolicy1.setHeightForWidth(self.create_todo_note_button.sizePolicy().hasHeightForWidth())
        self.create_todo_note_button.setSizePolicy(sizePolicy1)
        self.create_todo_note_button.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        icon5 = QIcon()
        icon5.addFile(u":/note_type/todo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.create_todo_note_button.setIcon(icon5)
        self.create_todo_note_button.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.create_todo_note_button)


        self.retranslateUi(NoteCreationMenuWidget)

        QMetaObject.connectSlotsByName(NoteCreationMenuWidget)
    # setupUi

    def retranslateUi(self, NoteCreationMenuWidget):
        NoteCreationMenuWidget.setWindowTitle(QCoreApplication.translate("NoteCreationMenuWidget", u"Note creation", None))
#if QT_CONFIG(tooltip)
        self.create_text_note_button.setToolTip(QCoreApplication.translate("NoteCreationMenuWidget", u"Create Text note", None))
#endif // QT_CONFIG(tooltip)
        self.create_text_note_button.setText("")
#if QT_CONFIG(tooltip)
        self.create_voice_note_button.setToolTip(QCoreApplication.translate("NoteCreationMenuWidget", u"Create Voice note", None))
#endif // QT_CONFIG(tooltip)
        self.create_voice_note_button.setText("")
#if QT_CONFIG(tooltip)
        self.create_video_note_button.setToolTip(QCoreApplication.translate("NoteCreationMenuWidget", u"Create Video note", None))
#endif // QT_CONFIG(tooltip)
        self.create_video_note_button.setText("")
#if QT_CONFIG(tooltip)
        self.create_paint_note_button.setToolTip(QCoreApplication.translate("NoteCreationMenuWidget", u"Create Paint note", None))
#endif // QT_CONFIG(tooltip)
        self.create_paint_note_button.setText("")
#if QT_CONFIG(tooltip)
        self.create_todo_note_button.setToolTip(QCoreApplication.translate("NoteCreationMenuWidget", u"Create Todo note", None))
#endif // QT_CONFIG(tooltip)
        self.create_todo_note_button.setText("")
    # retranslateUi

