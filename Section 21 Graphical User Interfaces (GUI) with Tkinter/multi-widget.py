from tkinter import *

window=Tk()

def convert_weights():
    val=float(e1_value.get())
    grams=val*1000 
    tgrams.insert(END, grams)
    pounds=val*2.20462
    tpounds.insert(END, pounds)
    ounces=val*35.274
    tounces.insert(END, ounces)

label=Label(window, text="Kg")
label.grid(row=0, column=0)

e1_value=StringVar()
# Input that can be interacted with
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b1=Button(window, text='Convert', command=convert_weights)
b1.grid(row=0,column=2)

# Text widgets
tgrams=Text(window, height=1, width=20)
tgrams.grid(row=1, column=0)

tpounds=Text(window, height=1, width=20)
tpounds.grid(row=1, column=1)

tounces=Text(window, height=1, width=20)
tounces.grid(row=1, column=2)

# This should always be at the end of the main script
window.mainloop()
