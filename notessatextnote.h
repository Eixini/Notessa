#ifndef NOTESSATEXTNOTE_H
#define NOTESSATEXTNOTE_H

#include "notessa.h"
#include "notemodel.h"

#include <QObject>
#include <QString>
#include <QSortFilterProxyModel>

class NotessaTextNote : public QObject
{
    Q_OBJECT
public:
    explicit NotessaTextNote(QObject *parent = nullptr);

    QString *nameTextNote;                   // Строка для хранения имени текстовой заметки
    QFile textFile;                          // Для работы с текстовыми файлами

private:

private slots:

    void generateNameForTextNote();          // Слот для генерации имени для текстовой заметки (в зависимости от текущего времени и даты), если не было введено название

public slots:

    void createTextNote(NoteModel & notemodel, QSystemTrayIcon & trayicon);                   // Слот для создания текстовой заметки
    void showTextNote(const QModelIndex & index, NoteModel & notemodel, QSortFilterProxyModel & sortmodel, QString & noteType);                     // Слот для просмотра/воспроизведения заметки

};

#endif // NOTESSATEXTNOTE_H
