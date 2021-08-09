import sqlite3
"""
def DatatoDatabase(s):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    sql = "create table graduate students (name text, major text, email text)"
    cursor.execute(sql)
    with open(s,'r') as f:
        for line in f:
"""



def main():
    conn = sqlite3.connect("grad.db")
    cursor = conn.cursor()
    sql1 = "create table stat (name text, email text)"
    sql2 = "create table am (name text, email text)"
    sql3 = "create table pm (name text, email text)"
    sql4 = "create table cs (name text, email text)"
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    cursor.execute(sql4)


    with open("students.txt", "r") as f:
        for line in f:
            line = line.replace("\n","")
            #print(line)
            L = line.split("\t")
            print(L)
            name = L[0].replace(" ","")
            major = L[1].replace(" ","")
            email = L[2].replace(" ","")
            if major == "STAT":
                sqlA = "insert into stat(name, email) values (:name, :email)"
                cursor.execute(sqlA,{"name":name, "email":email})
            elif major == "AM":
                sqlB = "insert into am(name, email) values (:name, :email)"
                cursor.execute(sqlB,{"name":name, "email":email})
            elif major == "PM":
                sqlC = "insert into pm(name, email) values (:name, :email)"
                cursor.execute(sqlC,{"name":name, "email":email})
            elif major == "CS":
                sqlD = "insert into cs(name, email) values (:name, :email)"
                cursor.execute(sqlD,{"name":name, "email":email})
            conn.commit()
    cursor.close()



    #DatatoDatabase("graduatestudents.txt")


