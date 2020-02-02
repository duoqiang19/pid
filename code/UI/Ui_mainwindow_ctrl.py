#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Ui_mainwindow_ctrl.py
#  Copyright 2020 Wang D.Q <Wang D.Q@DESKTOP-LTKS88H>
#  2020/01/31 23:24:03

import os
import sys
import winreg

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from UI.Ui_mainwindow import Ui_MainWindow
from UI.Ui_new_drawing_ctrl import *
from UI.Ui_drawing_info_ctrl import *

from func.handle_drawing_database import *

database_address = str("D:/GitHub/pid/data/drawings.xlsx").replace("\\", "/")

class Ui_mainwindow_ctrl(QMainWindow, Ui_MainWindow):

    signalize_drawing_info = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Ui_mainwindow_ctrl, self).__init__(parent)
        self.setupUi(self)

        self.drawing_info = {}

        self.drawing_database = Handle_drawing_info(database_address)

        # self.pushButton_drawing_no_input.clicked.connect(self.emit_signal_drawing_info)
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    def on_pushButton_new_drawing_clicked(self):
        self.open_dialog_new_drawing()

    def emit_signal_drawing_info(self):
        signal_drawing_info = self.drawing_info
        self.signalize_drawing_info.emit(signal_drawing_info)

    def open_dialog_drawing_info(self):
        self.dialog_drawing_info = Dialog_drawing_info_ctrl()
        # self.dialog_drawing_info.signalize_new_drawing.connect(self.emit_slot_label_status_bar)
        self.dialog_drawing_info.show()
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    def on_pushButton_drawing_no_input_clicked(self):
        self.drawing_info['drawing_no'] = self.lineEdit_drawing_no_input.text()
        self.open_dialog_drawing_info()

    def emit_slot_label_status_bar(self, signal_new_drawing):
        self.label_status_bar.setText(str(signal_new_drawing))

    def open_dialog_new_drawing(self):
        self.dialog_new_drawing = Ui_new_drawing_ctrl()
        self.dialog_new_drawing.signalize_new_drawing.connect(self.emit_slot_label_status_bar)
        self.dialog_new_drawing.show()
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    @pyqtSlot()
    def on_pushButton_review_report_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

