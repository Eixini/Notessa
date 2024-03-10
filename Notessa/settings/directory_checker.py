from PySide6.QtCore import QDir, QStandardPaths, QDirIterator


class DirectoryChecker():

    def __init__(self):
        self.applicationDataLocation = str(QStandardPaths.writableLocation(QStandardPaths.AppConfigLocation))

    def application_directory_checker(self):
        appDir = QDir()
        if not QDir(self.applicationDataLocation).exists():
            appDir.mkdir(self.applicationDataLocation)
            print(f'Directory create: {self.applicationDataLocation}')

    def notes_directory_checker(self):
        appDir = QDir()
        notesPath = f'{self.applicationDataLocation}{QDir.separator()}Notes'
        if not QDir(notesPath).exists():
            appDir.mkdir(notesPath)

    def text_notes_directory_checker(self):
        appDir = QDir()
        notesPath = f'{self.applicationDataLocation}{QDir.separator()}Notes{QDir.separator()}TextNotes'
        if not QDir(notesPath).exists():
            appDir.mkdir(notesPath)

    def voice_notes_directory_checker(self):
        appDir = QDir()
        notesPath = f'{self.applicationDataLocation}{QDir.separator()}Notes{QDir.separator()}VoiceNotes'
        if not QDir(notesPath).exists():
            appDir.mkdir(notesPath)

    def video_notes_directory_checker(self):
        appDir = QDir()
        notesPath = f'{self.applicationDataLocation}{QDir.separator()}Notes{QDir.separator()}VideoNotes'
        if not QDir(notesPath).exists():
            appDir.mkdir(notesPath)

    def paint_notes_directory_checker(self):
        appDir = QDir()
        notesPath = f'{self.applicationDataLocation}{QDir.separator()}Notes{QDir.separator()}PaintNotes'
        if not QDir(notesPath).exists():
            appDir.mkdir(notesPath)

    def text_notes_directory(self) -> str:
        return f'{self.applicationDataLocation}{QDir.separator()}Notes{QDir.separator()}TextNotes'

    def voice_notes_directory(self) -> str:
        return f'{self.applicationDataLocation}{QDir.separator()}Notes{QDir.separator()}VoiceNotes'

    def video_notes_directory(self) -> str:
        return f'{self.applicationDataLocation}{QDir.separator()}Notes{QDir.separator()}VideoNotes'

    def paint_notes_directory(self) -> str:
        return f'{self.applicationDataLocation}{QDir.separator()}Notes{QDir.separator()}PaintNotes'

    def size_notes_on_disk(self) -> str:
        """The method allows you to calculate the total number
        of notes in the notes directory and the amount of disk space they occupy.
        It also calculates for individual types of notes."""
        dirIter = QDirIterator(f'{self.applicationDataLocation}{QDir.separator()}Notes',
                               flags=QDirIterator.Subdirectories)

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
