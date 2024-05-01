import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: parent.width
    height: parent.height

    property string indicateText: ""
    property alias bsIndicator: bsIndicator
    property alias indicatorTxt: indicatorTxt
    property alias timer: timer

    Timer {
        id: timer
        interval: 10000
        repeat: false
        running: false
        onTriggered: {
            indicateText = ""
        }
    }

    Rectangle {
        id: container
        width: parent.width
        height: parent.height
        color: "transparent"
        BusyIndicator {
            id: bsIndicator
            height: parent.height / 1.5
            width: height
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: parent.right
            anchors.rightMargin: width / 5
            running: false
        }
        Text {
            id: indicatorTxt
            text: (bsIndicator.running) ? "Đang thực thi " : indicateText
            color: {
                if(text === "Đang thực thi ") {
                   "black"
                } else if(text === "Cập nhật thành công!") {
                   "green"
                } else {
                   "red"
                }
            }
            anchors.verticalCenter: parent.verticalCenter
            anchors.right: (text === "Đang thực thi ") ? bsIndicator.left : bsIndicator.right
            anchors.rightMargin: (text === "Đang thực thi ") ? 0 : bsIndicator.anchors.rightMargin
            font.pointSize: height / 1.5
        }
    }
}
