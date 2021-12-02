import sys
if sys.version_info[0] == 3:
    import tkinter as tk

import matplotlib.pyplot as plt

import IMGBB

main_dict = {'09:56:05': 56698.1, '09:56:08': 56698.1, '09:56:14': 56698.1, '09:56:21': 56698.1, '09:56:30': 56717.81, '09:56:39': 56717.81, '09:56:50': 56736.35, '09:57:02': 56750.24, '09:57:08': 56750.24, '09:57:14': 56750.24}

x = []
y= []

for key in main_dict.keys():
    x.append(key)

for value in main_dict.values():
    y.append(value)

plt.plot(x,y)
plt.tick_params(axis='x', which='major',labelsize=7)
plt.xlabel('Time (PST)')
plt.ylabel('USD')
plt.title('Recent BTC Trend Graph')
plt.savefig('recent_trend.png')
IMGBB.url_call()