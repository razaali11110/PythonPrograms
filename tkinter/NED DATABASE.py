# Tkinter Class Programs:


from tkinter import *
from tkinter import messagebox



def data():
    messagebox.showinfo("Data Information", "ID :\t"+id.get()+ '\nName :\t' + name.get() + '\nAge :\t' + age.get() + '\nAdress :\t' + address.get() )


m = Tk()
m.geometry("400x600")
m.title("JUNAID's DATABASE")
l=Label(m,text=" ").grid(row=0,column=0,padx=10)

label1=Label(m, text="\nNED DATABASE", width=30,font="Amonium").grid(row=0,column=2)        #Creating a label widget
l1 = Label(m, text="ID", bg="gold", fg="black", width=10).grid(row=1, column=1, pady=10)
l2 = Label(m, text="Name", bg="gold", fg="black", width=10).grid(row=2, column=1, pady=10)
l3 = Label(m, text="Age", bg="gold", fg="black", width=10).grid(row=3, column=1, pady=10)
l4 = Label(m, text="Address", bg="gold", fg="black", width=10).grid(row=4, column=1, pady=10)

bw=5
id = Entry(m, width=30,borderwidth=bw)
id.grid(row=1, column=2,columnspan=2, pady=10)

name = Entry(m, width=30,borderwidth=bw)
name.grid(row=2, column=2,columnspan=2, pady=10)

age = Entry(m, width=30,borderwidth=bw)
age.grid(row=3, column=2,columnspan=2, pady=10)

address = Entry(m, width=30,borderwidth=bw)
address.grid(row=4, column=2,columnspan=2, pady=10)

gender = Label(m,width=10, text='Gender',bg="gold", fg="black").grid(row=5, column=1, pady=10)

c1 = Checkbutton(m,width=25,text="Male", bg="gold", fg="black").grid(row=5, column=2, padx=5,pady=10)
c2 = Checkbutton(m,width=25, text="Female", bg="gold", fg="black").grid(row=6, column=2, padx=5, pady=10)

# img1 = PhotoImage(file=r"e:\cartoon.png")
# img2 = img1.subsample(2, 2)
# l5 = Label(m, image=img2)
# l5.grid(row=0, column=3, pady=10)

li = Listbox(m)
li.insert(0, 'SE (1st Year)')
li.insert(1, 'SE (2nd Year)')
li.insert(2, 'SE (3rd Year)')
li.insert(3, 'SE (4th Year)')
li.insert(4, 'CSIT (1st Year)')
li.insert(5, 'CSIT (2nd Year)')
li.insert(6, 'CSIT (3rd Year)')
li.insert(7, 'CSIT (4th Year)')
li.grid(row=7, column=2, pady=10)

b1 = Button(m,text="Submit",width=15, bg="gold", fg="black" ,command=data).grid(row=8, column=2)
m.mainloop()
#
# from tkinter import *
# from tkinter import messagebox
#
# z = 0
#
#
# def add():
#     x = op1.get()
#     y = op2.get()
#     z = int(x) + int(y)
#     v.config(text=z)
#     messagebox.showinfo("Result is", z)
#
#
# def subtract():
#     x = op1.get()
#     y = op2.get()
#     z = int(x) - int(y)
#     v.config(text=z)
#     messagebox.showinfo("Result is", z)
#
#
# def divide():
#     x = op1.get()
#     y = op2.get()
#     z = int(x) / int(y)
#     v.config(text=z)
#     messagebox.showinfo("Result is", z)
#
#
# def multiply():
#     x = op1.get()
#     y = op2.get()
#     z = int(x) * int(y)
#     v.config(text=z)
#     messagebox.showinfo("Result is", z)
#
#
# m = Tk()
# b1 = Button(m, text="Add", bg='black', fg='red', command=add).grid(row=5, column=0, pady=10)
# b2 = Button(m, text="Subtract", bg='black', fg='green', command=subtract).grid(row=5, column=1, pady=10)
# b3 = Button(m, text="Multiply", bg='black', fg='blue', command=multiply).grid(row=6, column=0, pady=10)
# b4 = Button(m, text="Divide", bg='black', fg='pink', command=divide).grid(row=6, column=1, pady=10)
# op1 = Entry(m)
# op1.grid(row=3, column=2, pady=15)
# op2 = Entry(m)
# op2.grid(row=4, column=2, pady=15)
# v = Label(m, bg='gold', fg='blue', width=20)
# v.grid(row=6, column=7, pady=10)
# # ____________________________________________________________
# m.mainloop()