from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QTranslator, QSettings, QFile
from Notessa.settings.ui_gen.ui_settings_widget import Ui_SettingsWidget
from Notessa.resource import styles_rc
from Notessa.resource import translations_rc
from Notessa.resource import icon_flags_rc

class SettingsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_SettingsWidget()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self.app = QApplication.instance()

        self.settings = QSettings('Notessa')
        self.translator = QTranslator(self.app)

        try:
            self.ui.language_combo_box.setPlaceholderText(self.settings.value('Language'))
            self.ui.style_combo_box.setPlaceholderText(self.settings.value('StyleName'))
        except Exception as err:
            print(err)

        # Translate
        self.ui.language_combo_box.addItem(QIcon(':/icon_flags/american.png'), 'English', ':/translations/en.qm')
        self.ui.language_combo_box.addItem(QIcon(':/icon_flags/russian.png'), 'Русский', ':/translations/ru.qm')

        # Style
        self.ui.style_combo_box.addItem('Kilimanjaro', ':/styles/kilimanjaro.qss')
        self.ui.style_combo_box.addItem('MorningStar', ':/styles/morningstar.qss')

        self.ui.language_combo_box.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.ui.language_combo_box.view().window().setAttribute(Qt.WA_TranslucentBackground)
        self.ui.style_combo_box.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        self.ui.style_combo_box.view().window().setAttribute(Qt.WA_TranslucentBackground)

        # Signal - Slot
        self.ui.language_combo_box.currentIndexChanged.connect(self.change_translation)
        self.ui.style_combo_box.currentIndexChanged.connect(self.change_style)
        self.ui.close_button.clicked.connect(self.close_settings)

    def change_translation(self):
        data = self.ui.language_combo_box.currentData()
        self.app.removeTranslator(self.translator)
        self.translator.load(data)
        self.app.installTranslator(self.translator)
        self.settings.remove('LanguagePath')
        self.settings.remove('Language')
        self.settings.setValue('Language', self.ui.language_combo_box.currentText())
        self.settings.setValue('LanguagePath', self.ui.language_combo_box.currentData())

    def change_style(self):
        data = self.ui.style_combo_box.currentData()
        style_file = QFile(data)
        style_file.open(QFile.OpenModeFlag.ReadOnly)
        convert = style_file.readAll().toStdString()
        self.app.setStyleSheet(convert)
        self.settings.remove('StylePath')
        self.settings.remove('StyleName')
        self.settings.setValue('StyleName', self.ui.style_combo_box.currentText())
        self.settings.setValue('StylePath', self.ui.style_combo_box.currentData())

    def close_settings(self):
        self.close()
