QT += quick
QT += sql
QT += network


# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

HEADERS += \
    Include/Worker.h \
    Include/WorkerController.h \
    Include/PreCondition.h \

SOURCES += \
    Source/main.cpp \
    Source/Worker.cpp \
    Source/WorkerController.cpp \
    Source/PreCondition.cpp \

RESOURCES += \
    qml.qrc \
    img.qrc \

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Additional import path used to resolve QML modules just for Qt Quick Designer
QML_DESIGNER_IMPORT_PATH =

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

DISTFILES += \
#    docs/ggsheet_creds.json \
#    docs/token.json \
#    tool/DataInterface.py \
#    tool/GetMachineInfo.py \
#    tool/SendMail.py \
#    tool/constants.py \
#    tool/GenLicenseKey.py \
#    GetMachineInfo.py \
#    SendMail.py \
