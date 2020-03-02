# pid - Ui_mainwindow_ctrl
# 2020/1/31 - 23:24
# Copyright 2020 Wang D.Q <Wang D.Q@PyCharm>
# !/venv python
# -*- coding: utf-8 -*-

# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI.Ui_drawing_info_ctrl import *
from UI.Ui_mainwindow import *
from UI.Ui_new_review_flow_ctrl import *
from func.handle_new_review_flow import *
database_address = str("D:/GitHub/pid/data/drawings.xlsx").replace("\\", "/")
profession_list = ['除灰', '电气二次', '电气一次', '化学', '建筑结构', '暖通', '热机', '热控', '水工工艺', '水工结构', '运煤', '总图运输']
'''
nrf = new_review_flow
'''
class Mainwindow_ctrl(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Mainwindow_ctrl, self).__init__(parent)
        self.setupUi(self)
        for element in profession_list:
            self.comboBox_profession.addItem(element)
        self.status = self.statusBar()
        self.pushButton_new_review_flow.clicked.connect(self.show_dlg_new_review_flow)
        self.pushButton_drawing_no_input.clicked.connect(self.show_dlg_drawing_info)

    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    def show_dlg_new_review_flow(self):
        review_info = {}
        try:
            review_info['drawing_qty'] = int(self.spinBox_drawing_qty.value())
        except ValueError:
            self.status.showMessage('图纸数目格式错误！')
        else:
            review_info['profession'] = self.comboBox_profession.currentText()

        if review_info == {}:
            self.status.showMessage('图纸数目不能为空！')
        else:
            dialog_new_review_flow = Dialog_new_review_flow_ctrl(review_info)
            dialog_new_review_flow.sgl_nrf.connect(self.take_slot_label_status_bar)
            dialog_new_review_flow.exec_()

    def take_slot_label_status_bar(self, nrf):
        try:
            self.status.showMessage('审查号：' + str(nrf['r1_review_no'])
                                    + '，本次审查' + str(nrf['drawing_qty'])
                                    + '册图纸')
        except KeyError:
            self.status.showMessage('取消新建审查流程')
        print(nrf)
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    def show_dlg_drawing_info(self):
        drawing_no = {}
        drawing_no['drawing_no'] = self.lineEdit_drawing_no_input.text()
        dlg_drawing_info = Dialog_drawing_info_ctrl(drawing_no)
        dlg_drawing_info.show()



    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    # @pyqtSlot()
    # def on_pushButton_review_report_clicked(self):
    #     """
    #     Slot documentation goes here.
    #     """
    #     # TODO: not implemented yet
    #     raise NotImplementedError

