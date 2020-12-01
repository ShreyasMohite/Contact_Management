import sqlite3

def Contact():
    conn=sqlite3.connect("Contact")
    cur=conn.cursor()
    cur.execute("create table if not exists contact_info(id integer primary key,name text,number text)")
    conn.commit()
    conn.close()
    
def add_contacts(name,number):
    conn=sqlite3.connect("Contact")
    cur=conn.cursor()
    cur.execute("insert into contact_info values(null,?,?)",(name,number))
    conn.commit()
    conn.close()
    
def view_contacts():
    conn=sqlite3.connect("Contact")
    cur=conn.cursor()
    cur.execute("select * from contact_info")
    row=cur.fetchall()
    conn.close()
    return row


def delete_contact(id):
    conn=sqlite3.connect("Contact")
    cur=conn.cursor()
    cur.execute("delete from contact_info where id=?",(id,))
    conn.commit()
    conn.close()

def update_contacts(id,name=" ",number=" "):
    conn=sqlite3.connect("Contact")
    cur=conn.cursor()
    cur.execute("select * from contact_info where name=? or number=?",(name,number,id))
    conn.commit()
    conn.close()




Contact()

