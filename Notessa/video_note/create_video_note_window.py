from PySide6.QtCore import QTimer, QDir, QUrl
from PySide6.QtGui import QIcon, QPixmap, QRegularExpressionValidator
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtMultimedia import QMediaFormat, QMediaRecorder, QMediaCaptureSession, QAudioInput, QCamera, QMediaDevices
from Notessa.video_note.ui_createvideonote import Ui_CreateVideoNoteWindow
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.resource import rc_icons

"""
Mark:
- check device availability before recording;
"""


class CreateVideoNote(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_CreateVideoNoteWindow()
        self.ui.setupUi(self)

        # Media devices input
        self._microphones = None
        self._cameras = None

        # Media settings
        self._capture_session = QMediaCaptureSession(self)
        self._camera = QCamera(self)
        self._media_recorder = QMediaRecorder(self)
        self._audio_input = QAudioInput(self)
        self._media_format = QMediaFormat()

        # Initializing media devices
        self.media_devices_initialization()

        # Icon set
        self.setWindowIcon(QIcon(':/resource/icons/video.png'))
        self.ui.recordButton.setIcon(QIcon(':/resource/icons/play.png'))
        self.ui.stopButton.setIcon(QIcon(':/resource/icons/stop.png'))
        self.ui.backButton.setIcon(QIcon(':/resource/icons/back.png'))
        self.ui.stateLabel.setPixmap(QPixmap(':/resource/icons/video_off.png').scaledToWidth(50).scaledToHeight(50))

        # Setting the note title entry format
        self.ui.videoNoteName.setValidator(QRegularExpressionValidator('([a-zA-Zа-яА-Я0-9-_]){255}'))

        # Alternative to QMediaRecorder.duration()
        self._duration = 0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.update_duration)

        # Signal - Slot
        self.ui.recordButton.clicked.connect(self.record)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui.backButton.clicked.connect(self.back)
        self.ui.muteButton.clicked.connect(self.mute)
        self._media_recorder.durationChanged.connect(self.changeLabel)
        self._media_recorder.recorderStateChanged.connect(self.update_record_state)
        self.ui.microphoneList.currentIndexChanged.connect(self.microphone_selection_changed)

    def media_devices_initialization(self):
        """ Method for initializing media devices such as microphone and camera """
        # Initializing the microphone
        self._microphones = QMediaDevices.audioInputs()
        if len(self._microphones) > 0:
            for mic in self._microphones:
                self.ui.microphoneList.addItem(mic.description())
            self._audio_input = QAudioInput(self._microphones[0])

        # Initializing the camera
        self._cameras = QMediaDevices.videoInputs()
        if len(self._cameras) > 0:
            for camera in self._cameras:
                self.ui.cameraList.addItem(camera.description())
            self._camera = QCamera(self._cameras[0])

        if self._camera.isAvailable():
            self._media_format.setFileFormat(QMediaFormat.FileFormat.AVI)
            self._media_format.setVideoCodec(QMediaFormat.VideoCodec.MPEG1)
            self._media_format.setAudioCodec(QMediaFormat.AudioCodec.WMA)
            self._media_recorder.setMediaFormat(self._media_format)
            self._capture_session.setRecorder(self._media_recorder)
            self._capture_session.setAudioInput(self._audio_input)
            self._media_recorder.setQuality(QMediaRecorder.Quality.VeryHighQuality)
            self._capture_session.setVideoOutput(self.ui.videoDisplay)
            self._capture_session.setCamera(self._camera)
            self.ui.videoDisplay.show()

            self._camera.start()

    def microphone_selection_changed(self):
        """ The method is called when the microphone selection has been changed """
        index = self.ui.microphoneList.currentIndex()
        self._audio_input = QAudioInput(self._microphones[index])
        self._capture_session.setAudioInput(self._audio_input)

    def camera_selection_changed(self):
        """ The method is called when the camera selection has been changed """
        index = self.ui.cameraList.currentIndex()
        self._camera = QCamera(self._cameras[index])
        self._capture_session.setCamera(self._camera)

    def update_record_state(self, state):
        print(f'Record state: {self._media_recorder.recorderState()}')
        if self._media_recorder.recorderState() == QMediaRecorder.RecorderState.RecordingState:
            self.ui.recordButton.setEnabled(False)
            self.ui.stopButton.setEnabled(True)
        elif self._media_recorder.recorderState() == QMediaRecorder.RecorderState.StoppedState:
            self.ui.recordButton.setEnabled(True)
            self.ui.stopButton.setEnabled(False)

    def mute(self):
        if self._audio_input.isMuted():
            self._audio_input.setMuted(False)
            self.ui.muteButton.setText(u'Mute')
        else:
            self._audio_input.setMuted(True)
            self.ui.muteButton.setText(u'Unmute')

    def record(self):
        if not self.ui.videoNoteName.text() == '':
            dirChecker = DirectoryChecker()
            file = f'{dirChecker.video_notes_directory()}{QDir.separator()}{self.ui.videoNoteName.text()}'
            url = f'{QDir.toNativeSeparators(file)}'
            self._media_recorder.setOutputLocation(QUrl.fromLocalFile(url))

            self._media_recorder.record()
            self.ui.stateLabel.setPixmap(QPixmap(':/resource/icons/recording.png').scaledToWidth(50).scaledToHeight(50))

            self._timer.start(1000)
        else:
            msgBox = QMessageBox()
            msgBox.setText('Please, enter note name.')
            msgBox.exec()


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

    def sec_convert(self, sec):
        result = {'min': 0, 'sec': 0}
        result['sec'] = sec
        if sec >= 60:
            result['min'] = int(sec / 60)
            result['sec'] = sec % 60
        return result
