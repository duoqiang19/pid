# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pid\GUI\pid_new_drawing.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(732, 180)
        Dialog.setSizeGripEnabled(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(300, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_drawing_no = QtWidgets.QLabel(Dialog)
        self.label_drawing_no.setGeometry(QtCore.QRect(30, 20, 51, 21))
        self.label_drawing_no.setObjectName("label_drawing_no")
        self.lineEdit_drawing_no = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_drawing_no.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.lineEdit_drawing_no.setObjectName("lineEdit_drawing_no")
        self.lineEdit_profession = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_profession.setGeometry(QtCore.QRect(320, 20, 113, 20))
        self.lineEdit_profession.setObjectName("lineEdit_profession")
        self.label_profession = QtWidgets.QLabel(Dialog)
        self.label_profession.setGeometry(QtCore.QRect(250, 20, 51, 21))
        self.label_profession.setObjectName("label_profession")
        self.label_profession_vol = QtWidgets.QLabel(Dialog)
        self.label_profession_vol.setGeometry(QtCore.QRect(470, 20, 51, 21))
        self.label_profession_vol.setObjectName("label_profession_vol")
        self.lineEdit_profession_vol = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_profession_vol.setGeometry(QtCore.QRect(540, 20, 113, 20))
        self.lineEdit_profession_vol.setObjectName("lineEdit_profession_vol")
        self.lineEdit_subvol_no = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_subvol_no.setGeometry(QtCore.QRect(540, 60, 113, 20))
        self.lineEdit_subvol_no.setObjectName("lineEdit_subvol_no")
        self.lineEdit_vol_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_vol_name.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.lineEdit_vol_name.setObjectName("lineEdit_vol_name")
        self.label_vol_name = QtWidgets.QLabel(Dialog)
        self.label_vol_name.setGeometry(QtCore.QRect(30, 60, 51, 21))
        self.label_vol_name.setObjectName("label_vol_name")
        self.label_subvol_no = QtWidgets.QLabel(Dialog)
        self.label_subvol_no.setGeometry(QtCore.QRect(410, 60, 111, 21))
        self.label_subvol_no.setObjectName("label_subvol_no")
        self.radioButton_integrity = QtWidgets.QRadioButton(Dialog)
        self.radioButton_integrity.setGeometry(QtCore.QRect(290, 60, 82, 17))
        self.radioButton_integrity.setObjectName("radioButton_integrity")
        self.label_memo = QtWidgets.QLabel(Dialog)
        self.label_memo.setGeometry(QtCore.QRect(20, 90, 291, 81))
        self.label_memo.setAutoFillBackground(True)
        self.label_memo.setWordWrap(True)
        self.label_memo.setObjectName("label_memo")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_drawing_no.setText(_translate("Dialog", "图号"))
        self.label_profession.setText(_translate("Dialog", "专业"))
        self.label_profession_vol.setText(_translate("Dialog", "专业分卷"))
        self.label_vol_name.setText(_translate("Dialog", "卷册名称"))
        self.label_subvol_no.setText(_translate("Dialog", "本次出版的分卷号"))
        self.radioButton_integrity.setText(_translate("Dialog", "完整卷册"))
        self.label_memo.setText(_translate("Dialog", "自动生成：审查号，录入日期，审核状态；自动调取：计划出版日期；可自定义修改：审查号，录入日期；需要的新功能：插入文件筐"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

