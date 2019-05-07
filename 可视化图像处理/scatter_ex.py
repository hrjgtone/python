# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
from openpyxl import *
#from openpyxl import load_workbook



# ---------------------------------------------------------------------
#   从文本中提取数据
#   数据关键字：时间X、站点Y
#
# ---------------------------------------------------------------------

date_wb = load_workbook('分析后数据表.xlsx')
date_ws = date_wb['Sheet']
#建立车站列表，自东莞火车站虎门火车站（0-14），车辆段15，控制中心16，旗峰主所17，厚街主所18，区间19
dated_station= {'dgz' : '0', 'csz' : '0', 'lhz' : '0', 'xqz' : '0', 'tbz' : '0', 'dcz' : '0', 'qfz' : '0', 'hfz' : '0', 'xpz' : '0', 'hdz' : '0', 'cwz' : '0', 'lxz' : '0', 'smz' : '0', 'zlz' : '0', 'hmz' : '0', 'socc' : '0', 'occ' : '0', 'qfzs' : '0', 'hjzs' : '0', 'qj' : '0',}
for date_ws_i in range(date_ws.max_row):
    if date_ws.cell(date_ws_i+1,7).value == '东莞站':
        dated_station['dgz'] = int (dated_station['dgz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '茶山站':
        dated_station['csz'] = int (dated_station['csz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '榴花站':
        dated_station['lhz'] = int (dated_station['lhz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '下桥站':
        dated_station['xqz'] = int (dated_station['xqz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '天宝站':
        dated_station['tbz'] = int (dated_station['tbz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '东城站':
        dated_station['dcz'] = int (dated_station['dcz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '旗峰站':
        dated_station['qfz'] = int (dated_station['qfz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '鸿福站':
        dated_station['hfz'] = int (dated_station['hfz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '西平站':
        dated_station['xpz'] = int (dated_station['xpz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '蛤地站':
        dated_station['hdz'] = int (dated_station['hdz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '陈屋站':
        dated_station['cwz'] = int (dated_station['cwz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '寮夏站':
        dated_station['lxz'] = int (dated_station['lxz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '珊美站':
        dated_station['smz'] = int (dated_station['smz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '展览站':
        dated_station['zlz'] = int (dated_station['zlz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '虎门站':
        dated_station['hmz'] = int (dated_station['hmz'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '车辆段':
        dated_station['socc'] = int (dated_station['socc'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '西平控制中心':
        dated_station['occ'] = int (dated_station['occ'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '旗峰主所':
        dated_station['qfzs'] = int (dated_station['qfzs'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '厚街主所':
        dated_station['hjzs'] = int (dated_station['hjzs'])+1
    elif date_ws.cell(date_ws_i+1,7).value == '区间':
        dated_station['qj'] = int (dated_station['qj'])+1



n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)

plt.axes([0.025,0.025,0.95,0.95])
plt.scatter(X,Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5,1.5), plt.xticks([])
plt.ylim(-1.5,1.5), plt.yticks([])

plt.show()
