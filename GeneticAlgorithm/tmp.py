
from tkinter import *
from Genetic_Function import *
import tkinter
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import random
import time
from matplotlib import pyplot as plt
from matplotlib import animation


class RegrMagic(object):
    """Mock for function Regr_magic()
    """

    def __init__(self):
        self.x = 0
        self.y=0

    def __call__(self):
        #time.sleep(random.random())
        self.x += 1
        self.y+=1
        return self.x, self.y


class App:
    x_lab = []  # x축 값
    y_lab = []  # y축 값
    x=[]
    y=[]
    t = plt
    regr_magic = RegrMagic()
    def __init__(self):
        self.window = Tk()
        self.tt = Label(self.window, text="비밀 번호를 입력하세요:")
        self.e1 = Entry(self.window)
        self.tt.pack()
        self.e1.pack()

        self.resultButton = Button(self.window, text="시작", command=self.startGenetic)
        self.resultButton.pack()

        self.window.mainloop()

    def animate(self, args):
        if(args[0]==10):
            self.anim.event_source.stop()
        self.x.append(args[0])
        self.y.append(args[1])
        return plt.plot(self.x, self.y, color='g')

    def frames(self):
        while True:
            yield self.regr_magic()

    def startGenetic(self):
        self.fig = self.t.figure(figsize=(5, 4), dpi=100)

        canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        canvas.get_tk_widget().pack()

        self.ax1 = self.fig.add_subplot(1,1,1)

        self.anim = animation.FuncAnimation(self.fig, self.animate, frames=self.frames, interval=1000)
        self.resultButton.configure(state='disabled')


App()


