from tkinter import *

win = Tk()
win.title("Junaid")
win.geometry("400x400")

space = Label(win,text="\n"*3)
space.pack()

canvas=Canvas(win,bg="white",height="150",width="200")
# cord = 10,50,240,210
arc = canvas.create_arc(0,0,1,1,start=0,extent=150)

line = canvas.create_line(0,0,1,1)
l=Label(canvas,text="junaid").pack()
canvas.pack()

def plus():
    E = int(E1.get())+int(E2.get())
    L1 = Label(win, text=E)
    L1.pack()


def minus():
    E = int(E1.get())-int(E2.get())
    L1 = Label(win, text=E)
    L1.pack()

def multi():
    E = int(E1.get())*int(E2.get())
    L1 = Label(win, text=E)
    L1.pack()


E1=Entry(win,text="Enter n : ")
E2=Entry(win,text="Enter m : ")
E1.pack()
E2.pack()


plus = Button(win,text="Plus",padx="10",pady="10",command=plus)
plus.pack()

minus=Button(win,text="minus",padx="10",pady="10",command=minus)
minus.pack()

multi=Button(win,text="multi",padx="10",pady="10",command=multi)
multi.pack()


# T=Text(win,text="Text")
# T.pack()
win.mainloop()

