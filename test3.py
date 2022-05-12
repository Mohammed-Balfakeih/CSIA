from PyQt5.QtWidgets import *
import datetime
import sys
from StuDoList import Task
#try listview, otherwise we might just have to revamp the entire thing in some way
#maybe since widgets can only have 1 parent, we store them all in a vbox or smth and only copy and change that around? code might get messy tho

class Window(QMainWindow):
    def init(self):
        #super().__init__()

        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        testtask = Task("Task 1", 1, 2021, 9, 3, "test", False, None, None)

        layout1 = QVBoxLayout()

        layout1.addWidget(testtask)

        wid = QWidget(self)
        self.setCentralWidget(wid)
        wid.setLayout(layout1)

        listView = QListView()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.init()
    ex.show()
    sys.exit(app.exec_())