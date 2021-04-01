from tkinter import *
from db_connect import  mysql as ms
import clogin as l
import cregister as r
import clanding as ld
from tkinter import ttk
from ttkthemes import themed_tk as tk

from PIL import Image,ImageTk

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
        a.set_theme('equilux')
        bg = Image.open('a.png')

       #a.attributes('')
        self.a = a
        self.uname = StringVar()
        self.password = StringVar()
        my_canvas = Canvas(a,width = 1280, height = 720)
        my_canvas.image = ImageTk.PhotoImage(bg)
        my_canvas.pack(fill = 'both', expand = True)
        my_canvas.create_image(0,0,image = my_canvas.image, anchor = 'nw' )

        #user = Frame(a)
        #ul = ttk.Label(a, text="Enter Username")

        my_canvas.create_text(550,200,text = "Enter Username:", fill = ms.color, font = ms.font)
        my_canvas.create_text(550, 300, text="Enter Password:", fill=ms.color, font= ms.font)

        #putl(ul, ue)
        #pwd = Frame(a)
        #pl = ttk.Label(a, text='Enter Password:')
        ue = Entry(a, textvariable=self.uname)
        pe = Entry(a, textvariable=self.password, show="*")
        my_canvas.create_window(740, 200, window=ue)
        my_canvas.create_window(740, 300, window=pe)
        #putl(pl, pe)
        loginbut = ttk.Button(a, text='Login', command=self.log, width = 15)
        registerbut = ttk.Button(a, text='Register', width = 15, command=self.reg)
        my_canvas.create_window(550, 400, window=loginbut)
        my_canvas.create_window(740, 400, window=registerbut)
        #put(user, pwd, loginbut, registerbut)
        a.mainloop()
if __name__ == "__main__":
    x = main()