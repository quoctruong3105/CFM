import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: parent.width
    height: parent.height
    property bool enabled
    Button {
        id:dbBtn
        width: parent.width
        height: width
        enabled: parent.enabled
        Text {
            text: "Database"
            font.pointSize: parent.height / 6
            anchors.centerIn: parent
        }
        onClicked: {
            dialog.openDialogAtCenter("db", dialog.writeDataDialog)
        }
    }
    Button {
        id: sheetBtn
        width: parent.width
        height: width
        enabled: parent.enabled
        Text {
            text: "Google \nSheet"
            font.pointSize: parent.height / 6
            anchors.centerIn: parent
            horizontalAlignment: Text.AlignHCenter
        }
        anchors.top: dbBtn.bottom
        onClicked: {
            dialog.openDialogAtCenter("sh", dialog.writeDataDialog)
        }
    }
    Button {
        id: genKey
        width: parent.width
        height: width
        enabled: parent.enabled
        anchors.top: sheetBtn.bottom
        Text {
            text: "Gen \nLicense"
            font.pointSize: parent.height / 6
            anchors.centerIn: parent
            horizontalAlignment: Text.AlignHCenter
        }
        onClicked: {
            //dialog.openDialogAtCenter("sh", dialog.genKeyDialog)
        }
    }
    Button {
        id: billGet
        width: parent.width
        height: width
        enabled: parent.enabled
        anchors.top: genKey.bottom
        Text {
            text: "Get \nRevenue"
            font.pointSize: parent.height / 6
            anchors.centerIn: parent
            horizontalAlignment: Text.AlignHCenter
        }
        onClicked: {
            //dialog.openDialogAtCenter("sh", dialog.genKeyDialog)
        }
    }
}
