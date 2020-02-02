# pid - Ui_drawing_info_ctrl
# 2020/1/31 - 23:24
# Copyright 2020 Wang D.Q <Wang D.Q@PyCharm>
# !/venv python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from UI.Ui_drawing_info import Ui_Dialog_drawing_info


class Dialog_drawing_info_ctrl(QDialog, Ui_Dialog_drawing_info):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        super(Dialog_drawing_info_ctrl, self).__init__(parent)
        self.setupUi(self)

        # self.mainwindow.signalize_drawing_no.connect(self.take_slot_drawing_no())

    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''

    def take_slot_drawing_no(self, signal_drawing_no):
        self.textBrowser.setText(str(signal_drawing_no))
