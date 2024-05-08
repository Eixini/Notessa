from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem
from PySide6.QtCore import QPoint, QRect, Qt
from PySide6.QtGui import QPixmap
from Notessa.resources.icons.note_type import note_type_icons_rc


class NoteItemDelegate(QStyledItemDelegate):

    def paint(self, painter, option, index):
        super(NoteItemDelegate, self).initStyleOption(option, index)
        option.Position = QStyleOptionViewItem.Position.Left

        note_type = index.data()

        icons = {
            'text': ':/note_type/text.png',
            'voice': ':/note_type/voice.png',
            'video': ':/note_type/video.png',
            'paint': ':/note_type/paint.png',
            'todo': ':/note_type/todo.png',
        }
        icon_example = QPixmap(':/note_type/text.png')
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
