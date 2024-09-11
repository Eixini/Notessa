from PySide6.QtCore import QUrl, QDir, Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

from Notessa.voice_note.ui_gen.ui_show_voicenote_widget import Ui_ShowVoiceNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.common_modules import constants

from Notessa.resources.icons.button import button_icons_rc


class ShowVoiceNoteWidget(QWidget):
    def __init__(self, parent, note_data: list):
        super().__init__(parent)
        self.ui = Ui_ShowVoiceNoteWidget()
        self.ui.setupUi(self)

        self.ui.play_button.setIcon(QIcon(':/button/play.png'))
        self.ui.pause_button.setIcon(QIcon(':/button/pause.png'))
        self.ui.stop_button.setIcon(QIcon(':/button/stop.png'))

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self._note_data = note_data

        self.ui.voicenote_name_label.setText(self._note_data[constants.NOTE_NAME])
        self.setWindowTitle(self._note_data[constants.NOTE_NAME])

        _dir_checker = DirectoryChecker()
        self._file_path = f'{_dir_checker.voice_notes_directory()}{QDir.separator()}{self._note_data[constants.NOTE_FILE_BASENAME]}.{self._note_data[constants.NOTE_FILE_TYPE]}'

        # Media settings
        self._media_player = QMediaPlayer()
        self._audio_output = QAudioOutput()
        self._media_player.setAudioOutput(self._audio_output)

        # Initial sound setup
        self._audio_output.setVolume(0.5)
        self.ui.volume_slider.setValue(self._audio_output.volume() * 100)

        # Setting a playback target
        self._media_player.setSource(QUrl.fromLocalFile(self._file_path))

        # Signal-Slot
        self.ui.play_button.clicked.connect(self.play)
        self.ui.stop_button.clicked.connect(self.stop)
        self.ui.pause_button.clicked.connect(self.pause)
        self._media_player.positionChanged.connect(self.on_position_changed)
        self.ui.position_slider.sliderMoved.connect(self.change_duration_slider)
        self.ui.volume_slider.sliderMoved.connect(self.change_volume_slider)

    def play(self):

        # Set the maximum slider value based on the final length of the audio file (msec)
        duration = self.msec_convert(self._media_player.duration())
        self.ui.duration_label.setText(f'{duration["min"]}:{duration["sec"]}')
        # Changing the position of the slider depending on the current moment of playback (msec)
        self.ui.position_slider.setMaximum(self._media_player.duration())

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
        self.ui.current_position_label.setText(f'{position["min"]}:{position["sec"]}')
        self.ui.position_slider.setValue(self._media_player.position())

    def change_duration_slider(self):
        self._media_player.setPosition(self.ui.position_slider.value())

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
