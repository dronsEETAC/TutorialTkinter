import tkinter as tk

class TopFrameClass:

    def buildFrame(self, fatherFrame):
        self.TopFrame = tk.LabelFrame(fatherFrame, text='Top')
        self.TopFrame.pack(fill="both", expand="yes", padx=10, pady=5)
        self.TopFrame.rowconfigure(0, weight=1)
        self.TopFrame.rowconfigure(1, weight=4)
        self.TopFrame.columnconfigure(0, weight=1)
        self.TopFrame.columnconfigure(1, weight=1)
        self.TopFrame.columnconfigure(2, weight=1)
        self.TopFrame.columnconfigure(3, weight=1)

        self.Button1 = tk.Button(self.TopFrame, text="Button 1", bg='red', fg="white", command=self.button1Clicked)
        self.Button1.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
        self.Button2 = tk.Button(self.TopFrame, text="Button 2", bg='blue', fg="white", command=self.button1Clicked)
        self.Button2.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")
        self.Button3 = tk.Button(self.TopFrame, text="Button 3", bg='yellow', fg="black", command=self.button1Clicked)
        self.Button3.grid(row=0, column=2, padx=5, pady=5, sticky="nesw")
        self.Button4 = tk.Button(self.TopFrame, text="Button 4", bg='green', fg="white", command=self.button1Clicked)
        self.Button4.grid(row=0, column=3, padx=5, pady=5, sticky="nesw")
        self.Button5 = tk.Button(self.TopFrame, text="Button 5", bg='pink', fg="black", command=self.button1Clicked)
        self.Button5.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="nesw")
        return self.TopFrame


    def button1Clicked (self):
        print ('button 1 clicked')


