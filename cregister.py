from db_connect import  mysql as ms
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk1

from PIL import Image,ImageTk

regsql = ms()
rmydb = regsql.mydb
rmycursor = regsql.mycursor
class register():

    def reg(self):
        r = tk1.ThemedTk()
        r.geometry('480x720')
        r.get_themes()
        r.set_theme('equilux')

        bg = Image.open('a.png')

        r_can = Canvas(r, width=480, height=720)
        r_can.image = ImageTk.PhotoImage(bg)
        r_can.create_image(-400, 0, image=r_can.image, anchor='nw')
        r_can.grid(row=0, column=0, sticky="ns")

        self.uev=StringVar()
        self.pwdev=StringVar()
        self.emailev=StringVar()

        r_can.create_text(240, 100, text=" Registeration ", fill=ms.color, font=ms.font)
        r_can.create_text(10, 200,anchor ='w', text="Enter Username: ", fill=ms.color, font=ms.font)
        ue = Entry(r, textvariable=self.uev)
        r_can.create_window(280,200,anchor ='w', window=ue )
        r_can.create_text(10, 300,anchor ='w', text="Enter Password: ", fill=ms.color, font=ms.font)

        pwde = Entry(r, textvariable=self.pwdev,show = '*')
        r_can.create_window(280, 300,anchor ='w', window=pwde)

        r_can.create_text(10, 400,anchor ='w', text="Enter Email ID: ", fill=ms.color, font=ms.font)

        emaile = Entry(r, textvariable=self.emailev)
        r_can.create_window(280, 400,anchor ='w', window=emaile)
        def mid():
            self.check()
            success = ttk.Label(r, text="registration successful!! Login now").grid(row=9, column=0)
            ok = ttk.Button(r, text='ok', command=r.destroy)
            r_can.create_window(240, 600,anchor ='w', window=ok)
        che = ttk.Button(r,text = 'Register', command = mid)
        r_can.create_window(240, 500,anchor ='w', window=che)
        r.mainloop()
    def check(self):
        try:
            sql = "insert into users(user_name,password,email_id) values(\"{}\",\"{}\",\"{}\")"

            rmycursor.execute(sql.format(str(self.uev.get()), self.pwdev.get(), self.emailev.get()))
            rmydb.commit()

        except Exception as e:
            msg = tk1.ThemedTk()
            msg.set_theme('radiance')
            l = ttk.Label(msg, text='Username and Email Should be unique').pack()
            ok = ttk.Button(msg, text='OK', command=msg.destroy).pack()
            msg.mainloop()