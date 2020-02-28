# pid - handle_new_review_flow
# 2020/1/31 - 22:59
# Copyright 2020 Wang D.Q <Wang D.Q@PyCharm>
# !/venv python
# -*- coding: utf-8 -*-
import sys, os
import json
folder_path = os.path.abspath(os.path.dirname(os.getcwd()))
database_address_json = str(
        os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) + "/data/drawings.json").replace(
        "\\", "/")

class Handle_new_review_flow():

    def __init__(self, address_json):
        self.address_json = address_json

    def write_new_in_json(self, flow_info):
        with open(self.address_json, 'w') as self.json:
            json.dump(flow_info, self.json, ensure_ascii=False, indent='\t')

    def read_new_review_flow():
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

if __name__ == '__main__':
    numbers = {
            '序号': 'database_series_no', '专业': 'profession', '专业分卷': 'vol_title',
            '图号': 'drawing_no', '施工图卷册名称': 'drawing_title', '出版状态': 'drawing_integrity',
            '出图阶段': 'release_stage', '审核状态': 'review_status', '出图计划2019': 'planned_release_date',
            '1轮送审时间': 'r1_review_date', '1轮文件号': 'r1_review_no', '1轮反馈时间': 'r1_feedback_date', '1轮审查结果': 'r1_feedback',
            '2轮送审时间': 'r2_review_date', '2轮文件号': 'r2_review_no', '2轮反馈时间': 'r2_feedback_date', '2轮审查结果': 'r2_feedback',
            '3轮送审时间': 'r3_review_date', '3轮文件号': 'r3_review_no', '3轮反馈时间': 'r3_feedback_date', '3轮审查结果': 'r3_feedback',
            # '施工单位需求【1.9版】': 'mark_1', '出图计划 【2.10更新】': 'mark_2', '备注': 'mark_3',
        }
    test_flow = Handle_new_review_flow(database_address_json)
    test_flow.write_new_in_json(numbers)


