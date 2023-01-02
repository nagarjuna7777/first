from tkinter import *
from tkinter import messagebox
gui = Tk()
gui.geometry("400x400")
gui.title("Temparature Conversation Application")
l1=Label(gui,text="Celisus to Fahernheit",font='Arial',fg='black',bg='red')
l2=Label(gui,text="Fahernheit to Celisus",font='Arial',fg='black',bg='red')
l1.grid(row=0,column=0,padx=10,pady=10)
l2.grid(row=0,column=1,padx=10,pady=10)
e1=Entry(gui,font="Arial")
e2=Entry(gui,font='Arial')
e1.grid(row=1,column=0,padx=10,pady=10)
e2.grid(row=1,column=1,padx=10,pady=10)
def ctof():
    c = float(e1.get())
    f = ( c * 9/5 ) + 32
    e2.delete(0,"end")
    e2.insert(0,str(f))
def ftoc():
    f=float(e2.get())
    c = (f - 32) * 5/9
    e1.delete(0,"end")
    e1.insert(0,str(c))
def clear():
    e1.delete(0,'end')
    e2.delete(0,'end')
    #messagebox.showerror("It is Cleared")
#Button1
b1 = Button(gui,text='Celisus to Fehernheit',command=ctof)
b2 = Button(gui,text='Celisus to Fehernheit',command=ftoc)
b1.grid(row=2,column=0,padx=10,pady=10)
b2.grid(row=2,column=1,padx=10,pady=10)
b3=Button(gui,text='Clear',command=clear)
#b3.pack()
b3.grid(row=4,column=1,padx=2,pady=0)

gui.mainloop()
