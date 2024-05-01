#include "Include/Precondition.h"
#include <QDebug>

PreCondition::PreCondition(QObject *parent) : QObject{parent}
{
    isValidLicense = checkLicenseState();
    qDebug() << isValidLicense;
}

bool PreCondition::getLicenseState()
{
    return isValidLicense;
}

QList<QString> PreCondition::getLicenseKeys()
{
    QList<QString> keyList;
    QSqlDatabase *db = new QSqlDatabase(QSqlDatabase::addDatabase("QPSQL"));
    db->setHostName("localhost");
    //    db->setHostName("hicoffee3105.hopto.org");
    db->setPort(5432);
    db->setDatabaseName("cf_prj_test");
    db->setUserName("truong");
    db->setPassword("truong");
    if (!db->open()) {
        QSqlError error = db->lastError();
        qDebug() << "Error connecting to PostgreSQL:";
        qDebug() << "Connection Name:" << db->connectionName();
        qDebug() << "Connection Options:" << db->connectOptions();
        return keyList;
    } else {
        qDebug() << "Connected to PostgreSQL!";
    }

    QSqlQuery query;
    query.exec(QString("SELECT * FROM license_keys"));

    while (query.next()) {
        keyList.append(query.value(0).toString());
    }

    if(db) {
        db->close();
        delete db;
        db = nullptr;
    }

    return keyList;
}

QString PreCondition::getMacAddress() {
    QList<QNetworkInterface> interfaces = QNetworkInterface::allInterfaces();
    foreach (const QNetworkInterface &interface, interfaces) {
        // Skip loopback and virtual interfaces
        if (interface.flags().testFlag(QNetworkInterface::IsLoopBack)) {
            continue;
        }

        // Return the MAC address of the first non-empty MAC address
        QString macAddress = interface.hardwareAddress();
        if (!macAddress.isEmpty()) {
            return macAddress;
        }
    }

    return QString();
}

QString PreCondition::getMachineProductId()
{
    QString productID;
    if (QSysInfo::productType() == "windows") {
        QSettings registrySettings("HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion",
                                   QSettings::NativeFormat);

        productID = registrySettings.value("ProductId").toString();
    } else {
        productID = "Not a Windows system";
    }
    return productID;
}

QString PreCondition::genLocalKey(const QString &macId, const QString &machineProductId)
{
    QString combinedData = productName + ":" + macId + ":" + machineProductId;

    // Hash the combined data
    QByteArray hash = QCryptographicHash::hash(combinedData.toLatin1(), QCryptographicHash::Sha256);

    // Base64 encode the hashed data
    QString licenseKey = QString(hash.toBase64());

    return licenseKey;
}

bool PreCondition::checkLicenseState()
{
    bool isValid = false;
    QList<QString> availableKeys = getLicenseKeys();

    if(availableKeys.isEmpty()) {
        qDebug() << "No available key";
        return isValid;
    }

    QString myKey = genLocalKey(getMacAddress(), getMachineProductId());
    foreach (auto const& key, availableKeys) {
        if(myKey == key) {
            isValid = true;
        }
    }
    return isValid;
}
