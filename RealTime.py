import tkinter as tk
from tkinter import *
import RealGraph
from tkinter import ttk
from db_connect import mysql as ms
class RealTime(tk.Frame):
    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        menu = Frame(self)
        self.sql = ms()
        self.mycursor = self.sql.mycursor
        self.db = self.sql.mydb
        l = Label(menu, text="Menu: ").pack(side=LEFT)
        bb = Button(menu, text="Landing", command=lambda: obj.display_page(obj.Landing)).pack(side=LEFT)
        bd = Button(menu, text="HistoricalAnomaly", command=lambda: obj.display_page(obj.HistoricalAnomaly)).pack(side=LEFT)
        menu.pack()
        l1 = Label(self,text="Realtime Graphe selection").pack()
        c_sel = StringVar()
        crypto_frame = Frame(self)
        currencies = self.sql.currencies
        l2 = Label(crypto_frame, text="Select Crypto Currency: ").pack(side=LEFT)
        self.paisa = ''
        def coin_sel(c_sel):
            x = c_sel.get()
            print("c_sel : ",x)
            global paisa
            self.paisa = currencies[x][0]
            print(self.paisa)
            self.sensitivity = sens.get() / 100

        sel1 = ttk.Combobox(crypto_frame, values=list(currencies.keys()), textvariable=c_sel).pack(side=LEFT)
        print(self.paisa)
        sense_frame = Frame(self)
        l2 = Label(sense_frame, text="Enter sensitivity for pump detection in percentage: ").pack(side=LEFT)
        sens = IntVar()
        sen = Entry(sense_frame, textvariable=sens).pack(side=LEFT)
        selb = Button(sense_frame, text="Select", command=lambda: coin_sel(c_sel)).pack(side=LEFT)



        crypto_frame.pack()
        sense_frame.pack()

        b = Button(self, text='OK', command=lambda: RealGraph.RealGraph(self.paisa,self.sensitivity)).pack()