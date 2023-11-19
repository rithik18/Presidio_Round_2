import sqlite3
from flask import render_template,request,make_response

a=sqlite3.connect('my_database.litedb')
c=a.cursor()
q='select sqlite_version()'
c.execute(q)
r=c.fetchall()
print(r)

def db_init():
    try:
        q='''create table movie(Sno integer primary key, Name text,Director text,Release_year integer,Language text,Rating real)'''
        c.execute(q)
        r=c.fetchall()
    except Exception as e:
        print("Error",e)
        pass
    try:
        with open("records.txt",'r') as file:
            l=file.readline()
            l=file.readline()
            while(l):
                s=l.split()
                q = "INSERT INTO movie VALUES (?,?, ?, ?, ?, ?)"
                c.execute(q, (int(s[0]),str(s[1]), str(s[2]), int(s[3]), str(s[4]), float(s[5])))
                r=c.fetchall()
                l=file.readline()
    except Exception as e:
        print(e)
        pass

def show_all():
    q='''select * from movie'''
    c.execute(q)
    r=c.fetchall()
    print("Sno\tName\tDirector Release_year Language\tRating ")
    for i in r:
        for j in i:
            print(j,end="\t")
        print("")
def add():
    try:
        q = "INSERT INTO movie VALUES (?,?, ?, ?, ?, ?)"
        s=[]
        s.append(int(input("Enter Serial number: ")))
        s.append(input("Enter Name: "))
        s.append(input("Enter Director: "))
        s.append(int(input("Enter Release Year: ")))
        s.append(input("Enter Language: "))
        s.append(float(input("Enter Rating(1-5): ")))
        c.execute(q, (int(s[0]),str(s[1]), str(s[2]), int(s[3]), str(s[4]), float(s[5])))
    except Exception as e:
        print(f"Error: {e}")
def filter():
    try:
        print("1)Name\n2)Director\n3)Release_year\n4)Language\n5)Rating ")
        f={
            1:'Name',2: "Director", 3:"Release_year",4: "Language", 5:"Rating"
        }
        v1=int(input("Enter a CHOICE: "))
        v2=input("Enter FILTER VALUE: ")
        q = f"SELECT * FROM movie WHERE "+f[v1]+"= '"+str(v2)+"'"
        c.execute(q)
        r=c.fetchall()
        print(f"MOvies with {f[v1]} {v2} is : \n")
        if(len(r)==0):
            print("None")
        else:
            for i in r:
                for j in i:
                    print(j,end="\t")
                print("")
    except Exception as e:
        print(f"Error: {e}")
def search():
    try:
        v2=input("Enter Search VALUE: ")
        q = f"SELECT * FROM movie WHERE Name like'"+str(v2)+"%' or Name like'%"+str(v2)+"' or Name like'%"+str(v2)+"%'"
        c.execute(q)
        r=c.fetchall()
        print(f"MOvies with Name {v2} is : \n")
        if(len(r)==0):
            print("None")
        else:
            for i in r:
                for j in i:
                    print(j,end="\t")
                print("")
    except Exception as e:
        print(f"Error: {e}")
def update():
    try:
        v3=int(input("Enter Movies Serial No: "))
        print("1)Name\n2)Director\n3)Release_year\n4)Language\n5)Rating ")
        f={
            1:'Name',2: "Director", 3:"Release_year",4: "Language", 5:"Rating"
        }
        v1=int(input("Enter a Field which need to be updated: "))
        v2=input("Enter Update VALUE: ")
        q = f"UPDATE movie SET "+str(f[v1]) +" =? where Sno = ?"
        c.execute(q,(v2,v3))
        r=c.fetchall()
        print(r)
        if(c):
            print("Updated sucessfully")
    except Exception as e:
        print(f"Error: {e}")
def delete():
    try:
        v3=int(input("Enter Movies Serial No: "))
        q = f"DELETE from movie where Sno = ?"
        c.execute(q,(v3,))
        r=c.fetchall()
        print(r)
        if(c):
            print("Deleted sucessfully")
    except Exception as e:
        print(f"Error: {e}")
def grp():
    try:
        q = f"select Language,count(Language) from movie group by Language"
        c.execute(q)
        r=c.fetchall()
        print("\nLanguage  Count")
        for i in r:
            for j in i:
                print(j,end="\t")
            print("")
    except Exception as e:
        print(f"Error: {e}")
    
def menu():
    # print("Select An Option\n")
    # print("""1)Show all Movies.\n2)Add a New Movie.\n3)Filter Movies based on criteria.\n4)Search for a Movie.\n5)Update a Movie's Details.\n6)Delete a Movie.\n7)Exit""")
    n=0
    while(n!=8):
        print("\nSelect An Option\n")
        print("""1)Show all Movies.\n2)Add a New Movie.\n3)Filter Movies based on criteria.\n4)Search for a Movie.\n5)Update a Movie's Details.\n6)Delete a Movie.\n7)Group by Language\n8)Exit""")
        n=int(input("\nEnter an option :"))
        if(n==1):
            show_all()
        if(n==2):
            add()
        if(n==3):
            filter()
        if(n==4):
            search()
        if(n==5):
            update()
        if(n==6):
            delete()
        if(n==7):
            grp()
     

db_init()
menu()
a.commit()
a.close()