import sys
import ctypes
import os

from PySide6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu
from PySide6.QtCore import QTranslator, QFile, QSettings
from PySide6.QtGui import QAction, QIcon, QPixmap

from Notessa.tray_menu.tray_menu import TrayMenu
from Notessa.resources.translations import translations_rc


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Notessa')
    app.setOrganizationName('Eixini Software')
    app.setApplicationVersion('3.0')

    app_id = f'{app.organizationName()}.{app.applicationName()}.{app.applicationVersion()}'

    # For Windows
    if os.name == 'nt':
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)

    tray_menu = TrayMenu()

    # Setting the translation
    translator = QTranslator(app)
    settings = QSettings(app)
    print(settings.fileName())
    try:
        print(settings.value('LanguagePath'))
        translator.load(settings.value('LanguagePath'))
        app.installTranslator(translator)
    except Exception as err:
        print(err)

    # Don't close the application when the last window is closed
    app.setQuitOnLastWindowClosed(False)
    app.exec()


if __name__ == '__main__':
    main()
