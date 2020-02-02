# pid - Ui_new_review_proccess_ctrl
# 2020/1/31 - 23:24
# Copyright 2020 Wang D.Q <Wang D.Q@PyCharm>
# !/venv python
# -*- coding: utf-8 -*-

import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI.Ui_new_review_proccess import Ui_Dialog_new_review_proccess

class Dialog_new_review_proccess_ctrl(QDialog, Ui_Dialog_new_review_proccess):

    signalize_new_review_proccess = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(Dialog_new_review_proccess_ctrl, self).__init__(parent)
        self.setupUi(self)
        self.new_review_proccess_info = {}
        self.buttonBox.accepted.connect(self.emit_signal_new_review_proccess_accepted)
        self.buttonBox.rejected.connect(self.emit_signal_new_review_proccess_rejected)
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    def on_buttonBox_accepted(self):
        self.new_review_proccess_info['drawing_no'] = self.lineEdit_drawing_no.text()
        self.new_review_proccess_info['drawing_name'] = self.lineEdit_drawing_name.text()
        self.new_review_proccess_info['drawing_subvol_no'] = self.lineEdit_drawing_subvol_no.text()
        self.new_review_proccess_info['profession'] = self.lineEdit_profession.text()
        self.new_review_proccess_info['profession_vol'] = self.lineEdit_profession_vol.text()

    def emit_signal_new_review_proccess_accepted(self):
        signal_new_review_proccess = self.new_review_proccess_info
        self.signalize_new_review_proccess.emit(signal_new_review_proccess)
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
    def on_buttonBox_rejected(self):
        self.new_review_proccess_info = {}

    def emit_signal_new_review_proccess_rejected(self):
        signal_new_review_proccess = self.new_review_proccess_info
        self.signalize_new_review_proccess.emit(signal_new_review_proccess)
    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''
# if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # dialog_drawing_info = Ui_drawing_info_ctrl()
    # dialog_drawing_info.show()
    # sys.exit(app.exec_())
