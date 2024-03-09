from PySide6.QtCore import QDir, QStandardPaths


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
