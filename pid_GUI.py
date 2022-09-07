#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:makang, ransa
# Description: 繪制PID交互曲線，可以觀察到Kp，Ki，Kd各參數對PID控制的影響  原作者是makang 在經過修改後可以直接輸入數值

import tkinter as tk
import PID
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np


# 繪圖函數
def drawPic():
    global r, g, b

    # 清空圖像，以使得前後兩次繪制的圖像不會重疊
    drawPic.f.clf()
    drawPic.a = drawPic.f.add_subplot(111)
    drawPic.a.grid(color='k', linestyle='-.')
    TestPID(Kp, Ki, Kd)

    # 每次繪圖改變線條顏色用以區別----第一種方法
    # drawPic.a.plot(PositionalXaxis, PositionalYaxis, color=(r, g, b) )  # 繪制圖形
    # r -= 0.15; g-=0.15; b-=0.15
    # if r < 0: r=0
    # if g < 0: g=0
    # if b < 0: b=0

    # 每次繪圖改變線條顏色用以區別----第二種方法
    color = ['b', 'r', 'y', 'g', 'grey', 'coral', 'darkgreen', 'c', 'cyan', 'steelblue']
    drawPic.a.plot(PositionalXaxis, PositionalYaxis, color=color[np.random.randint(len(color))] )  # 繪制圖形
    drawPic.canvas.draw()
    #每次繪圖完畢清空x，y
    PositionalXaxis.clear()
    PositionalYaxis.clear()


# 測試PID程序
def TestPID(P, I, D):
    global PositionalXaxis, PositionalYaxis, fig_num
    PositionalPid = PID.PositionalPID(P, I, D)
    for i in range(1, 500):
        # 位置式
        PositionalPid.SetStepSignal(100.2)
        PositionalPid.SetInertiaTime(3, 0.1)
        PositionalYaxis.append(PositionalPid.SystemOutput)
        PositionalXaxis.append(i)

#   改變Kp

def change_entry():
    global Kp ,Kp_entry, Ki, Ki_entry, Kd, Kd_entry, En_kp, En_ki, En_kd
    Kp = float(Kp_entry.get())
    Ki = float(Ki_entry.get())
    Kd = float(Kd_entry.get())
    var_kp.set('%.2f' % Kp)
    var_ki.set('%.2f' % Ki)
    var_kd.set('%.2f' % Kd) 
    drawPic()
    return Kp, Ki, Kd

def Kp_enlarge():
    global Kp, En_kp
    Kp += 0.05
    var_kp.set('%.2f'%Kp)
    drawPic()
    En_kp.set('%.2f'%Kp)
    return Kp
def Kp_reduce():
    global Kp, En_kp
    Kp -= 0.05
    if Kp<=0:
        Kp=0
    var_kp.set('%.2f'%Kp)
    drawPic()
    En_kp.set('%.2f'%Kp)
    return Kp

#   改變Ki
def Ki_enlarge():
    global Ki, En_ki
    Ki += 0.05
    var_ki.set('%.2f'%Ki)
    drawPic()
    En_ki.set('%.2f'%Ki)
    return Ki
def Ki_reduce():
    global Ki, En_ki
    Ki -= 0.05
    if Ki<=0:
        Ki=0
    var_ki.set('%.2f'%Ki)
    drawPic()
    En_ki.set('%.2f'%Ki)
    return Ki

#   改變Kd
def Kd_enlarge():
    global Kd, En_kd
    Kd += 0.05
    var_kd.set('%.2f'%Kd)
    drawPic()
    En_kd.set('%.2f'%Kd)
    return Kd
def Kd_reduce():
    global Kd, En_kd
    Kd -= 0.05
    if Kd<=0:
        Kd=0
    var_kd.set('%.2f'%Kd)
    drawPic()
    En_kd.set('%.2f'%Kd)
    return Kd


#   清空圖像
def clear_pic():
    global r, g, b
    drawPic.f.clf()
    drawPic.canvas.draw()
    drawPic.a = drawPic.f.add_subplot(111)
    r = 0.6;
    g = 0.8;
    b = 0.8

#   重置
def reset():
    global Kp, Ki, Kd, r, g, b
    drawPic.f.clf()
    drawPic.canvas.draw()
    Kp=0.1
    Ki=0.1
    Kd=0.1
    var_kp.set('%.2f' % Kp)
    En_kp.set('%.2f'%Kp)
    var_ki.set('%.2f' % Ki)
    En_ki.set('%.2f'%Ki)
    var_kd.set('%.2f' % Kd)
    En_kd.set('%.2f'%Kd)
    r = 0.6;
    g = 0.8;
    b = 0.8




if __name__ == '__main__':

    # 實例化object，建立窗口window
    window = tk.Tk()
    # 給窗口的可視化起名字
    window.title('PID_Display')
    # 設定窗口的大小(長 * 寬)
    window.geometry('800x760')  # 這里的乘是小x
    plt.use('TkAgg')


    En_kp = tk.StringVar()    
    En_ki = tk.StringVar()
    En_kd = tk.StringVar()

    var_kp = tk.StringVar()    
    var_ki = tk.StringVar()
    var_kd = tk.StringVar()
    Kp=0.1
    Ki=0.1
    Kd=0.1
    var_kp.set('%.2f' % Kp)
    var_ki.set('%.2f' % Ki)
    var_kd.set('%.2f' % Kd)
    PositionalXaxis = [0]
    PositionalYaxis = [0]

    #定義顏色
    r=0.6; g=0.8; b=0.8

    # 繪圖區域
    pic_area = tk.Label(window, bg='grey')
    pic_area.place(x=0, y=0, width='800', height='620')
    # 在Tk的GUI上放置一個畫布
    drawPic.f = Figure(figsize=(5, 4), dpi=100)
    drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=pic_area)
    drawPic.canvas.draw()
    drawPic.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    #調節控件
    Kp_entry = tk.Entry(justify='center', textvariable=En_kp,bg='grey')
    Kp_entry.place(x=20, y=680, width='50',height='50',)
    Kp_add_Btn = tk.Button(window, text='Kp Enlarge', font=('Arial', 10), width=10, height=1, command=Kp_enlarge)
    Kp_add_Btn.place(x=80, y=620, width='100', height='30')
    Kp_down_Btn = tk.Button(window,text='Kp Reduce', font=('Arial', 10), width=10, height=1, command=Kp_reduce)
    Kp_down_Btn.place(x=80, y=660, width='100', height='30')
    Kp_label = tk.Label(textvariable=var_kp, bg='grey')
    Kp_label.place(x=20, y= 630, width='50', height='50')


    Ki_entry = tk.Entry(justify='center', textvariable=En_ki,bg='grey')
    Ki_entry.place(x=210, y=680, width='50', height='50')
    Ki_add_Btn = tk.Button(window, text='Ki Enlarge', font=('Arial', 10), width=10, height=1, command=Ki_enlarge)
    Ki_add_Btn.place(x=270, y=620, width='100', height='30')
    Ki_down_Btn = tk.Button(window,text='Ki Reduce', font=('Arial', 10), width=10, height=1, command=Ki_reduce)
    Ki_down_Btn.place(x=270, y=660, width='100', height='30')
    Ki_label = tk.Label(textvariable=var_ki, bg='grey')
    Ki_label.place(x=210, y= 630, width='50', height='50')

    Kd_entry = tk.Entry(justify='center', textvariable=En_kd,bg='grey')
    Kd_entry.place(x=400, y=680, width='50', height='50')
    Kd_add_Btn = tk.Button(window, text='Kd Enlarge', font=('Arial', 10), width=10, height=1, command=Kd_enlarge)
    Kd_add_Btn.place(x=460, y=620, width='100', height='30')
    Kd_down_Btn = tk.Button(window,text='Kd Reduce', font=('Arial', 10), width=10, height=1, command=Kd_reduce)
    Kd_down_Btn.place(x=460, y=660, width='100', height='30')
    Kd_label = tk.Label(textvariable=var_kd, bg='grey')
    Kd_label.place(x=400, y= 630, width='50', height='50')

    Entry_enter = tk.Button(window, text='EnterValue', font=('Arial', 10), width=10, height=1, command=change_entry)
    Entry_enter.place(x=580, y=690, width='100', height='70')

    Clear_Btn = tk.Button(window, text='Clear', font=('Arial', 10), width=10, height=1, command=clear_pic)
    Clear_Btn.place(x=580, y=620, width='100', height='70')

    Reset_Btn = tk.Button(window, text='Reset', font=('Arial', 10), width=10, height=1, command=reset)
    Reset_Btn.place(x=680, y=620, width='100', height='70')
    window.mainloop()









    # 注意，loop因為是循環的意思，window.mainloop就會讓window不斷的刷新，如果沒有mainloop,就是一個靜態的window,傳入進去的值就不會有循環，mainloop就相當於一個很大的while循環，有個while，每點擊一次就會更新一次，所以我們必須要有循環
    # 所有的窗口文件都必須有類似的mainloop函數，mainloop是窗口文件的關鍵的關鍵。
