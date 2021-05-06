
from tkinter import *

from backend import Database

database=Database()

class Bookstore:
    def __init__(self) -> None:
        self.window=Tk()
        self.window.wm_title("Bookstore")

        self.l1 = Label(self.window, text="Title")
        self.l1.grid(row=0, column=0)

        self.l1 = Label(self.window, text="Author")
        self.l1.grid(row=0, column=2)

        self.l1 = Label(self.window, text="Year")
        self.l1.grid(row=1, column=0)

        self.l1 = Label(self.window, text="ISBN")
        self.l1.grid(row=1, column=2)

        self.title_text=StringVar()
        self.e1=Entry(self.window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text=StringVar()
        self.e2=Entry(self.window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text=StringVar()
        self.e3=Entry(self.window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text=StringVar()
        self.e4=Entry(self.window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        self.list1=Listbox(self.window, height=6, width=25)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.b1=Scrollbar(self.window)
        self.b1.grid(row=2, column=2, rowspan=6)

        # Configure the listbox for scrolling with the scrollbar
        self.list1.configure(yscrollcommand=self.b1.set)
        self.b1.configure(command=self.list1.yview)

        # Bind selecting records in the listbox to an event handler
        # Note: The way the function was written makes this binding unnecessary
        self.list1.bind('<<ListboxSelect>>', self.row_selected)

        self.b1=Button(self.window, text="View all", width=12, command=self.view_records)
        self.b1.grid(row=2, column=3)

        self.b2=Button(self.window, text="Search entry", width=12, command=self.search_records)
        self.b2.grid(row=3, column=3)

        self.b3=Button(self.window, text="Add entry", width=12, command=self.add_record)
        self.b3.grid(row=4, column=3)

        self.b4=Button(self.window, text="Update selected", width=12, command=self.update_record)
        self.b4.grid(row=5, column=3)

        self.b5=Button(self.window, text="Delete selected", width=12, command=self.delete_record)
        self.b5.grid(row=6, column=3)

        self.b6=Button(self.window, text="Close", width=12, command=self.window.destroy)
        self.b6.grid(row=7, column=3)

        # TODO: Add left and right padding to the self.window
        self.window.mainloop()

    def row_selected(self, event):
        try:
            index=self.list1.curselection()[0]
            self.selected_item=self.list1.get(index)

            # fill out the text boxes
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_item[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_item[2])
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_item[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_item[4])
        except IndexError:
            pass

    def view_records(self):
        # Delete from row with index 0 until the last row
        self.list1.delete(0, END)
        for view in database.view():
            self.list1.insert(END, view)

    def search_records(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_record(self):
        self.list1.delete(0, END)
        newid=database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        if (type(newid) == int):
            self.list1.insert(END, (newid, self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    def delete_record(self):
        id=self.selected_item[0]
        database.delete(id)

    def update_record(self):
        id=self.selected_item[0]
        title, author, year, isbn = self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()
        database.update(id, title, author, year, isbn)

def main():
    Bookstore()

if __name__=='__main__':
    main()
