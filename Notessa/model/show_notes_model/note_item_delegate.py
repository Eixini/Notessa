from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem
from PySide6.QtCore import QPoint, QRect, Qt
from PySide6.QtGui import QPixmap
from Notessa.resource import icons_rc


class NoteItemDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index):
        super(NoteItemDelegate, self).initStyleOption(option, index)
        option.Position = QStyleOptionViewItem.Position.Left

        note_type = index.data()

        icons = {
            'text': ':/icons/text.png',
            'voice': ':/icons/microphone.png',
            'video': ':/icons/video.png',
            'paint': ':/icons/brush.png',
            'todo': ':/icons/todo.png',
        }
        icon_example = QPixmap(':/icons/text.png')
        rect = QRect(QPoint(), icon_example.size().scaled(option.rect.size(), Qt.AspectRatioMode.KeepAspectRatio))
        rect.moveCenter(option.rect.center())

        if note_type == 'txt':
            painter.drawPixmap(rect, QPixmap(icons['text']))
        if note_type == 'wav':
            painter.drawPixmap(rect, QPixmap(icons['voice']))
        if note_type == 'mp4':
            painter.drawPixmap(rect, QPixmap(icons['video']))
        if note_type == 'png':
            painter.drawPixmap(rect, QPixmap(icons['paint']))
        if note_type == 'json':
            painter.drawPixmap(rect, QPixmap(icons['todo']))
