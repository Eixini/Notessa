from PySide6.QtCore import QAbstractTableModel, Qt, QDir, QFile, QFileInfo, QModelIndex
from Notessa.common_modules.directory_checker import DirectoryChecker
import os
# from Notessa.resource import icons_rc


class NotesModel(QAbstractTableModel):
    def __init__(self, *args):
        super(NotesModel, self).__init__()
        self._data = self.initialData()

    def columnCount(self, *args, **kwargs) -> int:
        return 3

    def rowCount(self, *args, **kwargs) -> int:
        return len(self._data)

    def data(self, index, role):
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:
                return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation: Qt.Orientation, role: Qt.ItemDataRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return {
                    0: 'Type',
                    1: 'Name',
                    2: 'Data changed'
                }.get(section)

    def removeRows(self, position: QModelIndex, rows: int, QModelIndex: QModelIndex):
        dir_checker = DirectoryChecker()
        self.layoutAboutToBeChanged.emit()
        self.beginRemoveRows(QModelIndex, position, position+rows-1)
        for i in range(rows):
            if self._data[position][0] == 'txt':
                file_name = f'{dir_checker.text_notes_directory()}{QDir.separator()}{self._data[position][1]}.txt'
                QFile(file_name).remove()
                print(f'File deleted: {file_name}')
            if self._data[position][0] == 'wav':
                file_name = f'{dir_checker.voice_notes_directory()}{QDir.separator()}{self._data[position][1]}.wav'
                QFile(file_name).remove()
                print(f'File deleted: {file_name}')
            if self._data[position][0] == 'mp4':
                file_name = f'{dir_checker.video_notes_directory()}{QDir.separator()}{self._data[position][1]}.mp4'
                QFile(file_name).remove()
                print(f'File deleted: {file_name}')
            if self._data[position][0] == 'png':
                file_name = f'{dir_checker.paint_notes_directory()}{QDir.separator()}{self._data[position][1]}.png'
                QFile(file_name).remove()
                print(f'File deleted: {file_name}')
            if self._data[position][0] == 'json':
                file_name = f'{dir_checker.todo_notes_directory()}{QDir.separator()}{self._data[position][1]}.json'
                QFile(file_name).remove()
                print(f'File deleted: {file_name}')
            del (self._data[position])

        self.endRemoveRows()
        self.layoutChanged.emit()
        return True

    def initialData(self):

        dir_checker = DirectoryChecker()
        # Getting a list of files
        file_info_list = []

        # TEXT NOTES
        text_notes_folder = dir_checker.text_notes_directory()
        for fileInfo in os.listdir(text_notes_folder):
            if '.txt' in fileInfo:
                dict = []
                fInfo = QFileInfo(f'{text_notes_folder}{QDir.separator()}{fileInfo}')
                dict.append(fInfo.suffix())
                dict.append(fInfo.baseName())
                dict.append(fInfo.birthTime().toString())

                file_info_list.append(dict)

        voice_notes_folder = dir_checker.voice_notes_directory()
        for fileInfo in os.listdir(voice_notes_folder):
            if '.wav' in fileInfo:
                dict = []
                fInfo = QFileInfo(f'{voice_notes_folder}{QDir.separator()}{fileInfo}')
                dict.append(fInfo.suffix())
                dict.append(fInfo.baseName())
                dict.append(fInfo.birthTime().toString())

                file_info_list.append(dict)

        video_notes_folder = dir_checker.video_notes_directory()
        for fileInfo in os.listdir(video_notes_folder):
            if '.mp4' in fileInfo:
                dict = []
                fInfo = QFileInfo(f'{video_notes_folder}{QDir.separator()}{fileInfo}')
                dict.append(fInfo.suffix())
                dict.append(fInfo.baseName())
                dict.append(fInfo.birthTime().toString())

                file_info_list.append(dict)

        paint_notes_folder = dir_checker.paint_notes_directory()
        for fileInfo in os.listdir(paint_notes_folder):
            if '.png' in fileInfo:
                dict = []
                fInfo = QFileInfo(f'{paint_notes_folder}{QDir.separator()}{fileInfo}')
                dict.append(fInfo.suffix())
                dict.append(fInfo.baseName())
                dict.append(fInfo.birthTime().toString())

                file_info_list.append(dict)

        todo_notes_folder = dir_checker.todo_notes_directory()
        for fileInfo in os.listdir(todo_notes_folder):
            if '.json' in fileInfo:
                dict = []
                fInfo = QFileInfo(f'{todo_notes_folder}{QDir.separator()}{fileInfo}')
                dict.append(fInfo.suffix())
                dict.append(fInfo.baseName())
                dict.append(fInfo.birthTime().toString())

                file_info_list.append(dict)

        return file_info_list

    def getNoteType(self, QModelIndex):
        return self._data[QModelIndex.row()][0]

    def getCurrentData(self, QModelIndex) -> list:
        return list(self._data[QModelIndex.row()])
