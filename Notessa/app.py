import sys
from PySide6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu
from PySide6.QtCore import QTranslator, QFile, QSettings
from PySide6.QtGui import QAction, QIcon, QPixmap
from Notessa.tray_menu.tray_menu import TrayMenu


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Notessa')
    app.setOrganizationName('Eixini Software')

    tray_menu = TrayMenu()

    app.setQuitOnLastWindowClosed(False)
    app.exec()


if __name__ == '__main__':
    main()
