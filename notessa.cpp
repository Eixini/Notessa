#include "notessa.h"

/*      ЧТО НУЖНО ИСПРАВИТЬ:

  - Добавить при создании заметки с одинаковым полным именем (имя файла + суффикс) - вывод сообщения об ошибке + убрать вылет из редактора создания;
    ! Временно сделал так, что при попытке создания файла с уже существующим именем - для нового файла будет установлено дефолтное имя.


  - При прослушиваниии голосовой заметки, если нажать на крестик (закрытие окна) - происходит падение приложения (в Windows OS);

*/

notessa::notessa(QDialog *parent) : QDialog(parent)
{
    // ::::::::::::::::::::::::::::::::::::::::: ИНИЦИАЛИЗАЦИЯ ОБЪЕКТОВ :::::::::::::::::::::::::::::::::::::::::
    {
    createTextNoteButton    = new QPushButton(tr("Add new Text note"));          // Кнопка для создания текстовой заметки
    createVoiceNoteButton   = new QPushButton(tr("Add new Voice Note"));         // Кнопка для создания голосовой заметки
    deleteNoteButton        = new QPushButton(tr("Delete note"));                // Кнопка для удаления заметки
    toMainMenuButton        = new QPushButton(tr("Main Menu"));                  // Кнопка для возврата в главное меню

    trayicon        = new QSystemTrayIcon(QIcon(":/morningstar_resources/icons/clipboard_icon.png")); // Создание объекта для уведомлений из панели задач

    buttonsLayout = new QHBoxLayout();                    // Горизонтальный компоновщик, в котором будут объекты (включая другие компоновщики)
    headLayout    = new QVBoxLayout();                // Вертикальный компоновщик для кнопок

    tableview        = new QTableView();              // Инициализация представления
    notemodel        = new NoteModel();               // Инициализация модели

    sortmodel        = new QSortFilterProxyModel();

    noteTypeComboBox = new QComboBox();

    }
    // +++++++++++++++++++++++++++++++++++++++++++ НАСТРОЙКА ОБЪЕКТОВ +++++++++++++++++++++++++++++++++++++++++++
    {
        createTextNoteButton->setIcon(QIcon(":/morningstar_resources/icons/clipboard_icon.png"));
        createVoiceNoteButton->setIcon(QIcon(":/morningstar_resources/icons/microphone_icon.png"));
        deleteNoteButton->setIcon(QIcon(":/morningstar_resources/icons/x_icon.png"));
        toMainMenuButton->setIcon(QIcon(":/morningstar_resources/icons/ms_icon.png"));

        noteTypeComboBox->addItem(tr("Show all note"));
        noteTypeComboBox->addItem(tr("Show only text note"));
        noteTypeComboBox->addItem(tr("Show only voice note"));

        sortmodel->setDynamicSortFilter(false);                                   // Отключение динамической сортировки
        sortmodel->setSourceModel(notemodel);

        tableview->setModel(sortmodel);
        tableview->setCornerButtonEnabled(false);                                 // Выключить кнопку для выделения всех элементов
        tableview->horizontalHeader()->setStretchLastSection(true);               // Убрать белое пространство после последнего столбца
        tableview->setShowGrid(false);                                            // Скрыть показ сетки
        tableview->verticalHeader()->hide();
        tableview->setColumnWidth(0,70);
        tableview->horizontalHeader()->setSectionResizeMode(1, QHeaderView::Stretch);
        tableview->resizeColumnToContents(2);
        tableview->setSelectionMode(QAbstractItemView::SingleSelection);
        tableview->setSelectionBehavior(QAbstractItemView::SelectRows);           // Установка поведения - при выборе ячейки, выбирается вся строка
        tableview->setSortingEnabled(true);
        tableview->setItemDelegateForColumn(0, new NoteTypeDelegate(tableview));

    }
    // ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ СОЗДАНИЕ СОЕДИНЕНИЙ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    {
    connect(createTextNoteButton, &QPushButton::clicked, &NotessaTextNote::createTextNote);   // Вызов окна для создания текстовой заметки
    connect(createVoiceNoteButton, &QPushButton::clicked, &NotessaVoiceNote::createVoiceNote); // Вызов окна для создания голосовой заметки
    connect(deleteNoteButton, &QPushButton::clicked, this, &notessa::deleteNote);           // Удаление заметки
    connect(tableview, &QTableView::doubleClicked, this, &notessa::showNote);
    connect(noteTypeComboBox, QOverload<int>::of(&QComboBox::currentIndexChanged),
        [=](int index)
        {
        if(index == 1)
        {
            sortmodel->setFilterRegularExpression(QRegularExpression("txt"));
            sortmodel->setFilterKeyColumn(0);
        }
        else if(index == 2)
        {
            sortmodel->setFilterRegularExpression(QRegularExpression("wav"));
            sortmodel->setFilterKeyColumn(0);
        }
        else
        {
            sortmodel->setFilterRegularExpression(QRegularExpression("([a-z]){3}"));
            sortmodel->setFilterKeyColumn(0);
        }
        }
             );
    }
    // ***************************************** УПРАВЛЕНИЕ КОМПОНОВКОЙ *****************************************
    {
    buttonsLayout->addWidget(createTextNoteButton);
    buttonsLayout->addWidget(createVoiceNoteButton);
    buttonsLayout->addWidget(deleteNoteButton);
    buttonsLayout->addWidget(noteTypeComboBox);
    buttonsLayout->addWidget(toMainMenuButton);

    headLayout->addLayout(buttonsLayout);
    headLayout->addWidget(tableview);

    }
}

void notessa::showNote(const QModelIndex & index)
{   // Слот для просмотра заметки

    QString noteType = notemodel->noteType(sortmodel->mapToSource(index));

    if("txt" == noteType)
    {       /* Если тип заметки - текстовая, то создается соотвествующее окно */
        NotessaTextNote textnote;
        textnote.showTextNote(index, *notemodel, *sortmodel, noteType);
    }
    if("wav" == noteType)
    {       /* Если тип заметки - голосовая, то создается соотвествующее окно */
        NotessaVoiceNote voicenote;
        voicenote.showVoiceNote(index, *notemodel, *sortmodel, noteType);

    }

}

void notessa::deleteNote()
{   // Слот для удаления заметки

    QModelIndex curIndex = sortmodel->mapToSource(tableview->selectionModel()->currentIndex());
    notemodel->removeData(curIndex.row());

}

void notessa::noteRead()
{   // Слот для проверки на существование директории и заметок в ней
    trayicon->setVisible(true);
    trayicon->showMessage(tr("Note"), tr("Checking files ..."));

    QString loc = QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation);  // "~/.config/<APPNAME>", "C:/Users/<USER>/AppData/Local/<APPNAME>"

    QDir morningstar_headDir(loc + "/Notessa");
    QDir morningstar_currentVersionDir(loc + "/Notessa");
    QDir morningstar_textnoteDir(loc + "/Notessa" + "/TextNote");
    QDir morningstar_voicenoteDir(loc + "/Notessa" + "/VoiceNote");

    if(!morningstar_headDir.exists())                    // Проверка на наличие главной директории приложения
    {
        trayicon->setVisible(true);
        trayicon->showMessage(tr("Note"),tr("The main application directory was not found.") + '\n' + tr(" A new one will be created."));
        morningstar_headDir.setPath(QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation));
        morningstar_headDir.mkdir("Notessa");
    }
    if(!morningstar_currentVersionDir.exists())         // Проверка на наличие директори текущей версии приложения
    {
        trayicon->setVisible(true);
        trayicon->showMessage(tr("Note"), tr("The directory for the current version of the application was not found.") + '\n' + tr(" A new one will be created."));
        morningstar_currentVersionDir.setPath(QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation) + "/Notessa");
        morningstar_currentVersionDir.mkdir("MorningStar_Reliza");
    }
    if(!morningstar_textnoteDir.exists())
    {
        trayicon->setVisible(true);
        trayicon->showMessage(tr("Note"), tr("The directory for text notes does not exist!") + '\n' + tr(" A new one will be created."));
        morningstar_textnoteDir.setPath(QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation) + "/Notessa");
        morningstar_textnoteDir.mkdir("TextNote");

    }
    if(!morningstar_voicenoteDir.exists())
    {
        trayicon->setVisible(true);
        trayicon->showMessage(tr("Note"), tr("The directory for voice memos does not exist!") + '\n' + tr(" A new one will be created."));
        morningstar_voicenoteDir.setPath(QStandardPaths::writableLocation(QStandardPaths::GenericConfigLocation) + "/Notessa");
        morningstar_voicenoteDir.mkdir("VoiceNote");
    }

}

notessa::~notessa() {}

