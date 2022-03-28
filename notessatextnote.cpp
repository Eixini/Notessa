#include "notessatextnote.h"
#include "notemodel.h"

NotessaTextNote::NotessaTextNote(QObject *parent) : QObject{parent}
{
    nameTextNote    = new QString("");                    // Строка для хранения имени текстовой заметки
}

void NotessaTextNote::createTextNote(NoteModel & notemodel,QSystemTrayIcon & trayicon)
{  // Слот для создания текстовой заметки

    /* -------------------------------------------- СОЗДАНИЕ ОБЪЕКТОВ ОКНА ТЕКСТОВЫХ ЗАМЕТОК ---------------------------------------- */
    QDialog *textNoteWindow = new QDialog();                // Создание диалогового окна

    textNoteWindow->setWindowTitle(tr("Create new Text note"));
    textNoteWindow->setWindowIcon(QIcon(":/morningstar_resources/icons/clipboard_icon.png"));

    QPushButton saveButtun(tr("Save"), textNoteWindow);                          // Кнопка для принятия установки изменения
    QPushButton cancelButton(tr("Cancel"), textNoteWindow);                      // Кнопка для отмены создания заметки

    QVBoxLayout textNoteVBoxLayout(textNoteWindow);                              // Компоновщик для размещения всех элементов данного окна
    QHBoxLayout textNoteLayoutButtons;                                           // Компоновщик для кнопок
    QFormLayout textTitleFormLayout;                                             // Компоновщик с текстовой меткой

    QLineEdit textNoteTitle(textNoteWindow);                                     // Поле ввода для названия текстовой заметки
    QTextEdit enterTextNote(textNoteWindow);                                     // Поле для воода текстовой заметки

    QRegularExpression regexp("([a-zA-Zа-яА-Я0-9-_]){255}");                               // Для ограничения по вводимым символам
    QRegularExpressionValidator REvalidator(regexp);

    /* :::::::::::::::::::::::::::::::::::::::::::::::::::::: НАСТРОЙКА ФУНКЦИОНАЛА ::::::::::::::::::::::::::::::::::::::::::::::::: */

    textNoteTitle.setPlaceholderText(tr("Допустимые символы: буквы (Lat, Cyr), цифры, тире, нижнее подчеркивание"));   // Установка текста заполнителя
    enterTextNote.setPlaceholderText(tr("Введите текст заметки..."));

    textNoteTitle.setValidator(&REvalidator);

    /* ++++++++++++++++++++++++++++++++++++++++++++++++++++++ ПОДКЛЮЧЕНИЕ К СИГНАЛАМ ++++++++++++++++++++++++++++++++++++++++++++++++ */
    connect(&cancelButton, &QPushButton::clicked, textNoteWindow, &QDialog::close);
    connect(&saveButtun, &QPushButton::clicked, textNoteWindow, [&]()
    {
      if(textNoteTitle.text() != "")
      {
          QString textNoteLoc = QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation) + "/MorningStar" + "/MorningStar_Reliza" + "/TextNote";

          if(!textFile.exists(textNoteLoc + "/" + textNoteTitle.text() + ".txt"))
                *nameTextNote = textNoteLoc + "/" + textNoteTitle.text() + ".txt";      // Установка названия для файла из поля для ввод
          else
          {
              trayicon.showMessage(tr("Text note"), tr("A file with the same name already exists."));
              generateNameForTextNote();
          }

      }
      else
          generateNameForTextNote();

      textFile.setFileName(*nameTextNote);                                        // Создание текстового файла
      textFile.open(QIODevice::WriteOnly);                                        // Открытие файла в режиме только для запси

      textFile.write(enterTextNote.toPlainText().toUtf8());                       // Запись в файл содержимого поле TextEdit
      notemodel.appendData(textFile);                                            // Сообщить моделе, что добавился новый текствоый файл

      textFile.close();                                                           // После завершения работы, сохранить данные и закрыть файл
      trayicon.setVisible(true);
      trayicon.showMessage("Text Note", "The text note has been created.");      // Вывод информации о создании заметки
    } );
    connect(&saveButtun, &QPushButton::clicked, textNoteWindow, &QDialog::close);   // После сохранения данных - вернуться в меню заметок

    /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ УПРАВЛЕНИЕ КОМПОНОВКОЙ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
    textTitleFormLayout.addRow(tr("Title: "), &textNoteTitle);

    textNoteLayoutButtons.addStretch(1);
    textNoteLayoutButtons.addWidget(&saveButtun);
    textNoteLayoutButtons.addWidget(&cancelButton);

    textNoteVBoxLayout.addLayout(&textTitleFormLayout);
    textNoteVBoxLayout.addWidget(&enterTextNote);
    textNoteVBoxLayout.addLayout(&textNoteLayoutButtons);

    textNoteWindow->setLayout(&textNoteVBoxLayout);                              // Установка компоновщика в качестве основного

    textNoteWindow->exec();
}

void NotessaTextNote::showTextNote(const QModelIndex & index, NoteModel & notemodel, QSortFilterProxyModel & sortmodel, QString & noteType)
{
    /* ++++++++++++++++++++++++++++++++++++++++++++++++++++++ ИНИЦИАЛИЗАЦИЯ ОБЪЕКТОВ ++++++++++++++++++++++++++++++++++++++++++++++++ */
    QDialog *showTextNoteWin = new QDialog();

    QSystemTrayIcon *trayiconShowTextNote = new QSystemTrayIcon(QIcon(":/morningstar_resources/icons/clipboard_icon.png"), showTextNoteWin);
    QVBoxLayout *textNoteVLayout = new QVBoxLayout(showTextNoteWin);
    QHBoxLayout *buttonHLayout = new QHBoxLayout();

    QPushButton editNoteButton;
    QPushButton saveNoteButton;
    QPushButton returnButton;

    QTextEdit showTextNote;

    // Получение полного имени файла (путь + имя файла с суффиксом), в зависимости от выбранного элемента в списке заметок
    QString textNoteFilePath = QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation)
                                + "/Notessa" + "/TextNote" + "/"
                                + notemodel.noteName(sortmodel.mapToSource(index)) + '.' + noteType;
    /* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ НАСТРОЙКА ОБЪЕКТОВ  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

    showTextNoteWin->setWindowTitle(tr("Show text note"));
    showTextNoteWin->setWindowIcon(QIcon(":/morningstar_resources/icons/clipboard_icon.png"));

    showTextNote.setReadOnly(true);

    editNoteButton.setText(tr("Edit note"));
    editNoteButton.setIcon(QIcon(":/morningstar_resources/icons/keyboard_icon.png"));
    saveNoteButton.setText(tr("Save"));
    saveNoteButton.setIcon(QIcon(":/morningstar_resources/icons/save_icon.png"));
    returnButton.setText(tr("Return"));
    returnButton.setIcon(QIcon(":/morningstar_resources/icons/file_icon.png"));

    /* ::::::::::::::::::::::::::::::::::::::::::::::::::::::  РАБОТА С ФУНКЦИОНАЛОМ  ::::::::::::::::::::::::::::::::::::::::::::::: */

    QFile textNoteFile(textNoteFilePath);
    textNoteFile.open(QIODevice::ReadOnly);
    if(textNoteFile.isOpen())
    {
        showTextNote.setText(textNoteFile.readAll());
        textNoteFile.close();
    }
    else
    {
        trayiconShowTextNote->setVisible(true);
        trayiconShowTextNote->showMessage(tr("Text note"),tr("File read error"));
    }
    trayiconShowTextNote->setVisible(false);

    /* ====================================================== ПОДКЛЮЧЕНИЕ К СИГНАЛАМ ================================================ */
    connect(&editNoteButton, &QPushButton::clicked, showTextNoteWin, [&]()
    {
        textNoteFile.open(QIODevice::ReadWrite);
        if(textNoteFile.isOpen())
        {
            showTextNote.setText(textNoteFile.readAll());
            showTextNote.setReadOnly(false);
            connect(&saveNoteButton, &QPushButton::clicked, showTextNoteWin, [&]()
            {
                textNoteFile.open(QIODevice::WriteOnly);
                textNoteFile.write(showTextNote.toPlainText().toUtf8());
                textNoteFile.close();
                showTextNote.setReadOnly(true);
            }
                    );
        }
        else
        {
            trayiconShowTextNote->setVisible(true);
            trayiconShowTextNote->showMessage(tr("Text note"),tr("File edit error!"));
        }
        textNoteFile.close();
    }
            );
    connect(&returnButton, &QPushButton::clicked, showTextNoteWin, &QDialog::accept);
    /* ...................................................... УПРАВЛЕНИЕ КОМПОНОВКОЙ ................................................ */

    buttonHLayout->addWidget(&editNoteButton);
    buttonHLayout->addWidget(&saveNoteButton);
    buttonHLayout->addWidget(&returnButton);

    textNoteVLayout->addWidget(&showTextNote);
    textNoteVLayout->addLayout(buttonHLayout);

    showTextNoteWin->exec();
}

void NotessaTextNote::generateNameForTextNote()
{ // Слот для генерации имени для текстовой заметки (в зависимости от текущего времени и даты), если не было введено название
    QDate date = QDate::currentDate();
    QTime time = QTime::currentTime();

    QString textNoteLoc = QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation) + "/Notessa" + "/TextNote";

    // Установка название файла исходя из вида заметки (текстовая) и момента создания (текущая дата + текущее время)
    *nameTextNote = textNoteLoc + "/morningstar-textnote_" + QString::number(date.year())     + "-"
                                                           + QString::number(date.month())    + "-"
                                                           + QString::number(date.day())      + "_"
                                                           + QString::number(time.hour())     + "-"
                                                           + QString::number(time.minute())   + "-"
                                                           + QString::number(time.second())   + ".txt";
}

