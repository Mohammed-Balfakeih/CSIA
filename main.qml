import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 1400
    height: 700
    title: "StuDoList"
    
    Drawer {
        id: drawer
        dragMargin: 1
        width: 0.66 * window.width
        height: window.height
    }

    Label {
        id: content

        text: "Hello World"
        font.pixelSize: 96
        anchors.fill: parent
        verticalAlignment: Label.AlignVCenter
        horizontalAlignment: Label.AlignHCenter

        transform: Translate {
            x: drawer.position * content.width * 0.33
        }
    }

}