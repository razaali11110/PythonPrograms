from tkinter import *

root=Tk()
# root.geometry("500x500")
root.title("Clicked The Button")

e = Entry(root)
e.pack()

def click():
    l = Label(root, text="Hello, "+e.get())
    l.pack()

b=Button(root,text="Click Here",padx=50,pady=50,command=click)


b.pack()

root.mainloop()