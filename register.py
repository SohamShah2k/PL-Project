from db_connect import  mysql as ms
from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk1
regsql = ms()
rmydb = regsql.mydb
rmycursor = regsql.mycursor
class register():

    def reg(self):
        r = tk1.ThemedTk()
        r.get_themes()
        r.set_theme('radiance')
        self.uev=StringVar()
        self.pwdev=StringVar()
        self.emailev=StringVar()
        top = ttk.Label(r,text = 'Registeration').grid(row = 0,column = 0, columnspan = 2)
        ul = ttk.Label(r,text = 'enter username: ').grid(row = 1, column = 0)
        ue = Entry(r, textvariable=self.uev).grid(row = 1, column = 1)
        pwdl = ttk.Label(r, text='enter Password: ').grid(row = 2, column = 0)
        pwde = Entry(r, textvariable=self.pwdev,show = '?').grid(row = 2, column = 1)
        emaill = ttk.Label(r, text='enter email id: ').grid(row = 3, column = 0)
        emaile = Entry(r, textvariable=self.emailev).grid(row = 3, column = 1)
        def mid():
            self.check()
            success = ttk.Label(r, text="registration successful!! Login now").grid(row=9, column=0)
            ok = ttk.Button(r, text='ok', command=r.destroy).grid(row=9, column=1)
        che = ttk.Button(r,text = 'Register', command = mid).grid(row = 8,column = 0, columnspan = 2)

        r.mainloop()
    def check(self):
        try:
            sql = "insert into users(user_name,password,email_id) values(\"{}\",\"{}\",\"{}\")"

            rmycursor.execute(sql.format(str(self.uev.get()), self.pwdev.get(), self.emailev.get()))
            rmydb.commit()

        except Exception as e:
            print("enter unique username and email id",e)