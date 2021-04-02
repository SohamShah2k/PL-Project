from tkinter import *
from datetime import datetime
from db_connect import mysql as ms
transql = ms()
tranmycursor = transql.mycursor
trandb = transql.mydb
class transaction():
    def __init__(self,tran,type):
        #pass

        if (tran.qty.get() < 0):
            warning = Tk()
            l1 = Label(warning, text="Please Enter a suitable quantity")
            l1.pack()
            warning.mainloop()
        else:
            if (type == 'buy'):
                sql = "insert into user_has(user_name,crypto_name,qty) values(\"{}\",\"{}\",{}) on duplicate key update qty = qty + {} "
                tranmycursor.execute(sql.format(tran.uname, tran.coi, tran.qty.get(), tran.qty.get()))
            elif (type == 'sell'):
                tranmycursor.execute("select qty from user_has where user_name = \"{}\" and crypto_name = \"{}\"".format(tran.uname,tran.coi))
                qtymax = int(tranmycursor.fetchone()[0])
                print(qtymax)
                if (tran.qty.get() > qtymax):
                    warning = Tk()
                    l1 = Label(warning, text="Please Enter a suitable quantity")
                    l1.pack()
                    warning.mainloop()
                else:
                    tranmycursor.execute("update user_has set qty = qty - {} where user_name = \"{}\" and crypto_name = \"{}\"".format(tran.qty.get(), tran.uname, tran.coi))


        print(tran.price,tran.uname,tran.coi,tran.qty.get(),type)
        sql = "insert into transactions(trans_price,user_name,crypto_name,trans_qty,trans_type) values({},\"{}\",\"{}\",{},\"{}\")"
        tranmycursor.execute(sql.format(tran.price,tran.uname,tran.coi,tran.qty.get(),type))
        trandb.commit()
        print("{} {} {}".format(type,tran.qty.get(),tran.coi))
