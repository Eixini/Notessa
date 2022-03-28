#ifndef NOTESSAVOICENOTE_H
#define NOTESSAVOICENOTE_H

#include "notessa.h"
#include "notemodel.h"

#include <QObject>
#include <QAudioInput>
#include <QAudioDevice>
#include <QAudioFormat>
#include <qendian.h>
#include <QString>
#include <QSortFilterProxyModel>

class NotessaVoiceNote : public QObject
{
    Q_OBJECT
public:
    explicit NotessaVoiceNote(QObject *parent = nullptr);

    QString *nameVoiceNote;                  // Строка для хранения имени голосовой заметки
    QFile audioFile;                         // Для работы с аудио файлами

private:

    QAudioInput *audioInput;                      // Создание объекта для потока записи с аудио
    QAudioFormat audioForm;                       // Создание объекта для установок форматов для аудио
    QAudioDevice audioDeviceInfo;                 // Создание объекта для получение инофрмации об устройстве записи

private slots:

    void recorderStart();                    // Слот для запуска записи
    void recorderStop();                     // Слот для окончания записи
    void handleStateChanged(QSystemTrayIcon & trayicon);               // Слот для информирвоания о состоянии записи
    void generateNameForVoiceNote();         // Слот для генерации имени для голосовой заметки (в зависимости от текущего времени и даты)
    void writeHeader();                      // Запись заголовка в аудио-файл

public slots:

    void createVoiceNote(QSystemTrayIcon & trayicon);                  // Слот для создания голосовой заметки
    void showVoiceNote(const QModelIndex & index, NoteModel & notemodel, QSortFilterProxyModel & sortmodel, QString & noteType);                     // Слот для просмотра/воспроизведения заметки

};

#endif // NOTESSAVOICENOTE_H
