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
from  Notessa.settings.directory_checker import DirectoryChecker
from Notessa import rc_icons


class CreateVoiceNote(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateVoiceNote()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(':/resource/icons/microphone.png'))
        self.ui.voiceNoteName.setReadOnly(False)

        self.ui.voiceNoteName.setValidator(QRegularExpressionValidator('([a-zA-Zа-яА-Я0-9-_]){255}'))

        # Buttons settings
        self.ui.pauseButton.setVisible(False)
        self.ui.stopButton.setEnabled(False)
        self.ui.recordButton.setEnabled(True)
        self.ui.recordButton.setIcon(QIcon(':/resource/icons/play.png'))
        self.ui.pauseButton.setIcon(QIcon(':/resource/icons/pause.png'))
        self.ui.stopButton.setIcon(QIcon(':/resource/icons/stop.png'))
        self.ui.backButtun.setIcon(QIcon(':/resource/icons/back.png'))

        # Timer
        # self.timer = QTimer()
        # self.timer.setInterval(100)  # msecs 100 = 1/10th sec
        # self.timer.timeout.connect(self.ui.durationLabel.setText())
        # self.timer.start()

        # For data input
        self.data = QByteArray()

        # Inputs devices
        self.input_devices = QMediaDevices.audioInputs()
        self.audioInput = QAudioInput(self.input_devices[0])

        # Audio settings
        self.session = QMediaCaptureSession()
        self.session.setAudioInput(self.audioInput)
        self.recorder = QMediaRecorder()
        self.recorder.setQuality(QMediaRecorder.VeryHighQuality)
        self._media_format = QMediaFormat()
        self._media_format.setFileFormat(QMediaFormat.FileFormat.Wave)
        self._media_format.setAudioCodec(QMediaFormat.AudioCodec.Wave)
        self.recorder.setMediaFormat(self._media_format)
        self.session.setRecorder(self.recorder)

        # ???????
        self.recorder.durationChanged.connect(self.changeLabel)

        # Signal - Slot
        self.ui.recordButton.clicked.connect(self.record_voice_note)
        self.ui.stopButton.clicked.connect(self.stop_voice_note)
        self.ui.backButtun.clicked.connect(self.back)
        self.ui.pauseButton.clicked.connect(self.pause_voice_note)

    def back(self):
        if self.recorder.recorderState() == 'RecorderState.RecordingState':
            self.recorder.stop()
        self.accept()

    def record_voice_note(self):
        if (not self.ui.voiceNoteName.text() == '' and
                not self.recorder.recorderState() == 'RecorderState.PausedState'):

            self.ui.stopButton.setEnabled(True)
            # self.ui.recordButton.setEnabled(False)

            # Avoid name change
            self.ui.voiceNoteName.setReadOnly(True)

            self.ui.pauseButton.setVisible(True)
            print(self.recorder.recorderState())
            dirChecker = DirectoryChecker()
            file = f'{dirChecker.voice_notes_directory()}{QDir.separator()}{self.ui.voiceNoteName.text()}'
            url = f'{QDir.toNativeSeparators(file)}'
            self.recorder.setOutputLocation(QUrl.fromLocalFile(url))

            self.recorder.record()
        elif self.recorder.recorderState() == 'RecorderState.PausedState':
            self.recorder.record()
        else:
            msgBox = QMessageBox()
            msgBox.setText('Please, enter note name.')
            msgBox.exec()

    def pause_voice_note(self):
        self.recorder.pause()

    def stop_voice_note(self):
        self.ui.stopButton.setEnabled(False)
        self.ui.recordButton.setEnabled(True)
        self.ui.pauseButton.setVisible(False)
        self.ui.voiceNoteName.setReadOnly(False)

        self.recorder.stop()

    def closeEvent(self, *args):
        if self.recorder is not None:
            self.recorder.stop()
        self.accept()

    def changeLabel(self):
        timeDuratin = self.msec_convert(self.recorder.duration())
        if(len(timeDuratin) == 3):
            self.ui.durationLabel.setText(f'{timeDuratin['min']}:{timeDuratin['sec']}.{timeDuratin['msec']}')

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
