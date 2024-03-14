import sys
from PySide6.QtWidgets import QApplication, QWidget
from Notessa.main_window.main_window import MainWindow
from Notessa.common_modules.directory_checker import DirectoryChecker


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Notessa')
    app.setApplicationVersion('0.1')

    window = MainWindow()
    window.show()

    # Checking and initializing note directories
    dirChecker = DirectoryChecker()
    dirChecker.application_directory_checker()
    dirChecker.notes_directory_checker()
    dirChecker.text_notes_directory_checker()
    dirChecker.voice_notes_directory_checker()
    dirChecker.video_notes_directory_checker()
    dirChecker.paint_notes_directory_checker()

    app.exec()

if __name__ == '__main__':
    main()
