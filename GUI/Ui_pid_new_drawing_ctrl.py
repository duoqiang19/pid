# -*- coding: utf-8 -*-

"""
Module implementing Ui_pid_new_drawing_ctrl.
"""

import os
import sys
import winreg

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_pid_new_drawing import Ui_Dialog

class Ui_pid_new_drawing_ctrl(QDialog, Ui_Dialog):

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
        super(Ui_pid_new_drawing_ctrl, self).__init__(parent)
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

