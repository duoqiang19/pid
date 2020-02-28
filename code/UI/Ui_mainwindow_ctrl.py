# pid - Ui_mainwindow_ctrl
# 2020/1/31 - 23:24
# Copyright 2020 Wang D.Q <Wang D.Q@PyCharm>
# !/venv python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
from UI.Ui_drawing_info_ctrl import *
from UI.Ui_mainwindow import *
from UI.Ui_new_review_flow_ctrl import *
from func.handle_new_review_flow import *

database_address = str("D:/GitHub/pid/data/drawings.xlsx").replace("\\", "/")
profession_list = ['除灰', '电气二次', '电气一次', '化学', '建筑结构', '暖通', '热机', '热控', '水工工艺', '水工结构', '运煤', '总图运输']

class Mainwindow_ctrl(QMainWindow, Ui_MainWindow):

    signalize_drawing_no = pyqtSignal(dict)
    signalize_review_info = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Mainwindow_ctrl, self).__init__(parent)
        self.setupUi(self)
        self.drawing_no = {}
        self.review_info = {}
        for element in profession_list:
            self.comboBox_profession.addItem(element)
        # self.drawing_database = Handle_new_review_flow(database_address)
        self.pushButton_drawing_no_input.released.connect(self.emit_signal_drawing_no)
        self.pushButton_new_review_flow.released.connect(self.emit_signal_review_info)
        self.status = self.statusBar()
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    def take_slot_label_status_bar(self, signal_new_review_flow):
        try:
            self.status.showMessage('审查号：' + str(signal_new_review_flow['r1_review_no'])
                                    + '，本次审查' + str(signal_new_review_flow['drawing_qty'])
                                    + '册图纸')
        except KeyError:
            self.status.showMessage('取消新建审查流程')

    def emit_signal_review_info(self):
        try:
            self.review_info['drawing_qty'] = int(self.lineEdit_drawing_qty.text())
        except ValueError:
                self.status.showMessage('图纸数目格式错误！')
        else:
            self.review_info['profession'] = self.comboBox_profession.currentText()

        # print(self.review_info)
        if self.review_info == {}:
            self.status.showMessage('图纸数目不能为空！')
        else:
            signal_review_info = self.review_info
            self.open_dialog_new_review_flow()
            self.signalize_review_info.emit(signal_review_info)

    def open_dialog_new_review_flow(self):
        self.signalize_review_info.connect(Dialog_new_review_flow_ctrl)
        # self.dialog_new_review_flow = Dialog_new_review_flow_ctrl()
        # self.dialog_new_review_flow.signalize_new_review_flow.connect(self.take_slot_label_status_bar)
        # self.dialog_new_review_flow.show()
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    # @pyqtSlot()
    # def on_pushButton_drawing_no_input_clicked(self):
    #     self.drawing_no['drawing_no'] = self.lineEdit_drawing_no_input.text()
    #     self.open_dialog_drawing_info()
    # @pyqtSlot()
    def emit_signal_drawing_no(self):
        self.drawing_no['drawing_no'] = self.lineEdit_drawing_no_input.text()
        signal_drawing_no = self.drawing_no
        self.open_dialog_drawing_info()
        self.signalize_drawing_no.emit(signal_drawing_no)

    def open_dialog_drawing_info(self):
        self.signalize_drawing_no.connect(Dialog_drawing_info_ctrl)
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    # @pyqtSlot()
    # def on_pushButton_review_report_clicked(self):
    #     """
    #     Slot documentation goes here.
    #     """
    #     # TODO: not implemented yet
    #     raise NotImplementedError

