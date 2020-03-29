from tkinter import *

root=Tk()
# root.geometry("500x500")
root.title("Clicked The Button")

def click():
    l = Label(root, text="2 is clicked",fg="yellow",bg="black")
    l.pack()

b=Button(root,text="2",padx=50,pady=50,command=click,fg="white",bg="black")


b.pack()

root.mainloop()