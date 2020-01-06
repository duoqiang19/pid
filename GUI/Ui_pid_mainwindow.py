# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pid\GUI\pid_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget_mainwindow = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget_mainwindow.setGeometry(QtCore.QRect(10, 80, 661, 411))
        self.tabWidget_mainwindow.setObjectName("tabWidget_mainwindow")
        self.tab_drawings = QtWidgets.QWidget()
        self.tab_drawings.setObjectName("tab_drawings")
        self.pushButton_new_drawing = QtWidgets.QPushButton(self.tab_drawings)
        self.pushButton_new_drawing.setGeometry(QtCore.QRect(10, 10, 83, 23))
        self.pushButton_new_drawing.setObjectName("pushButton_new_drawing")
        self.pushButton_review_report = QtWidgets.QPushButton(self.tab_drawings)
        self.pushButton_review_report.setGeometry(QtCore.QRect(110, 10, 90, 23))
        self.pushButton_review_report.setObjectName("pushButton_review_report")
        self.tabWidget_mainwindow.addTab(self.tab_drawings, "")
        self.tab_specifications = QtWidgets.QWidget()
        self.tab_specifications.setObjectName("tab_specifications")
        self.tabWidget_mainwindow.addTab(self.tab_specifications, "")
        self.label_status_bar = QtWidgets.QLabel(self.centralWidget)
        self.label_status_bar.setGeometry(QtCore.QRect(10, 510, 761, 81))
        self.label_status_bar.setTextFormat(QtCore.Qt.AutoText)
        self.label_status_bar.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_status_bar.setWordWrap(True)
        self.label_status_bar.setObjectName("label_status_bar")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_mainwindow.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_new_drawing.setText(_translate("MainWindow", "BUTTON_1"))
        self.pushButton_review_report.setText(_translate("MainWindow", "BUTTON_2"))
        self.tabWidget_mainwindow.setTabText(self.tabWidget_mainwindow.indexOf(self.tab_drawings), _translate("MainWindow", "A"))
        self.tabWidget_mainwindow.setTabText(self.tabWidget_mainwindow.indexOf(self.tab_specifications), _translate("MainWindow", "B"))
        self.label_status_bar.setText(_translate("MainWindow", "status bar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

