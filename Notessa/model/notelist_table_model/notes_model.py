from PySide6.QtCore import QAbstractTableModel, Qt, QDir, QFile, QFileInfo, QModelIndex
from Notessa.common_modules.directory_checker import DirectoryChecker
import os
import json
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
                    2: 'Deadline'
                }.get(section)

    def removeRows(self, position: QModelIndex, rows: int, QModelIndex: QModelIndex):
        dir_checker = DirectoryChecker()
        self.layoutAboutToBeChanged.emit()
        self.beginRemoveRows(QModelIndex, position, position+rows-1)
        for i in range(rows):
            if self._data[position][0] == 'rtf':
                note_file_name = f'{dir_checker.text_notes_directory()}{QDir.separator()}{self._data[position][3]}.txt'
                meta_data_file_name = f'{dir_checker.text_notes_directory()}{QDir.separator()}{self._data[position][3]}.json'
                QFile(note_file_name).remove()
                QFile(meta_data_file_name).remove()

            if self._data[position][0] == 'wav':
                note_file_name = f'{dir_checker.voice_notes_directory()}{QDir.separator()}{self._data[position][1]}.wav'
                meta_data_file_name = f'{dir_checker.voice_notes_directory()}{QDir.separator()}{self._data[position][1]}.json'
                QFile(note_file_name).remove()
                QFile(meta_data_file_name).remove()

            if self._data[position][0] == 'mp4':
                note_file_name = f'{dir_checker.video_notes_directory()}{QDir.separator()}{self._data[position][1]}.mp4'
                meta_data_file_name = f'{dir_checker.video_notes_directory()}{QDir.separator()}{self._data[position][1]}.json'
                QFile(note_file_name).remove()
                QFile(meta_data_file_name).remove()

            if self._data[position][0] == 'png':
                note_file_name = f'{dir_checker.paint_notes_directory()}{QDir.separator()}{self._data[position][1]}.png'
                meta_data_file_name = f'{dir_checker.paint_notes_directory()}{QDir.separator()}{self._data[position][1]}.json'
                QFile(note_file_name).remove()
                QFile(meta_data_file_name).remove()

            if self._data[position][0] == 'json':
                note_file_name = f'{dir_checker.todo_notes_directory()}{QDir.separator()}{self._data[position][1]}.json'
                meta_data_file_name = f'{dir_checker.todo_notes_directory()}{QDir.separator()}{self._data[position][1]}.json'
                QFile(note_file_name).remove()
                QFile(meta_data_file_name).remove()

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
                file_info = QFileInfo(f'{text_notes_folder}{QDir.separator()}{fileInfo}')
                dict.append(file_info.suffix())                 # 0
                # Reading metadata
                note_meta_data_file = f'{text_notes_folder}{QDir.separator()}{file_info.baseName()}.json'
                meta_data = None
                if QFile.exists(note_meta_data_file):
                    with open(note_meta_data_file, 'r') as file:
                        meta_data = json.load(file)
                    dict.append(meta_data.get('note_name'))     # 1
                    dict.append(meta_data.get('deadline'))      # 2
                else:
                    dict.append('No name TextNote')
                    dict.append(' ')
                dict.append(file_info.baseName())               # 3
                dict.append(file_info.birthTime().toString())   # 4

                file_info_list.append(dict)

        voice_notes_folder = dir_checker.voice_notes_directory()
        for fileInfo in os.listdir(voice_notes_folder):
            if '.wav' in fileInfo:
                dict = []
                file_info = QFileInfo(f'{voice_notes_folder}{QDir.separator()}{fileInfo}')
                dict.append(file_info.suffix())             # 0
                # Reading metadata
                note_meta_data_file = f'{voice_notes_folder}{QDir.separator()}{file_info.baseName()}.json'
                meta_data = None
                if QFile.exists(note_meta_data_file):
                    with open(note_meta_data_file, 'r') as file:
                        meta_data = json.load(file)
                    dict.append(meta_data.get('note_name'))  # 1
                    dict.append(meta_data.get('deadline'))   # 2
                else:
                    dict.append('No name TextNote')
                    dict.append(' ')
                dict.append(file_info.baseName())               # 3
                dict.append(file_info.birthTime().toString())   # 4

                file_info_list.append(dict)

        video_notes_folder = dir_checker.video_notes_directory()
        for fileInfo in os.listdir(video_notes_folder):
            if '.mp4' in fileInfo:
                dict = []
                file_info = QFileInfo(f'{video_notes_folder}{QDir.separator()}{fileInfo}')
                dict.append(file_info.suffix())             # 0
                # Reading metadata
                note_meta_data_file = f'{video_notes_folder}{QDir.separator()}{file_info.baseName()}.json'
                meta_data = None
                if QFile.exists(note_meta_data_file):
                    with open(note_meta_data_file, 'r') as file:
                        meta_data = json.load(file)
                    dict.append(meta_data.get('note_name'))  # 1
                    dict.append(meta_data.get('deadline'))   # 2
                else:
                    dict.append('No name TextNote')
                    dict.append(' ')
                dict.append(file_info.baseName())               # 3
                dict.append(file_info.birthTime().toString())   # 4

                file_info_list.append(dict)

        paint_notes_folder = dir_checker.paint_notes_directory()
        for fileInfo in os.listdir(paint_notes_folder):
            if '.png' in fileInfo:
                dict = []
                file_info = QFileInfo(f'{paint_notes_folder}{QDir.separator()}{fileInfo}')
                dict.append(file_info.suffix())     # 0
                # Reading metadata
                note_meta_data_file = f'{paint_notes_folder}{QDir.separator()}{file_info.baseName()}.json'
                meta_data = None
                if QFile.exists(note_meta_data_file):
                    with open(note_meta_data_file, 'r') as file:
                        meta_data = json.load(file)
                    dict.append(meta_data.get('note_name'))  # 1
                    dict.append(meta_data.get('deadline'))   # 2
                else:
                    dict.append('No name TextNote')
                    dict.append(' ')
                dict.append(file_info.baseName())               # 3
                dict.append(file_info.birthTime().toString())   # 4

                file_info_list.append(dict)

        todo_notes_folder = dir_checker.todo_notes_directory()
        for fileInfo in os.listdir(todo_notes_folder):
            if '.json' in fileInfo:
                dict = []
                file_info = QFileInfo(f'{todo_notes_folder}{QDir.separator()}{fileInfo}')
                dict.append(file_info.suffix())         # 0
                # Reading metadata
                note_meta_data_file = f'{todo_notes_folder}{QDir.separator()}{file_info.baseName()}.json'
                json_data = None
                if QFile.exists(note_meta_data_file):
                    with open(note_meta_data_file, 'r') as file:
                        json_data = json.load(file)

                    meta_data = json_data.get('meta_data')

                    dict.append(meta_data.get('note_name'))  # 1
                    dict.append(meta_data.get('deadline'))   # 2
                else:
                    dict.append('No name TextNote')
                    dict.append(' ')
                dict.append(file_info.baseName())               # 3
                dict.append(file_info.birthTime().toString())   # 4

                file_info_list.append(dict)

        return file_info_list

    def getNoteType(self, QModelIndex):
        return self._data[QModelIndex.row()][0]

    def getCurrentData(self, QModelIndex) -> list:
        return list(self._data[QModelIndex.row()])
