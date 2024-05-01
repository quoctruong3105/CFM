import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15

Item {
    width: parent.width
    height: parent.height
    property string title: ""
    property bool isChecked: false
    Rectangle {
        id: container
        width: parent.width
        height: parent.height
        color: "lightgrey"
        Rectangle {
            id: checkBox
            height: parent.height
            width: height
            antialiasing: true
            Text {
                id: tickTxt
                text: qsTr("✔")
                color: "green"
                font.pointSize: height
                visible: isChecked
                anchors.centerIn: parent
            }
            MouseArea {
                anchors.fill: parent
                onClicked: {
                    isChecked = !isChecked
                }
            }
        }
        Rectangle {
            id: titleContainer
            width: parent.width - checkBox.width
            height: parent.height
            color: "lightgrey"
            anchors.left: checkBox.right
            anchors.leftMargin: checkBox.width / 5
            Text {
                id: titleTxt
                text: title
                font.pointSize: titleContainer.height / 2
            }
        }
    }
}
