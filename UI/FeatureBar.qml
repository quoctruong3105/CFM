import QtQuick 2.15

Item {
    width: parent.width
    height: parent.height
    Rectangle {
        height: parent.height
        width: parent.width
        color: customColor.defaultColor
        FeatureButtonGroup {
            id: featureBtnGrp
            width: parent.width / 2
            height: parent.height
            anchors.left: parent.left
        }
        Rectangle {
            width: parent.width - featureBtnGrp.width
            height: parent.height
            color: "white"
            anchors.right: parent.right
        }
    }
}
