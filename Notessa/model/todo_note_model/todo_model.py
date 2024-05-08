from PySide6.QtCore import QAbstractListModel, Qt, QDir, QFile, QFileInfo
from Notessa.common_modules.directory_checker import DirectoryChecker
import os


class TodoModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self._todos = todos or []

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            text, _ = self._todos[index.row()]
            return text
        if role == Qt.ItemDataRole.CheckStateRole:
            _, status = self._todos[index.row()]
            return status

    def rowCount(self, index):
        return len(self._todos)
