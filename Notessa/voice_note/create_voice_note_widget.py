import json

from PySide6.QtCore import QUrl, QDir, Qt, QDateTime, QFile
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtMultimedia import QMediaDevices, QMediaFormat, QMediaRecorder, QMediaCaptureSession, QAudioInput
from Notessa.voice_note.ui_gen.ui_create_voice_note_widget import Ui_CreateVoiceNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker


class CreateVoiceNoteWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_CreateVoiceNoteWidget()
        self.ui.setupUi(self)

        # Set a default note deadline -
        self.note_deadline = ' '

        # Default value
        self.ui.indefinite_checkbox.setChecked(True)
        self.ui.note_deadline_label.setDisabled(True)
        self.ui.note_date_time_edit.setDisabled(True)

        self.ui.note_date_time_edit.setDateTime(QDateTime.currentDateTime())

        self.setAttribute(Qt.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        self.ui.voicenote_name_lineedit.setReadOnly(False)
        self.ui.pause_button.setEnabled(False)

        # self.ui.available_devices_combobox.view().window().setWindowFlags(Qt.Popup | Qt.FramelessWindowHint | Qt.NoDropShadowWindowHint)
        # self.ui.available_devices_combobox.view().window().setAttribute(Qt.WA_TranslucentBackground)

        self.ui.voicenote_name_lineedit.setValidator(QRegularExpressionValidator('([a-zA-Zа-яА-Я0-9-_ ]){255}'))

        # Audio settings
        self._input_devices = None
        self._audio_input = QAudioInput(self)
        self._session = QMediaCaptureSession(self)
        self._media_recorder = QMediaRecorder(self)
        self._media_format = QMediaFormat()

        self.microphone_initialization()

        # Signal - Slot
        self.ui.record_button.clicked.connect(self.record_voice_note)
        self.ui.stop_button.clicked.connect(self.stop_voice_note)
        self.ui.pause_button.clicked.connect(self.pause_voice_note)

        self._media_recorder.durationChanged.connect(self.change_label)
        self._media_recorder.recorderStateChanged.connect(self.update_record_state)
        self.ui.available_devices_combobox.currentIndexChanged.connect(self.microphone_selection_changed)
        self.ui.indefinite_checkbox.checkStateChanged.connect(self.indefinite_change)
        self.ui.note_date_time_edit.dateTimeChanged.connect(self.select_date_time_change)

    def indefinite_change(self):
        if self.ui.indefinite_checkbox.isChecked():
            self.note_deadline = ' '
            self.ui.note_deadline_label.setDisabled(True)
            self.ui.note_date_time_edit.setDisabled(True)
        else:
            self.note_deadline = self.ui.note_date_time_edit.dateTime().toLocalTime()
            self.ui.note_deadline_label.setEnabled(True)
            self.ui.note_date_time_edit.setEnabled(True)

    def select_date_time_change(self):
        self.note_deadline = self.ui.note_date_time_edit.dateTime().toLocalTime()
        print(self.ui.note_date_time_edit.dateTime().toLocalTime())

    def update_record_state(self):
        """
        Method for checking the status of a record.
        The state determines which buttons are available to press.
        """
        if self._media_recorder.recorderState() == QMediaRecorder.RecorderState.RecordingState:
            self.ui.record_button.setEnabled(False)
            self.ui.pause_button.setEnabled(True)
            self.ui.stop_button.setEnabled(True)
            # Remove the ability to change the deadline while recording a note
            self.ui.note_deadline_label.setDisabled(True)
            self.ui.note_date_time_edit.setDisabled(True)
        elif self._media_recorder.recorderState() == QMediaRecorder.RecorderState.PausedState:
            self.ui.record_button.setEnabled(True)
            self.ui.pause_button.setEnabled(False)
            self.ui.stop_button.setEnabled(True)
            # Remove the ability to change the deadline while recording a note
            self.ui.note_deadline_label.setDisabled(True)
            self.ui.note_date_time_edit.setDisabled(True)
        elif self._media_recorder.recorderState() == QMediaRecorder.RecorderState.StoppedState:
            self.ui.record_button.setEnabled(True)
            self.ui.pause_button.setEnabled(False)
            self.ui.stop_button.setEnabled(False)
            # Enable the ability to change the deadline, as a new note will be written
            self.ui.note_deadline_label.setEnabled(True)
            self.ui.note_date_time_edit.setEnabled(True)

    def microphone_initialization(self):
        """ Method for initializing the list of available microphones """
        self._input_devices = QMediaDevices.audioInputs()
        if len(self._input_devices) > 0:
            for aud_inp in self._input_devices:
                self.ui.available_devices_combobox.addItem(aud_inp.description())
            self._audio_input = QAudioInput(self._input_devices[0])

            self._session.setAudioInput(self._audio_input)
            self._media_recorder.setQuality(QMediaRecorder.Quality.VeryHighQuality)

            self._media_format.setFileFormat(QMediaFormat.FileFormat.Wave)
            self._media_format.setAudioCodec(QMediaFormat.AudioCodec.Wave)
            self._media_recorder.setMediaFormat(self._media_format)
            self._session.setRecorder(self._media_recorder)

    def microphone_selection_changed(self):
        """ The method is called when the microphone selection has been changed """
        index = self.ui.available_devices_combobox.currentIndex()
        print(f'Current index: {index}, value: {self._input_devices[index].description()}')
        self._audio_input = QAudioInput(self._input_devices[index])
        self._session.setAudioInput(self._audio_input)

    def audio_input_changed(self):
        self._media_recorder.setQuality(QMediaRecorder.Quality.VeryHighQuality)

        self._media_format.setFileFormat(QMediaFormat.FileFormat.Wave)
        self._media_format.setAudioCodec(QMediaFormat.AudioCodec.Wave)
        self._media_recorder.setMediaFormat(self._media_format)
        self._session.setRecorder(self._media_recorder)

    def record_voice_note(self):
        if self.date_time_check() == 'Correct' or self.date_time_check() == 'None':
            if (not self.ui.voicenote_name_lineedit.text() == '' and
                    not self._media_recorder.recorderState() == QMediaRecorder.RecorderState.PausedState):
                # Avoid name change
                self.ui.voicenote_name_lineedit.setReadOnly(True)

                dir_checker = DirectoryChecker()
                file = f'{dir_checker.voice_notes_directory()}{QDir.separator()}{self.ui.voicenote_name_lineedit.text()}'
                url = f'{QDir.toNativeSeparators(file)}'
                self._media_recorder.setOutputLocation(QUrl.fromLocalFile(url))

                self._media_recorder.record()

                # If the note file was created successfully
                dir_check = DirectoryChecker()
                file_name = f'{file}.wav'
                print(file_name)
                if QFile(file_name).exists():
                    note_meta_data_file_name = str(f'{dir_check.voice_notes_directory()}{QDir.separator()}{self.ui.voicenote_name_lineedit.text()}.json')

                    if not self.note_deadline == ' ':
                        meta_data_content = {'deadline': self.note_deadline.toString()}
                    else:
                        meta_data_content = {'deadline': ' '}

                    print(f'Note deadline: {meta_data_content}')

                    with open(note_meta_data_file_name, 'w') as file:
                        json.dump(meta_data_content, file, indent=4)

            elif self._media_recorder.recorderState() == QMediaRecorder.RecorderState.PausedState:
                self._media_recorder.record()
        else:
            msg_box = QMessageBox()
            msg_box.setText(u"The note's deadline date and time cannot be less than the current one")
            msg_box.setWindowTitle(u"Invalid value")
            msg_box.exec()
            return

    def pause_voice_note(self):
        self._media_recorder.pause()

    def stop_voice_note(self):
        self.ui.stop_button.setEnabled(False)
        self.ui.record_button.setEnabled(True)
        self.ui.pause_button.setEnabled(False)
        self.ui.voicenote_name_lineedit.setReadOnly(False)

        self._media_recorder.stop()

        self.ui.voicenote_name_lineedit.clear()

    def closeEvent(self, *args):
        if (self._media_recorder.recorderState() == QMediaRecorder.RecorderState.PausedState or
                self._media_recorder.recorderState() == QMediaRecorder.RecorderState.RecordingState):
            self._media_recorder.stop()
        self.accept()

    def change_label(self):
        time_duration = self.msec_convert(self._media_recorder.duration())
        if len(time_duration) == 3:
            self.ui.duration_label.setText(f'{time_duration["min"]}:{time_duration["sec"]}.{time_duration["msec"]}')

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

    def date_time_check(self):
        """ To check the correctness of the note's deadline """
        if not self.note_deadline == ' ':
            if QDateTime.currentDateTime() < self.ui.note_date_time_edit.dateTime():
                return 'Correct'
            else:
                return 'Incorrect'
        else:
            return 'None'

    def __del__(self):
        # Disconnect Signal - Slot
        self.ui.record_button.clicked.disconnect(self.record_voice_note)
        self.ui.stop_button.clicked.disconnect(self.stop_voice_note)
        self.ui.pause_button.clicked.disconnect(self.pause_voice_note)
        self._media_recorder.durationChanged.disconnect(self.change_label)
        self._media_recorder.recorderStateChanged.disconnect(self.update_record_state)
        self.ui.available_devices_combobox.currentIndexChanged.disconnect(self.microphone_selection_changed)
