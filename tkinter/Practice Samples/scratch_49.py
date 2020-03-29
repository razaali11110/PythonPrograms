# Tkinter Class Programs:
from tkinter import *
from tkinter import messagebox

def main():

    m = Tk()
    m.geometry("400x600")
    m.title("LOGIN FROM MUZ")
    l=Label(m,text=" ").grid(row=0,column=0,padx=10)
    # title = Label(m, text="Login System", font=("Calibri", 20, "bold"), bg="black", fg="yellow", bd=5, relief=GROOVE)
    # title.place(x=0, y=0, relwidth=1)

    f = Frame(m,bg="white").place(x=200,y=300)


    head=Label(f, text="Login System", font=("Calibri", 20, "bold"), bg="black", fg="yellow", bd=5, relief=GROOVE)        #Creating a label widget
    head.grid(row=0,column=2,pady=20)
    # head.grid(row=0,column=0,pady=20)
    username_l = Label(m, text="Username",bg="gold", fg="black", font=("bold"), width=10).grid(row=1, column=1, pady=10,padx=10)
    pass_l = Label(m, text="Password", bg="gold", fg="black", width=10, font=("bold")).grid(row=2, column=1, pady=10,padx=10)

    bw=5
    username_e = Entry(m, width=30,borderwidth=bw)
    username_e.grid(row=1, column=2,columnspan=2, pady=10)

    pass_e = Entry(m, width=30,borderwidth=bw)
    pass_e.grid(row=2, column=2,columnspan=2, pady=10)


    submit_b = Button(m,text="Submit",width=15, bg="gold", fg="black" ).grid(row=8, column=2)
    m.mainloop()

main()

# age = Entry(m, width=30,borderwidth=bw)
# age.grid(row=3, column=2,columnspan=2, pady=10)
#
# address = Entry(m, width=30,borderwidth=bw)
# address.grid(row=4, column=2,columnspan=2, pady=10)
#
# gender = Label(m,width=10, text='Gender',bg="gold", fg="black").grid(row=5, column=1, pady=10)
#
# c1 = Checkbutton(m,width=25,text="Male", bg="gold", fg="black").grid(row=5, column=2, padx=5,pady=10)
# c2 = Checkbutton(m,width=25, text="Female", bg="gold", fg="black").grid(row=6, column=2, padx=5, pady=10)

# img1 = PhotoImage(file=r"e:\cartoon.png")
# img2 = img1.subsample(2, 2)
# l5 = Label(m, image=img2)
# l5.grid(row=0, column=3, pady=10)

# li = Listbox(m)
# li.insert(0, 'SE (1st Year)')
# li.insert(1, 'SE (2nd Year)')
# li.insert(2, 'SE (3rd Year)')
# li.insert(3, 'SE (4th Year)')
# li.insert(4, 'CSIT (1st Year)')
# li.insert(5, 'CSIT (2nd Year)')
# li.insert(6, 'CSIT (3rd Year)')
# li.insert(7, 'CSIT (4th Year)')
# li.grid(row=7, column=2, pady=10)


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