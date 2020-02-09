# pid - Ui_drawing_info_ctrl
# 2020/1/31 - 23:24
# Copyright 2020 Wang D.Q <Wang D.Q@PyCharm>
# !/venv python
# -*- coding: utf-8 -*-

# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5 import QtCore, QtGui, QtWidgets

from UI.Ui_drawing_info import Ui_Dialog_drawing_info
from func.handle_drawing_database import Handle_drawing_database

database_address = str("D:/GitHub/pid/data/drawings.xlsx").replace("\\", "/")

class Dialog_drawing_info_ctrl(QDialog, Ui_Dialog_drawing_info):

    def __init__(self, parent=None):
        super(Dialog_drawing_info_ctrl, self).__init__(parent)
        self.setupUi(self)
        self.handle_drawing_info = Handle_drawing_database(database_address)
        self.checkBox_info_changabilty.stateChanged.connect(lambda: self.info_changabilty_checked(self.checkBox_info_changabilty))

    ''' -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- -*- '''

    def take_slot_drawing_no(self, signal_drawing_no):
        self.drawing_info = self.handle_drawing_info.read_drawing_info(signal_drawing_no['drawing_no'])
        self.lineEdit_drawing_no.setText(str(self.drawing_info['drawing_no']))
        self.lineEdit_database_series_no.setText(str(self.drawing_info['database_series_no']))
        self.lineEdit_drawing_title.setText(str(self.drawing_info['drawing_title']))
        self.lineEdit_profession.setText(str(self.drawing_info['profession']))
        self.lineEdit_profession_subvol.setText(str(self.drawing_info['profession_subvol']))
        self.lineEdit_drawing_integrity.setText(str(self.drawing_info['drawing_integrity']))
        self.lineEdit_release_stage.setText(str(self.drawing_info['release_stage']))
        self.lineEdit_review_status.setText(str(self.drawing_info['review_status']))
        self.lineEdit_planned_release_date.setText(str(self.drawing_info['planned_release_date']))

    def info_changabilty_checked(self, btn):
        self.lineEdit_drawing_no.setReadOnly(self.checkBox_info_changabilty.isChecked())
        self.lineEdit_database_series_no.setReadOnly(self.checkBox_info_changabilty.isChecked())
        self.lineEdit_drawing_title.setReadOnly(self.checkBox_info_changabilty.isChecked())
        self.lineEdit_profession.setReadOnly(self.checkBox_info_changabilty.isChecked())
        self.lineEdit_profession_subvol.setReadOnly(self.checkBox_info_changabilty.isChecked())
        self.lineEdit_drawing_integrity.setReadOnly(self.checkBox_info_changabilty.isChecked())
        self.lineEdit_release_stage.setReadOnly(self.checkBox_info_changabilty.isChecked())
        self.lineEdit_review_status.setReadOnly(self.checkBox_info_changabilty.isChecked())
        self.lineEdit_planned_release_date.setReadOnly(self.checkBox_info_changabilty.isChecked())
