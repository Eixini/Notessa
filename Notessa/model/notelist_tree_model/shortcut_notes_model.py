from PySide6.QtCore import QAbstractItemModel, Qt, QDir, QFile, QFileInfo, QModelIndex
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.model.notelist_tree_model.shortcut_notes_treeitem import TreeItem
import os

class TreeModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super(TreeModel, self).__init__(parent)
        """ subclassing the standard interface item models must use and 
                implementing index(), parent(), rowCount(), columnCount(), and data()."""

        self._data = self.initial_data()

        rootData = ['Note name']
        self.rootItem = TreeItem(rootData)
        indent = -1
        self.parents = [self.rootItem]
        self.indentations = [0]
        self.createData(self._data, indent)

    def createData(self, data, indent):
        if type(data) == dict:
            indent += 1
            position = 4 * indent
            for dict_keys, dict_values in data.items():
                if position > self.indentations[-1]:
                    if self.parents[-1].child_count() > 0:
                        self.parents.append(self.parents[-1].child(self.parents[-1].child_count() - 1))
                        self.indentations.append(position)
                else:
                    while position < self.indentations[-1] and len(self.parents) > 0:
                        self.parents.pop()
                        self.indentations.pop()
                parent = self.parents[-1]
                parent.insert_children(parent.child_count(), 1, parent.column_count())
                parent.child(parent.child_count() - 1).set_data(0, dict_keys)
                if type(dict_values) != dict:
                    parent.child(parent.child_count() - 1).set_data(0, str(dict_values))
                self.createData(dict_values, indent)

    def index(self, row, column, index=QModelIndex()):
        """ Returns the index of the item in the model specified by the given row, column and parent index """

        if not self.hasIndex(row, column, index):
            return QModelIndex()
        if not index.isValid():
            item = self.rootItem
        else:
            item = index.internalPointer()

        child = item.child(row)
        if child:
            return self.createIndex(row, column, child)
        return QModelIndex()

    def parent(self, index):
        """ Returns the parent of the model item with the given index
                If the item has no parent, an invalid QModelIndex is returned """

        if not index.isValid():
            return QModelIndex()
        item = index.internalPointer()
        if not item:
            return QModelIndex()

        parent = item.parent_item
        if parent == self.rootItem:
            return QModelIndex()
        else:
            return self.createIndex(parent.child_number(), 0, parent)

    def rowCount(self, index=QModelIndex()):
        """ Returns the number of rows under the given parent
                When the parent is valid it means that rowCount is returning the number of children of parent """

        if index.isValid():
            parent = index.internalPointer()
        else:
            parent = self.rootItem
        return parent.child_count()

    def columnCount(self, index=QModelIndex()):
        """ Returns the number of columns for the children of the given parent """

        return self.rootItem.column_count()

    def data(self, index, role=Qt.DisplayRole):
        """ Returns the data stored under the given role for the item referred to by the index """

        if index.isValid() and role == Qt.DisplayRole:
            return index.internalPointer().data(index.column())
        elif not index.isValid():
            return self.rootItem.data(index.column())

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """ Returns the data for the given role and section in the header with the specified orientation """

        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.rootItem.data(section)

    def initial_data(self):

        dir_checker = DirectoryChecker()
        # Getting a list of files
        file_info_list = {}

        # TEXT_NOTES
        text_notes_folder = dir_checker.text_notes_directory()
        for fileInfo in os.listdir(text_notes_folder):
            if '.txt' in fileInfo:
                data_dict = {}
                file_info = QFileInfo(f'{text_notes_folder}{QDir.separator()}{fileInfo}')
                data_dict['Type'] = file_info.suffix()
                data_dict['CreateDate'] = file_info.birthTime().toString()

                file_info_list[file_info.baseName()] = data_dict

        # VOICE_NOTE
        voice_notes_folder = dir_checker.voice_notes_directory()
        for fileInfo in os.listdir(voice_notes_folder):
            if '.wav' in fileInfo:
                data_dict = {}
                file_info = QFileInfo(f'{voice_notes_folder}{QDir.separator()}{fileInfo}')
                data_dict['Type'] = file_info.suffix()
                data_dict['CreateDate'] = file_info.birthTime().toString()

                file_info_list[file_info.baseName()] = data_dict

        # VIDEO_NOTE
        video_notes_folder = dir_checker.video_notes_directory()
        for fileInfo in os.listdir(video_notes_folder):
            if '.mp4' in fileInfo:
                data_dict = {}
                file_info = QFileInfo(f'{video_notes_folder}{QDir.separator()}{fileInfo}')
                data_dict['Type'] = file_info.suffix()
                data_dict['CreateDate'] = file_info.birthTime().toString()

                file_info_list[file_info.baseName()] = data_dict

        # PAINT_NOTE
        paint_notes_folder = dir_checker.paint_notes_directory()
        for fileInfo in os.listdir(paint_notes_folder):
            if '.png' in fileInfo:
                data_dict = {}
                file_info = QFileInfo(f'{paint_notes_folder}{QDir.separator()}{fileInfo}')
                data_dict['Type'] = file_info.suffix()
                data_dict['CreateDate'] = file_info.birthTime().toString()

                file_info_list[file_info.baseName()] = data_dict

        # TODO_NOTE
        todo_notes_folder = dir_checker.todo_notes_directory()
        for fileInfo in os.listdir(todo_notes_folder):
            if '.json' in fileInfo:
                data_dict = {}
                file_info = QFileInfo(f'{todo_notes_folder}{QDir.separator()}{fileInfo}')
                data_dict['Type'] = file_info.suffix()
                data_dict['CreateDate'] = file_info.birthTime().toString()

                file_info_list[file_info.baseName()] = data_dict

        return file_info_list
