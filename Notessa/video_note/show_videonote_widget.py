from PySide6.QtCore import QUrl, QDir, Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from Notessa.video_note.ui_gen.ui_show_videonote_widget import Ui_ShowVideoNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker


class ShowVideoNoteWidget(QWidget):
    def __init__(self, parent, note_data: list):
        super().__init__(parent)
        self.ui = Ui_ShowVideoNoteWidget()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self._note_data = note_data

        self.ui.videonote_name_label.setText(self._note_data[1])

        _dir_checker = DirectoryChecker()
        self._file_path = f'{_dir_checker.video_notes_directory()}{QDir.separator()}{self._note_data[1]}.{self._note_data[0]}'

        # Media settings
        self._media_player = QMediaPlayer()
        self._audio_output = QAudioOutput()
        self._media_player.setAudioOutput(self._audio_output)

        #
        self._audio_output.setVolume(0.5)
        self.ui.volume_slider.setValue(self._audio_output.volume() * 100)

        # Setting a playback target
        self._media_player.setSource(QUrl.fromLocalFile(self._file_path))
        self._media_player.setVideoOutput(self.ui.play_videonote_widget)

        # Signal - Slot
        self.ui.play_button.clicked.connect(self.play)
        self.ui.stop_button.clicked.connect(self.stop)
        self.ui.pause_button.clicked.connect(self.pause)
        self.ui.close_button.clicked.connect(self.close_note)
        self.ui.volume_slider.sliderMoved.connect(self.change_volume_slider)
        self._media_player.positionChanged.connect(self.on_position_changed)
        self.ui.duration_slider.sliderMoved.connect(self.change_duration_slider)

    def play(self):
        # Set the maximum slider value based on the final length of the audio file (msec)
        duration = self.msec_convert(self._media_player.duration())
        self.ui.duration_label.setText(f'{duration["min"]}:{duration["sec"]}')
        # Changing the position of the slider depending on the current moment of playback (msec)
        self.ui.duration_slider.setMaximum(self._media_player.duration())

        # Initialization if the recording has not yet been played or it was reset due to 'Stop'
        if (self._media_player.playbackState() != QMediaPlayer.PlaybackState.PlayingState and
                self._media_player.playbackState() != QMediaPlayer.PlaybackState.PausedState):
            self._media_player.play()
        else:
            self._media_player.play()

    def pause(self):
        if self._media_player.playbackState() != QMediaPlayer.PlaybackState.PausedState:
            self._media_player.pause()

    def stop(self):
        if self._media_player.playbackState() != QMediaPlayer.PlaybackState.StoppedState:
            self._media_player.stop()

    def close_note(self):
        self.close()

    def on_position_changed(self):
        position = self.msec_convert(self._media_player.position())
        self.ui.position_label.setText(f'{position["min"]}:{position["sec"]}')
        self.ui.duration_slider.setValue(self._media_player.position())

    def change_duration_slider(self):
        self._media_player.setPosition(self.ui.duration_slider.value())

    def change_volume_slider(self):
        self._audio_output.setVolume(self.ui.volume_slider.value()/100)

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
