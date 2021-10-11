from tkinter import *
import datetime
try:
    import mysql.connector
except Exception:
    print("please install connector using 'pip install connector'")
try:
    mydb=mysql.connector.connect(host='localhost',user='root',password='',database='BANK_MANAGEMENT')
except Exception:
    print("connection establishment failed maybe xamp is not running try resarting sql and apache in xamp")

def showtransaction():
    root2=Tk()
    root2.geometry("1200x700")
    Label(root2,text="Transaction History",padx=200,pady=20,font=("Arial",25)).pack()
    Label(root2,text="Enter the account number").pack()
    c=Entry(root2,width=20)
    c.pack()
    def st():
        a='select * from transactions where accno=%s'
        ac=c.get()
        data=(ac,)
        x=mydb.cursor()
        x.execute(a,data)
        result=x.fetchall()
        if result==[]:
            Label(root2,text="No Transactions").pack()
        for i in result:
            Label(root2,text=i).pack()
        return
    Button(root2,text="search",command=st,padx=30,pady=20).pack()
    root2.mainloop()
    
def transaction(ac,t):
    sql='insert into transactions values(%s,%s,%s,%s)'
    date=datetime.date.today()
    time=datetime.datetime.now().time()
    data=(ac,date,time,t)
    x=mydb.cursor()
    x.execute(sql,data)
    mydb.commit()
    return


def OpenAccount():
    root2=Tk()
    root2.geometry("1200x700")
    Label(root2,text="New Account",padx=200,pady=50,font=("Arial",25)).pack()
    Label(root2,text="Name: ").pack()
    n1=Entry(root2,width=20)
    n1.pack()
    Label(root2,text="Account No: ").pack()
    ac1=Entry(root2,width=20)
    ac1.pack()
    Label(root2,text="Date Of Birth: ").pack()
    db1=Entry(root2,width=20)
    db1.pack()
    Label(root2,text="Address: ").pack()
    add1=Entry(root2,width=20)
    add1.pack()
    Label(root2,text="Contact No: ").pack()
    cn1=Entry(root2,width=20)
    cn1.pack()
    Label(root2,text="Opening Balance: ").pack()
    ob1=Entry(root2,width=20)
    ob1.pack()    
    def oa():
        n=n1.get()
        ac=ac1.get()
        db=db1.get()
        add=add1.get()
        cn=cn1.get()
        ob=ob1.get()
        print(n,ac,db,add,cn,ob)
        data1=(n,ac,db,add,cn,ob)
        data2=(n,ac,ob)
        sql1=('insert into Account values(%s,%s,%s,%s,%s,%s)')
        sql2=('insert into Amount values(%s,%s,%s)')
        x=mydb.cursor()
        try:
            x.execute(sql1,data1)
            x.execute(sql2,data2)
            mydb.commit()
            transaction(ac,ob)
            Label(root2,text="Account Opened Successfully").pack()
        except Exception:
            Label(root2,text="Account Already Exists").pack()
        return
    Button(root2,text="Open",command=oa,padx=30,pady=20).pack()
    root2.mainloop()

def depositeAmount():
    root2=Tk()
    root2.geometry("1200x700")
    Label(root2,text="Deposit Amount",padx=200,pady=50,font=("Arial",25)).pack()
    Label(root2,text="Amount: ").pack()
    amount1=Entry(root2,width=20)
    amount1.pack()
    Label(root2,text="Account No: ").pack()
    ac1=Entry(root2,width=20)
    ac1.pack()
    def dep():
        amount=int(amount1.get())
        ac=ac1.get()
        a='select balance from Amount where AccNo=%s'
        data=(ac,)
        x=mydb.cursor()
        try:
            x.execute(a,data)
            result=x.fetchone()
            t=result[0]+amount
            sql=('update amount set balance=%s where AccNo=%s')
            d=(t,ac)
            x.execute(sql,d)
            mydb.commit()
            transaction(ac,amount)
            Label(root2,text="Amount Deposite Successfully").pack()
        except Exception:
            Label(root2,text="This Account Does Not Exist").pack()            
        return
    Button(root2,text="deposite",command=dep,padx=30,pady=20).pack()
    root2.mainloop()

def withdrawAmount():
    root2=Tk()
    root2.geometry("1200x700")
    Label(root2,text="Withdraw Amount",padx=200,pady=50,font=("Arial",25)).pack()
    Label(root2,text="Amount: ").pack()
    amount1=Entry(root2,width=20)
    amount1.pack()
    Label(root2,text="Account No: ").pack()
    ac1=Entry(root2,width=20)
    ac1.pack()
    def wit():
        amount=int(amount1.get())
        ac=ac1.get()
        a='select balance from Amount where AccNo=%s'
        data=(ac,)
        x=mydb.cursor()
        try:
            x.execute(a,data)
            result=x.fetchone()
            t=result[0]-amount
            sql=('update Amount set balance=%s where AccNo=%s')
            d=(t,ac)
            x.execute(sql,d)
            mydb.commit()
            transaction(ac,-amount)
            Label(root2,text="Amount Withdrawn Successfully").pack()
        except Exception:
            Label(root2,text="Accout Number Does Not Exist").pack()
        return
    Button(root2,text="Withdraw",command=wit,padx=30,pady=20).pack()
    root2.mainloop()

def BalanceEnquiry():
    root2=Tk()
    root2.geometry("1200x700")
    Label(root2,text="Balance Enquiry",padx=200,pady=50,font=("Arial",25)).pack()
    Label(root2,text="Account No: ").pack()
    ac1=Entry(root2,width=20)
    ac1.pack()
    def be():
        ac=ac1.get()
        a='select * from Amount where AccNo=%s'
        data=(ac,)
        x=mydb.cursor()
        try:
            x.execute(a,data)
            result=x.fetchone()
            Label(root2,text=f"Balance for account {ac} is {result[-1]} ").pack()
        except Exception:
            Label(root2,text="Account Does Not Exist").pack()
        return
    Button(root2,text="Show",command=be,padx=30,pady=20).pack()
    root2.mainloop()

def DisplayDetails():
    root2=Tk()
    root2.geometry("1200x700")
    Label(root2,text="Customer Details",padx=200,pady=50,font=("Arial",25)).pack()
    Label(root2,text="Account No: ").pack()
    ac1=Entry(root2,width=20)
    ac1.pack()
    def dd():
        ac=ac1.get()
        a='select * from account where AccNo=%s'
        data=(ac,)
        x=mydb.cursor()
        try:
            x.execute(a,data)
            result=x.fetchone()
            for i in result:
                Label(root2,text=f"{i} ").pack()
        except Exception:
            Label(root2,text="Account Does Not Exist").pack()
        return
    Button(root2,text="Display",command=dd,padx=30,pady=20).pack()
    root2.mainloop()

def CloseAccount():
    root2=Tk()
    root2.geometry("1200x700")
    Label(root2,text="Close An Account",padx=200,pady=50,font=("Arial",25)).pack()
    Label(root2,text="Account No: ").pack()
    ac1=Entry(root2,width=20)
    ac1.pack()
    def ca():
        ac=ac1.get()
        sql1='delete from account where AccNo=%s'
        sql2='delete from amount where AccNo=%s'
        data=(ac,)
        x=mydb.cursor()
        x.execute(sql1,data)
        x.execute(sql2,data)
        mydb.commit()
        Label(root2,text="Account Has Been Closed").pack()
        return
    Button(root2,text="Close",command=ca,padx=30,pady=20).pack()
    root2.mainloop()

def main():
    root=Tk()
    root.title("Home")
    root.geometry("1200x700")
    Label(root,text="Bank Management System",padx=200,pady=50,font=("Arial",25)).pack()
    frame=Frame(root).pack()
    Button(frame,text="New Account",command=OpenAccount,padx=30,pady=15).pack()
    Button(frame,text="Deposite Amount",command=depositeAmount,padx=30,pady=15).pack()
    Button(frame,text="Withdraw Amount",command=withdrawAmount,padx=30,pady=15).pack()
    Button(frame,text="Balance Enquiry",command=BalanceEnquiry,padx=30,pady=15).pack()
    Button(frame,text="Customer Details",command=DisplayDetails,padx=30,pady=15).pack()
    Button(frame,text="Close an account",command=CloseAccount,padx=30,pady=15).pack()
    Button(frame,text="Transaction History",command=showtransaction,padx=30,pady=15).pack()
    root.mainloop()
main()