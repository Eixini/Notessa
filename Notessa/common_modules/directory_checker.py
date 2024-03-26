from PySide6.QtCore import QDir, QStandardPaths, QDirIterator
from PySide6.QtWidgets import QApplication


class DirectoryChecker():

    def __init__(self):
        self.applicationDataLocation = str(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppConfigLocation))
        self.noteLocation = str(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation))
        self._application_name = QApplication.applicationName()
        if self._application_name == 'python':
            self._application_name = 'Notessa'

# Part of the code responsible for checking and working with the directory for storing configurations, style files, etc.
    def application_data_directory_checker(self):
        dataDir = QDir()
        if not QDir(self.applicationDataLocation).exists():
            dataDir.mkdir(self.applicationDataLocation)
            print(f'Directory create: {self.applicationDataLocation}')

    def style_directory_checker(self):
        data_dir = QDir()
        style_path = f'{self.applicationDataLocation}{QDir.separator()}styles'
        if not QDir(style_path).exists():
            data_dir.mkdir(style_path)
            print(f'Directory create: {style_path}')
        return style_path

    def translate_directory_checker(self):
        data_dir = QDir()
        translate_path = f'{self.applicationDataLocation}{QDir.separator()}translations'
        if not QDir(translate_path).exists():
            data_dir.mkdir(translate_path)
            print(f'Directory create: {translate_path}')
        return translate_path

# Part of the code responsible for checking and working with the directory for storing notes
    def notes_location_directory_checker(self):
        noteDir = QDir()
        if self._application_name is None:
            appPath = f'{self.noteLocation}{QDir.separator()}Notessa'
        else:
            appPath = f'{self.noteLocation}{QDir.separator()}{self._application_name}'

        if not QDir(appPath).exists():
            noteDir.mkdir(appPath)
            print(f'Directory create: {appPath}')

    def notes_directory_checker(self):
        noteDir = QDir()
        if self._application_name is None:
            notes_path = f'{self.noteLocation}{QDir.separator()}Notessa{QDir.separator()}Notes'
        else:
            notes_path = f'{self.noteLocation}{QDir.separator()}{self._application_name}{QDir.separator()}Notes'

        if not QDir(notes_path).exists():
            noteDir.mkdir(notes_path)
        return notes_path

    def text_notes_directory_checker(self):
        noteDir = QDir()
        if self._application_name is None:
            text_notes_path = f'{self.noteLocation}{QDir.separator()}Notessa{QDir.separator()}Notes{QDir.separator()}TextNotes'
        else:
            text_notes_path = f'{self.noteLocation}{QDir.separator()}{self._application_name}{QDir.separator()}Notes{QDir.separator()}TextNotes'

        if not QDir(text_notes_path).exists():
            noteDir.mkdir(text_notes_path)
        return text_notes_path

    def voice_notes_directory_checker(self):
        noteDir = QDir()
        if self._application_name is None:
            voice_notes_path = f'{self.noteLocation}{QDir.separator()}Notessa{QDir.separator()}Notes{QDir.separator()}VoiceNotes'
        else:
            voice_notes_path = f'{self.noteLocation}{QDir.separator()}{self._application_name}{QDir.separator()}Notes{QDir.separator()}VoiceNotes'

        if not QDir(voice_notes_path).exists():
            noteDir.mkdir(voice_notes_path)
        return voice_notes_path

    def video_notes_directory_checker(self):
        noteDir = QDir()
        if self._application_name is None:
            video_notes_path = f'{self.noteLocation}{QDir.separator()}Notessa{QDir.separator()}Notes{QDir.separator()}VideoNotes'
        else:
            video_notes_path = f'{self.noteLocation}{QDir.separator()}{self._application_name}{QDir.separator()}Notes{QDir.separator()}VideoNotes'

        if not QDir(video_notes_path).exists():
            noteDir.mkdir(video_notes_path)
        return video_notes_path

    def paint_notes_directory_checker(self):
        noteDir = QDir()
        if self._application_name is None:
            paint_notes_path = f'{self.noteLocation}{QDir.separator()}Notessa{QDir.separator()}Notes{QDir.separator()}PaintNotes'
        else:
            paint_notes_path = f'{self.noteLocation}{QDir.separator()}{self._application_name}{QDir.separator()}Notes{QDir.separator()}PaintNotes'

        if not QDir(paint_notes_path).exists():
            noteDir.mkdir(paint_notes_path)
        return paint_notes_path

    def todo_notes_directory_checker(self):
        noteDir = QDir()
        if self._application_name is None:
            todo_notes_path = f'{self.noteLocation}{QDir.separator()}Notessa{QDir.separator()}Notes{QDir.separator()}TodoNotes'
        else:
            todo_notes_path = f'{self.noteLocation}{QDir.separator()}{self._application_name}{QDir.separator()}Notes{QDir.separator()}TodoNotes'

        if not QDir(todo_notes_path).exists():
            noteDir.mkdir(todo_notes_path)
        return todo_notes_path

    def text_notes_directory(self) -> str:
        return self.text_notes_directory_checker()

    def voice_notes_directory(self) -> str:
        return self.voice_notes_directory_checker()

    def video_notes_directory(self) -> str:
        return self.video_notes_directory_checker()

    def paint_notes_directory(self) -> str:
        return self.paint_notes_directory_checker()

    def todo_notes_directory(self) -> str:
        return self.todo_notes_directory_checker()

    def size_notes_on_disk(self) -> str:
        """The method allows you to calculate the total number
        of notes in the notes directory and the amount of disk space they occupy.
        It also calculates for individual types of notes."""
        if self._application_name is None:
            dirIter = QDirIterator(f'{self.notes_directory_checker()}', flags=QDirIterator.Subdirectories)

        countAndSize = {
            'total': {
                'size': 0,
                'unit': 'Byte',
                'count': 0,
            },
            'text': {
                'size': 0,
                'unit': 'Byte',
                'count': 0,
            },
            'voice': {
                'size': 0,
                'unit': 'Byte',
                'count': 0,
            },
            'video': {
                'size': 0,
                'unit': 'Byte',
                'count': 0,
            },
            'paint': {
                'size': 0,
                'unit': 'Byte',
                'count': 0,
            },
            'todo': {
                'size': 0,
                'unit': 'Byte',
                'count': 0,
            },
        }

        while dirIter.hasNext():
            dirIter.next()
            print(dirIter.fileInfo().dir().dirName())
            if dirIter.fileInfo().dir().dirName() == 'TextNotes':
                print(dirIter.fileInfo().baseName())
                if dirIter.fileInfo().isFile():
                    countAndSize['total']['size'] += dirIter.fileInfo().size()
                    countAndSize['total']['count'] += 1
                    countAndSize['text']['size'] += dirIter.fileInfo().size()
                    countAndSize['text']['count'] += 1
            if dirIter.fileInfo().dir().dirName() == 'VoiceNotes':
                print(dirIter.fileInfo().baseName())
                if dirIter.fileInfo().isFile():
                    countAndSize['total']['size'] += dirIter.fileInfo().size()
                    countAndSize['total']['count'] += 1
                    countAndSize['voice']['size'] += dirIter.fileInfo().size()
                    countAndSize['voice']['count'] += 1
            if dirIter.fileInfo().dir().dirName() == 'VideoNotes':
                print(dirIter.fileInfo().baseName())
                if dirIter.fileInfo().isFile():
                    countAndSize['total']['size'] += dirIter.fileInfo().size()
                    countAndSize['total']['count'] += 1
                    countAndSize['video']['size'] += dirIter.fileInfo().size()
                    countAndSize['video']['count'] += 1
            if dirIter.fileInfo().dir().dirName() == 'PaintNotes':
                print(dirIter.fileInfo().baseName())
                if dirIter.fileInfo().isFile():
                    countAndSize['total']['size'] += dirIter.fileInfo().size()
                    countAndSize['total']['count'] += 1
                    countAndSize['paint']['size'] += dirIter.fileInfo().size()
                    countAndSize['paint']['count'] += 1
            if dirIter.fileInfo().dir().dirName() == 'TodoNotes':
                print(dirIter.fileInfo().baseName())
                if dirIter.fileInfo().isFile():
                    countAndSize['total']['size'] += dirIter.fileInfo().size()
                    countAndSize['total']['count'] += 1
                    countAndSize['todo']['size'] += dirIter.fileInfo().size()
                    countAndSize['todo']['count'] += 1

        for key, value in countAndSize.items():
            countAndSize[key] = self.convertSize(countAndSize[key])

        return countAndSize

    def convertSize(self, val: dict):
        print(val)
        # Byte to KByte
        if val['size'] > 1024 and val['unit'] == 'Byte':
            val['size'] = round(val['size'] / 1024, 2)
            val['unit'] = 'Kb'
        # KByte to MByte
        if val['size'] > 1024 and val['unit'] == 'Kb':
            val['size'] = round(val['size'] / 1024, 2)
            val['unit'] = 'Mb'
        # MByte to GByte
        if val['size'] > 1024 and val['unit'] == 'Mb':
            val['size'] = round(val['size'] / 1024, 2)
            val['unit'] = 'Gb'

        return val
