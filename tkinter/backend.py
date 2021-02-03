import sqlite3



def connecct():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()

    return conn,cur


def create_table():
    #conn=sqlite3.connect("lite.db")
    #cur=conn.cursor()
    conn,cur=connecct()

    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    #conn = sqlite3.connect("lite.db")
    #cur = conn.cursor()
    conn,cur=connecct()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))

    #cur.execute("insert into store values ('%s','%s','%s')" %(item ,qty,price))--sql injection, don't use
    #cur.execute("insert into store values (%s,%s,%s)", (item ,qty,price))
    conn.commit()
    conn.close()
    select()

def select():
    #conn = sqlite3.connect("lite.db")
    #cur = conn.cursor()
    conn,cur=connecct()
    print(cur.execute("SELECT * FROM book"))
    rows=cur.fetchall()

    conn.commit()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn,cur=connecct()

    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows



def delete(id):
    #conn = sqlite3.connect("lite.db")
    #cur = conn.cursor()
    conn,cur=connecct()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    #conn = sqlite3.connect("lite.db")
    #cur = conn.cursor()
    conn,cur=connecct()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()

#insert("seccond item",25,230.0)
#insert("first item",787,457.0)

#delete(r"third%")
#delete(r"seccond%")
#select()
#update(r"secc%",72,88.0)

#create_table()
#insert("The Sun","Deb Smith",1918,913323132)
#insert(" Sun","Deb ",1915,913323232)
#insert("The "," Smith",1916,913333132)
#insert("The don","sar Smith",1913,943323132)
#delete(3)
#update(4,"The moon","John Smooth",1917,99999)
#print(view())
#print(search(author="John Smooth"))
#select()