from tkinter import *

root=Tk()
# root.geometry("500x500")
root.title("Clicked The Button")

def click():
    l = Label(root, text="I clicked...")
    l.pack()

b=Button(root,text="Click Here",padx=50,pady=50,command=click)
b.pack()

root.mainloop()