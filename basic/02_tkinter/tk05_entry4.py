from tkinter import *

window = Tk()

def process1():
    temp = ((float(e1.get())) - 32) / 1.8
    e2.delete(0, "end")
    e2.insert(0, temp)

def process2():
    temp = ((float(e2.get())) * 1.8) + 32
    e1.delete(0, "end")
    e1.insert(0, temp)


l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window, bg="skyblue", fg="white")
e2 = Entry(window, bg="skyblue", fg="white")
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(window, text="화씨 → 섭씨", command=process1)
b2 = Button(window, text="섭씨 → 화씨", command=process2)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)


window.mainloop()
