#include <Include/Worker.h>

Worker::Worker(QObject *parent) : QObject{parent}
{

}

void Worker::doWork(const QStringList &strList)
{
    qDebug() << strList;
//    QString programPath = QDir::currentPath() + "/tool/DataInterface.py";
//    if (!QFile::exists(programPath)) {
//        qDebug() << "Error: Python script not found at" << programPath;
//        emit resultReady(false); // Signal error
//        return;
//    }
    QString programPath = "E:/CFM/tool/DataInterface.py";
    QProcess UpdateCoffeeData;
    UpdateCoffeeData.setProgram("python");
    QStringList arguments;
    arguments << programPath << strList;
    UpdateCoffeeData.setArguments(arguments);
    UpdateCoffeeData.start();

    UpdateCoffeeData.waitForFinished(-1);

    qDebug() << "Acess Paycheck sheet exit with: " << UpdateCoffeeData.exitCode();

    emit resultReady(((UpdateCoffeeData).exitCode() == 0) ? true : false);
}

void Worker::setup(const bool &state)
{
    qDebug() << QString::number(state);
//    QString programPath = QDir::currentPath() + "/tool/ToolManager.py";
//    if (!QFile::exists(programPath)) {
//        qDebug() << "Error: Python script not found at" << programPath;
//        emit resultReady(false); // Signal error
//        return;
//    }
    QString programPath = "E:/CFM/tool/ToolManager.py";
    QProcess toolSetup;
    toolSetup.setProgram("python");
    QStringList arguments;
    arguments << programPath << QString::number(state);
    toolSetup.setArguments(arguments);
    toolSetup.start();
    toolSetup.waitForFinished(-1);
}

