#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  main.py
#  Copyright 2020 Wang D.Q <Wang D.Q@DESKTOP-LTKS88H>
#  2020/01/31 12:55:23

# import os
import sys
# import winreg

# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

from UI.Ui_mainwindow_ctrl import *
# from UI.Ui_new_drawing_ctrl import *

# from func.pid_handle_drawing_database import *

# database_address = str("D:/GitHub/pid/data/drawings.xlsx").replace("\\", "/")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Ui_mainwindow_ctrl()
    mainwindow.show()
    sys.exit(app.exec_())
