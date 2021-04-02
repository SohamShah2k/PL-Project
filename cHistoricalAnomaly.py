import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import *
from db_connect import mysql as ms
from ttkthemes import themed_tk as tk1
import datetime
from cHistGraph import HistGraph
from PIL import Image,ImageTk



class HistoricalAnomaly(ttk.Frame):
    def __init__(self, window, obj):
        ttk.Frame.__init__(self, window)

        self.sql = ms()


        bg = Image.open('a.png')

        hg_can = Canvas(window, width=1280, height=720)

        hg_can.image = ImageTk.PhotoImage(bg)
        hg_can.create_image(0, 0, image=hg_can.image, anchor='nw')
        hg_can.grid(row=0, column=0, sticky="nsew")

        hg_can.create_text(250, 100, anchor='w', text="Menu:", fill=ms.color, font=ms.font)
        bb = ttk.Button(window, text="Landing", width=15,command=lambda: obj.display_page(obj.Landing))  # .pack(side=LEFT)
        bd = ttk.Button(window, text="Trade", width=15,command=lambda: obj.display_page(obj.Trade))  # .pack(side=LEFT)

        bt = ttk.Button(window, text="Realtime Graph",command=lambda: obj.display_page(obj.RealTime))  # .pack(side=LEFT)
        hg_can.create_window(450, 100, anchor='w', window=bb)
        hg_can.create_window(650, 100, anchor='w', window=bd)
        hg_can.create_window(850, 100, anchor='w', window=bt)

        hg_can.create_text(640, 200, text="Historical Graph selection", fill=ms.color, font=ms.font)

        c_sel = StringVar()

        currencies = self.sql.currencies
        start_date = datetime.datetime.now()
        hg_can.create_text(550, 300, anchor='e', text="Select Crypto Currency: ", fill=ms.color, font=ms.font)

        sel1 = ttk.Combobox(window, values=list(currencies.keys()), textvariable=c_sel)
        hg_can.create_window(600, 300, anchor='w', window=sel1)

        def coin_sel(c_sel):
            self.coin = c_sel
            print(self.coin)

        selb = ttk.Button(window, text="Select", command=lambda: coin_sel(c_sel.get()))
        hg_can.create_window(850, 300, window=selb)
        b = ttk.Button(window, text='OK', command=lambda: self.HistoricGraph())
        hg_can.create_window(650, 400, window=b)









    def HistoricGraph(self):
        HistGraph(self.coin)



