from tkinter import *
from tkinter import ttk   # <-- Add this line
from tkinter import messagebox
from PIL import ImageTk

top = Tk()
top.geometry('1200x600')


def showpass():
    if e2.cget('show') == "*":
        e2.config(show='')
    else:
        e2.config(show="*")


def Login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='A123456s', db='project4pm')
    cur = db.cursor()
    cur.execute("select * from admins where name=%s and password=%s", (e1.get(), e2.get()))
    result = cur.fetchone()
    if result==None:
        messagebox.showinfo("Result","Login fail")

    else:
        top.destroy()
        import main




L5 = Label(top,bg="black")
L5.pack()




L = Label(top,text = 'Login', bg = 'black', fg = 'white', font=('Arial 25 bold'))
L.place(x=500,y=50)

L1 = Label(top,text = 'Name', bg = 'black', fg = 'white', font=('Arial 25 bold'))
L1.place(x=200,y=200)

e1 = Entry(top,font = ('Arial 20 bold'))
e1.place(x=380,y=200)


L2 = Label(top,text = 'Password', bg = 'black', fg = 'white', font=('Arial 25 bold'))
L2.place(x=200,y=250)

e2 = Entry(top,font = ('Arial 20 bold'))
e2.place(x=380,y=250)


b2 = Button(top,text='Login',font = ('Arial 20 bold'),command=Login)
b2.place(x = 400,y=300)


v=Checkbutton(top,command=showpass)
v.place(x=655,y=255)

top.mainloop()