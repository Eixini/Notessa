from PySide6.QtWidgets import QDialog
from Notessa.paint_note.ui_savemessagebox import Ui_SaveMessageBox


class SaveMessageBox(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SaveMessageBox()
        self.ui.setupUi(self)

        self.ui.saveButton.clicked.connect(self.save)
        self.ui.cancelButton.clicked.connect(self.cancel)

    def get(self) -> str:
        return self.ui.note_name_lineedit.text()

    def exec(self):
        return super().exec(), self.ui.note_name_lineedit.text()

    def save(self):
        self.accept()

    def cancel(self):
        self.reject()
