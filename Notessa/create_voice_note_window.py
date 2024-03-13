from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QTimer,
    QSize, QTime, QUrl, Qt, QByteArray, QIODevice, QDir, QRegularExpression)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QRegularExpressionValidator)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget, QMessageBox,)
from PySide6.QtMultimedia import (QAudioFormat, QAudioSource, QMediaDevices,
    QAudioSink, QAudioDevice, QMediaFormat, QMediaRecorder, QMediaCaptureSession, QAudioInput)
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from Notessa.windows.ui_createvoicenote import Ui_CreateVoiceNote
from Notessa.settings.directory_checker import DirectoryChecker
from Notessa import rc_icons

"""
Mark:
- check device availability before recording;
"""

class CreateVoiceNote(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateVoiceNote()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(':/resource/icons/microphone.png'))
        self.ui.voiceNoteName.setReadOnly(False)

        self.ui.voiceNoteName.setValidator(QRegularExpressionValidator('([a-zA-Zа-яА-Я0-9-_]){255}'))

        # Buttons settings
        self.ui.recordButton.setIcon(QIcon(':/resource/icons/play.png'))
        self.ui.pauseButton.setIcon(QIcon(':/resource/icons/pause.png'))
        self.ui.stopButton.setIcon(QIcon(':/resource/icons/stop.png'))
        self.ui.backButtun.setIcon(QIcon(':/resource/icons/back.png'))

        # Inputs devices
        self.input_devices = QMediaDevices.audioInputs()
        self.audioInput = QAudioInput(self.input_devices[0])

        # Audio settings
        self.session = QMediaCaptureSession()
        self.session.setAudioInput(self.audioInput)
        self._media_recorder = QMediaRecorder()
        self._media_recorder.setQuality(QMediaRecorder.Quality.VeryHighQuality)
        self._media_format = QMediaFormat()
        self._media_format.setFileFormat(QMediaFormat.FileFormat.Wave)
        self._media_format.setAudioCodec(QMediaFormat.AudioCodec.Wave)
        self._media_recorder.setMediaFormat(self._media_format)
        self.session.setRecorder(self._media_recorder)

        # Signal - Slot
        self.ui.recordButton.clicked.connect(self.record_voice_note)
        self.ui.stopButton.clicked.connect(self.stop_voice_note)
        self.ui.backButtun.clicked.connect(self.back)
        self.ui.pauseButton.clicked.connect(self.pause_voice_note)

        self._media_recorder.durationChanged.connect(self.changeLabel)
        self._media_recorder.recorderStateChanged.connect(self.update_record_state)

    def update_record_state(self, state):
        print(f'Record state: {self._media_recorder.recorderState()}')
        if self._media_recorder.recorderState() == QMediaRecorder.RecorderState.RecordingState:
            self.ui.recordButton.setEnabled(False)
            self.ui.pauseButton.setEnabled(True)
            self.ui.stopButton.setEnabled(True)
        elif self._media_recorder.recorderState() == QMediaRecorder.RecorderState.PausedState:
            self.ui.recordButton.setEnabled(True)
            self.ui.pauseButton.setEnabled(False)
            self.ui.stopButton.setEnabled(True)
        elif self._media_recorder.recorderState() == QMediaRecorder.RecorderState.StoppedState:
            self.ui.recordButton.setEnabled(True)
            self.ui.pauseButton.setEnabled(False)
            self.ui.stopButton.setEnabled(False)


    def back(self):
        if self._media_recorder.recorderState() == 'RecorderState.RecordingState':
            self._media_recorder.stop()
        self.accept()

    def record_voice_note(self):
        if (not self.ui.voiceNoteName.text() == '' and
                not self._media_recorder.recorderState() == QMediaRecorder.RecorderState.PausedState):
            # Avoid name change
            self.ui.voiceNoteName.setReadOnly(True)

            dirChecker = DirectoryChecker()
            file = f'{dirChecker.voice_notes_directory()}{QDir.separator()}{self.ui.voiceNoteName.text()}'
            url = f'{QDir.toNativeSeparators(file)}'
            self._media_recorder.setOutputLocation(QUrl.fromLocalFile(url))

            self._media_recorder.record()
        elif self._media_recorder.recorderState() == QMediaRecorder.RecorderState.PausedState:
            self._media_recorder.record()
        else:
            msgBox = QMessageBox()
            msgBox.setText('Please, enter note name.')
            msgBox.exec()

    def pause_voice_note(self):
        self._media_recorder.pause()

    def stop_voice_note(self):
        self.ui.stopButton.setEnabled(False)
        self.ui.recordButton.setEnabled(True)
        self.ui.pauseButton.setVisible(False)
        self.ui.voiceNoteName.setReadOnly(False)

        self._media_recorder.stop()

    def closeEvent(self, *args):
        if self._media_recorder is not None:
            self._media_recorder.stop()
        self.accept()

    def changeLabel(self):
        timeDuratin = self.msec_convert(self._media_recorder.duration())
        if(len(timeDuratin) == 3):
            self.ui.durationLabel.setText(f'{timeDuratin["min"]}:{timeDuratin["sec"]}.{timeDuratin["msec"]}')

    def msec_convert(self, ms):
        result = {'min': 0, 'sec': 0, 'msec': 0}
        sec = int(ms/1000)
        msec = ms % 1000
        result['sec'] = sec
        result['msec'] = msec
        if sec >= 60:
            result['min'] = int(sec / 60)
            result['sec'] = sec % 60
        return result
