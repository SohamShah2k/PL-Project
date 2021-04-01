from tkinter import *
import tkinter as tk
from tkinter import ttk
from cHistoricalAnomaly import HistoricalAnomaly
from cRealTime import RealTime
from cTrade import Trade
from tkinter import ttk
from ttkthemes import themed_tk as tk1
from PIL import Image,ImageTk

from db_connect import mysql as ms
#import RealGraph as rg
#from RealGraph import RealGraph
#import matplotlib.animation as animation

class landing(tk1.ThemedTk):
    def __init__(self, uname ,*args, **kwargs):
        tk1.ThemedTk.__init__(self, *args, **kwargs)
        self.set_theme('equilux')
        self.uname = uname
        #window = self
        window = Frame(self)
        self.window = window
        self.HistoricalAnomaly = HistoricalAnomaly
        self.RealTime = RealTime
        self.Landing = Landing
        self.Trade = Trade
        #bg = PhotoImage(file='b.png')
        #print(type(bg))
        #land_can = Canvas(window, width=1280, height=720)
        #land_can.grid(row=0, column=0, sticky="nsew")
        #land_can.create_image(0, 0, image=bg, anchor='nw')
        #self.HistGraph = HistGraph
        #self.RealGraph = RealGraph
        #window.grid()
        #window.grid_rowconfigure(0, weight=1)
        #window.grid_columnconfigure(0, weight=1)
        self.display_page(Landing)

    def display_page(self, sel):
        """if(sel == RealGraph):
            page = sel(self.window, self,self.anime)
        else:"""
        page = sel(self.window,self)
        page.grid(row=0, column=0, sticky="nsew")




class Landing(ttk.Frame):

    def __init__(self,window,obj):
        ttk.Frame.__init__(self,window)
        bg = Image.open('a.png')

        land_can = Canvas(window,width = 1280, height = 720)
        land_can.image = ImageTk.PhotoImage(bg)
        land_can.grid(row=0, column=0, sticky="nsew")

        land_can.create_image(0, 0, image=land_can.image, anchor='nw')

        land_can.create_text(640, 200, text=" Welcome  {} ".format(obj.uname), fill=ms.color, font=ms.font)
        bb = ttk.Button(window,text="Check Historical Anomalies",command=lambda: obj.display_page(HistoricalAnomaly))#.pack()#, command=lambda: obj.display_page(Buy)
        bs = ttk.Button(window, text="Check Real time prices/anomalies",command=lambda: obj.display_page(RealTime))#.pack()#, command=lambda: obj.display_page(Sell)
        bt = ttk.Button(window, text="Trade", command=lambda: obj.display_page(Trade))
        land_can.create_window(640,300, window = bb)
        land_can.create_window(640, 400, window= bs)
        land_can.create_window(640, 500, window=bt)
        window.grid()



class land():
    def __init__(self,uname):

        landp = landing(uname)
        landp.geometry('1280x720')
        #landp.title("Landing page")
        #landp.wm_attributes('-transparentcolor','white')
        #ani = animation.FuncAnimation(rg.f, rg.animate, interval=1000)
        landp.mainloop()
##C:\gui\ary(1)