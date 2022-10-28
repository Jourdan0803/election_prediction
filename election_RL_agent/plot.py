#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import matplotlib.pyplot as plt
import matplotlib



"""
left:x coordinate of the rectangle middle point
height: height of rectangle
width: width of rectangle ，default is 0.8
"""
state_list = ['CA', 'FL', 'GA', 'IL', 'MI', 'NY', 'NC', 'OH', 'PA', 'TX']
trump_in_state = [7138, 4173, 912, 1892, 1127, 6523, 1287, 1044, 2280, 3918]
biden_in_state = [9086, 4584, 426, 1432, 394, 5121, 492, 879, 1544, 3796]
x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
font = {'family': 'Times New Roman', 'weight': 'normal', 'size': 12}
font_title = {'family': 'Times New Roman', 'weight': 'normal', 'size': 15}
rects1 = plt.bar(x=x, height=trump_in_state, width=0.7, color='red', label="Trump")
rects2 = plt.bar(x=[i + 0.7 for i in x], height=biden_in_state, width=0.7, color='blue', label="Biden")

# for a, b in zip(x, trump_in_state):
#     plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=29)
plt.ylim(0, 10000)  # y轴取值范围
plt.ylabel("Tweets", font)
plt.xlabel("States code", font)
plt.title("Number of Tweets from 10 Most Populous States of the US", font_title)
"""
设置x轴刻度显示值
参数一：中点坐标
参数二：显示值
"""
plt.xticks([index + 0.2 for index in x], state_list)


plt.legend()  # 设置题注
# 编辑文本
for rect in rects1:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
for rect in rects2:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
plt.show()
