#ifndef NOTESSA_H
#define NOTESSA_H

#include <QDialog>
#include <QFile>
#include <QHeaderView>
#include <QTableWidgetItem>
#include <QTableView>
#include <QHBoxLayout>
#include <QVBoxLayout>
#include <QFormLayout>
#include <QPushButton>
#include <QIcon>
#include <QLineEdit>
#include <QTextEdit>
#include <QSystemTrayIcon>
#include <QString>
#include <QStandardPaths>
#include <QDir>
#include <QModelIndex>
#include <QTime>
#include <QTimer>
#include <QDate>
#include <QDebug>
#include <QMessageBox>
#include <QRegularExpression>
#include <QRegularExpression>
#include <QMediaPlayer>
#include <QUrl>
#include <QSlider>
#include <QLabel>
#include <QComboBox>
#include <QPixmap>
#include <QModelIndexList>
#include <QSortFilterProxyModel>
#include <QItemSelectionModel>

#include "notemodel.h"
#include "notetypedelegate.h"
#include "notessatextnote.h"
#include "notessavoicenote.h"
#include "notessavideonote.h"

class notessa : public QDialog
{
    Q_OBJECT
public:
    explicit notessa(QDialog *parent = nullptr);
    ~notessa();

    NoteModel *notemodel;                    // Создание объекта модели для предоставления способа работы с данными
    QSortFilterProxyModel *sortmodel;         // Создание объекта для сортировки заметок
    QSystemTrayIcon *trayicon;               // Создание объекта для иконки панель задачь и показе информации

public slots:

    void noteRead();                         // Слот для проверки на существование директории и заметок в ней

private:

    QTableView *tableview;                   // Создание объекта для хранения виджетов (текстовых и голосовых заметок)

    QPushButton *toMainMenuButton;           // Кнопка для возврата в главное меню
    QPushButton *createTextNoteButton;       // Кнопка для открытия окна, где создается новая текстовая заметка
    QPushButton *createVoiceNoteButton;      // Кнопка для открытия окна, где создается новая голосовая заметка
    QPushButton *deleteNoteButton;           // Кнопка для удаления заметки

    QHBoxLayout *buttonsLayout;
    QVBoxLayout *headLayout;

    QComboBox *noteTypeComboBox;                      // Для выбора фильтра отображения типа заметки

private slots:

    void deleteNote();                       // Слот для удаления заметки
    void showNote(const QModelIndex & index);                     // Слот для просмотра/воспроизведения заметки

};

#endif // NOTESSA_H
