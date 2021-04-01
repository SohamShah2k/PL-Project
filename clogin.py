from tkinter import *
from db_connect import mysql as ms
from ttkthemes import themed_tk as tk
from tkinter import ttk
logsql = ms()
lmydb = logsql.mydb
lmycursor = logsql.mycursor
class login():

    def log(self,uname,password):
        try:
            lmycursor.execute('select user_name,password from users where user_name = \"{}\" and password = \"{}\" '.format(uname,password))
            unm,pwd = lmycursor.fetchall()[0]

        except:

            msg = tk.ThemedTk()
            msg.set_theme('radiance')
            l = ttk.Label(msg,text='Username or password incorrect').pack()
            ok = ttk.Button(msg,text = 'OK',command=msg.destroy).pack()
            msg.mainloop()