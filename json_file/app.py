import json
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def show_all():
    try:
        with open("db.json",'r') as file:
            a=json.load(file)
            for i in a[0].keys():
                print(i,end=" ")
            print("")
            for i in a:
                for j in i.keys():
                    print(i[j],end="\t")
                print("")
    except Exception as e:
        print(e)
        pass



def add():
    try:   
        s={}
        s["Sno"]=(int(input("Enter Serial number: ")))
        s["Name"]=(input("Enter Name: "))
        s["Director"]=(input("Enter Director: "))
        s["Release_year"]=(int(input("Enter Release Year: ")))
        s["Language"]=(input("Enter Language: "))
        s["Ratings"]=(float(input("Enter Rating(1-5): ")))
        d=[]
        with open("db.json",'r') as file:
            d=json.load(file)
            
        d.append(s)
        # print(d)
        with open("db.json",'w') as file:
            a=json.dump(d,file)
            print(a)
            
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
        d=[]
        with open("db.json",'r') as file:
            d=json.load(file)
        for i in d[0].keys():
            print(i,end=" ")
        print("")
        for i in d:
            if(str(i[f[v1]])==v2):
                for j in i.values():
                    print(j,end="\t")
                print("")
    except Exception as e:
        print(f"Error: {e}")
def search():
    try:
        d=[]
        v2=input("Enter Search VALUE: ")
        with open("db.json",'r') as file:
            d=json.load(file)
        for i in d[0].keys():
            print(i,end=" ")
        print("")
        for i in d:
            if(similar(str(i["Name"]).lower(),v2.lower())>=0.5):
                for j in i.keys():
                    print(i[j],end="\t")
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
        d=[]
        with open("db.json",'r') as file:
            d=json.load(file)
        for i in d:
            if(i["Sno"]==v3):
                i[f[v1]]=v2 
        with open("db.json",'w') as file:
            a=json.dump(d,file)
    except Exception as e:
        print(f"Error: {e}")
def delete():
    try:
        v3=int(input("Enter Movies Serial No: "))
        with open("db.json",'r') as file:
            d=json.load(file)
        c=0
        for i in d:
            if(i["Sno"]==v3):
                break
            else:
                c+=1
        d.pop(c)
        with open("db.json",'w') as file:
            a=json.dump(d,file)
        
    except Exception as e:
        print(f"Error: {e}")
def grp():
    try:
        with open("db.json",'r') as file:
            d=json.load(file)
        f={}
        for i in d:
            if(i["Language"] in f):
                f[i["Language"]]+=1
            else:
                f[i["Language"]]=1
        for i in f.keys():
            print(i,end=" ")
        print("")
        for i in f.values():
            print(i,end="   ")
            
    except Exception as e:
        print(f"Error: {e}")
    
def menu():
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
     
menu()
