# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'task.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionyourothermom = QAction(MainWindow)
        self.actionyourothermom.setObjectName(u"actionyourothermom")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TaskLabel = QLabel(self.centralwidget)
        self.TaskLabel.setObjectName(u"TaskLabel")

        self.verticalLayout.addWidget(self.TaskLabel)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.PriorityLabel = QLabel(self.centralwidget)
        self.PriorityLabel.setObjectName(u"PriorityLabel")

        self.horizontalLayout_2.addWidget(self.PriorityLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.DeadlineLabel = QLabel(self.centralwidget)
        self.DeadlineLabel.setObjectName(u"DeadlineLabel")

        self.horizontalLayout.addWidget(self.DeadlineLabel)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setDate(QDate(2021, 9, 6))

        self.horizontalLayout.addWidget(self.dateEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignHCenter)

        self.Description_Label = QLabel(self.centralwidget)
        self.Description_Label.setObjectName(u"Description_Label")

        self.verticalLayout_2.addWidget(self.Description_Label, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_3.addWidget(self.checkBox, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMouseTracking(False)

        self.horizontalLayout_4.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.subtask = QPushButton(self.centralwidget)
        self.subtask.setObjectName(u"subtask")

        self.gridLayout.addWidget(self.subtask, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionyourothermom.setText(QCoreApplication.translate("MainWindow", u"yourothermom", None))
        self.TaskLabel.setText(QCoreApplication.translate("MainWindow", u"Task", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Priority:", None))
        self.PriorityLabel.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.DeadlineLabel.setText(QCoreApplication.translate("MainWindow", u"Deadine:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.Description_Label.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Completed", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Subtasks:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Subtask", None))
        self.subtask.setText(QCoreApplication.translate("MainWindow", u"Subtask", None))
    # retranslateUi

