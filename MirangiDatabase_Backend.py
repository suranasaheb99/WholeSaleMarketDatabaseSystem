import sqlite3
#backEND

def workerDATA():
    con=sqlite3.connect("worker.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS worker (WorkerId text PRIMARY KEY, FirstName text, LastName text,birth_date text, address text, mobile_number INTEGER(10))")
    con.commit()
    con.close()


def addwdata(worker_id, first_name, last_name, birth_date, address, mobile_number):
    con=sqlite3.connect("worker.db")
    cur = con.cursor()
    cur.execute("INSERT INTO worker VALUES (?,?,?,?,?,?)",(worker_id, first_name, last_name, birth_date, address, mobile_number))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect("worker.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM worker")
    row = cur.fetchall()
    con.close()
    return row

def deleteRec(worker_id):
    con=sqlite3.connect("worker.db")
    cur = con.cursor()
    print(worker_id)
    cur.execute("DELETE FROM worker WHERE WorkerId=?",(worker_id,))
    con.commit()
    con.close()

def searchData(worker_id="", first_name="", last_name="", birth_date="", address="", mobile_number=""):
    con=sqlite3.connect("worker.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM worker WHERE WorkerId=? OR FirstName=? OR LastName=? OR birth_date=? OR address=? OR mobile_number=?", (worker_id, first_name, last_name, birth_date, address, mobile_number))
    row = cur.fetchall()
    con.close()
    return row

def dataUpdate(worker_id="", first_name="", last_name="", birth_date="", address="", mobile_number=""):
    print(worker_id)
    con=sqlite3.connect("worker.db")
    cur = con.cursor()
    cur.execute("UPDATE worker SET WorkerId=?, FirstName=?, LastName=?, birth_date=?, address=?, mobile_number=?", (worker_id, first_name, last_name, birth_date, address, mobile_number))
    con.commit()
    con.close()


























        
