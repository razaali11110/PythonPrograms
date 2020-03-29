from tkinter import *
def login():
    # lm = Toplevel(m)

    username = Label(m,text="Username : ",font=("Calibri",18)).grid(row=1,column=2)
    userE = Entry(m,width=50).grid(row=1,column=3,pady=10)



def register():
    print("Register Session Start")

def main():
    global m
    m = Tk()

    m.title("Junaid Ali")
    m.geometry("1000x600")

    title = Label(m, text="Login System", font=("Calibri", 20, "bold"), bg="black", fg="yellow", bd=5, relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)


    loginB =    Button(m,text="Login",width=20,command = login).grid(row=0,column=0,padx=10,pady=10)
    regisB=     Button(m,text="Register",width=20,command = register).grid(row=0,column=1,padx=10,pady=10)






    m.mainloop()

main()