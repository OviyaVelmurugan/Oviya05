from tkinter import*
win=Tk()
win.title("Bill Management")
win.geometry("800x500")

lbl=Label(win,text="BILL MANAGEMENT SYSTEM",font=("times",15),fg="white",pady=10,background="black")
lbl.grid(columnspan=4)


def Total():
    
    try:a1=int(E1.get())
    except:a1=0
    c1=60*a1
    

    try:a2=int(E2.get())
    except:a2=0
    c2=30*a2

    try:a3=int(E3.get())
    except:a3=0
    c3=7*a3

    try:a4=int(E4.get())
    except:a4=0
    c4=100*a4

    try:a5=int(E5.get())
    except:a5=0
    c5=20*a5

    try:a6=int(E6.get())
    except:a6=0
    c6=15*a6

    try:a7=int(E7.get())
    except:a7=0
    c7=7*a7

    

    Total=c1+c2+c3+c4+c5+c6+c7
    E8.delete(0,END)
    E8.insert(0,Total)
    


def Reset():
    E1.delete(0,END)
    E2.delete(0,END)
    E3.delete(0,END)
    E4.delete(0,END)
    E5.delete(0,END)
    E6.delete(0,END)
    E7.delete(0,END)



frame1=Frame(win,highlightbackground="black",highlightthickness=2,padx=20,pady=20)
frame1.grid(row=1,column=0,padx=20,pady=50)

lbl=Label(frame1,text="MENU",font=("times",15,"bold"),fg="green",pady=10)
lbl.grid(columnspan=2)

lblname=Label(frame1,text="Dosa....Rs.60/plate",font=("times",15,"bold"),pady=10)
lblname.grid(row=1,column=0)

lblname=Label(frame1,text="Cookies....Rs.30/plate",font=("times",15,"bold"),pady=10)
lblname.grid(row=2,column=0)


lblname=Label(frame1,text="Tea....Rs.7/cup",font=("times",15,"bold"),pady=10)
lblname.grid(row=3,column=0)

lblname=Label(frame1,text="Coffee..../Rs.100/cup",font=("times",15,"bold"),pady=10)
lblname.grid(row=4,column=0)

lblname=Label(frame1,text="Juice..../Rs.20/glass",font=("times",15,"bold"),pady=10)
lblname.grid(row=5,column=0)

lblname=Label(frame1,text="Pancakes....Rs.15/pack",font=("times",15,"bold"),pady=10)
lblname.grid(row=6,column=0)

lblname=Label(frame1,text="Eggs....Rs.15/pack",font=("times",15,"bold"),pady=10)
lblname.grid(row=7,column=0)



frame2=Frame(win,highlightbackground="black",highlightthickness=2,padx=20,pady=20)
frame2.grid(row=1,column=2,padx=30,pady=50)

lblname=Label(frame2,text="Dosa",font=("times",15,"bold"),padx=5,pady=5,width=5)
lblname.grid(row=1,column=0)
E1=Entry(frame2,font=("times",15,"bold"))
E1.grid(row=1,column=1)

lblname=Label(frame2,text="Cookies",font=("times",15,"bold"),padx=10,pady=5,width=5)
lblname.grid(row=2,column=0)
E2=Entry(frame2,font=("times",15,"bold"))
E2.grid(row=2,column=1)

lblname=Label(frame2,text="Tea",font=("times",15,"bold"),padx=10,pady=5,width=5)
lblname.grid(row=3,column=0)
E3=Entry(frame2,font=("times",15,"bold"))
E3.grid(row=3,column=1)

lblname=Label(frame2,text="Coffee",font=("times",15,"bold"),padx=10,pady=5,width=5)
lblname.grid(row=4,column=0)
E4=Entry(frame2,font=("times",15,"bold"))
E4.grid(row=4,column=1)

lblname=Label(frame2,text="Juice",font=("times",15,"bold"),padx=10,pady=5,width=5)
lblname.grid(row=5,column=0)
E5=Entry(frame2,font=("times",15,"bold"))
E5.grid(row=5,column=1)

lblname=Label(frame2,text="Pancakes",font=("times",15,"bold"),padx=10,pady=5,width=5)
lblname.grid(row=6,column=0)
E6=Entry(frame2,font=("times",15,"bold"))
E6.grid(row=6,column=1)

lblname=Label(frame2,text="Eggs",font=("times",15,"bold"),padx=10,pady=5,width=5)
lblname.grid(row=7,column=0)
E7=Entry(frame2,font=("times",15,"bold"))
E7.grid(row=7,column=1,padx=10,pady=5)



res=Button(frame2,text="Reset",font=("times",15),bg="green",fg="white",padx=10,pady=5,width=5,command=Reset)
res.grid(row=11,column=1,sticky=W)

tot=Button(frame2,text="Total",font=("times",15),bg="green",fg="white",padx=10,pady=5,width=5,command=Total)
tot.grid(row=11,column=1,sticky=E)

frame3=Frame(win,highlightbackground="black",highlightthickness=2,padx=20,pady=20)
frame3.grid(row=1,column=3,padx=30,pady=50)

lblname=Label(frame3,text="BILL",font=("times",15,"bold"),padx=5,pady=5,width=5,fg="black")
lblname.grid(columnspan=2)

lblname=Button(frame3,text="Total",font=("times",15,"bold"),padx=5,pady=5,width=5,fg="white",background="green",command=Total)
lblname.grid(row=1,column=0,padx=10,pady=5)
E8=Entry(frame3,font=("times",15,"bold"))
E8.grid(row=2,column=0,padx=10,pady=5)



win.mainloop()
