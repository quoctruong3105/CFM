import QtQuick 2.15
import TT.Worker.Module 1.0
import TT.WorkerController.Module 1.0
import TT.PreCondition.Module 1.0

Item {
    property alias workerCtrl: workerCtrl
    property alias preCondition: preCondition
    property alias worker: worker

    PreCondition {
        id: preCondition
    }
    Worker {
        id: worker
    }
    WorkerController {
        id: workerCtrl
        onGetConfirmed: {
            var confirmation = res
            if(confirmation) {
                // console.log(confirmation)
                for(var i = 0; i < checkList.length; ++i) {
                    if(checkList[i].isChecked) {
                        checkList[i].isChecked = !checkList[i].isChecked
                    }
                }
                indicator.indicateText = "Cập nhật thành công!"
                noteArea.text = ""
            } else {
                indicator.indicateText = "Cập nhật thất bại!"
            }
            indicator.bsIndicator.running = false
            indicator.timer.running = true
        }
    }
}
