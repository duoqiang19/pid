#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  main.py
#  Copyright 2020 Wang D.Q <Wang D.Q@DESKTOP-LTKS88H>
#  2020/01/31 12:55:23

import os
import sys
import winreg

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from UI.Ui_mainwindow import Ui_MainWindow
from UI.Ui_new_drawing import Ui_Dialog_new_drawing

from func.pid_handle_drawing_database import *

database_address = str("D:/GitHub/pid/data/drawings.xlsx").replace("\\", "/")

class Ui_mainwindow_ctrl(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(Ui_mainwindow_ctrl, self).__init__(parent)
        self.setupUi(self)

        self.drawing_database = Handle_drawing_info(database_address)

    def open_dialog_new_drawing(self):
        self.dialog_new_drawing = Ui_pid_new_drawing_ctrl()
        self.dialog_new_drawing.signalize_new_drawing.connect(self.emit_slot_label_status_bar)
        self.dialog_new_drawing.show()

    def emit_slot_label_status_bar(self, signal_new_drawing):
        self.label_status_bar.setText(str(signal_new_drawing))

    @pyqtSlot()
    def on_pushButton_new_drawing_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.open_dialog_new_drawing()

    @pyqtSlot()
    def on_pushButton_review_report_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError



class Ui_new_drawing_ctrl(QDialog, Ui_Dialog_new_drawing):

    signalize_new_drawing = pyqtSignal(dict)
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(Ui_new_drawing_ctrl, self).__init__(parent)
        self.setupUi(self)
        self.new_drawing_info = {}
        self.buttonBox.accepted.connect(self.emit_signal_new_drawing_accepted)
        self.buttonBox.rejected.connect(self.emit_signal_new_drawing_rejected)

    def on_buttonBox_accepted(self):
        self.new_drawing_info['drawing_no'] = self.lineEdit_drawing_no.text()
        self.new_drawing_info['drawing_name'] = self.lineEdit_drawing_name.text()
        self.new_drawing_info['drawing_subvol_no'] = self.lineEdit_drawing_subvol_no.text()
        self.new_drawing_info['profession'] = self.lineEdit_profession.text()
        self.new_drawing_info['profession_vol'] = self.lineEdit_profession_vol.text()

    def on_buttonBox_rejected(self):
        self.new_drawing_info = {}

    def emit_signal_new_drawing_accepted(self):
        signal_new_drawing = self.new_drawing_info
        self.signalize_new_drawing.emit(signal_new_drawing)

    def emit_signal_new_drawing_rejected(self):
        signal_new_drawing = self.new_drawing_info
        self.signalize_new_drawing.emit(signal_new_drawing)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Ui_mainwindow_ctrl()
    mainwindow.show()
    sys.exit(app.exec_())
