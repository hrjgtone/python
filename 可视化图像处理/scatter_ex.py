# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from openpyxl import *

# from openpyxl import load_workbook


# ---------------------------------------------------------------------
#   从文本中提取数据
#   数据关键字：时间X、站点Y
#
# ---------------------------------------------------------------------

data_wb = load_workbook('分析后数据表.xlsx')
data_ws = data_wb['Sheet']
# 建立车站列表，自东莞火车站虎门火车站（0-14），车辆段15，控制中心16，旗峰主所17，厚街主所18，区间19
datad_station = {'dgz': '0', 'csz': '0', 'lhz': '0', 'xqz': '0', 'tbz': '0', 'dcz': '0', 'qfz': '0', 'hfz': '0',
                 'xpz': '0', 'hdz': '0', 'cwz': '0', 'lxz': '0', 'smz': '0', 'zlz': '0', 'hmz': '0', 'socc': '0',
                 'occ': '0', 'qfzs': '0', 'hjzs': '0', 'qj': '0', }
for data_ws_i in range(data_ws.max_row):
    if data_ws.cell(data_ws_i + 1, 7).value == '东莞站':
        datad_station['dgz'] = int(datad_station['dgz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '茶山站':
        datad_station['csz'] = int(datad_station['csz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '榴花站':
        datad_station['lhz'] = int(datad_station['lhz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '下桥站':
        datad_station['xqz'] = int(datad_station['xqz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '天宝站':
        datad_station['tbz'] = int(datad_station['tbz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '东城站':
        datad_station['dcz'] = int(datad_station['dcz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '旗峰站':
        datad_station['qfz'] = int(datad_station['qfz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '鸿福站':
        datad_station['hfz'] = int(datad_station['hfz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '西平站':
        datad_station['xpz'] = int(datad_station['xpz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '蛤地站':
        datad_station['hdz'] = int(datad_station['hdz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '陈屋站':
        datad_station['cwz'] = int(datad_station['cwz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '寮夏站':
        datad_station['lxz'] = int(datad_station['lxz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '珊美站':
        datad_station['smz'] = int(datad_station['smz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '展览站':
        datad_station['zlz'] = int(datad_station['zlz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '虎门站':
        datad_station['hmz'] = int(datad_station['hmz']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '车辆段':
        datad_station['socc'] = int(datad_station['socc']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '西平控制中心':
        datad_station['occ'] = int(datad_station['occ']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '旗峰主所':
        datad_station['qfzs'] = int(datad_station['qfzs']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '厚街主所':
        datad_station['hjzs'] = int(datad_station['hjzs']) + 1
    elif data_ws.cell(data_ws_i + 1, 7).value == '区间':
        datad_station['qj'] = int(datad_station['qj']) + 1

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5), plt.xticks([])
plt.ylim(-1.5, 1.5), plt.yticks([])

plt.show()
