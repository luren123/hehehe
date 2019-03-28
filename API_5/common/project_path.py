# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 21:24
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : project_path.py
import os
#文件的路径 放到这里
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# print(project_path)
#测试用例的路径
case_path=os.path.join(project_path,'test_cases','接口测试第五阶段测试用例.xlsx')
# print(case_path)

#测试报告的路径
report_path=os.path.join(project_path,'conf1','test_report.html')
# print(report_path)
# 日志的路径
# log_path=os.path.join(project_path,'conf1','test.log')
# print(log_path)
#配置文件的路径
conf_path=os.path.join(project_path,'conf1','case.conf')
# print(conf_path)