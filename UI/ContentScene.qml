import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    property alias stackView: stackView
    property var listPage: [ basicInfo, inventory, bill, discount ]

    StackView {
        id: stackView
        objectName: stackView
        anchors.fill: parent
        width: parent.width
        height: parent.height
        anchors.left: parent.left
        initialItem: basicInfo
        clip: true

        Page {
            id: basicInfo
            InfoContent {

            }
        }

        Page {
            id: inventory
            InventoryContent {

            }
        }

        Page {
            id: bill
            BillContent {

            }
        }

        Page {
            id: discount
            DiscountContent {

            }
        }
    }
}
