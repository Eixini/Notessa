from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QTimer,
                            QSize, QTime, QUrl, Qt, QByteArray, QIODevice, QDir, QRegularExpression, Slot)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QRegularExpressionValidator)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget, QMessageBox,)
from PySide6.QtMultimedia import (QAudioFormat, QAudioSource, QMediaDevices, QImageCapture, QVideoFrame,
    QAudioSink, QAudioDevice, QMediaFormat, QMediaRecorder, QMediaCaptureSession, QAudioInput, QCamera, QVideoSink)
from Notessa.windows.ui_createvideonote import Ui_CreateVideoNoteWindow
from Notessa.settings.directory_checker import DirectoryChecker
from Notessa import rc_icons

"""
Mark:
- check device availability before recording;
"""


class CreateVideoNote(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateVideoNoteWindow()
        self.ui.setupUi(self)

        # Icon set
        self.setWindowIcon(QIcon(':/resource/icons/video.png'))
        self.ui.recordButton.setIcon(QIcon(':/resource/icons/play.png'))
        self.ui.pauseButton.setIcon(QIcon(':/resource/icons/pause.png'))
        self.ui.stopButton.setIcon(QIcon(':/resource/icons/stop.png'))
        self.ui.backButton.setIcon(QIcon(':/resource/icons/back.png'))

        self.ui.stateLabel.setPixmap(QPixmap(':/resource/icons/video_off.png').scaledToWidth(50).scaledToHeight(50))

        # Media settings
        self._capture_session = QMediaCaptureSession()
        self._camera = QCamera()
        self._capture_session.setCamera(self._camera)
        self._media_recorder = QMediaRecorder()
        self._audio_input = QAudioInput()
        self._capture_session.setRecorder(self._media_recorder)
        self._capture_session.setAudioInput(self._audio_input)
        self._media_recorder.setQuality(QMediaRecorder.Quality.VeryHighQuality)

        self._video_sink = QVideoSink()
        self._capture_session.setVideoOutput(self._video_sink)

        self._camera.start()

        self._media_format = QMediaFormat(QMediaFormat.FileFormat.MPEG4)
        self._media_format.setVideoCodec(QMediaFormat.VideoCodec.MPEG4)
        self._media_format.setAudioCodec(QMediaFormat.AudioCodec.Wave)
        self._media_recorder.setMediaFormat(self._media_format)

        #
        self.ui.videoNoteName.setValidator(QRegularExpressionValidator('([a-zA-Zа-яА-Я0-9-_]){255}'))

        # Alternative to QMediaRecorder.duration()
        self._duration = 0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.update_duration)

        # Signal - Slot
        self.ui.recordButton.clicked.connect(self.record)
        self.ui.pauseButton.clicked.connect(self.pause)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui.backButton.clicked.connect(self.back)
        self.ui.muteButton.clicked.connect(self.mute)

        self._media_recorder.durationChanged.connect(self.changeLabel)
        self._media_recorder.recorderStateChanged.connect(self.update_record_state)

        self._video_sink.videoFrameChanged.connect(self.video_frame_changed)

    def video_frame_changed(self):
        self.ui.videoLabel.setPixmap(QPixmap(self._video_sink.videoFrame().toImage()))

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

    def mute(self):
        if self._audio_input.isMuted():
            self._audio_input.setMuted(False)
            self.ui.muteButton.setText(u'Mute')
        else:
            self._audio_input.setMuted(True)
            self.ui.muteButton.setText(u'Unmute')

    def record(self):
        if (not self.ui.videoNoteName.text() == '' and
                not self._media_recorder.recorderState() == QMediaRecorder.RecorderState.PausedState):
            dirChecker = DirectoryChecker()
            file = f'{dirChecker.video_notes_directory()}{QDir.separator()}{self.ui.videoNoteName.text()}'
            url = f'{QDir.toNativeSeparators(file)}'
            self._media_recorder.setOutputLocation(QUrl.fromLocalFile(url))

            self._media_recorder.record()
            self.ui.stateLabel.setPixmap(QPixmap(':/resource/icons/recording.png').scaledToWidth(50).scaledToHeight(50))

            self._timer.start(1000)
        elif self._media_recorder.recorderState() == QMediaRecorder.RecorderState.PausedState:
            self._media_recorder.record()
            self._timer.start(1000)
        else:
            msgBox = QMessageBox()
            msgBox.setText('Please, enter note name.')
            msgBox.exec()

    def pause(self):
        self._media_recorder.pause()
        self.ui.stateLabel.setPixmap(QPixmap(':/resource/icons/pause.png').scaledToWidth(50).scaledToHeight(50))
        #
        self._timer.stop()

    def stop(self):
        self._media_recorder.stop()
        self.ui.stateLabel.setPixmap(QPixmap(':/resource/icons/video_off.png').scaledToWidth(50).scaledToHeight(50))
        # Reset duration
        self._timer.stop()
        self._duration = 0

    def back(self):
        self.reject()

    def changeLabel(self):
        timeDuratin = self.sec_convert(self._duration)
        self.ui.durationLabel.setText(f'{timeDuratin["min"]}:{timeDuratin["sec"]}')

    def update_duration(self):
        self._duration += 1
        print(f'Duration: {self._duration}')

    def sec_convert(self, sec):
        result = {'min': 0, 'sec': 0}
        result['sec'] = sec
        if sec >= 60:
            result['min'] = int(sec / 60)
            result['sec'] = sec % 60
        return result
