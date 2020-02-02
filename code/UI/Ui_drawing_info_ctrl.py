#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Ui_drawing_info_ctrl.py
#  Copyright 2020 Wang D.Q <Wang D.Q@DESKTOP-LTKS88H>
#  2020/01/31 23:24:23


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
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog_drawing_info_ctrl, self).__init__(parent)
        self.setupUi(self)

