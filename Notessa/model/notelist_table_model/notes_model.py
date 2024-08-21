from PySide6.QtCore import QAbstractTableModel, Qt, QDir, QFile, QFileInfo, QModelIndex
from Notessa.common_modules.directory_checker import DirectoryChecker
import os
import json
# from Notessa.resource import icons_rc


class NotesModel(QAbstractTableModel):
    def __init__(self, *args):
        super(NotesModel, self).__init__()
        self._data = self.initialData()
        self.corrupted_files = list()

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
            if self._data[position][0] == 'txt':
                note_file_name = f'{dir_checker.text_notes_directory()}{QDir.separator()}{self._data[position][3]}.txt'
                meta_data_file_name = f'{dir_checker.text_notes_directory()}{QDir.separator()}{self._data[position][3]}.json'
                QFile(note_file_name).remove()
                QFile(meta_data_file_name).remove()

            if self._data[position][0] == 'wav':
                note_file_name = f'{dir_checker.voice_notes_directory()}{QDir.separator()}{self._data[position][3]}.wav'
                meta_data_file_name = f'{dir_checker.voice_notes_directory()}{QDir.separator()}{self._data[position][3]}.json'
                QFile(note_file_name).remove()
                QFile(meta_data_file_name).remove()

            if self._data[position][0] == 'mp4':
                note_file_name = f'{dir_checker.video_notes_directory()}{QDir.separator()}{self._data[position][3]}.mp4'
                meta_data_file_name = f'{dir_checker.video_notes_directory()}{QDir.separator()}{self._data[position][3]}.json'
                QFile(note_file_name).remove()
                QFile(meta_data_file_name).remove()

            if self._data[position][0] == 'png':
                note_file_name = f'{dir_checker.paint_notes_directory()}{QDir.separator()}{self._data[position][3]}.png'
                meta_data_file_name = f'{dir_checker.paint_notes_directory()}{QDir.separator()}{self._data[position][3]}.json'
                QFile(note_file_name).remove()
                QFile(meta_data_file_name).remove()

            if self._data[position][0] == 'json':
                note_file_name = f'{dir_checker.todo_notes_directory()}{QDir.separator()}{self._data[position][3]}.json'
                meta_data_file_name = f'{dir_checker.todo_notes_directory()}{QDir.separator()}{self._data[position][3]}.json'
                QFile(note_file_name).remove()
                QFile(meta_data_file_name).remove()

            del (self._data[position])

        self.endRemoveRows()
        self.layoutChanged.emit()
        return True

    def initialData(self):
        """
        In this method, data for the model is initialized.
        Data is taken when reading note directories.
        Data will only be added to the model if the note has a metadata file.
        """

        dir_checker = DirectoryChecker()
        # Getting a list of files
        file_info_list = []

        # TEXT NOTES
        text_notes_folder = dir_checker.text_notes_directory()
        for fileInfo in os.listdir(text_notes_folder):
            if '.txt' in fileInfo:
                model_elements = []
                file_info = QFileInfo(f'{text_notes_folder}{QDir.separator()}{fileInfo}')
                note_meta_data_file = f'{text_notes_folder}{QDir.separator()}{file_info.baseName()}.json'

                if QFile.exists(note_meta_data_file):
                    meta_data = None
                    with open(note_meta_data_file, 'r') as file:
                        try:
                            meta_data = json.load(file)
                        except json.decoder.JSONDecodeError:
                            print(f'Error file: {note_meta_data_file}')
                            self.corrupted_files.append(note_meta_data_file)
                            continue
                    model_elements.append(file_info.suffix())                   # 0
                    model_elements.append(meta_data.get('note_name'))           # 1
                    model_elements.append(meta_data.get('deadline'))            # 2
                    model_elements.append(file_info.baseName())                 # 3
                    model_elements.append(file_info.birthTime().toString())     # 4
                    model_elements.append(meta_data.get('uuid'))                # 5
                else:
                    break

                file_info_list.append(model_elements)

        # VOICE NOTES
        voice_notes_folder = dir_checker.voice_notes_directory()
        for fileInfo in os.listdir(voice_notes_folder):
            if '.wav' in fileInfo:
                model_elements = []
                file_info = QFileInfo(f'{voice_notes_folder}{QDir.separator()}{fileInfo}')
                note_meta_data_file = f'{voice_notes_folder}{QDir.separator()}{file_info.baseName()}.json'

                if QFile.exists(note_meta_data_file):
                    meta_data = None
                    with open(note_meta_data_file, 'r') as file:
                        try:
                            meta_data = json.load(file)
                        except json.decoder.JSONDecodeError:
                            print(f'Error file: {note_meta_data_file}')
                            self.corrupted_files.append(note_meta_data_file)
                            continue
                    model_elements.append(file_info.suffix())                   # 0
                    model_elements.append(meta_data.get('note_name'))           # 1
                    model_elements.append(meta_data.get('deadline'))            # 2
                    model_elements.append(file_info.baseName())                 # 3
                    model_elements.append(file_info.birthTime().toString())     # 4
                    model_elements.append(meta_data.get('uuid'))                # 5
                else:
                    break

                file_info_list.append(model_elements)

        # VIDEO NOTES
        video_notes_folder = dir_checker.video_notes_directory()
        for fileInfo in os.listdir(video_notes_folder):
            if '.mp4' in fileInfo:
                model_elements = []
                file_info = QFileInfo(f'{video_notes_folder}{QDir.separator()}{fileInfo}')
                note_meta_data_file = f'{video_notes_folder}{QDir.separator()}{file_info.baseName()}.json'

                if QFile.exists(note_meta_data_file):
                    meta_data = None
                    with open(note_meta_data_file, 'r') as file:
                        try:
                            meta_data = json.load(file)
                        except json.decoder.JSONDecodeError:
                            print(f'Error file: {note_meta_data_file}')
                            self.corrupted_files.append(note_meta_data_file)
                            continue

                    model_elements.append(file_info.suffix())                   # 0
                    model_elements.append(meta_data.get('note_name'))           # 1
                    model_elements.append(meta_data.get('deadline'))            # 2
                    model_elements.append(file_info.baseName())                 # 3
                    model_elements.append(file_info.birthTime().toString())     # 4
                    model_elements.append(meta_data.get('uuid'))                # 5
                else:
                    break

                file_info_list.append(model_elements)

        # PAINT NOTES
        paint_notes_folder = dir_checker.paint_notes_directory()
        for fileInfo in os.listdir(paint_notes_folder):
            if '.png' in fileInfo:
                model_elements = []
                file_info = QFileInfo(f'{paint_notes_folder}{QDir.separator()}{fileInfo}')
                note_meta_data_file = f'{paint_notes_folder}{QDir.separator()}{file_info.baseName()}.json'

                if QFile.exists(note_meta_data_file):
                    meta_data = None
                    with open(note_meta_data_file, 'r') as file:
                        try:
                            meta_data = json.load(file)
                        except json.decoder.JSONDecodeError:
                            print(f'Error file: {note_meta_data_file}')
                            self.corrupted_files.append(note_meta_data_file)
                            continue

                    model_elements.append(file_info.suffix())                   # 0
                    model_elements.append(meta_data.get('note_name'))           # 1
                    model_elements.append(meta_data.get('deadline'))            # 2
                    model_elements.append(file_info.baseName())                 # 3
                    model_elements.append(file_info.birthTime().toString())     # 4
                    model_elements.append(meta_data.get('uuid'))                # 5
                else:
                    break

                file_info_list.append(model_elements)

        # TOD0 NOTES
        todo_notes_folder = dir_checker.todo_notes_directory()
        for fileInfo in os.listdir(todo_notes_folder):
            if '.json' in fileInfo:
                model_elements = []
                file_info = QFileInfo(f'{todo_notes_folder}{QDir.separator()}{fileInfo}')
                note_meta_data_file = f'{todo_notes_folder}{QDir.separator()}{file_info.baseName()}.json'

                if QFile.exists(note_meta_data_file):
                    json_data = None
                    with open(note_meta_data_file, 'r') as file:
                        try:
                            json_data = json.load(file)
                        except json.decoder.JSONDecodeError:
                            print(f'Error file: {note_meta_data_file}')
                            self.corrupted_files.append(note_meta_data_file)
                            continue

                        meta_data = json_data.get('meta_data')

                        model_elements.append(file_info.suffix())                   # 0
                        model_elements.append(meta_data.get('note_name'))           # 1
                        model_elements.append(meta_data.get('deadline'))            # 2
                        model_elements.append(file_info.baseName())                 # 3
                        model_elements.append(file_info.birthTime().toString())     # 4
                        model_elements.append(meta_data.get('uuid'))                # 5
                else:
                    break

                file_info_list.append(model_elements)

        return file_info_list

    def getNoteType(self, QModelIndex):
        return self._data[QModelIndex.row()][0]

    def getCurrentData(self, QModelIndex) -> list:
        return list(self._data[QModelIndex.row()])

    def get_corrupted_files(self):
        """ Returns a list of corrupted files with metadata """
        return self.corrupted_files
