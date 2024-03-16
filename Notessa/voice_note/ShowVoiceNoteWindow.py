from PySide6.QtCore import QUrl, QDir
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from Notessa.voice_note.ui_showvoicenotewindow import Ui_ShowVoiceNoteWindow
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.resource import rc_icons


class ShowVoiceNoteWindow(QDialog):
    def __init__(self, parent, noteData: list):
        super().__init__(parent)
        self.ui = Ui_ShowVoiceNoteWindow()
        self.ui.setupUi(self)

        self.noteData = noteData

        # Icon set
        self.setWindowIcon(QIcon(':/resource/icons/microphone.png'))
        self.ui.playButton.setIcon(QIcon(':/resource/icons/play.png'))
        self.ui.pauseButton.setIcon(QIcon(':/resource/icons/pause.png'))
        self.ui.stopButton.setIcon(QIcon(':/resource/icons/stop.png'))
        self.ui.backButton.setIcon(QIcon(':/resource/icons/back.png'))

        self.ui.voiceNoteName.setText(self.noteData[1])

        _dir_checker = DirectoryChecker()
        self._file_path = f'{_dir_checker.voice_notes_directory()}{QDir.separator()}{self.noteData[1]}.{self.noteData[0]}'

        # Media settings
        self._media_player = QMediaPlayer()
        self._audio_output = QAudioOutput()
        self._media_player.setAudioOutput(self._audio_output)

        #
        self._audio_output.setVolume(0.5)
        self.ui.volumeSlider.setValue(self._audio_output.volume() * 100)

        # Setting a playback target
        self._media_player.setSource(QUrl.fromLocalFile(self._file_path))

        # Signal-Slot
        self.ui.backButton.clicked.connect(self.back)
        self.ui.playButton.clicked.connect(self.play)
        self.ui.stopButton.clicked.connect(self.stop)
        self.ui.pauseButton.clicked.connect(self.pause)
        self._media_player.positionChanged.connect(self.on_position_changed)
        self.ui.positionSlider.sliderMoved.connect(self.change_duration_slider)
        self.ui.volumeSlider.sliderMoved.connect(self.change_volume_slider)

    def back(self):
        self.reject()

    def play(self):

        # Set the maximum slider value based on the final length of the audio file (msec)
        duration = self.msec_convert(self._media_player.duration())
        self.ui.durationLabel.setText(f'{duration["min"]}:{duration["sec"]}')
        # Changing the position of the slider depending on the current moment of playback (msec)
        self.ui.positionSlider.setMaximum(self._media_player.duration())

        # Initialization if the recording has not yet been played or it was reset due to 'Stop'
        if (self._media_player.playbackState() != QMediaPlayer.PlaybackState.PlayingState and
                self._media_player.playbackState() != QMediaPlayer.PlaybackState.PausedState):
            self._media_player.play()
        else:
            self._media_player.play()


    def stop(self):
        if self._media_player.playbackState() != QMediaPlayer.PlaybackState.StoppedState:
            self._media_player.stop()

    def pause(self):
        if self._media_player.playbackState() != QMediaPlayer.PlaybackState.PausedState:
            self._media_player.pause()

    def on_position_changed(self):
        position = self.msec_convert(self._media_player.position())
        self.ui.currentPositionLabel.setText(f'{position["min"]}:{position["sec"]}')
        self.ui.positionSlider.setValue(self._media_player.position())

    def change_duration_slider(self):
        self._media_player.setPosition(self.ui.positionSlider.value())

    def change_volume_slider(self):
        self._audio_output.setVolume(self.ui.volumeSlider.value()/100)

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
