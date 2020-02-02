# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pid\code\UI\drawing_info.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_drawing_info(object):
    def setupUi(self, Dialog_drawing_info):
        Dialog_drawing_info.setObjectName("Dialog_drawing_info")
        Dialog_drawing_info.resize(421, 116)
        Dialog_drawing_info.setSizeGripEnabled(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_drawing_info)
        self.buttonBox.setGeometry(QtCore.QRect(240, 70, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog_drawing_info)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 391, 71))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Dialog_drawing_info)
        QtCore.QMetaObject.connectSlotsByName(Dialog_drawing_info)

    def retranslateUi(self, Dialog_drawing_info):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_drawing_info = QtWidgets.QDialog()
    ui = Ui_Dialog_drawing_info()
    ui.setupUi(Dialog_drawing_info)
    Dialog_drawing_info.show()
    sys.exit(app.exec_())

