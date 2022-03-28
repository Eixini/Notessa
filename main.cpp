#include "notessa.h"

#include <QApplication>
#include <QIcon>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    notessa window;

    window.setWindowTitle("Notessa");
    window.setWindowIcon(QIcon(":/notessa_resources/icon/notessa_logo.png"));
    window.show();

    return app.exec();
}
