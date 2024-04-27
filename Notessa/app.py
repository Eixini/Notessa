import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QTranslator, QFile, QSettings
from Notessa.main_window.main_window import MainWindow
from Notessa.shortcut_notes.shortcut_notes_widget import ShortcutNotesWidget
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.resource import styles_rc
from Notessa.resource import translations_rc


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Notessa')

    # Checking application data directories
    directory_checker = DirectoryChecker()
    directory_checker.application_data_directory_checker()
    directory_checker.style_directory_checker()

    # Checking directories with notes
    directory_checker.notes_location_directory_checker()
    directory_checker.notes_directory_checker()
    directory_checker.text_notes_directory_checker()
    directory_checker.voice_notes_directory_checker()
    directory_checker.video_notes_directory_checker()
    directory_checker.paint_notes_directory_checker()
    directory_checker.todo_notes_directory_checker()

    # Setting the translation
    translator = QTranslator(app)
    settings = QSettings('Notessa')
    print(settings.fileName())
    try:
        translator.load(settings.value('LanguagePath'))
        app.installTranslator(translator)
    except Exception as err:
        print(err)

    if not settings.value('StylePath'):
        style_file = QFile(':/styles/kilimanjaro.qss')
    else:
        style_file = QFile(settings.value('StylePath'))
    style_file.open(QFile.OpenModeFlag.ReadOnly)
    convert = style_file.readAll().toStdString()
    app.setStyleSheet(convert)

    main_window = MainWindow()
    main_window.show()

    shortcut_notes_widget = ShortcutNotesWidget()
    shortcut_notes_widget.show()

    app.exec()

if __name__ == '__main__':
    main()
