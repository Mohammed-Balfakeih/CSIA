from PyQt5.QtWidgets import *
import datetime
import sys
import task


class Task(QPushButton):
    def __init__(self,name,priority,year,month,day,description,completed,subtasks,uppertask):
        #super(QPushButton, self).__init__()
        self.name = name
        self.priority = priority
        self.date = datetime.date(year,month,day)
        self.description = description
        self.completed = completed
        self.subtasks = subtasks
        self.uppertask = uppertask

        upper = ""
        if self.uppertask != None:
            upper = self.uppertask.name

        if self.completed == False:
            completed = "incomplete"
        else:
            completed = "completed"

        label = self.name + " " + "Priority: " + str(self.priority) + " " + str(self.date) + " " + upper + " " + completed
        super(QPushButton, self).__init__(label)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('StuDoList')

        # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        # add all widgets
        self.btn_1 = QPushButton('By Date', self)
        self.btn_2 = QPushButton('By Priority', self)
        self.btn_3 = QPushButton('Projects', self)
        self.btn_4 = QPushButton('History', self)
        self.btn_5 = QPushButton('Help', self)

        self.btn_1.clicked.connect(self.button1)
        self.btn_2.clicked.connect(self.button2)
        self.btn_3.clicked.connect(self.button3)
        self.btn_4.clicked.connect(self.button4)
        self.btn_5.clicked.connect(self.button5)
        
        self.windowTest = QMainWindow()
        self.window1 = task.TaskWindow()
        self.window1.setupUi(self.windowTest)
        self.task = self.set_tasks()
        self.task.clicked.connect(self.go_to_task)


        # add tabs
        self.tab1 = self.ui1()
        self.tab2 = self.ui2()
        self.tab3 = self.ui3()
        self.tab4 = self.ui4()
        self.tab5 = self.ui5()
        
        self.initUI()

    def initUI(self):
        #Left layout
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.btn_1)
        left_layout.addWidget(self.btn_2)
        left_layout.addWidget(self.btn_3)
        left_layout.addWidget(self.btn_4)
        left_layout.addWidget(self.btn_5)
        left_layout.addStretch(5)
        left_layout.setSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_layout)


        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName("mainTab")

        self.right_widget.addTab(self.tab1, '')
        self.right_widget.addTab(self.tab2, '')
        self.right_widget.addTab(self.tab3, '')
        self.right_widget.addTab(self.tab4, '')
        self.right_widget.addTab(self.tab5, '')

        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''') #removes the top part of the window that would otherwise show up, to use the left buttons instead

        main_layout = QHBoxLayout()
        main_layout.addWidget(left_widget)
        main_layout.addWidget(self.right_widget)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    # ----------------- 
    # buttons

    def button1(self):
        self.right_widget.setCurrentIndex(0)

    def button2(self):
        self.right_widget.setCurrentIndex(1)

    def button3(self):
        self.right_widget.setCurrentIndex(2)

    def button4(self):
        self.right_widget.setCurrentIndex(3)

    def button5(self):
        self.right_widget.setCurrentIndex(4)
    
    def go_to_task(self):
        if self.windowTest.isVisible():
            self.windowTest.hide()
        else:
            self.windowTest.show()

    # ----------------- 
    # pages

    def set_tasks(self):
        tasks = []
        #Test tasks
        tasks.append(Task("Task 1", 1, 2021, 9, 3, "test", False, None, None))
        return tasks[0]

    def ui1(self): #By Date
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Date'))
        main_layout.addWidget(self.task)
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui2(self): #By priority
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Priority'))
        main_layout.addWidget(self.task)
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui3(self): #Projects
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Projects'))
        #main_layout.addWidget(self.task)
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main

    def ui4(self): #History
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('History'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main
    
    def ui5(self): #Help
        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Help'))
        main_layout.addStretch(5)
        main = QWidget()
        main.setLayout(main_layout)
        return main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())