# -*- coding: utf-8 -*-

"""
Module implementing Ui_MainWindow_ctrl.
"""
import os
import sys
import winreg

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_pid_mainwindow import Ui_MainWindow


class Ui_pid_mainwindow_ctrl(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Ui_pid_mainwindow_ctrl, self).__init__(parent)
        self.setupUi(self)
    
    @pyqtSlot()
    def on_pushButton_new_drawing_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_pushButton_review_report_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pid_mainwindow = Ui_pid_mainwindow_ctrl()
    pid_mainwindow.show()
    sys.exit(app.exec_())
