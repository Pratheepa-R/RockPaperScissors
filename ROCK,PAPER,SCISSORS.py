def game():
    global c
    if c==0:
        c=1
        root.destroy()
    import tkinter as tk
    global r
    r=tk.Tk()
    r.title("THE GAME")
    canvas=tk.Canvas(r,height=1900,width=1900,bg="white").pack()
    frame=tk.Frame(canvas,bg="yellow")
    frame.place(relheight=0.93,relwidth=0.98,relx=0.01,rely=0.01)
    label=tk.Label(frame,text="WHICH ONE DO YOU CHOOSE?",font=("arial black",35)).pack()
    import random
    global x
    x=random.randint(1,3)
    button1=tk.Button(frame,text="ROCK",font=("arial black",30),bg="light green",fg="white",padx=50,command=score1).place(x=800,y=200)
    button2=tk.Button(frame,text="PAPER",font=("arial black",30),bg="light green",fg="white",padx=40,command=score2).place(x=800,y=400)
    button3=tk.Button(frame,text="SCISSORS",font=("arial black",30),bg="light green",fg="white",command=score3).place(x=800,y=600)
def final():
    import tkinter as tk
    window=tk.Tk()
    window.title("THE GAME")
    canvas=tk.Canvas(window,height=1900,width=1900,bg="white").pack()
    frame=tk.Frame(canvas,bg="yellow")
    frame.place(relheight=0.93,relwidth=0.98,relx=0.01,rely=0.01)
    if appy>you:
        tk.Label(frame,text="APPY WINS WITH",font=("arial black",35)).place(x=550,y=400)
        tk.Label(frame,text=appy,font=("arial black",35)).place(x=1010,y=400)
        tk.Label(frame,text="POINT(S)",font=("arial black",35)).place(x=1050,y=400)
    elif you>appy:
        tk.Label(frame,text="YOU WIN WITH",font=("arial black",35)).place(x=600,y=400)
        tk.Label(frame,text=you,font=("arial black",35)).place(x=1000,y=400)
        tk.Label(frame,text="POINT(S)",font=("arial black",35)).place(x=1040,y=400)
    else:
        tk.Label(frame,text="THE GAME IS DRAWN",font=("arial black",35)).place(x=650,y=400)
def score1():
    global count
    count+=1
    global appy
    global you
    import tkinter as tk
    global r1
    r1=tk.Tk()
    r1.title("THE GAME")
    canvas=tk.Canvas(r1,height=1900,width=1900,bg="white").pack()
    frame=tk.Frame(canvas,bg="yellow")
    frame.place(relheight=0.93,relwidth=0.98,relx=0.01,rely=0.01)
    if x==1:
        tk.Label(frame,text="APPY ALSO KEEPS ROCK",font=("arial black",35)).place(x=600,y=100)
        tk.Label(frame,text="NO ONE GETS A POINT",font=("arial black",35)).place(x=625,y=200)
    elif x==2:
        tk.Label(frame,text="APPY KEEPS PAPER",font=("arial black",35)).place(x=700,y=100)
        tk.Label(frame,text="APPY GETS A POINT",font=("arial black",35)).place(x=700,y=200)
        appy+=1
    elif x==3:
        tk.Label(frame,text="APPY KEEPS SCISSORS",font=("arial black",35)).place(x=650,y=100)
        tk.Label(frame,text="YOU GET A POINT",font=("arial black",35)).place(x=700,y=200)
        you+=1
    if count==10:
        tk.Button(frame,text="CONTINUE",font=("arial black",30),bg="light green",fg="white",command=final).place(x=800,y=400)
    else:
        tk.Button(frame,text="CONTINUE",font=("arial black",30),bg="light green",fg="white",command=game).place(x=800,y=400)
def score2():
    global count
    count+=1
    global you
    global appy
    import tkinter as tk
    global r2
    r2=tk.Tk()
    r2.title("THE GAME")
    canvas=tk.Canvas(r2,height=1900,width=1900,bg="white").pack()
    frame=tk.Frame(canvas,bg="yellow")
    frame.place(relheight=0.93,relwidth=0.98,relx=0.01,rely=0.01)
    if x==1:
        tk.Label(frame,text="APPY KEEPS ROCK",font=("arial black",35)).place(x=700,y=100)
        tk.Label(frame,text="YOU GET A POINT",font=("arial black",35)).place(x=700,y=200)
        you+=1
    elif x==2:
        tk.Label(frame,text="APPY ALSO KEEPS PAPER",font=("arial black",35)).place(x=600,y=100)
        tk.Label(frame,text="NO ONE GETS A POINT",font=("arial black",35)).place(x=625,y=200)
    elif x==3:
        tk.Label(frame,text="APPY KEEPS SCISSORS",font=("arial black",35)).place(x=650,y=100)
        tk.Label(frame,text="APPY GETS A POINT",font=("arial black",35)).place(x=700,y=200)
        appy+=1
    if count==10:
        tk.Button(frame,text="CONTINUE",font=("arial black",30),bg="light green",fg="white",command=final).place(x=800,y=400)
    else:
        tk.Button(frame,text="CONTINUE",font=("arial black",30),bg="light green",fg="white",command=game).place(x=800,y=400)
def score3():
    global count
    count+=1
    global appy
    global you
    import tkinter as tk
    global r3
    r3=tk.Tk()
    r3.title("THE GAME")
    canvas=tk.Canvas(r3,height=1900,width=1900,bg="white").pack()
    frame=tk.Frame(canvas,bg="yellow")
    frame.place(relheight=0.93,relwidth=0.98,relx=0.01,rely=0.01)
    if x==1:
        tk.Label(frame,text="APPY KEEPS ROCK",font=("arial black",35)).place(x=700,y=100)
        tk.Label(frame,text="APPY GETS A POINT",font=("arial black",35)).place(x=685,y=200)
        appy+=1
    elif x==2:
        tk.Label(frame,text="APPY KEEPS PAPER",font=("arial black",35)).place(x=700,y=100)
        tk.Label(frame,text="YOU GET A POINT",font=("arial black",35)).place(x=725,y=200)
        you+=1
    elif x==3:
        tk.Label(frame,text="APPY ALSO KEEPS SCISSORS",font=("arial black",35)).place(x=600,y=100)
        tk.Label(frame,text="NO ONE GETS A POINT",font=("arial black",35)).place(x=650,y=200)
    if count==10:
        tk.Button(frame,text="CONTINUE",font=("arial black",30),bg="light green",fg="white",command=final).place(x=800,y=400)
    else:
        tk.Button(frame,text="CONTINUE",font=("arial black",30),bg="light green",fg="white",command=game).place(x=800,y=400)
from tkinter import * 
global root
root=Tk()
root.title("ROCK,PAPER,SCISSORS")
canvas=Canvas(root,height=1900,width=1900,bg="white").pack()
frame=Frame(canvas,bg="yellow")
frame.place(relheight=0.93,relwidth=0.98,relx=0.01,rely=0.01)
label=Label(frame,text="ROCK, PAPER, SCISSORS",font=("arial black",35)).pack()
b=Button(frame,text="PLAY A GAME OF 10",font=("arial black",30),bg="light green",fg="white",padx=15,command=game).place(x=675,y=200)
c=count=you=appy=0
