from tkinter import *

root=Tk()
root.title("Simple Calculator")
# root.geometry("400x400")


label1=Label(root, text="\nSIMPLE CALCULATOR", font="Anonim")        #Creating a label widget



e = Entry(root,width=50,borderwidth=5)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))



def clear():
    e.delete(0,END)


button_1=Button(root, text="1",padx=20,pady=20,command=lambda : button_click(1))
button_2=Button(root, text="2",padx=20,pady=20,command=lambda : button_click(2))
button_3=Button(root, text="3",padx=20,pady=20,command=lambda : button_click(3))
button_4=Button(root, text="4",padx=20,pady=20,command=lambda : button_click(4))
button_5=Button(root, text="5",padx=20,pady=20,command=lambda : button_click(5))
button_6=Button(root, text="6",padx=20,pady=20,command=lambda : button_click(6))
button_7=Button(root, text="7",padx=20,pady=20,command=lambda : button_click(7))
button_8=Button(root, text="8",padx=20,pady=20,command=lambda : button_click(8))
button_9=Button(root, text="9",padx=20,pady=20,command=lambda : button_click(9))
button_0=Button(root, text="0",padx=20,pady=20,command=lambda : button_click(0))

button_equal=Button(root, text="=",padx=20,pady=20)
button_clear=Button(root, text="CLEAR",padx=20,pady=20,command=clear)




# label1.grid(row=2,column=1,columnspan=3)
# e.grid(row=3,column=1,columnspan=3,padx=10,pady=10)

label1.grid(row=0,column=0,columnspan=3)
e.grid(row=1,column=0,columnspan=4,padx=10,pady=10)

button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_0.grid(row=5,column=1)
button_equal.grid(row=5,column=3)
button_clear.grid(row=3,column=3)

root.mainloop()

#
# label1=Label(root, text="\nHello World!", font="Anonim").grid(row=2,column=1)        #Creating a label widget
# label2=Label(root, text="This is new Junaid's calculator", font="Arial").grid(row=3,column=1)
