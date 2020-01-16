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
from Ui_pid_new_drawing_ctrl import Ui_pid_new_drawing_ctrl


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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    pid_mainwindow = Ui_pid_mainwindow_ctrl()
    pid_mainwindow.show()
    sys.exit(app.exec_())
