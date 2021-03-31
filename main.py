from tkinter import *

import login as l
import register as r
import landing as ld
from tkinter import ttk
from ttkthemes import themed_tk as tk

def put(*l):
    for i in l:
        i.pack()


def putl(*l):
    for i in l:
        i.pack(side = LEFT)

class main():
    def log(self):

        userx = l.login()
        userx.log(self.uname.get(), self.password.get())
        self.a.destroy()
        self.d = ld.land(self.uname.get())
    def reg(self):
        self.a.destroy()
        userx = r.register()
        userx.reg()

    def __init__(self):
        a = tk.ThemedTk()
        a.geometry('1280x720')
        a.get_themes()
        a.set_theme('radiance')
        self.a = a
        self.uname = StringVar()
        self.password = StringVar()
        user = Frame(a)
        ul = ttk.Label(user, text="Enter Username")
        ue = Entry(user, textvariable=self.uname)
        putl(ul, ue)
        pwd = Frame(a)
        pl = ttk.Label(pwd, text='Enter Password:')
        pe = Entry(pwd, textvariable=self.password, show="*")
        putl(pl, pe)
        loginbut = ttk.Button(a, text='Login', command=self.log)
        registerbut = ttk.Button(a, text='Register', command=self.reg)
        put(user, pwd, loginbut, registerbut)
        a.mainloop()
if __name__ == "__main__":
    x = main()