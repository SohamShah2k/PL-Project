import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import *
from db_connect import mysql as ms
import datetime
from HistGraph import HistGraph
class HistoricalAnomaly(tk.Frame):
    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        menu = Frame(self)
        self.sql = ms()
        self.mycursor = self.sql.mycursor
        self.db = self.sql.mydb
        l = Label(menu, text="Menu: ").pack(side=LEFT)
        bb = Button(menu, text="Landing page", command=lambda: obj.display_page(obj.Landing)).pack(side=LEFT)

        bd = Button(menu, text="Realtime Graph", command=lambda: obj.display_page(obj.RealTime)).pack(side=LEFT)
        menu.pack()
        l1 = Label(self, text="Historical Graph selection").pack()
        c_sel = StringVar()
        crypto_frame = Frame(self)
        currencies = self.sql.currencies
        start_date = datetime.datetime.now()
        l2 = Label(crypto_frame, text="Select Crypto Currency: ").pack(side=LEFT)
        sel1 = ttk.Combobox(crypto_frame, values=list(currencies.keys()), textvariable=c_sel).pack(side=LEFT)
        def coin_sel(c_sel):
            self.coin = c_sel
            print(self.coin)

        selb = Button(crypto_frame, text="Select", command=lambda : coin_sel(c_sel.get())).pack(side=LEFT)
        crypto_frame.pack()
        b = Button(self, text='OK', command=lambda: self.HistoricGraph()).pack()

    def HistoricGraph(self):
        HistGraph(self.coin)



