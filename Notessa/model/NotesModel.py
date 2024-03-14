from PySide6.QtCore import QAbstractTableModel, Qt, QDir, QFile, QFileInfo
from Notessa.common_modules.directory_checker import DirectoryChecker
import os
from Notessa.resource import rc_icons


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


    def removeRows(self, position, rows, QModelIndex):
        dirChecker = DirectoryChecker()
        self.layoutAboutToBeChanged.emit()
        self.beginRemoveRows(QModelIndex, position, position+rows-1)
        for i in range(rows):
            if self._data[position][0] == 'txt':
                fileName = f'{dirChecker.text_notes_directory()}{QDir.separator()}{self._data[position][1]}.txt'
                QFile(fileName).remove()
                print(f'File deleted: {fileName}')
            if self._data[position][0] == 'wav':
                fileName = f'{dirChecker.voice_notes_directory()}{QDir.separator()}{self._data[position][1]}.wav'
                QFile(fileName).remove()
                print(f'File deleted: {fileName}')
            if self._data[position][0] == 'mp4':
                fileName = f'{dirChecker.video_notes_directory()}{QDir.separator()}{self._data[position][1]}.mp4'
                QFile(fileName).remove()
                print(f'File deleted: {fileName}')
            if self._data[position][0] == 'png':
                fileName = f'{dirChecker.paint_notes_directory()}{QDir.separator()}{self._data[position][1]}.png'
                QFile(fileName).remove()
                print(f'File deleted: {fileName}')
            del (self._data[position])

        self.endRemoveRows()
        self.layoutChanged.emit()
        return True

    def initialData(self):

        dirChecker = DirectoryChecker()
        # Getting a list of files
        fileInfoList = []

        # TEXT NOTES
        textNotesFolder = dirChecker.text_notes_directory()
        for fileInfo in os.listdir(textNotesFolder):
            if '.txt' in fileInfo:
                dict = []
                fInfo = QFileInfo(f'{textNotesFolder}{QDir.separator()}{fileInfo}')
                dict.append(fInfo.suffix())
                dict.append(fInfo.baseName())
                dict.append(fInfo.birthTime().toString())

                fileInfoList.append(dict)

        voiceNotesFolder = dirChecker.voice_notes_directory()
        for fileInfo in os.listdir(voiceNotesFolder):
            if '.wav' in fileInfo:
                dict = []
                fInfo = QFileInfo(f'{voiceNotesFolder}{QDir.separator()}{fileInfo}')
                dict.append(fInfo.suffix())
                dict.append(fInfo.baseName())
                dict.append(fInfo.birthTime().toString())

                fileInfoList.append(dict)

        videoNotesFolder = dirChecker.video_notes_directory()
        for fileInfo in os.listdir(videoNotesFolder):
            if '.mp4' in fileInfo:
                dict = []
                fInfo = QFileInfo(f'{videoNotesFolder}{QDir.separator()}{fileInfo}')
                dict.append(fInfo.suffix())
                dict.append(fInfo.baseName())
                dict.append(fInfo.birthTime().toString())

                fileInfoList.append(dict)

        paintNotesFolder = dirChecker.paint_notes_directory()
        for fileInfo in os.listdir(paintNotesFolder):
            if '.png' in fileInfo:
                dict = []
                fInfo = QFileInfo(f'{paintNotesFolder}{QDir.separator()}{fileInfo}')
                dict.append(fInfo.suffix())
                dict.append(fInfo.baseName())
                dict.append(fInfo.birthTime().toString())

                fileInfoList.append(dict)

        return fileInfoList

    def getNoteType(self, QModelIndex):
        return self._data[QModelIndex.row()][0]

    def getCurrentData(self, QModelIndex) -> list:
        return list(self._data[QModelIndex.row()])
