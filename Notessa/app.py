import sys
from PySide6.QtWidgets import QApplication, QWidget
from main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
