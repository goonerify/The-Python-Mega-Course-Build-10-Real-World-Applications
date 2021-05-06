
from tkinter import *
from typing import List

window=Tk()

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l1 = Label(window, text="Author")
l1.grid(row=0, column=2)

l1 = Label(window, text="Year")
l1.grid(row=1, column=0)

l1 = Label(window, text="ISBN")
l1.grid(row=1, column=2)

title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e1=Entry(window, textvariable=author_text)
e1.grid(row=0, column=3)

year_text=StringVar()
e1=Entry(window, textvariable=year_text)
e1.grid(row=1, column=1)

isbn_text=StringVar()
e1=Entry(window, textvariable=isbn_text)
e1.grid(row=1, column=3)

list1=Listbox(window, height=6, width=25)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

b1=Button(window, text="View all", width=12)
b1.grid(row=2, column=3)

b1=Button(window, text="Search entry", width=12)
b1.grid(row=3, column=3)

b1=Button(window, text="Add entry", width=12)
b1.grid(row=4, column=3)

b1=Button(window, text="Update selected", width=12)
b1.grid(row=5, column=3)

b1=Button(window, text="Delete selected", width=12)
b1.grid(row=6, column=3)

b1=Button(window, text="Close", width=12)
b1.grid(row=7, column=3)

window.mainloop()
