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
from UI.Ui_new_review_proccess_ctrl import *
from func.handle_new_review_proccess import *

database_address = str("D:/GitHub/pid/data/drawings.xlsx").replace("\\", "/")

class Mainwindow_ctrl(QMainWindow, Ui_MainWindow):

    signalize_drawing_no = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Mainwindow_ctrl, self).__init__(parent)
        self.setupUi(self)
        self.drawing_no = {}
        self.drawing_database = Handle_new_review_proccess(database_address)
        self.pushButton_drawing_no_input.clicked.connect(self.emit_signal_drawing_no)
        self.status = self.statusBar()
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    @pyqtSlot()
    def on_pushButton_new_review_proccess_clicked(self):
        self.open_dialog_new_review_proccess()

    def take_slot_label_status_bar(self, signal_new_review_proccess):
        self.status.showMessage(str(signal_new_review_proccess['drawing_name']))

    def open_dialog_new_review_proccess(self):
        self.dialog_new_review_proccess = Dialog_new_review_proccess_ctrl()
        self.dialog_new_review_proccess.signalize_new_review_proccess.connect(self.take_slot_label_status_bar)
        self.dialog_new_review_proccess.show()
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    @pyqtSlot()
    def on_pushButton_drawing_no_input_clicked(self):
        self.drawing_no['drawing_no'] = self.lineEdit_drawing_no_input.text()
        self.open_dialog_drawing_info()

    def emit_signal_drawing_no(self):
        signal_drawing_no = self.drawing_no
        self.signalize_drawing_no.emit(signal_drawing_no)

    def open_dialog_drawing_info(self):
        self.dialog_drawing_info = Dialog_drawing_info_ctrl()
        self.signalize_drawing_no.connect(self.dialog_drawing_info.take_slot_drawing_no)
        self.dialog_drawing_info.show()
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    # @pyqtSlot()
    # def on_pushButton_review_report_clicked(self):
    #     """
    #     Slot documentation goes here.
    #     """
    #     # TODO: not implemented yet
    #     raise NotImplementedError

