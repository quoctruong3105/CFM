#ifndef WORKERCONTROLLER_H
#define WORKERCONTROLLER_H

#include <QObject>
#include <QThread>
#include <QDebug>
#include "Include/Worker.h"

class WorkerController : public QObject
{
    Q_OBJECT
public:
    WorkerController(QObject *parent = nullptr);
    ~WorkerController();
public slots:
    void startThread();
    void sendResult(const bool& res);
private slots:
    void killThread();
signals:
    void startWork(QStringList);
    void getConfirmed(const bool &res);
private:
    Worker *worker;
    QThread workerThread;
};

#endif // WORKERCONTROLLER_H
