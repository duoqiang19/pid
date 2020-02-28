# pid - Ui_new_review_flow_ctrl
# 2020/1/31 - 23:24
# Copyright 2020 Wang D.Q <Wang D.Q@PyCharm>
# !/venv python
# -*- coding: utf-8 -*-


import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI.Ui_new_review_flow import Ui_Dialog_new_review_flow

release_stage_list = ['施工图','备料图']

class Dialog_new_review_flow_ctrl(QDialog, Ui_Dialog_new_review_flow):

    signalize_new_review_flow = pyqtSignal(dict)

    def __init__(self, signalize_review_info, parent=None):
        super(Dialog_new_review_flow_ctrl, self).__init__(parent)
        self.new_review_flow_info = signalize_review_info
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.emit_signal_new_review_flow_accepted)
        self.buttonBox.rejected.connect(self.emit_signal_new_review_flow_rejected)
        for element in release_stage_list:
            self.comboBox_release_stage.addItem(element)
        self.dateEdit_start_flow.setDisplayFormat("yyyy.MM.dd")
        self.dateEdit_start_flow.setDate(QDate.currentDate())
        self.lineEdit_profession.setText(str(self.new_review_flow_info['profession']))
        self.drawing_qty = 1

        self.pushButton_qty_add.clicked.connect(lambda: self.setupUi_qty_add(self))
        self.pushButton_qty_minus.clicked.connect(lambda: self.setupUi_qty_minus(self))
        # self.setupUi(self)
        self.show()
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    def on_buttonBox_accepted(self):
        self.new_review_flow_info['r1_review_no'] = self.lineEdit_r1_review_no.text()
        # self.new_review_flow_info['drawing_qty'] = self.drawing_qty
        # self.new_review_flow_info['profession'] = self.comboBox_profession.currentText()
        self.new_review_flow_info['release_stage'] = self.comboBox_release_stage.currentText()
        self.new_review_flow_info['date_start_flow'] = self.dateEdit_start_flow.date()
        self.new_review_flow_info['drawing_no_01'] = self.lineEdit_drawing_no_01.text()
        self.new_review_flow_info['drawing_title_01'] = self.lineEdit_drawing_title_01.text()
        self.new_review_flow_info['vol_title_01'] = self.lineEdit_vol_title_01.text()

    def emit_signal_new_review_flow_accepted(self):
        signal_new_review_flow = self.new_review_flow_info
        self.signalize_new_review_flow.emit(signal_new_review_flow)
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    def on_buttonBox_rejected(self):
        self.new_review_flow_info = {}

    def emit_signal_new_review_flow_rejected(self):
        signal_new_review_flow = self.new_review_flow_info
        self.signalize_new_review_flow.emit(signal_new_review_flow)
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    def setupUi_qty_add(self, Dialog_new_review_flow):
        self.drawing_qty += 1
        if self.drawing_qty > 99:
            self.drawing_qty = 99
        print(self.drawing_qty)
        Dialog_new_review_flow.resize(842, 62 + 31 * int(self.drawing_qty))
        # for i in range(self.drawing_qty):
        self.label_drawing_no = QtWidgets.QLabel(Dialog_new_review_flow)
        self.label_drawing_no.setObjectName("label_drawing_no_" + str(self.drawing_qty))
        self.gridLayout.addWidget(self.label_drawing_no, self.drawing_qty, 0, 1, 1)
        _translate = QtCore.QCoreApplication.translate
        self.label_drawing_no.setText(_translate("Dialog_new_review_flow", "图号" + str(self.drawing_qty)))
        self.buttonBox.deleteLater()
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_new_review_flow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, self.drawing_qty+1 , 7, 1, 6)

    def setupUi_qty_minus(self, Dialog_new_review_flow):
        self.drawing_qty -= 1
        if self.drawing_qty < 1:
            self.drawing_qty = 1
        print(self.drawing_qty)
        self.label_drawing_no.deleteLater()
        # self.buttonBox.deleteLater()
        # self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_new_review_flow)
        # self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        # self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        # self.buttonBox.setObjectName("buttonBox")
        # self.gridLayout.addWidget(self.buttonBox, self.drawing_qty + 1, 7, 1, 6)
        Dialog_new_review_flow.resize(842, 62 + 31 * int(self.drawing_qty))


    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''

