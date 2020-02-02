# -*- coding: utf-8 -*-

"""
Module implementing Dialog_drawing_info_ctrl.
"""
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_drawing_info import Ui_Dialog_drawing_info


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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog_drawing_info_ctrl()
    dialog.show()
    sys.exit(app.exec_())
