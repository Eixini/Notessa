#include "notessavoicenote.h"

// ::::::::::::::::::::::::::::::::::::::::::::: Заголовки для WAV-файла ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
struct RIFFHeader
{
    char    chunkId[4];         // Символы "RIFF" в ASCII-кодировке, начало RIFF цепочки
    quint32 chunkSize;          // Оставшийся размер RIFF цепочки (без chunkId и chunkSize)
    char    format[4];          // Символы "WAVE" в ASCII-кодировке
};

struct WAVEHeader
{
    char    subchunk1Id[4];     // Символы "fmt" в ASCII-кодировке
    quint32 subchunk1Size;      // 16 байт для формата PCM, размер оставшейся подцепочки (без subchunk1Id и subchunk1Size)
    quint16 audioFormat;        // Аудио формат, для PCM = 1 (линейное квантование). Отличное от 1 - некоторый формат сжатия
    quint16 numChannels;        // Количество каналов (1 - Моно, 2 - Стерео и т.д)
    quint32 sampleRate;         // Частота дискретизации (например 8000 Гц, 441000 Гц и т.д)
    quint32 byteRate;           // Количество байт, переданных за секунду воспроизведения
    quint16 blockAlign;         // Количество байт для одного sample
    quint16 bitsPerSample;      // Количество бит в sample (глубина или точность звучания, например 8 бит, 16 бит и т.д)
};

struct DATAHeader
{
    char    subchank2Id[4];     // Символы "data" в ASCII-кодировке
    quint32 subchunk2Size;      // Количество байт в области данных
};

NotessaVoiceNote::NotessaVoiceNote(QObject *parent): QObject{parent}
{
    nameVoiceNote   = new QString("");                    // Строка для хранения имени голосовой заметки
}

void NotessaVoiceNote::createVoiceNote(QSystemTrayIcon & trayicon)
{   // Слот для создания голосовой заметки
    /* -------------------------------------------- СОЗДАНИЕ ОБЪЕКТОВ ОКНА ТЕКСТОВЫХ ЗАМЕТОК ---------------------------------------- */
    QDialog *voiceNoteWin = new QDialog();

    voiceNoteWin->setWindowTitle(tr("Create new Voice note"));
    voiceNoteWin->setWindowIcon(QIcon(":/morningstar_resources/icons/microphone_icon.png"));

    QVBoxLayout voiceNoteVBoxLayout(voiceNoteWin);                              // Компоновщик для размещения в нем кнопок окна

    QLineEdit voiceNoteTitle(voiceNoteWin);                                     // Поле ввода для названия текстовой заметки

    QRegularExpression regexp("([a-zA-Zа-яА-Я0-9-_]){255}");                               // Для ограничения по вводимым символам
    QRegularExpressionValidator REvalidator(regexp);

    QPushButton recordingStartButton(tr("Start"));                              // Кнопка для начала записи звука
    QPushButton recordingStopButton(tr("Stop"));                                // Кнопка для завершения записи звука
    QPushButton returnButton(tr("Return"));                                     // Кнопка для возврата в меню заметок

    QFormLayout noteNameFormLayout;

    /* :::::::::::::::::::::::::::::::::::::::::::::::::::::: НАСТРОЙКА ФУНКЦИОНАЛА ::::::::::::::::::::::::::::::::::::::::::::::::: */
    voiceNoteTitle.setPlaceholderText(tr("Enter a name and then start recording ..."));   // Установка текста заполнителя

    voiceNoteTitle.setValidator(&REvalidator);

    recordingStartButton.setIcon(QIcon(":/notessa_resources/icon/player/play_icon.png"));
    recordingStopButton.setIcon(QIcon(":/notessa_resources/icon/player/stop_icon.png"));

    /* ++++++++++++++++++++++++++++++++++++++++++++++++++++++ ПОДКЛЮЧЕНИЕ К СИГНАЛАМ ++++++++++++++++++++++++++++++++++++++++++++++++ */
    connect(&returnButton, &QPushButton::clicked, voiceNoteWin, &QDialog::close);
    connect(&recordingStartButton,&QPushButton::clicked, this,[&]()
    {
        if(voiceNoteTitle.text() != "")
        {

            if(!audioFile.exists(QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation) + "/MorningStar" + "/MorningStar_Reliza" + "/VoiceNote" + "/" + voiceNoteTitle.text() + ".wav"))
                  *nameVoiceNote = QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation) + "/MorningStar" + "/MorningStar_Reliza" + "/VoiceNote" + "/" + voiceNoteTitle.text() + ".wav";    // Установка названия для файла из поля для ввод
            else
            {
                trayicon.showMessage(tr("Voice note"), tr("A file with the same name already exists."));
                generateNameForVoiceNote();
            }

        }
        else
        {
            generateNameForVoiceNote();
        }
    }
            );
    connect(&recordingStartButton, &QPushButton::clicked, this, &NotessaVoiceNote::recorderStart);
    connect(&recordingStopButton, &QPushButton::clicked, this, &NotessaVoiceNote::recorderStop);
    connect(&recordingStopButton, &QPushButton::clicked, voiceNoteWin, &QDialog::accept);

    /* ====================================================== РАБОТА С ФУНКЦИОНАЛОМ ================================================= */
    audioForm.setChannelCount(2);                          // Количество каналов (1 - моно, 2 - стерео и т.д)
    audioForm.setByteOrder(QAudioFormat::LittleEndian);    // Порядок байтов (LittleEndian - от младшего к старшему, BigEndian - от старшего к младшему)
    audioForm.setCodec("audio/pcm");                       // Установка режима шифратора/дешифратора (обычно ставится "audio/pcm")
    audioForm.setSampleSize(8);                            // Уровень выборки Импульсно-Кодовой Модуляции (pcm)
    audioForm.setSampleRate(44100);                         // Скорость оцифровки (количество отчетов в 1 сек)
    audioForm.setSampleFormat(QAudioFormat::UInt8);        // Численное представлени выборки (для pcm обычно SignedInt или UnSignedInt)

    audioDeviceInfo = QAudioDevice::defaultInputDevice();

    if(!audioDeviceInfo.isFormatSupported(audioForm))
    {
        qWarning() << "Default format not supported, trying to use the nearest.";
        trayicon.setVisible(true);
        trayicon.showMessage("Warning!", "Default format not supported, trying to use the nearest.", QIcon(":/image/icon/info_icon.png"), 3000);
        audioForm = audioDeviceInfo.nearestFormat(audioForm);
    }
    /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ УПРАВЛЕНИЕ КОМПОНОВКОЙ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
    noteNameFormLayout.addRow(tr("Name: "), &voiceNoteTitle);

    voiceNoteVBoxLayout.addLayout(&noteNameFormLayout);
    voiceNoteVBoxLayout.addWidget(&recordingStartButton);
    voiceNoteVBoxLayout.addWidget(&recordingStopButton);
    voiceNoteVBoxLayout.addStretch(1);
    voiceNoteVBoxLayout.addWidget(&returnButton);

    voiceNoteWin->setLayout(&voiceNoteVBoxLayout);                              // Установка компоновщика в качестве основного

    voiceNoteWin->exec();
}

void NotessaVoiceNote::showVoiceNote(const QModelIndex & index, NoteModel & notemodel, QSortFilterProxyModel & sortmodel, QString & noteType)
{
    QDialog *playVoiceNoteWin = new QDialog();
    playVoiceNoteWin->setWindowTitle(tr("Play voice note"));
    playVoiceNoteWin->setWindowIcon(QIcon(":/morningstar_resources/icons/microphone_icon.png"));
    playVoiceNoteWin->setFixedHeight(150);

    // Получение полного имени файла (путь + имя файла с суффиксом), в зависимости от выбранного элемента в списке заметок
    QString voiceNoteFilePath = QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation)
                                + "/Notessa" + "/VoiceNote" + "/"
                                + notemodel.noteName(sortmodel.mapToSource(index)) + '.' + noteType;
    /* ++++++++++++++++++++++++++++++++++++++++++++++++++++++ ИНИЦИАЛИЗАЦИЯ ОБЪЕКТОВ ++++++++++++++++++++++++++++++++++++++++++++++++ */
    QVBoxLayout *voiceNoteVLayout = new QVBoxLayout(playVoiceNoteWin);
    QHBoxLayout layoutSlider;
    QHBoxLayout layoutVolume;
    QSlider audioProgressLine;
    QSlider audioVolumeLine;
    QPushButton playAndStopButton;
    QPushButton stopButton;
    QMediaPlayer *mediaPlayer = new QMediaPlayer;
    QLabel currentAudioTime;                                        // Текстовая метка для хранения текущего времени проигрывания аудио-файла
    QLabel durationAudioTime;                                       // Текстовая метка для хранения максимального времени аудио-файла
    QLabel audioMutedStatus;
    QLabel audioMaxStatus;
    QTimer currentAudioTimer;

    /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ НАСТРОЙКА ОБЪЕКТОВ  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
    audioProgressLine.setOrientation(Qt::Horizontal);
    audioProgressLine.setMinimum(0);

    playAndStopButton.setIcon(QIcon(":/notessa_resources/icon/player/pause_icon.png"));
    stopButton.setIcon(QIcon(":/notessa_resources/icon/player/stop_icon.png"));

    mediaPlayer->setMedia(QUrl::fromLocalFile(voiceNoteFilePath));
    mediaPlayer->setVolume(50);
    mediaPlayer->play();

    audioVolumeLine.setOrientation(Qt::Horizontal);
    audioVolumeLine.setMinimum(0);
    audioVolumeLine.setMaximum(100);
    audioVolumeLine.setSliderPosition(mediaPlayer->volume());

    currentAudioTime.setText(tr("Current"));
    durationAudioTime.setText(tr("End"));

    audioMutedStatus.setPixmap(QIcon(":/morningstar_resources/icons/player/volume_muted_icon.svg").pixmap(QSize(20,20)));
    audioMaxStatus.setPixmap(QIcon(":/morningstar_resources/icons/player/volume_max_icon.svg").pixmap(QSize(20,20)));

    /* ====================================================== ПОДКЛЮЧЕНИЕ К СИГНАЛАМ ================================================ */
    connect(mediaPlayer, &QMediaPlayer::durationChanged, playVoiceNoteWin,
            [&]()
    {
        int dMin = (mediaPlayer->duration() / 1000) / 60;            // Получение части мин
        int dSec = (mediaPlayer->duration() / 1000) - (dMin * 60);   // Получени части сек
        int dHour = 0;
        if(dMin > 60)
        {
            dHour =  dMin / 60;
            dMin-=(dHour*60);                                        // Изменение количества минут, так как значение превысило 60
            durationAudioTime.setText(QString(QString::number(dHour) + ":" +QString::number(dMin).rightJustified(2,'0') + ":" + QString::number(dSec).rightJustified(2,'0')));
        }
        else
            durationAudioTime.setText(QString(QString::number(dMin).rightJustified(2,'0') + ":" + QString::number(dSec).rightJustified(2,'0')));

        audioProgressLine.setMaximum(mediaPlayer->duration());     // Аккуратно! Если значение будет слишком большое (больше Инта), то будет плохо

    }
    );

    // При изменении позиции воспроизводимой аудио-записи, будет меняться позиция ползунка и текстовая метка с текущим временем
    connect(mediaPlayer, &QMediaPlayer::positionChanged, playVoiceNoteWin, [&]()
    {
        int cMin = (mediaPlayer->position() / 1000) / 60;            // Получение части мин
        int cSec = (mediaPlayer->position() / 1000) - (cMin * 60);   // Получени части сек
        int cHour = 0;

        if(cMin > 60)
        {
            cHour =  cMin / 60;
            cMin-=(cHour*60);                                        // Изменение количества минут, так как значение превысило 60
            currentAudioTime.setText(QString(QString::number(cHour) + ":" +QString::number(cMin).rightJustified(2,'0') + ":" + QString::number(cSec).rightJustified(2,'0')));
        }
        else
            currentAudioTime.setText(QString(QString::number(cMin).rightJustified(2,'0') + ":" + QString::number(cSec).rightJustified(2,'0')));

        audioProgressLine.setSliderPosition(mediaPlayer->position());
    }
            );

    connect(&playAndStopButton, &QPushButton::clicked, mediaPlayer, [&]()
    {
        if(mediaPlayer->state() == QMediaPlayer::PlayingState)
        {
                mediaPlayer->pause();
        }
        else
        {
               mediaPlayer->play();
        }
    }
            );

    connect(&audioProgressLine, &QSlider::valueChanged, mediaPlayer, &QMediaPlayer::setPosition);

    // В зависимости от состояния, будет меняться текст кнопки.
    connect(mediaPlayer, &QMediaPlayer::stateChanged, playVoiceNoteWin, [&]()
    {
        if(mediaPlayer->state() == QMediaPlayer::PlayingState)
            playAndStopButton.setIcon(QIcon(":/notessa_resources/icon/player/pause_icon.png"));
        if(mediaPlayer->state() == QMediaPlayer::PausedState)
            playAndStopButton.setIcon(QIcon(":/notessa_resources/icon/player/play_icon.png"));
        if(mediaPlayer->state() == QMediaPlayer::StoppedState)
            playAndStopButton.setIcon(QIcon(":/notessa_resources/icon/player/play_icon.png"));
    }
            );

    connect(&audioVolumeLine, &QSlider::valueChanged, mediaPlayer, &QMediaPlayer::setVolume);
    connect(&stopButton, &QPushButton::clicked, playVoiceNoteWin, [&](){mediaPlayer->stop(); });
    connect(playVoiceNoteWin, &QDialog::finished, playVoiceNoteWin, [&](){mediaPlayer->stop(); });
    connect(&stopButton, &QPushButton::clicked, playVoiceNoteWin, &QDialog::accept);

    /* ...................................................... УПРАВЛЕНИЕ КОМПОНОВКОЙ ................................................ */

    layoutSlider.addWidget(&currentAudioTime);
    layoutSlider.addWidget(&audioProgressLine);
    layoutSlider.addWidget(&durationAudioTime);

    layoutVolume.addWidget(&audioMutedStatus);
    layoutVolume.addWidget(&audioVolumeLine);
    layoutVolume.addWidget(&audioMaxStatus);

    voiceNoteVLayout->addLayout(&layoutSlider);
    voiceNoteVLayout->addLayout(&layoutVolume);
    voiceNoteVLayout->addWidget(&playAndStopButton);
    voiceNoteVLayout->addWidget(&stopButton);

    playVoiceNoteWin->exec();
}

void NotessaVoiceNote::recorderStart()
{   // Слот для запуска записи

    audioFile.setFileName(*nameVoiceNote);
    audioFile.open( QIODevice::WriteOnly | QIODevice::Truncate );
    audioInput = new QAudioInput(audioForm, this);
    connect(audioInput, &QAudioInput::stateChanged, this, &NotessaVoiceNote::handleStateChanged);
    audioInput->start(&audioFile);

}

void NotessaVoiceNote::recorderStop()
{   // Слот для окончания записи
    audioInput->stop();                     // Остановка записи
    writeHeader();                          // Запись в файл заголовков
    notemodel->appendData(audioFile);       // Сообщить моделе, что произошло добавление нового аудио-файла
    audioFile.close();                      // Закрытие файла

    disconnect(audioInput, &QAudioInput::stateChanged, this, &NotessaVoiceNote::handleStateChanged);

    trayicon->setVisible(true);
    trayicon->showMessage("Voice Note Info", tr("Sound recording is complete."));

}

void NotessaVoiceNote::handleStateChanged(QSystemTrayIcon & trayicon)
{  // Слот по информированию о состоянии потока записи
    switch (audioInput->state())
    {
        case QAudio::StoppedState:
            if(audioInput->error() != QAudio::NoError)
            {
                trayicon.setVisible(true);
                trayicon.showMessage("Voice Note Info", tr("Error, sound recording is not possible!"));
            }
            else
            {
                audioInput->stop();
            }
            break;

       case QAudio::ActiveState:
       {
            trayicon.setVisible(true);
            trayicon.showMessage("Voice Note Info", tr("Sound recording in progress."));
            break;
       }

    }

}

void NotessaVoiceNote::writeHeader()
{   // Запись заголовка в аудио-файл
    QFileInfo sizefile;
    sizefile.setFile(audioFile);
    quint32 datasize = sizefile.size();         // Размер аудио-данных, которые были записаны в файл (без учета заголовков)

    audioFile.seek(0);                          // Установка "каретки" в самое начало файла

    RIFFHeader  riffheader;                     // Создание объекта RIFF заголовка
    WAVEHeader  waveheader;                     // Создание объекта WAVE заголовка
    DATAHeader  dataheader;                     // Создание объекта DATA заголовка

    for(int i = 0; i < 4; ++i)                  // Запись симоволов RIFF
        riffheader.chunkId[i] = "RIFF"[i];
    riffheader.chunkSize = sizeof(quint32) + sizeof(WAVEHeader) + sizeof(quint64) + dataheader.subchunk2Size;      // Отсавшийся размер RIFF цепочки

    for(int i = 0; i < 4; ++i)                  // Запись симоволов WAVE
        riffheader.format[i] = "WAVE"[i];

    for(int i = 0; i < 4; ++i)                  // Запись симоволов fmt
        waveheader.subchunk1Id[i] = "fmt "[i];
    waveheader.subchunk1Size = (sizeof(WAVEHeader) - sizeof(quint64));      // Оставшийся размер WAVEHeader, без subchunk1Id и subchunk1Size
    waveheader.audioFormat = 1;                 // Установка аудио формата (для PCM = 1 , линейное квантование)
    waveheader.numChannels = 2;                 // Установка количества каналов (1 = Моно, 2 = Стерео и т.д)
    waveheader.sampleRate = 44100;               // Установка частоты дискретизации (Гц)
    waveheader.bitsPerSample = 8;               // Установка количества бит в sample (глубина звучания, например 8 бит, 16 бит и т.д)
    waveheader.byteRate =   waveheader.sampleRate
                        *   waveheader.numChannels
                        *   waveheader.bitsPerSample / 8;         // Установка количества байт, переданных за секунду воспроизведения
    waveheader.blockAlign = waveheader.numChannels
                          * waveheader.bitsPerSample / 8;       // Установка количества байт для одного sample

    for(int i = 0; i < 4; ++i)                  // Запись симоволов data
        dataheader.subchank2Id[i] = "data"[i];
    dataheader.subchunk2Size = datasize;        // Установка размера данных аудио-файла без учета RIFF-цепочки

    // Запись заголовков в начало файла
    {
        audioFile.write(reinterpret_cast<char*>(&riffheader.chunkId),sizeof(char[4]));
        audioFile.write(reinterpret_cast<char*>(&riffheader.chunkSize),sizeof(quint32));
        audioFile.write(reinterpret_cast<char*>(&riffheader.format),sizeof(char[4]));
        audioFile.write(reinterpret_cast<char*>(&waveheader.subchunk1Id),sizeof(char[4]));
        audioFile.write(reinterpret_cast<char*>(&waveheader.subchunk1Size),sizeof(quint32));
        audioFile.write(reinterpret_cast<char*>(&waveheader.audioFormat),sizeof(quint16));
        audioFile.write(reinterpret_cast<char*>(&waveheader.numChannels),sizeof(quint16));
        audioFile.write(reinterpret_cast<char*>(&waveheader.sampleRate),sizeof(quint32));
        audioFile.write(reinterpret_cast<char*>(&waveheader.byteRate),sizeof(quint32));
        audioFile.write(reinterpret_cast<char*>(&waveheader.blockAlign),sizeof(quint16));
        audioFile.write(reinterpret_cast<char*>(&waveheader.bitsPerSample),sizeof(quint16));
        audioFile.write(reinterpret_cast<char*>(&dataheader.subchank2Id),sizeof(char[4]));
        audioFile.write(reinterpret_cast<char*>(&dataheader.subchunk2Size),sizeof(quint32));
    }
}

void NotessaVoiceNote::generateNameForVoiceNote()
{ // Слот для генерации имени для голосовой заметки (в зависимости от текущего времени и даты)
    QDate date = QDate::currentDate();
    QTime time = QTime::currentTime();

    QString voiceNoteLoc = QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation) + "/Notessa" + "/VoiceNote";

    // Установка название файла исходя из вида заметки (голосовая) и момента записи (текущая дата + текущее время)
    *nameVoiceNote = voiceNoteLoc + "/morningstar-voicenote_" + QString::number(date.year())     + "-"
                                                              + QString::number(date.month())    + "-"
                                                              + QString::number(date.day())      + "_"
                                                              + QString::number(time.hour())     + "-"
                                                              + QString::number(time.minute())   + "-"
                                                              + QString::number(time.second())   + ".wav";
}

