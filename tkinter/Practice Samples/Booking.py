from tkinter import *
from tkinter import messagebox

# class Void (tk.Tk) :
#     def __init__ (self, color='black') :
#         tk.Tk.__init__(self)
#         self.wm_state('zoomed')
#         self.config(bg=color)
#         self.overrideredirect(True)
#         self.attributes('-topmost', True)



def main():
    root=Tk()
    root.geometry("500x500")
    root.title("Aeroplane Booking System")
    root.wm_state('zoomed')
    # root.overrideredirect(True)
    # root.attributes('-topmost', True)


    first_class = []
    Executive = []
    economy = []
    def fc_booked():
        # messagebox.showinfo("First Class Booking", "You've booked seat no.")
        first_class.append(1)



    # def e_booked():
    #     messagebox.showinfo("First Class Booking", "You've booked seat no.")
    # def economy():
    #     messagebox.showinfo("First Class Booking", "You've booked seat no.")


    f=Frame(root,bg="white")
    f.place(x=50,y=100)
    title = Label(root, text="Booking", font=("Calibri", 30, "bold"), bg="black", fg="yellow", bd=5, relief=GROOVE)
    title.place(x=0, y=0, relwidth=1)
    width,height=6,3
    #first seat
    if 1 in first_class:
        first=Button(f,text="1",width=width,height=height,bg="white",fg="red",font=("Arial",12,"bold"),bd=5, relief=GROOVE).grid(row=1,column=0)
    else:
        first=Button(f,text="1",width=width,height=height,bg="white",fg="Green",font=("Arial",12,"bold"),bd=5, relief=GROOVE,command=fc_booked).grid(row=1,column=0)
        second=Button(f,text="2",width=width,height=height,bg="white",fg="Green",font=("Arial",12,"bold"),bd=5, relief=GROOVE,command=fc_booked)
        second.grid(row=1, column=1)


    #
    # label1=Label(f, text="Hello World!", bg="black",fg="white",font=("Arial",12,"bold"))     #Creating a label widget
    # label1.grid(row=2,column=1)
    # label2=Label(f, text="This is new Junaid's calculator", font="Arial").grid(row=3,column=1)
    # global nth
    # n=6
    # for i in range(n):
    #     for j in range(n):
    #         #BOOKED
    #         if 1+j+(n)*i in first_class:
    #             Button(f,text=str(1+j+(n)*i),width=6,height=3,bg="gold",fg="black",font="bold",command=fc_booked() and first_class.append(1+j+(n)*i)).grid(row=i,column=j)
    #
    #         else:
    #             nth=1+j+(n)*i
    #             Button(f,text=str(1+j+(n)*i),width=6,height=3,fg="black",font="bold",command=fc_booked).grid(row=i,column=j)
    root.mainloop()


main()








#
# label1=Label(root, text="\nHello World!", font="Anonim").grid(row=2,column=1)        #Creating a label widget
# label2=Label(root, text="This is new Junaid's calculator", font="Arial").grid(row=3,column=1)
