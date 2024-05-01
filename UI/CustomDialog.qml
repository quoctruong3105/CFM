import QtQuick 2.15
import QtQuick.Controls 2.15
//

Item {
    width: parent.width
    height: parent.height

    property alias writeDataDialog: writeDataDialog
    property alias genKeyDialog: genKeyDialog

    function openDialogAtCenter(mode, dialogName) {
        writeDataDialog.mode = mode
        dialogName.x = (mainContainer.width - dialogName.width + buttonBar.width * 2) / 2
        dialogName.y = (mainContainer.height - dialogName.height) / 2
        dialogName.open()
    }

    Dialog {
        id: writeDataDialog
        title: "Cập nhật dữ liệu " + ((mode == "db") ? "Database" : "Google Sheet")
        width: parent.width / 2
        height: usernameInput.height * 7
        modal: true
        standardButtons: Dialog.Ok | Dialog.Cancel

        property string mode: ""

        Text {
            id: title
            text: qsTr("Đăng nhập database")
            anchors.top: parent.top
            font.pointSize: height / 1.2
            anchors.horizontalCenter: parent.horizontalCenter
        }
        TextField {
            id: usernameInput
            placeholderText: "username"
            font.pointSize: height / 2
            height: parent.width / 10
            width: parent.width / 1.2
            anchors {
                horizontalCenter: parent.horizontalCenter
                top: title.bottom
                topMargin: width / 20
            }
        }
        TextField {
            id: passwordInput
            placeholderText: "password"
            font.pointSize: height / 2
            height: usernameInput.height
            width: parent.width / 1.2
            anchors {
                horizontalCenter: parent.horizontalCenter
                top: usernameInput.bottom
                topMargin: width / 30
            }
            echoMode: TextField.Password
        }

        onAccepted: {
            var user = usernameInput.text
            var pass = passwordInput.text
            print(noteArea.text)
            if(user === "truong" && pass === "truong") {
                var args = [ user, pass, mode, noteArea.text ]
                for(var i = 0; i < checkList.length; ++i) {
                    if(checkList[i].isChecked) {
                        console.log(tableList[i])
                        args.push(tableList[i])
                    }
                }
                core.workerCtrl.startThread()
                core.workerCtrl.startWork(args)
                indicator.indicatorTxt.visible = true
                indicator.bsIndicator.running = true
            }
            usernameInput.text = ""
            passwordInput.text = ""
            mode = ""
        }

        onRejected: {
        }
    }

    Dialog {
        id: genKeyDialog
        title: "Cập nhật dữ liệu " + ((mode == "db") ? "Database" : "Google Sheet")
        width: parent.width / 2
        height: usernameInput.height * 9.5
        modal: true
        standardButtons: Dialog.Ok | Dialog.Cancel

        property string mode: ""

        Text {
            id: title1
            text: qsTr("Đăng nhập database")
            anchors.top: parent.top
            font.pointSize: height / 1.2
            anchors.horizontalCenter: parent.horizontalCenter
        }
        TextField {
            id: usernameInput1
            placeholderText: "username"
            font.pointSize: height / 2
            height: usernameInput.height
            width: parent.width / 1.2
            anchors {
                horizontalCenter: parent.horizontalCenter
                top: title1.bottom
                topMargin: width / 20
            }
        }
        TextField {
            id: passwordInput1
            placeholderText: "password"
            font.pointSize: height / 2
            height: usernameInput.height
            width: parent.width / 1.2
            anchors {
                horizontalCenter: parent.horizontalCenter
                top: usernameInput1.bottom
                topMargin: width / 30
            }
            echoMode: TextField.Password
        }
        TextField {
            id: macId
            placeholderText: "macID"
            font.pointSize: height / 2
            height: usernameInput.height
            width: parent.width / 1.2
            anchors {
                horizontalCenter: parent.horizontalCenter
                top: passwordInput1.bottom
                topMargin: width / 30
            }
            echoMode: TextField.Password
        }
        TextField {
            id: hostname
            placeholderText: "hostname"
            font.pointSize: height / 2
            height: usernameInput.height
            width: parent.width / 1.2
            anchors {
                horizontalCenter: parent.horizontalCenter
                top: macId.bottom
                topMargin: width / 30
            }
            echoMode: TextField.Password
        }
        onAccepted: {
        }

        onRejected: {
        }
    }
}
