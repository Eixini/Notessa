import json, uuid, os, platform

from PySide6.QtCore import QTimer, QDir, QUrl, Qt, QDateTime
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtMultimedia import QMediaFormat, QMediaRecorder, QMediaCaptureSession, QAudioInput, QCamera, QMediaDevices
from Notessa.video_note.ui_gen.ui_create_videonote_widget import Ui_CreateVideoNoteWidget
from Notessa.common_modules.directory_checker import DirectoryChecker
from Notessa.common_modules.forming_note_name import forming_note_file_name
from Notessa.save_dialog.save_dialog import SaveDialog

from Notessa.resources.icons.button import button_icons_rc


class CreateVideoNoteWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.ui = Ui_CreateVideoNoteWidget()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)
        self.installEventFilter(self.parent())

        # Set a default note deadline -
        self.note_deadline = 'None'

        # Media devices input
        self._microphones = None
        self._cameras = None

        # Media settings
        self._camera = QCamera(self)
        self._capture_session = QMediaCaptureSession(self)
        self._media_recorder = QMediaRecorder(self)
        self._audio_input = QAudioInput(self)
        self._media_format = QMediaFormat()

        # Initializing media devices
        self.media_devices_initialization()

        # Icon set
        self.ui.state_label.setPixmap(QPixmap(':/button/video_off.png').scaledToWidth(50).scaledToHeight(50))
        self.ui.record_button.setIcon(QIcon(':/button/play.png'))
        self.ui.stop_button.setIcon(QIcon(':/button/stop.png'))
        self.ui.mute_button.setIcon(QIcon(':/button/microphone_off.png'))

        # Alternative to QMediaRecorder.duration()
        self._duration = 0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.update_duration)

        # Signal - Slot
        self.ui.reload_devices_button.clicked.connect(self.reload_devices)
        self.ui.record_button.clicked.connect(self.record)
        self.ui.stop_button.clicked.connect(self.stop)
        self.ui.mute_button.clicked.connect(self.mute)

        self._media_recorder.durationChanged.connect(self.change_label)
        self._media_recorder.recorderStateChanged.connect(self.update_record_state)
        self.ui.microphones_combobox.currentIndexChanged.connect(self.microphone_selection_changed)
        self.ui.cameras_combobox.currentIndexChanged.connect(self.camera_selection_changed)

        self._camera.errorChanged.connect(self.disconnect_devices_handler)

    def media_devices_initialization(self):
        """ Method for initializing media devices such as microphone and camera """
        # Initializing the microphone
        # self._microphones = QMediaDevices.audioInputs()
        # if len(self._microphones) > 0:
        #     for mic in self._microphones:
        #         self.ui.microphones_combobox.addItem(mic.description())
        #     self._audio_input = QAudioInput(self._microphones[0])
        #
        # # Initializing the camera
        # self._cameras = QMediaDevices.videoInputs()
        # if len(self._cameras) > 0:
        #     for camera in self._cameras:
        #         self.ui.cameras_combobox.addItem(camera.description())
        #     self._camera = QCamera(self._cameras[0])

        if self._camera.isAvailable():
            self._media_format.setFileFormat(QMediaFormat.FileFormat.AVI)
            self._media_format.setVideoCodec(QMediaFormat.VideoCodec.MPEG1)
            self._media_format.setAudioCodec(QMediaFormat.AudioCodec.WMA)
            self._media_recorder.setMediaFormat(self._media_format)
            self._capture_session.setRecorder(self._media_recorder)
            self._capture_session.setAudioInput(self._audio_input)
            self._media_recorder.setQuality(QMediaRecorder.Quality.VeryHighQuality)
            self._capture_session.setVideoOutput(self.ui.video_display)
            self._capture_session.setCamera(self._camera)
            self.ui.video_display.show()

            self._camera.start()

    def microphone_selection_changed(self):
        """ The method is called when the microphone selection has been changed """
        index = self.ui.microphones_combobox.currentIndex()
        self._audio_input = QAudioInput(self._microphones[index])
        self._capture_session.setAudioInput(self._audio_input)

        self.media_devices_initialization()

    def camera_selection_changed(self):
        """ The method is called when the camera selection has been changed """
        index = self.ui.cameras_combobox.currentIndex()
        self._camera = QCamera(self._cameras[index])
        self._capture_session.setCamera(self._camera)

        self.media_devices_initialization()

    def update_record_state(self, state):
        if self._media_recorder.recorderState() == QMediaRecorder.RecorderState.RecordingState:
            self.ui.record_button.setEnabled(False)
            self.ui.stop_button.setEnabled(True)
        elif self._media_recorder.recorderState() == QMediaRecorder.RecorderState.StoppedState:
            self.ui.record_button.setEnabled(True)
            self.ui.stop_button.setEnabled(False)

    def mute(self):
        if self._audio_input.isMuted():
            self._audio_input.setMuted(False)
            self.ui.mute_button.setIcon(QIcon(':/button/microphone_off.png'))
        else:
            self._audio_input.setMuted(True)
            self.ui.mute_button.setIcon(QIcon(':/button/microphone.png'))

    def record(self):
        save_dialog = SaveDialog(self)
        _, note_name, deadline_datetime = save_dialog.exec()

        dir_checker = DirectoryChecker()

        file_name = forming_note_file_name('VideoNote')
        file_path = str(f"{dir_checker.video_notes_directory()}{QDir.separator()}{file_name}")
        meta_data_file_path = str(f'{dir_checker.video_notes_directory()}{QDir.separator()}{file_name}.json')

        meta_data_content = {'note_name': note_name}

        url = f'{QDir.toNativeSeparators(file_path)}'
        self._media_recorder.setOutputLocation(QUrl.fromLocalFile(url))

        if not self.note_deadline == 'None':
            meta_data_content.update({'deadline': deadline_datetime.toString()})
        else:
            meta_data_content.update({'deadline': None})

        note_uuid = uuid.uuid1()
        meta_data_content.update({'uuid': f'{note_uuid}'})

        with open(meta_data_file_path, 'w') as file:
            json.dump(meta_data_content, file, indent=4)

        self._media_recorder.record()
        self.ui.state_label.setPixmap(QPixmap(':/button/recording.png').scaledToWidth(50).scaledToHeight(50))

        self._timer.start(1000)

    def stop(self):
        self._media_recorder.stop()
        self.ui.state_label.setPixmap(QPixmap(':/icons/video_off.png').scaledToWidth(50).scaledToHeight(50))
        # Reset duration
        self._timer.stop()
        self._duration = 0

        self.parent().close()
        self.close()

    def disconnect_devices_handler(self):
        """
        If the devices suddenly turn off, you need to:
            1. Display a message to the user about the loss of signal with the device;
            2. Offer to save a note / cancel recording / pause / continue recording;
        """

        if self._camera.error() == 'Error.CameraError':
            print(self._camera.error())
            self.stop()

    def reload_devices(self):
        # Microphones
        self._microphones = QMediaDevices.audioInputs()
        print(f'Microphones list: {[mic.description() for mic in self._microphones]}')
        self.ui.microphones_combobox.clear()
        if len(self._microphones) > 0:
            for mic in self._microphones:
                self.ui.microphones_combobox.addItem(mic.description())

        # Cameras
        self._cameras = QMediaDevices.videoInputs()
        print(f'Cameras list: {[cam.description() for cam in self._cameras]}')
        self.ui.cameras_combobox.clear()
        if len(self._cameras) > 0:
            for cam in self._cameras:
                self.ui.cameras_combobox.addItem(cam.description())

    def change_label(self):
        time_duration = self.sec_convert(self._duration)
        self.ui.duration_label.setText(f'{time_duration["min"]}:{time_duration["sec"]}')

    # def event(self, event):
    #     print(event.type())

    def nativeEvent(self, eventType, message):
        print(message)

    def update_duration(self):
        self._duration += 1

    def sec_convert(self, sec):
        result = {'min': 0, 'sec': 0}
        result['sec'] = sec
        if sec >= 60:
            result['min'] = int(sec / 60)
            result['sec'] = sec % 60
        return result

    # def __del__(self):
    #     self._camera.deleteLater()
    #     self._media_recorder.deleteLater()
    #     self._audio_input.deleteLater()
    #     self._capture_session.deleteLater()
    #
    #     # Disconnect Signal - Slot
    #     self._timer.timeout.disconnect(self.update_duration)
    #     self.ui.record_button.clicked.disconnect(self.record)
    #     self.ui.stop_button.clicked.disconnect(self.stop)
    #     self.ui.mute_button.clicked.disconnect(self.mute)
    #     self._media_recorder.durationChanged.disconnect(self.change_label)
    #     self._media_recorder.recorderStateChanged.disconnect(self.update_record_state)
    #     self.ui.microphones_combobox.currentIndexChanged.disconnect(self.microphone_selection_changed)
