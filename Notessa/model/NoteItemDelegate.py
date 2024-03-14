import PyQt6.QtWidgets
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem, QItemDelegate, QStyle
from PySide6.QtCore import QModelIndex, QPoint, QRect, QModelRoleData, Qt
from PySide6.QtGui import QIcon, QPixmap
from Notessa.resource import rc_icons

class NoteItemDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index):
        super(NoteItemDelegate, self).initStyleOption(option, index)
        option.Position = QStyleOptionViewItem.Position.Left

        noteType = index.data()

        icons = {
            'text': ':/resource/icons/text.png',
            'voice': ':/resource/icons/microphone.png',
            'video': ':/resource/icons/video.png',
            'paint': ':/resource/icons/brush.png'
        }
        iconExample = QPixmap(':/resource/icons/text.png')
        rect = QRect(QPoint(), iconExample.size().scaled(option.rect.size(), Qt.AspectRatioMode.KeepAspectRatio))
        rect.moveCenter(option.rect.center())

        if noteType == 'txt':
            painter.drawPixmap(rect, QPixmap(icons['text']))
        if noteType == 'wav':
            painter.drawPixmap(rect, QPixmap(icons['voice']))
        if noteType == 'mp4':
            painter.drawPixmap(rect, QPixmap(icons['video']))
        if noteType == 'png':
            painter.drawPixmap(rect, QPixmap(icons['paint']))
