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
    QAudioSink, QAudioDevice, QMediaFormat, QMediaRecorder, QMediaCaptureSession, QAudioInput, QCamera, QVideoSink)
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from Notessa.windows.ui_createvideonote import Ui_CreateVideoNoteWindow
from  Notessa.settings.directory_checker import DirectoryChecker
from Notessa import rc_icons


class CreateVideoNote(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CreateVideoNoteWindow()
        self.ui.setupUi(self)

        # Icon set
        self.setWindowIcon(QIcon(':/resources/icons/video.png'))
        self.ui.recordButton.setIcon(QIcon(':/resource/icons/play.png'))
        self.ui.pauseButton.setIcon(QIcon(':/resource/icons/pause.png'))
        self.ui.stopButton.setIcon(QIcon(':/resource/icons/stop.png'))
        self.ui.backButton.setIcon(QIcon(':/resource/icons/back.png'))

        # Media settings
        self._capture_session = QMediaCaptureSession()
        self._camera = QCamera()
        self._capture_session.setCamera(self._camera)
        self._media_recorder = QMediaRecorder()
        self._capture_session.setRecorder(self._media_recorder)
        self._video_sink = QVideoSink()

        self._capture_session.setVideoSink(self._video_sink)

        self._camera.start() # ??????????????

        self._media_format = QMediaFormat(QMediaFormat.FileFormat.MPEG4)
        self._media_format.setVideoCodec(QMediaFormat.VideoCodec.MPEG4)
        self._media_format.setAudioCodec(QMediaFormat.AudioCodec.MP3)
        self._media_recorder.setMediaFormat(self._media_format)

        # Signal - Slot
        self.ui.recordButton.clicked.connect(self.record)
        self.ui.pauseButton.clicked.connect(self.pause)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui.backButton.clicked.connect(self.back)

    def record(self):
        self.ui.pauseButton.setVisible(True)
        print(self._media_recorder.recorderState())
        #
        datetime = QDateTime().currentDateTime()
        datetime = datetime.time().msec()
        #
        dirChecker = DirectoryChecker()
        file = f'{dirChecker.video_notes_directory()}{QDir.separator()}{datetime}'
        url = f'{QDir.toNativeSeparators(file)}'
        self._media_recorder.setOutputLocation(QUrl.fromLocalFile(url))

        self._media_recorder.record()

    def pause(self):
        self._media_recorder.pause()

    def stop(self):
        self._media_recorder.stop()

    def back(self):
        self.reject()
