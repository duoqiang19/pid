# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\GitHub\pid\bin\UI\new_drawing.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_new_drawing(object):
    def setupUi(self, Dialog_new_drawing):
        Dialog_new_drawing.setObjectName("Dialog_new_drawing")
        Dialog_new_drawing.resize(732, 180)
        Dialog_new_drawing.setSizeGripEnabled(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_new_drawing)
        self.buttonBox.setGeometry(QtCore.QRect(300, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_drawing_no = QtWidgets.QLabel(Dialog_new_drawing)
        self.label_drawing_no.setGeometry(QtCore.QRect(30, 20, 51, 21))
        self.label_drawing_no.setObjectName("label_drawing_no")
        self.lineEdit_drawing_no = QtWidgets.QLineEdit(Dialog_new_drawing)
        self.lineEdit_drawing_no.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.lineEdit_drawing_no.setObjectName("lineEdit_drawing_no")
        self.lineEdit_profession = QtWidgets.QLineEdit(Dialog_new_drawing)
        self.lineEdit_profession.setGeometry(QtCore.QRect(320, 20, 113, 20))
        self.lineEdit_profession.setObjectName("lineEdit_profession")
        self.label_profession = QtWidgets.QLabel(Dialog_new_drawing)
        self.label_profession.setGeometry(QtCore.QRect(250, 20, 51, 21))
        self.label_profession.setObjectName("label_profession")
        self.label_profession_vol = QtWidgets.QLabel(Dialog_new_drawing)
        self.label_profession_vol.setGeometry(QtCore.QRect(470, 20, 51, 21))
        self.label_profession_vol.setObjectName("label_profession_vol")
        self.lineEdit_profession_vol = QtWidgets.QLineEdit(Dialog_new_drawing)
        self.lineEdit_profession_vol.setGeometry(QtCore.QRect(540, 20, 113, 20))
        self.lineEdit_profession_vol.setObjectName("lineEdit_profession_vol")
        self.lineEdit_drawing_subvol_no = QtWidgets.QLineEdit(Dialog_new_drawing)
        self.lineEdit_drawing_subvol_no.setGeometry(QtCore.QRect(540, 60, 113, 20))
        self.lineEdit_drawing_subvol_no.setObjectName("lineEdit_drawing_subvol_no")
        self.lineEdit_drawing_name = QtWidgets.QLineEdit(Dialog_new_drawing)
        self.lineEdit_drawing_name.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.lineEdit_drawing_name.setObjectName("lineEdit_drawing_name")
        self.label_vol_name = QtWidgets.QLabel(Dialog_new_drawing)
        self.label_vol_name.setGeometry(QtCore.QRect(30, 60, 51, 21))
        self.label_vol_name.setObjectName("label_vol_name")
        self.label_subvol_no = QtWidgets.QLabel(Dialog_new_drawing)
        self.label_subvol_no.setGeometry(QtCore.QRect(410, 60, 111, 21))
        self.label_subvol_no.setObjectName("label_subvol_no")
        self.radioButton_integrity = QtWidgets.QRadioButton(Dialog_new_drawing)
        self.radioButton_integrity.setGeometry(QtCore.QRect(290, 60, 82, 17))
        self.radioButton_integrity.setObjectName("radioButton_integrity")
        self.label_memo = QtWidgets.QLabel(Dialog_new_drawing)
        self.label_memo.setGeometry(QtCore.QRect(20, 90, 291, 81))
        self.label_memo.setAutoFillBackground(True)
        self.label_memo.setWordWrap(True)
        self.label_memo.setObjectName("label_memo")

        self.retranslateUi(Dialog_new_drawing)
        self.buttonBox.accepted.connect(Dialog_new_drawing.accept)
        self.buttonBox.rejected.connect(Dialog_new_drawing.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_new_drawing)
        Dialog_new_drawing.setTabOrder(self.lineEdit_drawing_no, self.lineEdit_profession)
        Dialog_new_drawing.setTabOrder(self.lineEdit_profession, self.lineEdit_profession_vol)
        Dialog_new_drawing.setTabOrder(self.lineEdit_profession_vol, self.lineEdit_drawing_name)
        Dialog_new_drawing.setTabOrder(self.lineEdit_drawing_name, self.radioButton_integrity)
        Dialog_new_drawing.setTabOrder(self.radioButton_integrity, self.lineEdit_drawing_subvol_no)

    def retranslateUi(self, Dialog_new_drawing):
        _translate = QtCore.QCoreApplication.translate
        Dialog_new_drawing.setWindowTitle(_translate("Dialog_new_drawing", "新图纸"))
        self.label_drawing_no.setText(_translate("Dialog_new_drawing", "图号"))
        self.label_profession.setText(_translate("Dialog_new_drawing", "专业"))
        self.label_profession_vol.setText(_translate("Dialog_new_drawing", "专业分卷"))
        self.label_vol_name.setText(_translate("Dialog_new_drawing", "卷册名称"))
        self.label_subvol_no.setText(_translate("Dialog_new_drawing", "本次出版的分册号"))
        self.radioButton_integrity.setText(_translate("Dialog_new_drawing", "完整卷册"))
        self.label_memo.setText(_translate("Dialog_new_drawing", "自动生成：审查号，录入日期，审核状态；自动调取：计划出版日期；可自定义修改：审查号，录入日期；需要的新功能：插入文件筐"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_new_drawing = QtWidgets.QDialog()
    ui = Ui_Dialog_new_drawing()
    ui.setupUi(Dialog_new_drawing)
    Dialog_new_drawing.show()
    sys.exit(app.exec_())

