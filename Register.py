from tkinter import *
from tkinter import ttk, messagebox     # <-- Add this line
from PIL import ImageTk
import pymysql

top = Tk()
top.state('zoomed')
top.geometry('1200x600')
top.resizable(0,0)
top.title("Welcome")



img = ImageTk.PhotoImage(file="C:/Users/Anik Raj/OneDrive/Pictures/kkk.jpg")


def get_db_connection():
    return pymysql.connect(host='localhost',user='root',password='A123456s',database='project4pm')

def submit():
    name=e1.get()
    lastname=e2.get()
    age=e3.get()
    contact=e4.get()
    course=cb.get()
    deposit=e6.get()
    pending_fees=e7.get()

    if not name or not lastname or not age or not contact:
        messagebox.showerror("Error", "Please fill in all fields")
        return

    db = get_db_connection()

    try:
        cur=db.cursor()

        sql = "Insert into emp(name,lastname,age,contact,course,pending_fees,deposit_fees)values (%s,%s,%s,%s,%s,%s,%s))"

        values = (name,lastname,age,contact,course,pending_fees,deposit_fees)

        cur.execute(sql, values)
        db.commit()

        messagebox.showinfo("Success", "Record inserted successfully")

        clear_fields()

    finally:
        db.close()

def clear_fields():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    cb.delete(0)




def update():
    name=e1.get()
    lastname=e2.get()
    age=int(e3.get())
    contact=int(e4.get())
    course=cb.get()

    if not name:
        messagebox.showerror(
            "Error",
            "Enter Name to update"
        )
        return

    db = get_db_connection()

    try:
        cur = db.cursor()

        sql = "UPDATE emp SET lastname=%s,age=%s,contact=%s,course=%s WHERE name=%s "

        values = (lastname,age,contact,course,name)

        result = cur.execute(sql,values)
        db.commit()

        if(result>0):
            messagebox.showinfo("Result","Record update successful")
        else:
            messagebox.showinfo("Result","Record not updated successfully")

    finally:
        db.close()



# ========================== DELETE ===============================



def Update_fees():
    top12 = Toplevel()
    top12.geometry('1200x600')
    img23 = ImageTk.PhotoImage(file="C:/Users/Anik Raj/OneDrive/Pictures/kkk.jpg")
    L = Label(top12, image=img23)
    L.pack()
    L.img = img23

    f = Frame(top12, height=202, width=300, bg='blue')
    f.place(x=800, y=50)


    def InsertFee():
        r=[]
        n9=E10.get()               # name
        course = cb.get()          # course
        f = E20.get()              # Deposited fee

        import pymysql as sql
        db = sql.connect(host='localhost', user='root', password='A123456s', db='project4pm')
        cur = db.cursor()

        h= "Select course_fee from Course_Fee where course=%s"
        cur.execute(h,course)
        result = cur.fetchone()
        t=result[0]
        print(t)

        cur2=db.cursor()

        h3 = "select * from emp where course = %s "
        cur2.execute(h3,course)
        result2 = cur2.fetchall()
        for col2 in result2:
            v2=col2[5]
            r.append(v2)
        t2=r[0]
        r = "UPDATE Course_fee SET Course_Fee=%s WHERE course=%s"

        print(t2)

        if t2 is not None:
            df2 = t2 - int(f)
            b=(df2,n9)
            n2 = "UPDATE emp SET Pending_Fees=%s WHERE name=%s"
            result3 = cur.execute(n2, b)
            if (result3 > 0):
                messagebox.showinfo("Result", "Your Record Updated Successfully")
            else:
                messagebox.showinfo("Result", "Record Not Updated")

        else:
            df = t - int(f)
            n2 = "UPDATE emp set Deposite_Fees=%s, Pending_Fees=%s WHERE name=%s"
            b=(f,df,n9)
            result3 = cur.execute(n2,b)
            if (result3 > 0):
                messagebox.showinfo("Result", "Your Record update successfully")
            else:
                messagebox.showinfo("Result", "Record Not Updated")

        db.commit()

    k = ['Select', 'Python', 'Java', 'PHP', 'ML', 'Python AI', 'SQL', 'DA', 'DSA']
    L1 = Label(top12, text='Name', bg='black', fg='white', font=('Arial 20 bold'))
    L1.place(x=200, y=100)
    E10 = Entry(top12, font=('Arial 20 bold'))
    E10.place(x=400, y=100)

    L2 = Label(top12, text='Course', bg='black', fg='white', font=('Arial 20 bold'))
    L2.place(x=200, y=150)
    cb = ttk.Combobox(top12, values=k, font=('Arial 20 bold'))
    cb.place(x=400, y=150)
    cb.current(0)

    L3 = Label(top12, text='DepositedFee', bg='black', fg='white', font=('Arial 20 bold'))
    L3.place(x=200, y=200)
    E20 = Entry(top12, font=('Arial 20 bold'))
    E20.place(x=400, y=200)

    b8 = Button(top12, text='Submit', font=('Arial 20 bold'),command=InsertFee)
    b8.place(x=450, y=480)


def delete():
    k=e1.get()
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='A123456s', db='project4pm')
    cur = db.cursor()
    s=("delete from emp where name=%s")
    result= cur.execute(s,k)
    if (result > 0):
        messagebox.showinfo("Result", "Record insert successfully")
    else:
        messagebox.showinfo("Result", "Record not inserted")

    db.commit()


def login():
    top.destroy()
    import login



def show():
    for i in tv.get_children():
        tv.delete(i)
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='A123456s', db='project4pm')
    cur = db.cursor()
    s = "select * from emp"
    cur.execute(s)
    result=cur.fetchall()
    for col in result:
        name=col[0]
        lastname=col[1]
        age=col[2]
        contact=col[3]
        course=col[4]
        pending_fees=col[5]
        deposite_fees=col[6]
        tv.insert("",'end',values=(name,lastname,age,contact,course,pending_fees,deposite_fees))


def search():
    v=e6.get()
    for i in tv.get_children():
        tv.delete(i)
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='A123456s', db='project4pm')
    cur = db.cursor()
    s = "select * from emp where course = %s"
    cur.execute(s,v)
    result = cur.fetchall()
    for col in result:
        name=col[0]
        lastname=col[1]
        age=col[2]
        contact=col[3]
        course=col[4]
        Pending_fees=col[5]
        Deposite_fees=col[6]
        tv.insert("",'end',values=(name,lastname,age,contact,course,Pending_fees,Deposite_fees))




L=Label(top,image=img)
L.pack()




tv = ttk.Treeview(top,height=15)
tv['columns']=('Name','Lastname','Age','Contact','Course','Pending_fees','Deposite_fees')
tv.column('#0', width=0, stretch=NO)

tv.column('Name', anchor=CENTER, width=120)
tv.column('Lastname', anchor=CENTER, width=120)
tv.column('Age', anchor=CENTER, width=120)
tv.column('Contact', anchor=CENTER, width=120)
tv.column('Course', anchor=CENTER, width=120)
tv.column('Pending_fees', anchor=CENTER, width=120)
tv.column('Deposite_fees', anchor=CENTER, width=120)

tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('Lastname', text='Lastname', anchor=CENTER)
tv.heading('Age', text='Age', anchor=CENTER)
tv.heading('Contact', text='Contact', anchor=CENTER)
tv.heading('Course', text='Course',anchor=CENTER)
tv.heading('Pending_fees', text='Pending_fees',anchor=CENTER)
tv.heading('Deposite_fees', text='Deposite_fees',anchor=CENTER)

tv.place(x=700,y=150)






h=['select','Python','java','Php','Net','AI','ML','DATAScience']

L = Label(top,text = 'Registration', bg = 'green', fg = 'white', font=('Arial 25 bold'))
L.place(x=450,y=50)

L1 = Label(top,text = 'Name', bg = 'green', fg = 'white', font=('Arial 20 bold'))
L1.place(x=200,y=200)

e1 = Entry(top,font = ('Arial 20 bold'))
e1.place(x=350,y=200)

L2 = Label(top,text = 'Lastname', bg = 'green', fg = 'white', font=('Arial 20 bold'))
L2.place(x=200,y=250)

e2 = Entry(top,font = ('Arial 20 bold'))
e2.place(x=350,y=250)

L3 = Label(top,text = 'AGE', bg = 'green', fg = 'white', font=('Arial 20 bold'))
L3.place(x=200,y=300)

e3 = Entry(top,font = ('Arial 20 bold'))
e3.place(x=350,y=300)


L4 = Label(top,text = 'Contact', bg = 'green', fg = 'white', font=('Arial 20 bold'))
L4.place(x=200,y=350)

e4 = Entry(top,font = ('Arial 20 bold'))
e4.place(x=350,y=350)

L5 = Label(top,text = 'Course', bg = 'green', fg = 'white', font=('Arial 20 bold'))
L5.place(x=200,y=400)



cb=ttk.Combobox(top,value=h,font=('Arial 20 bold'))
cb.place(x=350,y=400)
cb.current(2)

L6 = Label(top,text = 'Deposite_fees', bg = 'green', fg = 'white', font=('Arial 20 bold'))
L6.place(x=200,y=450)

e6 = Entry(top,font = ('Arial 20 bold'))
e6.place(x=350,y=450)

L7 = Label(top,text = 'Pending_fees', bg = 'green', fg = 'white', font=('Arial 20 bold'))
L7.place(x=200,y=500)

e7 = Entry(top,font = ('Arial 20 bold'))
e7.place(x=350,y=500)

b1 = Button(top,text='Submit',font = ('Arial 20 bold'))
b1.place(x=350,y=600)

b2 = Button(top,text='Delete',font = ('Arial 20 bold'),command=delete)
b2.place(x = 520,y=600)

b3 = Button(top,text='SHOW',font = ('Arial 20 bold'),command=show)
b3.place(x = 690,y=600)

b4 = Button(top,text='Login',font = ('Arial 20 bold'),command=login)
b4.place(x = 810,y=600)

e6 = Entry(top,font = ('Arial 20 bold'))
e6.place(x=930,y=70)

b6 = Button(top,text='Search',font = ('Arial 20 bold'),command=search)
b6.place(x = 750,y=70)


b7 = Button(top,text='update',font = ('Arial 20 bold'),command=update)
b7.place(x = 900,y=70)

b8 = Button(top,text='Update_fees',font = ('Arial 20 bold'),command=Update_fees)
b8.place(x = 950,y=570)




top.config(bg = 'green')
top.mainloop()








