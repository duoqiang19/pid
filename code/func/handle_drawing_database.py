# pid - handle_drawing_database
# 2020/2/2 - 22:31
# Copyright 2020 Wang D.Q <Wang D.Q@PyCharm>
# !/venv python
# -*- coding: utf-8 -*-

import openpyxl

class Handle_drawing_database():

    def __init__(self, address):
        self.address = address
        self.book = openpyxl.load_workbook(self.address)
        self.sheet = self.book['出图详细']

    def read_drawing_info(self, drawing_no):
        drawing_info = {}
        column_titles = ['database_series_no', 'profession', 'vol_title',
            'drawing_no', 'drawing_title', 'drawing_integrity',
            'release_stage', 'review_status', 'planned_release_date',
            'r1_review_date', 'r1_review_no', 'r1_feedback_date', 'r1_feedback',
            'r2_review_date', 'r2_review_no', 'r2_feedback_date', 'r2_feedback',
            'r3_review_date', 'r3_review_no', 'r3_feedback_date', 'r3_feedback',
            'mark_1', 'mark_2', 'mark_3']
        for row in list(self.sheet.rows):
            for cell in row:
                if cell.value == drawing_no:
                    for element in list(self.sheet.rows)[cell.row-1]:
                        column_title = self.cn_eng(list(self.sheet.rows)[2][element.column-1].value)
                        if column_title in column_titles:
                            drawing_info[column_title] = element.value
                    return drawing_info

    def cn_eng(self, var):
        return {
            '序号': 'database_series_no', '专业': 'profession', '专业分卷': 'vol_title',
            '图号': 'drawing_no', '施工图卷册名称': 'drawing_title', '出版状态': 'drawing_integrity',
            '出图阶段': 'release_stage', '审核状态': 'review_status', '出图计划2019': 'planned_release_date',
            '1轮送审时间': 'r1_review_date', '1轮文件号': 'r1_review_no', '1轮反馈时间': 'r1_feedback_date', '1轮审查结果': 'r1_feedback',
            '2轮送审时间': 'r2_review_date', '2轮文件号': 'r2_review_no', '2轮反馈时间': 'r2_feedback_date', '2轮审查结果': 'r2_feedback',
            '3轮送审时间': 'r3_review_date', '3轮文件号': 'r3_review_no', '3轮反馈时间': 'r3_feedback_date', '3轮审查结果': 'r3_feedback',
            # '施工单位需求【1.9版】': 'mark_1', '出图计划 【2.10更新】': 'mark_2', '备注': 'mark_3',
        }.get(var, 'error')

if __name__ == '__main__':
    import sys, os

    database_address = str(
        os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "/data/drawings.xlsx").replace(
        "\\", "/")
    # os.getcwd() 方法用于返回当前项目工作目录。
    # os.path.dirname(path) 去掉文件名，返回目录
    # os.path.abspath(path) 返回绝对路径
    # __file__ 当前文件的绝对路径
    test_drawing_info = {'drawing_no':'T0711'}
    test_run = Handle_drawing_database(database_address)
    print(test_run.read_drawing_info(test_drawing_info['drawing_no']))


