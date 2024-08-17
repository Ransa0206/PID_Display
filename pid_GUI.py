import customtkinter as ctk
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

    # 每次繪圖改變線條顏色用以區別
    color = ['b', 'r', 'y', 'g', 'grey', 'coral', 'darkgreen', 'c', 'cyan', 'steelblue']
    drawPic.a.plot(PositionalXaxis, PositionalYaxis, color=color[np.random.randint(len(color))])  # 繪制圖形
    drawPic.canvas.draw()
    #每次繪圖完畢清空x，y
    PositionalXaxis.clear()
    PositionalYaxis.clear()

# 測試PID程序
def TestPID(P, I, D):
    global PositionalXaxis, PositionalYaxis
    PositionalPid = PID.PositionalPID(P, I, D)
    for i in range(1, 500):
        # 位置式
        PositionalPid.SetStepSignal(100.2)
        PositionalPid.SetInertiaTime(3, 0.1)
        PositionalYaxis.append(PositionalPid.SystemOutput)
        PositionalXaxis.append(i)

def change_entry():
    global Kp, Ki, Kd
    Kp = float(Kp_entry.get())
    Ki = float(Ki_entry.get())
    Kd = float(Kd_entry.get())
    var_kp.set(f'{Kp:.2f}')
    var_ki.set(f'{Ki:.2f}')
    var_kd.set(f'{Kd:.2f}') 
    drawPic()
    return Kp, Ki, Kd

# Functions to adjust Kp, Ki, and Kd
def Kp_enlarge():
    global Kp
    Kp += 0.05
    var_kp.set(f'{Kp:.2f}')
    drawPic()
    En_kp.set(f'{Kp:.2f}')
    return Kp

def Kp_reduce():
    global Kp
    Kp -= 0.05
    if Kp <= 0:
        Kp = 0
    var_kp.set(f'{Kp:.2f}')
    drawPic()
    En_kp.set(f'{Kp:.2f}')
    return Kp

def Ki_enlarge():
    global Ki
    Ki += 0.05
    var_ki.set(f'{Ki:.2f}')
    drawPic()
    En_ki.set(f'{Ki:.2f}')
    return Ki

def Ki_reduce():
    global Ki
    Ki -= 0.05
    if Ki <= 0:
        Ki = 0
    var_ki.set(f'{Ki:.2f}')
    drawPic()
    En_ki.set(f'{Ki:.2f}')
    return Ki

def Kd_enlarge():
    global Kd
    Kd += 0.05
    var_kd.set(f'{Kd:.2f}')
    drawPic()
    En_kd.set(f'{Kd:.2f}')
    return Kd

def Kd_reduce():
    global Kd
    Kd -= 0.05
    if Kd <= 0:
        Kd = 0
    var_kd.set(f'{Kd:.2f}')
    drawPic()
    En_kd.set(f'{Kd:.2f}')
    return Kd

# Function to clear the plot
def clear_pic():
    global r, g, b
    drawPic.f.clf()
    drawPic.canvas.draw()
    drawPic.a = drawPic.f.add_subplot(111)
    r = 0.6
    g = 0.8
    b = 0.8

# Function to reset the PID values
def reset():
    global Kp, Ki, Kd, r, g, b
    drawPic.f.clf()
    drawPic.canvas.draw()
    Kp = 0.1
    Ki = 0.1
    Kd = 0.1
    var_kp.set(f'{Kp:.2f}')
    En_kp.set(f'{Kp:.2f}')
    var_ki.set(f'{Ki:.2f}')
    En_ki.set(f'{Ki:.2f}')
    var_kd.set(f'{Kd:.2f}')
    En_kd.set(f'{Kd:.2f}')
    r = 0.6
    g = 0.8
    b = 0.8

if __name__ == '__main__':
    # Initialize the main window using customtkinter
    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
    
    window = ctk.CTk()
    window.title('PID_Display')
    window.geometry('580x620')  # Set the window size
    window.resizable(0, 0)
    
    En_kp = ctk.StringVar()    
    En_ki = ctk.StringVar()
    En_kd = ctk.StringVar()

    var_kp = ctk.StringVar()    
    var_ki = ctk.StringVar()
    var_kd = ctk.StringVar()
    Kp = 0.1
    Ki = 0.1
    Kd = 0.1
    var_kp.set(f'{Kp:.2f}')
    var_ki.set(f'{Ki:.2f}')
    var_kd.set(f'{Kd:.2f}')
    PositionalXaxis = [0]
    PositionalYaxis = [0]

    # Define color variables
    r = 0.6
    g = 0.8
    b = 0.8

    # Drawing area
    pic_area = ctk.CTkFrame(window, fg_color='grey', width=800, height=620)
    pic_area.place(x=20, y=0)  # Removed width and height from place method

    
    drawPic.f = Figure(figsize=(5, 4), dpi=100)
    drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=pic_area)
    drawPic.canvas.draw()
    drawPic.canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)

    # Control widgets
    Kp_entry = ctk.CTkEntry(master=window, justify='center', textvariable=En_kp, fg_color='grey', width=50, height=50)
    Kp_entry.place(x=20, y=480)
    Kp_add_Btn = ctk.CTkButton(window, text='Kp Enlarge', command=Kp_enlarge, width=100, height=30)
    Kp_add_Btn.place(x=80, y=420)
    Kp_down_Btn = ctk.CTkButton(window, text='Kp Reduce', command=Kp_reduce, width=100, height=30)
    Kp_down_Btn.place(x=80, y=460)
    Kp_label = ctk.CTkLabel(window, textvariable=var_kp, fg_color='grey', width=50, height=50)
    Kp_label.place(x=20, y=420)

    Ki_entry = ctk.CTkEntry(master=window, justify='center', textvariable=En_ki, fg_color='grey', width=50, height=50)
    Ki_entry.place(x=210, y=480)
    Ki_add_Btn = ctk.CTkButton(window, text='Ki Enlarge', command=Ki_enlarge, width=100, height=30)
    Ki_add_Btn.place(x=270, y=420)
    Ki_down_Btn = ctk.CTkButton(window, text='Ki Reduce', command=Ki_reduce, width=100, height=30)
    Ki_down_Btn.place(x=270, y=460)
    Ki_label = ctk.CTkLabel(window, textvariable=var_ki, fg_color='grey', width=50, height=50)
    Ki_label.place(x=210, y=420)

    Kd_entry = ctk.CTkEntry(master=window, justify='center', textvariable=En_kd, fg_color='grey', width=50, height=50)
    Kd_entry.place(x=400, y=480)
    Kd_add_Btn = ctk.CTkButton(window, text='Kd Enlarge', command=Kd_enlarge, width=100, height=30)
    Kd_add_Btn.place(x=460, y=420)
    Kd_down_Btn = ctk.CTkButton(window, text='Kd Reduce', command=Kd_reduce, width=100, height=30)
    Kd_down_Btn.place(x=460, y=460)
    Kd_label = ctk.CTkLabel(window, textvariable=var_kd, fg_color='grey', width=50, height=50)
    Kd_label.place(x=400, y=420)

    Entry_enter = ctk.CTkButton(window, text='EnterValue', command=change_entry, width=90, height=60)
    Entry_enter.place(x=120, y=550)

    Clear_Btn = ctk.CTkButton(window, text='Clear', command=clear_pic, width=90, height=60)
    Clear_Btn.place(x=220, y=550)

    Reset_Btn = ctk.CTkButton(window, text='Reset', command=reset, width=90, height=60)
    Reset_Btn.place(x=320, y=550)

    devby = ctk.CTkLabel(window,text=" | Dev By: Ransa | ")
    devby.place(x=450, y=580)
    
    window.mainloop()
