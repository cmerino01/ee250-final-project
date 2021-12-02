import sys
if sys.version_info[0] == 3:
    import tkinter as tk

import matplotlib.pyplot as plt

import IMGBB

#this is just static, but should be obtained through tcp_server.py, it should be whatever the pickle/dict had
main_dict = {'09:56:05': 56698.1, '09:56:08': 56698.1, '09:56:14': 56698.1, '09:56:21': 56698.1, '09:56:30': 56717.81, '09:56:39': 56717.81, '09:56:50': 56736.35, '09:57:02': 56750.24, '09:57:08': 56750.24, '09:57:14': 56750.24}

#declare x and y lists
x = []
y= []

#go through and collect keys(timestamps)
for key in main_dict.keys():
    x.append(key)

#go through and collect values(values)
for value in main_dict.values():
    y.append(value)

#plot x and y
plt.plot(x,y)
#adjust x access size
plt.tick_params(axis='x', which='major',labelsize=7)
#set x label
plt.xlabel('Time (PST)')
#set y label
plt.ylabel('USD')
#set title
plt.title('Recent BTC Trend Graph')
#save the graph - very important that this file be in the same directory as IMGBB.py & tcp_server.py
plt.savefig('recent_trend.png')
#calls the api
IMGBB.url_call()