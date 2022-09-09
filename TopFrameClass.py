import tkinter as tk
from tkinter import messagebox
from ParameterFrameClass import ParameterFrameClass

class TopFrameClass:

    def buildFrame(self, fatherFrame):
        self.TopFrame = tk.LabelFrame(fatherFrame, text='Top')
        self.TopFrame.pack(fill="both", expand="yes", padx=10, pady=5)
        self.TopFrame.rowconfigure(0, weight=1)
        self.TopFrame.rowconfigure(1, weight=1)
        self.TopFrame.rowconfigure(2, weight=1)
        self.TopFrame.columnconfigure(0, weight=1)
        self.TopFrame.columnconfigure(1, weight=1)
        self.TopFrame.columnconfigure(2, weight=1)
        self.TopFrame.columnconfigure(3, weight=1)

        self.Button1 = tk.Button(self.TopFrame, text="Show alert", bg='red', fg="white", command=self.button1Clicked)
        self.Button1.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.Button2 = tk.Button(self.TopFrame, text="Parameters", bg='blue', fg="white", command=self.button2Clicked)
        self.Button2.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")
        self.Button3 = tk.Button(self.TopFrame, text="Get Value", bg='yellow', fg="black", command=self.button1Clicked)
        self.Button3.grid(row=0, column=2, padx=5, pady=5, sticky="nesw")
        self.value = tk.StringVar()
        self.valueLabel = tk.Label(self.TopFrame, borderwidth=2, relief="groove", textvariable=self.value)
        self.valueLabel.grid(row=0, column=3, padx=5, pady=5, sticky="nesw")
        self.Button5 = tk.Button(self.TopFrame, text="Button 5", bg='pink', fg="black", command=self.button1Clicked)
        self.Button5.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nesw")

        self.inputFrame = tk.Frame(self.TopFrame)
        tk.Label(self.inputFrame, text='Name').grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.entryName = tk.Entry(self.inputFrame)
        self.entryName.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")
        tk.Label(self.inputFrame, text='Age').grid(row=0, column=2, padx=5, pady=5, sticky="nesw")
        self.entryAge = tk.Entry(self.inputFrame)
        self.entryAge.grid(row=0, column=3, padx=5, pady=5, sticky="nesw")
        self.Button6 = tk.Button(self.inputFrame, text="Enter new user", bg='green', fg="white",
                                 command=self.button6Clicked)
        self.Button6.grid(row=0, column=4, padx=5, pady=5, sticky="nesw")

        self.inputFrame.grid(row = 2, column = 0, columnspan = 4, padx = 250, pady = 5, sticky = "nesw")

        return self.TopFrame


    def button1Clicked (self):
        messagebox.showinfo('information', 'Hello')


    def button1Clicked (self):
        self.value.set(45)

    def button6Clicked (self):
        self.rightFrameClass.PutEntry(self.entryName.get(),self.entryAge.get())

    def setRightFrame (self, rightFrameClass):
        self.rightFrameClass = rightFrameClass

    def button2Clicked (self):
        newWindow = tk.Toplevel(self.TopFrame)
        newWindow.title("Parameter Window")

        # sets the geometry of toplevel
        newWindow.geometry("800x600")
        parameterFrameClass = ParameterFrameClass()
        parameterFrame = parameterFrameClass.buildFrame(newWindow)
        parameterFrame.pack(fill="both", expand="yes", padx=10, pady=10)
