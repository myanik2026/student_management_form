from tkinter import messagebox
from database import db

def show(tv):
    tv.delete(*tv.get_children())
    con=db(); cur=con.cursor()
    cur.execute("SELECT name,lastname,age,contact,course,Pending_Fees,Deposit_Fees,Total_Fees FROM emp")
    for r in cur.fetchall(): tv.insert("", "end", values=r)
    con.close()

def clear(tv):
    tv.delete(*tv.get_children())

def submit(e):
    con=db();
    cur=con.cursor()

    cur.execute("SELECT course_fees FROM Course_Fee WHERE course_name=%s",(e[4].get(),))

    result = cur.fetchone()

    if result is None:
        messagebox.showerror("Error", "Course fee not found")
        con.close()
        return

    total = result[0]
    deposit = int(e[5].get())
    pending = total - deposit

    if pending < 0:
        messagebox.showerror("Error", "Deposit is greater than total fees")
        con.close()
        return

    cur.execute(
        """INSERT INTO emp
        (name,lastname,age,contact,course,Total_Fees,Deposit_Fees,Pending_Fees)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
        (
            e[0].get(),
            e[1].get(),
            e[2].get(),
            e[3].get(),
            e[4].get(),
            total,
            deposit,
            pending
        )
    )

    con.commit()
    con.close()

    messagebox.showinfo("Success", "Student registered successfully")




def delete(name,tv):
    con=db(); cur=con.cursor()
    cur.execute("DELETE FROM emp WHERE name=%s",(name.get(),))
    con.commit(); con.close(); show(tv)

def update(e,tv):
    con=db(); cur=con.cursor()
    cur.execute("UPDATE emp SET lastname=%s,age=%s,contact=%s,course=%s WHERE name=%s",
    (e[1].get(),e[2].get(),e[3].get(),e[4].get(),e[0].get()))
    con.commit(); con.close(); show(tv)

def search(course,tv):
    tv.delete(*tv.get_children())
    con=db(); cur=con.cursor()
    cur.execute("SELECT name,lastname,age,contact,course,Pending_Fees,Deposit_Fees,Total_Fees FROM emp WHERE course=%s",(course.get(),))
    for r in cur.fetchall(): tv.insert("", "end", values=r)
    con.close()