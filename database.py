import pymysql

def db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="A123456s",
        database="project4pm"
    )