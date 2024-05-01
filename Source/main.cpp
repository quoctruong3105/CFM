#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlContext>
#include <QIcon>

#include "Include/Worker.h"
#include "Include/WorkerController.h"
#include "Include/PreCondition.h"

int main(int argc, char *argv[])
{
#if QT_VERSION < QT_VERSION_CHECK(6, 0, 0)
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
#endif
    QGuiApplication app(argc, argv);
    QQmlApplicationEngine engine;

    qmlRegisterType<Worker>("TT.Worker.Module", 1, 0, "Worker");
    qmlRegisterType<WorkerController>("TT.WorkerController.Module", 1, 0, "WorkerController");
    qmlRegisterType<PreCondition>("TT.PreCondition.Module", 1, 0, "PreCondition");

    const QUrl url(QStringLiteral("qrc:/UI/Main.qml"));
    QObject::connect(&engine, &QQmlApplicationEngine::objectCreated,
        &app, [url](QObject *obj, const QUrl &objUrl) {
            if (!obj && url == objUrl)
                QCoreApplication::exit(-1);
        }, Qt::QueuedConnection);
    engine.load(url);
    QIcon icon(":/img/app_icon.ico");
    app.setWindowIcon(icon);
    return app.exec();
}
