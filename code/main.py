# pid - main
# 2020/1/31 - 12:55
# Copyright 2020 Wang D.Q <Wang D.Q@PyCharm>
# !/venv python
# -*- coding: utf-8 -*-

# import os
import sys
# import winreg
from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
from UI.Ui_mainwindow_ctrl import *
# from UI.Ui_new_drawing_ctrl import *
# from func.pid_handle_drawing_database import *
# database_address = str("D:/GitHub/pid/data/drawings.xlsx").replace("\\", "/")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Mainwindow_ctrl()
    mainwindow.show()
    sys.exit(app.exec_())
