# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 220)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget_mainwindow = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget_mainwindow.setGeometry(QtCore.QRect(10, 10, 400, 200))
        self.tabWidget_mainwindow.setObjectName("tabWidget_mainwindow")
        self.tab_drawings = QtWidgets.QWidget()
        self.tab_drawings.setObjectName("tab_drawings")
        self.pushButton_new_review_proccess = QtWidgets.QPushButton(self.tab_drawings)
        self.pushButton_new_review_proccess.setGeometry(QtCore.QRect(10, 10, 80, 25))
        self.pushButton_new_review_proccess.setObjectName("pushButton_new_review_proccess")
        self.pushButton_review_report = QtWidgets.QPushButton(self.tab_drawings)
        self.pushButton_review_report.setGeometry(QtCore.QRect(100, 10, 80, 25))
        self.pushButton_review_report.setObjectName("pushButton_review_report")
        self.lineEdit_drawing_no_input = QtWidgets.QLineEdit(self.tab_drawings)
        self.lineEdit_drawing_no_input.setGeometry(QtCore.QRect(190, 10, 80, 23))
        self.lineEdit_drawing_no_input.setObjectName("lineEdit_drawing_no_input")
        self.pushButton_drawing_no_input = QtWidgets.QPushButton(self.tab_drawings)
        self.pushButton_drawing_no_input.setGeometry(QtCore.QRect(280, 10, 80, 25))
        self.pushButton_drawing_no_input.setTabletTracking(False)
        self.pushButton_drawing_no_input.setAutoDefault(False)
        self.pushButton_drawing_no_input.setDefault(False)
        self.pushButton_drawing_no_input.setObjectName("pushButton_drawing_no_input")
        self.tabWidget_mainwindow.addTab(self.tab_drawings, "")
        self.tab_specifications = QtWidgets.QWidget()
        self.tab_specifications.setObjectName("tab_specifications")
        self.tabWidget_mainwindow.addTab(self.tab_specifications, "")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_mainwindow.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_new_review_proccess.setText(_translate("MainWindow", "新建审查流程"))
        self.pushButton_review_report.setText(_translate("MainWindow", "图纸送审"))
        self.lineEdit_drawing_no_input.setText(_translate("MainWindow", "C0101"))
        self.pushButton_drawing_no_input.setText(_translate("MainWindow", "Go"))
        self.tabWidget_mainwindow.setTabText(self.tabWidget_mainwindow.indexOf(self.tab_drawings), _translate("MainWindow", "A"))
        self.tabWidget_mainwindow.setTabText(self.tabWidget_mainwindow.indexOf(self.tab_specifications), _translate("MainWindow", "B"))
