# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_drawing_info.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_drawing_info(object):
    def setupUi(self, Dialog_drawing_info):
        Dialog_drawing_info.setObjectName("Dialog_drawing_info")
        Dialog_drawing_info.resize(520, 240)
        Dialog_drawing_info.setSizeGripEnabled(True)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_drawing_info)
        self.buttonBox.setGeometry(QtCore.QRect(340, 190, 160, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_drawing_title = QtWidgets.QLabel(Dialog_drawing_info)
        self.label_drawing_title.setGeometry(QtCore.QRect(20, 70, 80, 20))
        self.label_drawing_title.setObjectName("label_drawing_title")
        self.lineEdit_drawing_title = QtWidgets.QLineEdit(Dialog_drawing_info)
        self.lineEdit_drawing_title.setGeometry(QtCore.QRect(110, 70, 390, 20))
        self.lineEdit_drawing_title.setText("")
        self.lineEdit_drawing_title.setReadOnly(True)
        self.lineEdit_drawing_title.setObjectName("lineEdit_drawing_title")
        self.lineEdit_drawing_no = QtWidgets.QLineEdit(Dialog_drawing_info)
        self.lineEdit_drawing_no.setGeometry(QtCore.QRect(110, 40, 140, 20))
        self.lineEdit_drawing_no.setAutoFillBackground(False)
        self.lineEdit_drawing_no.setText("")
        self.lineEdit_drawing_no.setDragEnabled(False)
        self.lineEdit_drawing_no.setReadOnly(True)
        self.lineEdit_drawing_no.setObjectName("lineEdit_drawing_no")
        self.label_drawing_no = QtWidgets.QLabel(Dialog_drawing_info)
        self.label_drawing_no.setGeometry(QtCore.QRect(20, 40, 80, 20))
        self.label_drawing_no.setObjectName("label_drawing_no")
        self.lineEdit_database_series_no = QtWidgets.QLineEdit(Dialog_drawing_info)
        self.lineEdit_database_series_no.setGeometry(QtCore.QRect(360, 40, 140, 20))
        self.lineEdit_database_series_no.setText("")
        self.lineEdit_database_series_no.setReadOnly(True)
        self.lineEdit_database_series_no.setObjectName("lineEdit_database_series_no")
        self.label_database_series_no = QtWidgets.QLabel(Dialog_drawing_info)
        self.label_database_series_no.setGeometry(QtCore.QRect(270, 40, 80, 20))
        self.label_database_series_no.setObjectName("label_database_series_no")
        self.label_profession_subvol = QtWidgets.QLabel(Dialog_drawing_info)
        self.label_profession_subvol.setGeometry(QtCore.QRect(270, 100, 80, 20))
        self.label_profession_subvol.setObjectName("label_profession_subvol")
        self.lineEdit_profession_subvol = QtWidgets.QLineEdit(Dialog_drawing_info)
        self.lineEdit_profession_subvol.setGeometry(QtCore.QRect(360, 100, 140, 20))
        self.lineEdit_profession_subvol.setText("")
        self.lineEdit_profession_subvol.setReadOnly(True)
        self.lineEdit_profession_subvol.setObjectName("lineEdit_profession_subvol")
        self.label_profession = QtWidgets.QLabel(Dialog_drawing_info)
        self.label_profession.setGeometry(QtCore.QRect(20, 100, 80, 20))
        self.label_profession.setObjectName("label_profession")
        self.lineEdit_profession = QtWidgets.QLineEdit(Dialog_drawing_info)
        self.lineEdit_profession.setGeometry(QtCore.QRect(110, 100, 140, 20))
        self.lineEdit_profession.setText("")
        self.lineEdit_profession.setReadOnly(True)
        self.lineEdit_profession.setObjectName("lineEdit_profession")
        self.lineEdit_drawing_integrity = QtWidgets.QLineEdit(Dialog_drawing_info)
        self.lineEdit_drawing_integrity.setGeometry(QtCore.QRect(110, 130, 140, 20))
        self.lineEdit_drawing_integrity.setText("")
        self.lineEdit_drawing_integrity.setReadOnly(True)
        self.lineEdit_drawing_integrity.setObjectName("lineEdit_drawing_integrity")
        self.label_release_stage = QtWidgets.QLabel(Dialog_drawing_info)
        self.label_release_stage.setGeometry(QtCore.QRect(270, 130, 80, 20))
        self.label_release_stage.setObjectName("label_release_stage")
        self.lineEdit_release_stage = QtWidgets.QLineEdit(Dialog_drawing_info)
        self.lineEdit_release_stage.setGeometry(QtCore.QRect(360, 130, 140, 20))
        self.lineEdit_release_stage.setText("")
        self.lineEdit_release_stage.setReadOnly(True)
        self.lineEdit_release_stage.setObjectName("lineEdit_release_stage")
        self.label_release_status = QtWidgets.QLabel(Dialog_drawing_info)
        self.label_release_status.setGeometry(QtCore.QRect(20, 130, 80, 20))
        self.label_release_status.setObjectName("label_release_status")
        self.label_review_status = QtWidgets.QLabel(Dialog_drawing_info)
        self.label_review_status.setGeometry(QtCore.QRect(20, 160, 80, 20))
        self.label_review_status.setObjectName("label_review_status")
        self.lineEdit_review_status = QtWidgets.QLineEdit(Dialog_drawing_info)
        self.lineEdit_review_status.setGeometry(QtCore.QRect(110, 160, 140, 20))
        self.lineEdit_review_status.setText("")
        self.lineEdit_review_status.setReadOnly(True)
        self.lineEdit_review_status.setObjectName("lineEdit_review_status")
        self.label_planned_release_date = QtWidgets.QLabel(Dialog_drawing_info)
        self.label_planned_release_date.setGeometry(QtCore.QRect(270, 160, 80, 20))
        self.label_planned_release_date.setObjectName("label_planned_release_date")
        self.lineEdit_planned_release_date = QtWidgets.QLineEdit(Dialog_drawing_info)
        self.lineEdit_planned_release_date.setGeometry(QtCore.QRect(360, 160, 140, 20))
        self.lineEdit_planned_release_date.setText("")
        self.lineEdit_planned_release_date.setReadOnly(True)
        self.lineEdit_planned_release_date.setObjectName("lineEdit_planned_release_date")
        self.checkBox_info_changabilty = QtWidgets.QCheckBox(Dialog_drawing_info)
        self.checkBox_info_changabilty.setGeometry(QtCore.QRect(20, 10, 70, 20))
        self.checkBox_info_changabilty.setChecked(True)
        self.checkBox_info_changabilty.setObjectName("checkBox_info_changabilty")
        self.pushButton = QtWidgets.QPushButton(Dialog_drawing_info)
        self.pushButton.setGeometry(QtCore.QRect(110, 10, 91, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog_drawing_info)
        QtCore.QMetaObject.connectSlotsByName(Dialog_drawing_info)
        Dialog_drawing_info.setTabOrder(self.lineEdit_drawing_no, self.lineEdit_database_series_no)
        Dialog_drawing_info.setTabOrder(self.lineEdit_database_series_no, self.lineEdit_drawing_title)
        Dialog_drawing_info.setTabOrder(self.lineEdit_drawing_title, self.lineEdit_profession)
        Dialog_drawing_info.setTabOrder(self.lineEdit_profession, self.lineEdit_profession_subvol)
        Dialog_drawing_info.setTabOrder(self.lineEdit_profession_subvol, self.lineEdit_drawing_integrity)
        Dialog_drawing_info.setTabOrder(self.lineEdit_drawing_integrity, self.lineEdit_release_stage)
        Dialog_drawing_info.setTabOrder(self.lineEdit_release_stage, self.lineEdit_review_status)
        Dialog_drawing_info.setTabOrder(self.lineEdit_review_status, self.lineEdit_planned_release_date)

    def retranslateUi(self, Dialog_drawing_info):
        _translate = QtCore.QCoreApplication.translate
        Dialog_drawing_info.setWindowTitle(_translate("Dialog_drawing_info", "图纸信息"))
        self.label_drawing_title.setText(_translate("Dialog_drawing_info", "施工图卷册名称"))
        self.label_drawing_no.setText(_translate("Dialog_drawing_info", "图号"))
        self.label_database_series_no.setText(_translate("Dialog_drawing_info", "数据序号"))
        self.label_profession_subvol.setText(_translate("Dialog_drawing_info", "专业分卷"))
        self.label_profession.setText(_translate("Dialog_drawing_info", "专业"))
        self.label_release_stage.setText(_translate("Dialog_drawing_info", "出图阶段"))
        self.label_release_status.setText(_translate("Dialog_drawing_info", "出版状态"))
        self.label_review_status.setText(_translate("Dialog_drawing_info", "审核状态"))
        self.label_planned_release_date.setText(_translate("Dialog_drawing_info", "计划出版日期"))
        self.checkBox_info_changabilty.setText(_translate("Dialog_drawing_info", "修改锁定"))
        self.pushButton.setText(_translate("Dialog_drawing_info", "PushButton"))
