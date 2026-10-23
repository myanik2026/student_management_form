from tkinter import *
from tkinter import ttk, messagebox, filedialog
from reportlab.pdfgen import canvas
from datetime import datetime
from database import db

def update_fees(parent, show):
    w = Toplevel(parent)
    w.geometry("600x400")

    Label(w, text="Name").pack()
    name = Entry(w)
    name.pack()

    Label(w, text="Course").pack()
    course = ttk.Combobox(w, values=[
        "Python", "Java", "PHP", "ML", "Python AI", "SQL", "DA", "DSA"
    ])
    course.pack()

    Label(w, text="Deposit Fee").pack()
    fee = Entry(w)
    fee.pack()

    def save():
        con = db()
        cur = con.cursor()

        cur.execute(
            "SELECT Total_fees, deposit_fees FROM emp WHERE name=%s",
            (name.get(),)
        )
        result = cur.fetchone()

        if result is None:
            messagebox.showerror("Error", "Student not found")
            con.close()
            return

        total, old_deposit = result
        deposit = int(fee.get())
        new_deposit = (old_deposit or 0) + deposit
        pending = total - new_deposit

        if pending < 0:
            messagebox.showerror("Error", "Deposit is greater than total fees")
            con.close()
            return

        cur.execute(
            "UPDATE emp SET Deposit_Fees=%s, Pending_Fees=%s WHERE name=%s",
            (new_deposit, pending, name.get())
        )

        con.commit()
        con.close()

        # Download recipt

        path = filedialog.asksaveasfilename(
            title="Save Fee Receipt",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            initialfile=name.get() + "_fee_receipt.pdf"
        )

        if path:
            pdf = canvas.Canvas(path)

            pdf.setFont("Helvetica-Bold", 20)
            pdf.drawCentredString(300, 780, "FEE RECEIPT")

            pdf.setFont("Helvetica", 12)
            pdf.drawString(70, 730, "Student Name: " + name.get())
            pdf.drawString(70, 705, "Course: " + course.get())
            pdf.drawString(70, 680, "Date: " + datetime.now().strftime("%d-%m-%Y %H:%M"))

            pdf.drawString(70, 640, "Total Fees: Rs. " + str(total))
            pdf.drawString(70, 615, "Previous Deposit: Rs. " + str(old_deposit))
            pdf.drawString(70, 590, "Current Deposit: Rs. " + str(deposit))
            pdf.drawString(70, 565, "Total Deposit: Rs. " + str(new_deposit))
            pdf.drawString(70, 540, "Pending Fees: Rs. " + str(pending))

            pdf.setFont("Helvetica-Bold", 13)
            pdf.drawString(70, 490, "Payment Status: Payment Received")

            pdf.save()

            messagebox.showinfo("Result", "Fees updated")

        show()
        w.destroy()

    Button(w, text="Submit", command=save).pack(pady=20)