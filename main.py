from tkinter import *
from tkinter import ttk
from PIL import ImageTk

from employee import submit, show, delete, update, search, clear
from fees import update_fees


top = Tk()
top.state("zoomed")
top.geometry("1200x600")
top.resizable(0, 0)
top.title("Welcome")
top.config(bg="#2F4A63")


Label(top).pack()


tv = ttk.Treeview(top, height=15)

tv["columns"] = ("Name", "Lastname", "Age", "Contact","Course", "Pending_fees", "Deposit_fees", "Total_fees")

tv.column("#0", width=0, stretch=NO)

for col in tv["columns"]:
    tv.column(col, anchor=CENTER, width=90)
    tv.heading(col, text=col, anchor=CENTER)

tv.place(x=770, y=210)


Label(top,text="Student Registration" ,bg="#D6EAF8",fg="#154360",font=("Arial", 28, "bold")).place(x=580, y=20)




Label(top,text="Registration form" ,bg="#D6EAF8",fg="black",font=("Arial", 33, "bold")).place(x=70, y=115)


Label(top, text="Name", bg="#D6EAF8", fg="black",font=("Arial", 20, "bold")).place(x=70, y=210)

e1 = Entry(top, font=("Arial", 20, "bold"))
e1.place(x=290, y=210)


Label(top, text="Lastname", bg="#D6EAF8", fg="black",font=("Arial", 20, "bold")).place(x=70, y=260)

e2 = Entry(top, font=("Arial", 20, "bold"))
e2.place(x=290, y=260)


Label(top, text="AGE", bg="#D6EAF8", fg="black",font=("Arial", 20, "bold")).place(x=70, y=310)

e3 = Entry(top, font=("Arial", 20, "bold"))
e3.place(x=290, y=310)


Label(top, text="Contact", bg="#D6EAF8", fg="black",font=("Arial", 20, "bold")).place(x=70, y=360)

e4 = Entry(top, font=("Arial", 20, "bold"))
e4.place(x=290, y=360)


Label(top, text="Course", bg="#D6EAF8", fg="black",font=("Arial", 20, "bold")).place(x=70, y=410)


cb = ttk.Combobox(top,values=["select","Python","Java","PHP","ML","Python AI","SQL","DA","DSA"],font=("Arial", 20, "bold"))

cb.place(x=290, y=410)
cb.current(2)

Label(top, text="Deposit_amount", bg="#D6EAF8", fg="black",font=("Arial", 20, "bold")).place(x=70, y=460)

e6 = Entry(top, font=("Arial", 20, "bold"))
e6.place(x=290, y=460)



search_entry = Entry(top, font=("Arial", 20, "bold"))
search_entry.place(x=950, y=155)


Button(top,text="[Submit]",bg = "#D6EAF8",font=("Arial", 20, "bold"),command=lambda: submit([e1, e2, e3, e4, cb,e6 ])).place(x=70, y=620)


Button(top,text="[Delete]",bg = "#D6EAF8",font=("Arial", 20, "bold"),command=lambda: delete(e1, tv)).place(x=450, y=620)


Button(top,text="[Show]",bg = "#D6EAF8", font=("Arial", 20, "bold"),command=lambda: show(tv)).place(x=640, y=620)


Button(top,text="[Search]",bg = "#D6EAF8",font=("Arial", 20, "bold"),command=lambda: search(search_entry, tv)).place(x=780, y=140)


Button(top,text="[Update]",bg = "#D6EAF8",font=("Arial", 20, "bold"),command=lambda: update([e1, e2, e3, e4, cb], tv)).place(x=260, y=620)


Button(top,text="[Update_fees]",bg = "#D6EAF8",font=("Arial", 20, "bold"),command=lambda: update_fees(top, lambda: show(tv))).place(x=950, y=620)


def login():
    top.destroy()
    import login


Button(top,text="[Clear]",font=("Arial", 20, "bold"),command=lambda: clear(tv)).place(x=1210, y=620)


top.mainloop()