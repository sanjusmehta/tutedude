import tkinter
from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry('500x450')

border_frame = tkinter.Frame(window,bd=5, relief="ridge", bg="#D4D4D2")
border_frame.pack(padx=10, pady=10, fill="both", expand=True)

e = Entry(window, justify="right", width=15, font=("Terminal", 24, "normal"))
e.place(x=60, y=20)

def click(num):
    result = e.get() # gets the text visible in e
    e.delete(0,END) # after getting text we are clearing e
    e.insert(0,str(result) + str(num)) # we are adding the next value to the previous value

b1 = Button(window, text='1', width= 11, font=("Arial",12,"bold"), command=lambda:click(1))
b1.place(x=50, y=100)
b2 = Button(window, text='2', width= 11, font=("Arial",12,"bold"), command=lambda:click(2))
b2.place(x=200, y=100)
b3 = Button(window, text='3', width= 11, font=("Arial",12,"bold"), command=lambda:click(3))
b3.place(x=350, y=100)

b4 = Button(window, text='4', width= 11, font=("Arial",12,"bold"), command=lambda:click(4))
b4.place(x=50, y=150)
b5 = Button(window, text='5', width= 11, font=("Arial",12,"bold"), command=lambda:click(5))
b5.place(x=200, y=150)
b6 = Button(window, text='6', width= 11, font=("Arial",12,"bold"), command=lambda:click(6))
b6.place(x=350, y=150)

b7 = Button(window, text='7', width= 11, font=("Arial",12,"bold"), command=lambda:click(7))
b7.place(x=50, y=200)
b8 = Button(window, text='8', width= 11, font=("Arial",12,"bold"), command=lambda:click(8))
b8.place(x=200, y=200)
b9 = Button(window, text='9', width= 11, font=("Arial",12,"bold"), command=lambda:click(9))
b9.place(x=350, y=200)

b0 = Button(window, text='0', width= 11, font=("Arial",12,"bold"), command=lambda:click(0))
b0.place(x=200, y=250)


def add():
    global num1
    num1 = int(e.get())
    e.delete(0,END)
    global action
    action = "add"

badd = Button(window, text='+', width= 11, bg="#FF9500", font=("Arial",12,"bold"), command=add)
badd.place(x=50, y=300)

def sub():
    global num1
    num1 = int(e.get())
    e.delete(0, END)
    global action
    action = "sub"

bsub = Button(window, text='-', width= 11, bg="#FF9500", font=("Arial",12,"bold"), command=sub)
bsub.place(x=200, y=300)

def mul():
    global num1
    num1 = int(e.get())
    e.delete(0, END)
    global action
    action = "mul"

bmul = Button(window, text='X', width= 11, bg="#FF9500", font=("Arial",12,"bold"), command=mul)
bmul.place(x=350, y=300)

def div():
    global num1
    num1 = int(e.get())
    e.delete(0, END)
    global action
    action = "div"

bdiv = Button(window, text='÷', width= 11, bg="#FF9500", font=("Arial",12,"bold"), command=div)
bdiv.place(x=50, y=350)

def equal():
    num2 = int(e.get())
    e.delete(0,END)
    if(action == "add"):
        e.insert(0, int(num1 + num2))
    elif(action == "sub"):
        e.insert(0, int(num1 - num2))
    elif(action == "mul"):
        e.insert(0, num1 * num2)
    elif(action == "div"):
        e.insert(0, int(num1 / num2))


bequal = Button(window, text='=', width= 11,  font=("Arial",12,"bold"),command=equal)
bequal.place(x=200, y=350)

def ac():
    e.delete(0,END)

bac = Button(window, text='AC', width= 11, bg="#505050", font=("Arial",12,"bold"), command=ac)
bac.place(x=350, y=350)

window.mainloop()
