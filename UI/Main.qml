import QtQuick 2.7
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0

ApplicationWindow {
    id: root
    visible: true
    width: 640
    height: groupButton.width * 4
    maximumHeight: groupButton.width * 4
    maximumWidth: 640
    minimumHeight: maximumHeight
    minimumWidth: maximumWidth
    title: "SWFM"
    property bool isValidLicense: core.preCondition.getLicenseState()
    property var tableList: [ "drink", "cake" , "topping", "material", "bank", "info", "discount" ]
    property var checkList: [ drink, cake, topping, material, bank, info, discount ]

    Component.onCompleted: {
        // Tool set up
        core.worker.setup(1)
    }

    onClosing: {
        // Tool tear down
        core.worker.setup(0)
    }

    Core {
        id: core
    }

    CustomDialog {
        id: dialog
        width: mainContainer.width
        height: mainContainer.height
    }

    Rectangle {
        width: parent.width
        height: parent.height
        Text {
            id: warningTxt
            text: qsTr("            Thiết bị này chưa được cấp bản quyền!")
            anchors.centerIn: parent
            font.pointSize: parent.height / 20
            visible: !isValidLicense
        }
        Rectangle {
            id: mainContainer
            width: parent.width * 2.6 / 3
            height: parent.height
            anchors.right: parent.right
            color: "lightgrey"
            visible: isValidLicense
            Rectangle {
                id: checkBoxGroup
                width: parent.width / 1.2
                height: drinkContainer.height * 4 + toppingContainer.anchors.topMargin * 3
                anchors.horizontalCenter: parent.horizontalCenter
                anchors.top: parent.top
                anchors.topMargin: drinkContainer.height / 2
                color: "transparent"

                Rectangle {
                    id: drinkContainer
                    width: parent.width / 3
                    height: width / 6
                    CustomCheckBox {
                        id: drink
                        title: "Nước uống"
                    }
                }
                Rectangle {
                    id: cakeContainer
                    width: parent.width / 3
                    height: width / 6
                    anchors.left: drinkContainer.right
                    anchors.leftMargin: drinkContainer.width / 2
                    CustomCheckBox {
                        id: cake
                        title: "Bánh"
                    }
                }
                Rectangle {
                    id: toppingContainer
                    width: parent.width / 3
                    height: width / 6
                    anchors.left: drinkContainer.left
                    anchors.top: drinkContainer.bottom
                    anchors.topMargin: drinkContainer.height / 2
                    CustomCheckBox {
                        id: topping
                        title: "Topping"
                    }
                }
                Rectangle {
                    id: materialContainer
                    width: parent.width / 3
                    height: width / 6
                    anchors.left: cakeContainer.left
                    anchors.top: drinkContainer.bottom
                    anchors.topMargin: drinkContainer.height / 2
                    CustomCheckBox {
                        id: material
                        title: "Nguyên liệu"
                    }
                }
                Rectangle {
                    id: bankContainer
                    width: parent.width / 3
                    height: width / 6
                    anchors.left: toppingContainer.left
                    anchors.top: toppingContainer.bottom
                    anchors.topMargin: toppingContainer.height / 2
                    CustomCheckBox {
                        id: bank
                        title: "Ngân hàng"
                    }
                }
                Rectangle {
                    id: infoContainer
                    width: parent.width / 3
                    height: width / 6
                    anchors.left: materialContainer.left
                    anchors.top: materialContainer.bottom
                    anchors.topMargin: materialContainer.height / 2
                    CustomCheckBox {
                        id: info
                        title: "Thông tin chung"
                    }
                }
//                Rectangle {
//                    id: billContainer
//                    width: parent.width / 3
//                    height: width / 6
//                    anchors.left: bankContainer.left
//                    anchors.top: bankContainer.bottom
//                    anchors.topMargin: bankContainer.height / 2
//                    CustomCheckBox {
//                        id: bill
//                        title: "Hóa đơn"
//                    }
//                }
                Rectangle {
                    id: discountContainer
                    width: parent.width / 3
                    height: width / 6
                    anchors.left: bankContainer.left
                    anchors.top: bankContainer.bottom
                    anchors.topMargin: bankContainer.height / 2
                    CustomCheckBox {
                        id: discount
                        title: "Khuyến mãi"
                    }
                }
            }
            Rectangle {
                id: noteContainer
                color: "transparent"
                width: parent.width / 1.2
                height: checkBoxGroup.height / 1.1
                anchors.top: checkBoxGroup.bottom
                anchors.topMargin: drinkContainer.height / 1.5
                anchors.horizontalCenter: parent.horizontalCenter
                NoteArea {
                    id: noteArea
                    width: parent.width
                    height: parent.height
                }
            }

            Rectangle {
                id: indicatorContainer
                width: parent.width
                height: noteContainer.height / 3
                anchors.bottom: parent.bottom
                color: "transparent"
                Indicator {
                    id: indicator
                    width: parent.width
                    height: parent.height
                }
            }
        }
        Rectangle {
            id: buttonBar
            width: parent.width - mainContainer.width
            anchors.left: parent.left
            FeatureButtonGroup {
                id: groupButton
                width: parent.width
                height: parent.height
                enabled: isValidLicense
            }
        }
    }
}
