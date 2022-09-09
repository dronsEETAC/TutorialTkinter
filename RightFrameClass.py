import tkinter as tk
from  tkinter import ttk

class RightFrameClass:

    def buildFrame(self, fatherFrame):
        self.RightFrame = tk.LabelFrame(fatherFrame, text='Right')
        self.table = ttk.Treeview(self.RightFrame)
        s = ttk.Style()
        s.theme_use('clam')
        # Configure the style of Heading in Treeview widget
        s.configure('Treeview.Heading', background="green3")

        self.count = 2
        self.table['columns'] = ('Name', 'Age')

        self.table.column("#0", width=0, stretch=tk.NO)
        self.table.column('Name', anchor=tk.CENTER, width=120)
        self.table.column("Age", anchor=tk.CENTER, width=120)

        self.table.heading("#0", text="", anchor=tk.CENTER)
        self.table.heading("Name", text="Name", anchor=tk.CENTER)
        self.table.heading("Age", text="Age", anchor=tk.CENTER)

        self.table.insert(parent='', index='end', iid=0, text='',
                       values=('Miguel', '23'))
        self.table.insert(parent='', index='end', iid=1, text='',
                          values=('Juan', '33'))

        self.table.pack()


        return self.RightFrame

    def PutEntry (self, name, age):
        self.table.insert(parent='', index='end', iid=self.count, text='',
                          values=(name, age))
        self.count = self.count + 1
