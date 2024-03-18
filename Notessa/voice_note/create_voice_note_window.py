from PySide6.QtCore import QUrl, QDir
from PySide6.QtGui import QIcon, QRegularExpressionValidator
from PySide6.QtWidgets import QDialog, QMessageBox
from PySide6.QtMultimedia import QMediaDevices, QMediaFormat, QMediaRecorder, QMediaCaptureSession, QAudioInput
from Notessa.voice_note.ui_createvoicenote import Ui_CreateVoiceNote
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.resource import rc_icons

"""
Mark:
- check device availability before recording;
"""

class CreateVoiceNote(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_CreateVoiceNote()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(':/resource/icons/microphone.png'))
        self.ui.voiceNoteName.setReadOnly(False)
        self.ui.pauseButton.setEnabled(False)

        self.ui.voiceNoteName.setValidator(QRegularExpressionValidator('([a-zA-Zа-яА-Я0-9-_]){255}'))

        # Buttons settings
        self.ui.recordButton.setIcon(QIcon(':/resource/icons/play.png'))
        self.ui.pauseButton.setIcon(QIcon(':/resource/icons/pause.png'))
        self.ui.stopButton.setIcon(QIcon(':/resource/icons/stop.png'))
        self.ui.backButtun.setIcon(QIcon(':/resource/icons/back.png'))

        # Audio settings
        self._input_devices = None
        self._audio_input = QAudioInput(self)
        self._session = QMediaCaptureSession(self)
        self._media_recorder = QMediaRecorder(self)
        self._media_format = QMediaFormat()

        self.microphone_initialization()

        # Signal - Slot
        self.ui.recordButton.clicked.connect(self.record_voice_note)
        self.ui.stopButton.clicked.connect(self.stop_voice_note)
        self.ui.pauseButton.clicked.connect(self.pause_voice_note)

        self._media_recorder.durationChanged.connect(self.changeLabel)
        self._media_recorder.recorderStateChanged.connect(self.update_record_state)
        self.ui.availableDevicesList.currentIndexChanged.connect(self.microphone_selection_changed)

        # Signal - Slot
        self.ui.backButtun.clicked.connect(self.back)

    def update_record_state(self):
        """
        Method for checking the status of a record.
        The state determines which buttons are available to press.
        """
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

    def microphone_initialization(self):
        """ Method for initializing the list of available microphones """
        self._input_devices = QMediaDevices.audioInputs()
        if len(self._input_devices) > 0:
            for aud_inp in self._input_devices:
                self.ui.availableDevicesList.addItem(aud_inp.description())
            self._audio_input = QAudioInput(self._input_devices[0])

            self._session.setAudioInput(self._audio_input)
            self._media_recorder.setQuality(QMediaRecorder.Quality.VeryHighQuality)

            self._media_format.setFileFormat(QMediaFormat.FileFormat.Wave)
            self._media_format.setAudioCodec(QMediaFormat.AudioCodec.Wave)
            self._media_recorder.setMediaFormat(self._media_format)
            self._session.setRecorder(self._media_recorder)
        else:
            msg = QMessageBox()
            msg.setText('No microphones available')
            msg.setIcon(QIcon(':/resource/icons/microphone_off.png'))

    def microphone_selection_changed(self):
        """ The method is called when the microphone selection has been changed """
        index = self.ui.availableDevicesList.currentIndex()
        print(f'Current index: {index}, value: {self._input_devices[index].description()}')
        self._audio_input = QAudioInput(self._input_devices[index])
        self._session.setAudioInput(self._audio_input)

    def audio_input_changed(self):
        print('Audio input changed')
        self._media_recorder.setQuality(QMediaRecorder.Quality.VeryHighQuality)

        self._media_format.setFileFormat(QMediaFormat.FileFormat.Wave)
        self._media_format.setAudioCodec(QMediaFormat.AudioCodec.Wave)
        self._media_recorder.setMediaFormat(self._media_format)
        self._session.setRecorder(self._media_recorder)

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
        self.ui.pauseButton.setEnabled(False)
        self.ui.voiceNoteName.setReadOnly(False)

        self._media_recorder.stop()

    def closeEvent(self, *args):
        if (self._media_recorder.recorderState() == QMediaRecorder.RecorderState.PausedState or
                self._media_recorder.recorderState() == QMediaRecorder.RecorderState.RecordingState):
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

    def __del__(self):
        # Signal - Slot
        self.ui.recordButton.clicked.connect(self.record_voice_note)
        self.ui.stopButton.clicked.connect(self.stop_voice_note)
        self.ui.pauseButton.clicked.connect(self.pause_voice_note)

        self._media_recorder.durationChanged.connect(self.changeLabel)
        self._media_recorder.recorderStateChanged.connect(self.update_record_state)
        self.ui.availableDevicesList.currentIndexChanged.connect(self.microphone_selection_changed)

        # Signal - Slot
        self.ui.backButtun.clicked.connect(self.back)
