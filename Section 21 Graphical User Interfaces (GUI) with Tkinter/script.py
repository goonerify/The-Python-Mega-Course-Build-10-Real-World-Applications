from tkinter import *

window=Tk()

def km_to_miles():
    miles=float(e1_value.get())*1.6
    t1.insert(END, miles)

b1=Button(window, text='Convert KM to Miles', command=km_to_miles)
b1.grid(row=0,column=0)

e1_value=StringVar()
# Input that can be interacted with
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

# Text widget
t1=Text(window, height=1, width=20)
t1.grid(row=0, column=2)

# This should always be at the end of the main script
window.mainloop()
