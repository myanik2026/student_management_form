from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)


def get_db_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="A123456s",
        database="project4pm",
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route("/")
def home():
    db = get_db_connection()

    try:
        with db.cursor() as cursor:
            cursor.execute("select * from emp")
            emp = cursor.fetchall()
    finally:
        db.close()

    return render_template("index.html", emp=emp)




@app.route("/add", methods=["POST"])
def add_employee():

    name = request.form["name"]
    lastname = request.form["lastname"]
    age = request.form["age"]
    contact = request.form["contact"]
    course = request.form["course"]
    deposit_fees = request.form["deposit_fees"]
    pending_fees = request.form["pending_fees"]

    db = get_db_connection()

    try:
        with db.cursor() as cursor:

            sql = "INSERT INTO emp(name, lastname, age, contact, course, Pending_Fees, Deposite_Fees) VALUES (%s, %s, %s, %s, %s, %s, %s)"

            cursor.execute(sql,(name,lastname,age,contact,course,pending_fees,deposit_fees))

        db.commit()

    finally:
        db.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)