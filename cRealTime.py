import tkinter as tk
from tkinter import *
import cRealGraph
from tkinter import ttk
from db_connect import mysql as ms
from PIL import Image,ImageTk


class RealTime(ttk.Frame):

    def __init__(self, window, obj):
        ttk.Frame.__init__(self, window)

        self.sql = ms()

        bg = Image.open('a.png')

        rt_can = Canvas(window, width=1280, height=720)
        rt_can.image = ImageTk.PhotoImage(bg)
        rt_can.create_image(0, 0, image=rt_can.image, anchor = 'nw')
        rt_can.grid(row=0, column=0, sticky="nsew")
        #l = ttk.Label(menu, text="Menu: ").pack(side=LEFT)
        rt_can.create_text(250,100,anchor = 'w',text = "Menu:", fill=ms.color, font = ms.font)
        bb = ttk.Button(window, text="Landing",width = 15,command=lambda: obj.display_page(obj.Landing))#.pack(side=LEFT)
        bd = ttk.Button(window, text="HistoricalAnomaly",width = 15, command=lambda: obj.display_page(obj.HistoricalAnomaly))#.pack(side=LEFT)
        bt = ttk.Button(window, text="Trade", width=15,command=lambda: obj.display_page(obj.Trade))
        rt_can.create_window(450,100,anchor = 'w',window = bb)
        rt_can.create_window(650, 100 ,anchor = 'w',window=bd)
        rt_can.create_window(850, 100,anchor = 'w', window=bt)

        rt_can.create_text(650,200,text = "Realtime Graphe selection", fill=ms.color, font = ms.font)
        c_sel = StringVar()
        currencies = self.sql.currencies
        rt_can.create_text(600, 300,anchor = 'e', text="Select Crypto Currency: ", fill=ms.color, font=ms.font)
        rt_can.create_text(600, 400,anchor = 'e', text="Enter sensitivity for \npump detection in percentage: ", fill=ms.color, font=ms.font)
        self.paisa = ''

        def coin_sel(c_sel):
            x = c_sel.get()
            print("c_sel : ", x)
            global paisa
            self.paisa = currencies[x][0]
            print(self.paisa)
            self.sensitivity = sens.get() / 100

        sel1 = ttk.Combobox(window, values=list(currencies.keys()), textvariable=c_sel)
        rt_can.create_window(700, 300,anchor = 'w', window=sel1)
        print(self.paisa)

        sens = IntVar()
        sen = ttk.Entry(window, textvariable=sens)
        rt_can.create_window(700, 400,anchor = 'w', window=sen)
        selb = ttk.Button(window, text="Select", command=lambda: coin_sel(c_sel))
        rt_can.create_window(900, 400, window=selb)

        b = ttk.Button(window, text='OK', command=lambda: cRealGraph.RealGraph(self.paisa, self.sensitivity))
        rt_can.create_window(650, 500, window=b)

        #window.grid()#row=0, column=0, sticky="nsew")
        #menu.pack()
        #l1 = ttk.Label(self,text="Realtime Graphe selection").pack()








