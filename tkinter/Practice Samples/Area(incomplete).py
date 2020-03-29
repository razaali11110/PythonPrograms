from tkinter import *

root=Tk()
# root.geometry("500x500")
root.title("Area Finder")

def square():
    
    l2 =Lable(root,text="Hy")
    l2.pack()

l1= Label(root, text="\nArea Finder", font="Anonim")
e = Entry(root,width=50,borderwidth=5)
b1 = Button(root,text="Find",command=lambda : square)

l1.pack()
e.pack()
b1.pack()

root.mainloop()