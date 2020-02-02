#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Ui_new_drawing_ctrl.py
#  Copyright 2020 Wang D.Q <Wang D.Q@DESKTOP-LTKS88H>
#  2020/01/31 23:24:23

import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI.Ui_new_drawing import Ui_Dialog_new_drawing

class Ui_new_drawing_ctrl(QDialog, Ui_Dialog_new_drawing):

    signalize_new_drawing = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Ui_new_drawing_ctrl, self).__init__(parent)
        self.setupUi(self)
        self.new_drawing_info = {}
        self.buttonBox.accepted.connect(self.emit_signal_new_drawing_accepted)
        self.buttonBox.rejected.connect(self.emit_signal_new_drawing_rejected)
# -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- #
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
# -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- #
    def emit_signal_new_drawing_rejected(self):
        signal_new_drawing = self.new_drawing_info
        self.signalize_new_drawing.emit(signal_new_drawing)
# -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- #
# if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # dialog_drawing_info = Ui_drawing_info_ctrl()
    # dialog_drawing_info.show()
    # sys.exit(app.exec_())
