#ifndef WORKER_H
#define WORKER_H

#include <QObject>
#include <QEventLoop>
#include <QProcess>
#include <QDir>

class Worker : public QObject
{
    Q_OBJECT
public:
    Worker(QObject *parent = nullptr);

public slots:
    void doWork(const QStringList &strList);
    void setup(const bool &state);
signals:
    void resultReady(bool);
private:
};

#endif // WORKER_H
