from tkinter import *
from db_connect import  mysql as ms
logsql = ms()
lmydb = logsql.mydb
lmycursor = logsql.mycursor
class login():

    def log(self,uname,password):
        try:
            sql = 'select user_name,password from users where user_name = \"{}\" and password = \"{}\" '
            lmycursor.execute(sql.format(uname,password))
            unm,pwd = lmycursor.fetchall()[0]

        except:
            msg = Tk()
            l = Label(msg,text='Username or password incorrect').pack()
            ok = Button(msg,text = 'OK',command=msg.destroy).pack()
            msg.mainloop()