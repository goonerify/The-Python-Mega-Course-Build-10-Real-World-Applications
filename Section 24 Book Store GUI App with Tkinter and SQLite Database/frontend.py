
from tkinter import *

import backend


def row_selected(event):
    try:
        global selected_item
        index=list1.curselection()[0]
        selected_item=list1.get(index)

        # fill out the text boxes
        e1.delete(0, END)
        e1.insert(END, selected_item[1])
        e2.delete(0, END)
        e2.insert(END, selected_item[2])
        e3.delete(0, END)
        e3.insert(END, selected_item[3])
        e4.delete(0, END)
        e4.insert(END, selected_item[4])
    except IndexError:
        pass


# def get_selected_row():
#     global selected_item
#     index=list1.curselection()[0]
#     selected_item=list1.get(index)

#     return selected_item

def view_records():
    # Delete from row with index 0 until the last row
    list1.delete(0, END)
    for view in backend.view():
        list1.insert(END, view)

def search_records():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_record():
    list1.delete(0, END)
    newid=backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    if (type(newid) == int):
        list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_record():
    id=selected_item[0]
    # id=get_selected_row()[0]
    backend.delete(id)

def update_record():
    id=selected_item[0]
    # id=get_selected_row()[0]
    title, author, year, isbn = title_text.get(), author_text.get(), year_text.get(), isbn_text.get()
    backend.update(id, title, author, year, isbn)

window=Tk()
window.wm_title("Bookstore")

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
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1=Listbox(window, height=6, width=25)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# Configure the listbox for scrolling with the scrollbar
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# Bind selecting records in the listbox to an event handler
# Note: The way the function was written makes this binding unnecessary
list1.bind('<<ListboxSelect>>', row_selected)

b1=Button(window, text="View all", width=12, command=view_records)
b1.grid(row=2, column=3)

b1=Button(window, text="Search entry", width=12, command=search_records)
b1.grid(row=3, column=3)

b1=Button(window, text="Add entry", width=12, command=add_record)
b1.grid(row=4, column=3)

b1=Button(window, text="Update selected", width=12, command=update_record)
b1.grid(row=5, column=3)

b1=Button(window, text="Delete selected", width=12, command=delete_record)
b1.grid(row=6, column=3)

b1=Button(window, text="Close", width=12, command=window.destroy)
b1.grid(row=7, column=3)

# TODO: Add left and right padding to the window
window.mainloop()
