import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import *
from db_connect import mysql as ms
from ttkthemes import themed_tk as tk1
import datetime
from cHistGraph import HistGraph
from PIL import Image,ImageTk
import json
import urllib.request as req
import pandas as pd
from ctransaction import transaction


class Trade(ttk.Frame):
    def __init__(self, window, obj):
        ttk.Frame.__init__(self, window)

        self.sql = ms()
        self.mycursor = self.sql.mycursor
        self.db = self.sql.mydb
        self.uname = obj.uname

        bg = Image.open('a.png')

        hg_can = Canvas(window, width=1280, height=720)

        hg_can.image = ImageTk.PhotoImage(bg)
        hg_can.create_image(0, 0, image=hg_can.image, anchor='nw')
        hg_can.grid(row=0, column=0, sticky="nsew")

        hg_can.create_text(250, 100, anchor='w', text="Menu:", fill=ms.color, font=ms.font)

        bd = ttk.Button(window, text="HistoricalAnomaly", width=15,command=lambda: obj.display_page(obj.HistoricalAnomaly))  # .pack(side=LEFT)

        bb = ttk.Button(window, text="Landing", command=lambda: obj.display_page(obj.Landing))  # .pack(side=LEFT)
        bt = ttk.Button(window, text="Realtime Graph", command=lambda: obj.display_page(obj.RealTime))  # .pack(side=LEFT)
        hg_can.create_window(450, 100, anchor='w', window=bb)
        hg_can.create_window(650, 100, anchor='w', window=bd)
        hg_can.create_window(850, 100, anchor='w', window=bt)
        hg_can.create_text(640, 200, text="Trade", fill=ms.color, font=ms.font)

        c_sel = StringVar()

        currencies = self.sql.currencies
        start_date = datetime.datetime.now()
        hg_can.create_text(550, 300, anchor='e', text="Select Crypto Currency: ", fill=ms.color, font=ms.font)

        sel1 = ttk.Combobox(window, values=list(currencies.keys()), textvariable=c_sel)
        hg_can.create_window(600, 300, anchor='w', window=sel1)

        def coin_sel(c_sel):
            self.coin = c_sel
            url = 'https://poloniex.com/public?command=returnTicker'
            self.coi = currencies[c_sel][0]
            print(self.coin,self.coi)
            json_obj = req.urlopen(url)
            data = json.load(json_obj)
            df = pd.DataFrame(data)
            self.price = (round((pd.to_numeric(df['USDT_{}'.format(self.coi)]['last'])),2))
            self.mycursor.execute("select qty from user_has where user_name = \"{}\" and crypto_name = \"{}\"".format(obj.uname,self.coi))
            self.uhas = self.mycursor.fetchone()[0]
            print(self.uhas)
            hg_can.create_text(600, 400, anchor='w', text="$ {}".format(self.price), fill=ms.color, font=ms.font)
            hg_can.create_text(600, 500, anchor='w', text="{} ".format(self.uhas), fill=ms.color, font=ms.font)

        selb = ttk.Button(window, text="Select", command=lambda: coin_sel(c_sel.get()))
        hg_can.create_window(850, 300, window=selb)
        hg_can.create_text(550, 400, anchor='e', text="Current Price: ", fill=ms.color, font=ms.font)
        hg_can.create_text(550, 500, anchor='e', text="You have: ", fill=ms.color, font=ms.font)
        hg_can.create_text(550, 600, anchor='e', text="Enter Quantity: ", fill=ms.color, font=ms.font)
        self.qty = IntVar()
        quant = ttk.Entry(window, textvariable=self.qty)
        hg_can.create_window(600, 600, anchor='w', window=quant)

        bb = ttk.Button(window, text='BUY', command=lambda: transaction(self,"buy"))
        hg_can.create_window(590, 700,anchor='e', window=bb)
        bs = ttk.Button(window, text='SELL', command=lambda: transaction(self,"sell"))
        hg_can.create_window(690, 700,anchor='w' ,window=bs)