import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: parent.width
    height: parent.height
    property alias text: textArea.text
    Rectangle {
        id: container
        width: parent.width
        height: parent.height
        color: "transparent"

        Rectangle {
            id: textContainer
            width: container.width
            height: parent.height
            color: "transparent"
            Rectangle {
                anchors.fill: parent
                anchors.horizontalCenter: parent.horizontalCenter
                color: "transparent"
                TextArea {
                    id: textArea
                    width: parent.width
                    height: parent.height
                    wrapMode: TextEdit.Wrap
                    font.pointSize: height / 12
                    placeholderText: "Ghi chú tại đây..."
                }
            }
        }
    }
}
