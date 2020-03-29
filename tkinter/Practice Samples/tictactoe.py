from tkinter import *
from tkinter import messagebox

A=[]
def p1():


def main():
    root=Tk()
    root.geometry("500x500")
    root.title("TicTacToe Game")

    f=Frame(root,bg="white")
    f.place(x=50,y=100)
    title = Label(root, text="TicTacToe", font=("Calibri", 30, "bold"), bg="black", fg="yellow", bd=5, relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)
    width,height=10,5
    if 1 in A:
        first=Button(f,text="1",width=width,height=height,bg="white",fg="Green",font=("Arial",12,"bold"),bd=5, relief=GROOVE)
        first.grid(row=1,column=0)
    else:
        first=Button(f,text="1",width=width,height=height,bg="white",fg="Green",font=("Arial",12,"bold"),command=p1,bd=5, relief=GROOVE)
        first.grid(row=1,column=0)
    second=Button(f,text="",width=width,height=height,bg="white",fg="Green",font=("Arial",12,"bold"),command=p1,bd=5, relief=GROOVE)
    second.grid(row=1, column=1)
    root.mainloop()

main()