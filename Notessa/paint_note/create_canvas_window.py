from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QSize
from Notessa.paint_note.ui_createcanvaswindow import Ui_CreateCanvasWindow

class CreateCanvasWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateCanvasWindow()
        self.ui.setupUi(self)

        """ 
            The recommended minimum window width is 250 px, since there are buttons in the panel.
        """
        self.ui.widthSize.setMinimum(250)
        self.ui.heightSize.setMinimum(250)

        # Signal - Slot
        self.ui.okButton.clicked.connect(self.ok)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def exec(self):
        self.ui.heightSize.value()
        return super().exec(), QSize(self.ui.widthSize.value(), self.ui.heightSize.value())

    def ok(self):
        self.accept()

    def cancel(self):
        self.reject()