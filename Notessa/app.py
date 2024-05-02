import sys
from PySide6.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu
from PySide6.QtCore import QTranslator, QFile, QSettings
from PySide6.QtGui import QAction, QIcon, QPixmap
from Notessa.tray_menu.tray_menu import TrayMenu
from Notessa.resources.icons import common_icons_rc


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Notessa')
    # app.setQuitOnLastWindowClosed(False)
    tray_menu = TrayMenu(app)

    # if QSystemTrayIcon.isSystemTrayAvailable():
    #     print('SysTray available!')
    # else:
    #     print('SysTray NOT available!')

    # testwidget = QWidget()
    #
    # # Actions
    # quit_action = QAction(u'Quit')
    # quit_action.triggered.connect(app.quit)
    #
    # test_widget = QAction(u'Test')
    # test_widget.triggered.connect(testwidget.show)
    #
    # # Tray Menu
    # menu = QMenu()
    # menu.addAction(quit_action)
    # menu.addAction(test_widget)
    #
    # # Tray
    # tray = QSystemTrayIcon()
    # tray.setIcon(QPixmap(':/common/notessa_logo.png'))
    # tray.setVisible(True)
    # tray.setContextMenu(menu)

    app.setQuitOnLastWindowClosed(False)
    app.exec()


if __name__ == '__main__':
    main()
